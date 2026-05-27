from __future__ import annotations

from pathlib import Path

import pytest

try:
    import smog3
    from smog3 import cli, smog2_native
    from openmm import Context, CustomNonbondedForce, NonbondedForce, Platform, Vec3, VerletIntegrator
    from openmm.app import Simulation
    from openmm.unit import kilojoule_per_mole, nanometer, picosecond
except Exception as exc:  # pragma: no cover - only used when optional test deps are absent.
    pytest.skip(f"SMOG3/OpenMM integration dependencies are unavailable: {exc}", allow_module_level=True)

from OpenSMOG.OpenSMOG import SBM


SMOG3_ROOT = Path(smog3.__file__).resolve().parents[2]
PDB = SMOG3_ROOT / "SMOG-CHECK" / "share" / "PDB.files" / "2ci2_v2.pdb"


def _new_sbm() -> SBM:
    return SBM(time_step=0.002, collision_rate=1.0, r_cutoff=0.65, temperature=0.5, cmm=False, pbc=False, warn=False)


def _energy(sbm: SBM) -> float:
    context = Context(sbm.system, VerletIntegrator(0.001), Platform.getPlatformByName("Reference"))
    context.setPositions(sbm.Gro.getPositions())
    try:
        return context.getState(getEnergy=True).getPotentialEnergy().value_in_unit(kilojoule_per_mole)
    finally:
        del context


def _nonbonded_exclusions(system) -> set[tuple[int, int]]:
    for force in system.getForces():
        if isinstance(force, NonbondedForce):
            return {
                tuple(sorted((int(force.getExceptionParameters(i)[0]), int(force.getExceptionParameters(i)[1]))))
                for i in range(force.getNumExceptions())
            }
    raise AssertionError("system has no NonbondedForce")


def _custom_nonbonded_exclusions(system) -> set[tuple[int, int]]:
    for force in system.getForces():
        if isinstance(force, CustomNonbondedForce):
            return {
                tuple(sorted((int(force.getExclusionParticles(i)[0]), int(force.getExclusionParticles(i)[1]))))
                for i in range(force.getNumExclusions())
            }
    raise AssertionError("system has no CustomNonbondedForce")


def _short_verlet_trajectory(sbm: SBM, positions, steps: int = 5) -> tuple[list[float], object]:
    integrator = VerletIntegrator(0.0005 * picosecond)
    simulation = Simulation(sbm.Top.topology, sbm.system, integrator, Platform.getPlatformByName("Reference"), {})
    simulation.context.setPositions(positions)
    simulation.context.setVelocities([Vec3(0, 0, 0) for _ in range(sbm.system.getNumParticles())] * (nanometer / picosecond))
    energies = []
    final_positions = None
    try:
        for step in range(steps + 1):
            state = simulation.context.getState(getEnergy=True, getPositions=True)
            energies.append(state.getPotentialEnergy().value_in_unit(kilojoule_per_mole))
            final_positions = state.getPositions().value_in_unit(nanometer)
            if step < steps:
                simulation.step(1)
        return energies, final_positions
    finally:
        del simulation
        del integrator


def _rmsd(left, right) -> float:
    total = 0.0
    count = 0
    for lvec, rvec in zip(left, right):
        total += (lvec.x - rvec.x) ** 2 + (lvec.y - rvec.y) ** 2 + (lvec.z - rvec.z) ** 2
        count += 1
    return (total / count) ** 0.5


