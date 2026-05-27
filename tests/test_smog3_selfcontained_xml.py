from __future__ import annotations

from pathlib import Path

import pytest

try:
    import smog3
    from smog3 import cli, smog2_native
    from openmm import Context, CustomNonbondedForce, NonbondedForce, Platform, VerletIntegrator
    from openmm.unit import kilojoule_per_mole
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