def test_smog3_pdb_xml_loads_like_classic_gro_top_xml(tmp_path: Path) -> None:
    if not PDB.exists():
        pytest.skip(f"SMOG3 checkout PDB fixture not found: {PDB}")

    classic_dir = tmp_path / "classic"
    classic_dir.mkdir()
    classic_top = classic_dir / "model.top"
    classic_gro = classic_dir / "model.gro"
    classic_xml = classic_dir / "model.xml"
    assert smog2_native.main(
        [
            "-i",
            str(PDB),
            "-AA",
            "-OpenSMOG",
            "-OpenSMOGxml",
            str(classic_xml),
            "-o",
            str(classic_top),
            "-g",
            str(classic_gro),
            "-n",
            str(classic_dir / "model.ndx"),
            "-s",
            str(classic_dir / "model.contacts"),
        ]
    ) == 0

    selfcontained_dir = tmp_path / "selfcontained"
    assert cli._run_opensmog_shortcut(
        [
            "-i",
            str(PDB),
            "--model",
            "AA",
            "--prefix",
            "model",
            "--output-dir",
            str(selfcontained_dir),
        ]
    ) == 0
    assert {path.name for path in selfcontained_dir.iterdir()} == {"model.pdb", "model.xml"}

    classic = _new_sbm()
    classic.loadSystem(Grofile=str(classic_gro), Topfile=str(classic_top), Xmlfile=str(classic_xml))
    direct = _new_sbm()
    direct.loadSystem(Pdbfile=str(selfcontained_dir / "model.pdb"), Xmlfile=str(selfcontained_dir / "model.xml"))

    assert classic.system.getNumParticles() == direct.system.getNumParticles()
    assert [force.__class__.__name__ for force in classic.system.getForces()] == [
        force.__class__.__name__ for force in direct.system.getForces()
    ]
    assert _nonbonded_exclusions(classic.system) == _nonbonded_exclusions(direct.system)
    assert _custom_nonbonded_exclusions(classic.system) == _custom_nonbonded_exclusions(direct.system)
    assert _energy(classic) == pytest.approx(_energy(direct), abs=1e-8)

    classic_energies, classic_positions = _short_verlet_trajectory(classic, classic.Gro.getPositions())
    direct_energies, direct_positions = _short_verlet_trajectory(direct, classic.Gro.getPositions())
    assert classic_energies == pytest.approx(direct_energies, abs=1e-8)
    assert _rmsd(classic_positions, direct_positions) == pytest.approx(0.0, abs=1e-10)


def _write_smog3_xml(path: Path, system_body: str) -> None:
    path.write_text(
        "<OpenSMOGforces><smog3_system version=\"1\" index_base=\"1\" units=\"gromacs\">"
        + system_body
        + "</smog3_system></OpenSMOGforces>\n",
        encoding="utf-8",
    )


def _minimal_system_body(bond_i: int = 1, bond_j: int = 2, coordinate_count: int = 2) -> str:
    coordinates = "".join(
        f"<atom index=\"{idx}\" x=\"0\" y=\"0\" z=\"0\"/>" for idx in range(1, coordinate_count + 1)
    )
    return f"""
      <coordinates><box values="1 1 1"/>{coordinates}</coordinates>
      <topology>
        <atomtypes><atomtype name="CA" mass="12.0" charge="0" c6_or_sigma="0" c12_or_epsilon="0"/></atomtypes>
        <moleculetype name="Macromolecule" nrexcl="3"/>
        <atoms>
          <atom index="1" type="CA" residue_index="1" residue_name="ALA" atom_name="CA"/>
          <atom index="2" type="CA" residue_index="2" residue_name="ALA" atom_name="CA"/>
        </atoms>
        <bonds><bond i="{bond_i}" j="{bond_j}" function="1" length="0.38" k="1000"/></bonds>
        <angles/>
        <dihedrals/>
        <pairs/>
        <exclusions><exclusion atoms="1 2"/></exclusions>
      </topology>
    """


def test_smog3_xml_reports_missing_required_topology_sections(tmp_path: Path, capsys) -> None:
    xml = tmp_path / "missing.xml"
    _write_smog3_xml(xml, "<coordinates><atom index=\"1\" x=\"0\" y=\"0\" z=\"0\"/></coordinates><topology/>")

    with pytest.raises(SystemExit):
        _new_sbm()._parse_smog3_system_xml(str(xml))

    assert "missing <topology><atomtypes>" in capsys.readouterr().out


def test_smog3_xml_reports_coordinate_atom_count_mismatch(tmp_path: Path, capsys) -> None:
    xml = tmp_path / "count.xml"
    _write_smog3_xml(xml, _minimal_system_body(coordinate_count=1))

    with pytest.raises(SystemExit):
        _new_sbm()._parse_smog3_system_xml(str(xml))

    assert "atom-count mismatch" in capsys.readouterr().out


def test_smog3_xml_reports_bad_topology_indices(tmp_path: Path, capsys) -> None:
    xml = tmp_path / "bad-index.xml"
    _write_smog3_xml(xml, _minimal_system_body(bond_i=1, bond_j=99))

    with pytest.raises(SystemExit):
        _new_sbm()._parse_smog3_system_xml(str(xml))

    output = capsys.readouterr().out
    assert "bonds row 1" in output
    assert "out-of-range atom index" in output
