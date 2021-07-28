# Copyright (c) 2020-2021 The Center for Theoretical Biological Physics (CTBP) - Rice University
# This file is from the OpenSMOG project, released under the MIT License. 

R"""  
The :class:`~.OpenSMOG` classes perform molecular dynamics using Structure-Based Models (SBM) for biomolecular simulations.
:class:`~.OpenSMOG` allows the simulations of a wide variety of potential forms, including the most commonly employed models such as the C-alpha and All-Atoms.
Details about the models can be found below:
    - **SMOG server**: https://smog-server.org/
    - **C-alpha**: Clementi, C., Nymeyer, H. and Onuchic, J.N., 2000. Topological and energetic factors: what determines the structural details of the transition state ensemble and “en-route” intermediates for protein folding? An investigation for small globular proteins. Journal of molecular biology, 298(5), pp.937-953.
    - **All-Atom**: Whitford, P.C., Noel, J.K., Gosavi, S., Schug, A., Sanbonmatsu, K.Y. and Onuchic, J.N., 2009. An all‐atom structure‐based potential for proteins: bridging minimal models with all‐atom empirical forcefields. Proteins: Structure, Function, and Bioinformatics, 75(2), pp.430-441.
"""

from simtk.openmm.app import *
from simtk.openmm import *
from simtk.unit import *
import os
import numpy as np
import xml.etree.ElementTree as ET
import warnings
from sys import stdout
from lxml import etree
from .OpenSMOG_Reporter import forcesReporter

class SBM:

    R"""  
    The :class:`~.SBM` class performs Molecular dynamics simulations using structure-based models to investigate a broad range of biomolecular dynamics, including domain rearrangements in proteins, folding and ligand binding in RNA, and large-scale rearrangements in ribonucleoprotein assemblies. In its simplest form, a structure-based model defines a particular structure (usually obtained from X-ray, or NMR, methods) as the energetic global minimum.
    
    
    The :class:`~.SBM` sets the environment to start the molecular dynamics simulations.
    
    Args:
        name (str):
            Name used in the output files. (Default value: *SBM*). 
        time_step (float, required):
            Simulation time step in units of :math:`\tau`. (Default value = 0.0005).
        collision_rate (float, required):
            Friction/Damping constant in units of reciprocal time (:math:`1/\tau`). (Default value = 1.0).
        r_cutoff (float, required):
            Cutoff distance to consider non-bonded interactions in units of nanometers. (Default value = 3.0).
        temperature (float, required):
            Temperature in reduced units. (Default value = 0.5).
    """


    def __init__(self, 
        name = "SBM",
        time_step = 0.0005,
        collision_rate = 1.0,
        r_cutoff = 3.0,
        temperature = 0.5):
        
            self.name = name
            self.dt = time_step * picoseconds
            self.gamma = collision_rate / picosecond
            self.rcutoff = r_cutoff * nanometers  
            self.temperature = (temperature / 0.008314) * kelvin
            self.forceApplied = False
            self.loaded = False
            self.folder = "."
            self.forceNamesCA = {0 : "eletrostastic", 1 : "Non-Contacts", 2 : "Bonds", 3 : "Angles", 4 : "Dihedrals"}
            self.forceNamesAA = {0 : "eletrostastic", 1 : "Non-Contacts", 2 : "Bonds", 3 : "Angles", 4 : "Dihedrals", 5 : "Impropers"}
            self.forceCount = 0
            
    def setup_openmm(self, platform='cuda', precision='single', GPUindex='default', integrator="langevin"):
        
        R"""Sets up the parameters of the simulation OpenMM platform.

        Args:

            platform (str, optional):
                Platform to use in the simulations. Opitions are *CUDA*, *OpenCL*, *HIP*, *CPU*, *Reference*. (Default value: *CUDA*). 
            precision (str, optional):
                Numerical precision type of the simulation. Opitions are *single*, *mixed*, *double*. (Default value: *single*). For details check the `OpenMM Documentation <http://docs.openmm.org/latest/developerguide/developer.html#numerical-precision>`__. 
            GPUIndex (str, optional):
                Set of Platform device index IDs. Ex: 0,1,2 for the system to use the devices 0, 1 and 2. (Use only when GPU != default)
            integrator (str):
                Integrator to use in the simulations. Options are *langevin*,  *variableLangevin*, *verlet*, *variableVerlet* and, *brownian*. (Default value: *langevin*).
        """

        precision = precision.lower()
        if precision not in ["mixed", "single", "double"]:
            raise ValueError("Presision must be mixed, single or double")
            
        properties = {}
        properties["Precision"] = precision
        if GPUindex.lower() != "default":
            properties["DeviceIndex"] = GPUindex
            
        self.properties = properties

        if platform.lower() == "opencl":
            platformObject = Platform.getPlatformByName('OpenCL')

        elif platform.lower() == "reference":
            platformObject = Platform.getPlatformByName('Reference')

        elif platform.lower() == "cuda":
            platformObject = Platform.getPlatformByName('CUDA')

        elif platform.lower() == "cpu":
            platformObject = Platform.getPlatformByName('CPU')
            self.properties = {}

        elif platform.lower() == "hip":
            platformObject = Platform.getPlatformByName('HIP')

        else:
            self.exit("\n!!!! Unknown platform !!!!\n")
        
        self.platform = platformObject
        
        if integrator.lower() == "langevin":
            self.integrator = LangevinIntegrator(self.temperature,
                self.gamma, self.dt)
        else:
            self.integrator = integrator
            self.integrator_type = "UserDefined"
            
        self.forceDict = {}
        self.forcesDict = {}
        
    def saveFolder(self, folder):

        R"""Sets the folder path to save data.

        Args:

            folder (str, optional):
                Folder path to save the simulation data. If the folder path does not exist, the function will create the directory.
        """
    
        if os.path.exists(folder) == False:
            os.mkdir(folder)
        self.folder = folder

    def loadSystem(self, Grofile, Topfile, Xmlfile):

        R"""Loads the input files in the OpenMM system platform. The input files are generated using SMOG2 software with the flag :code:`-openSMOG`. Details on how to create the files can be found in the `SMOG2 User Manual <https://smog-server.org/smog2/>`__.
        A tutorial on how to generate the inputs files for a C-alpha model simulation can be found `here <https://opensmog.readthedocs.io>`__.

        Args:

            Grofile (file, required):
                Initial structure for the MD simulations in *.gro* file format generated by SMOG2 software with the flag :code:`-openSMOG`.  (Default value: :code:`None`).
            Topfile (file, required):
                Topology *.top* file format generated by SMOG2 software with the flag :code:`-openSMOG`. The topology file lists the interactions between the system atoms expect for the "Native Contacts" potential that is provided to OpenSMOG in a *.xml* file. (Default value: :code:`None`).
            Xmlfile (file, required):
                The *.xml* file that contains the information on the "Contacts" potential. The *.xml* file is generated by SMOG2 software with the flag :code:`-openSMOG` and accepts Custom Potential forms. (Default value: :code:`None`).
        """
        def _checknames(f1,f2,f3):
            fn1 = os.path.basename(f1).rsplit('.', 1)[0]
            fn2 = os.path.basename(f2).rsplit('.', 1)[0]
            fn3 = os.path.basename(f3).rsplit('.', 1)[0]
            if fn1 == fn2 and fn1 ==fn3:
                return False
            else:
                return True
        
        if _checknames(Grofile, Topfile, Xmlfile):
            warnings.warn('The file names are different. Make sure this is not a mistake!')

        self._check_file(Grofile, '.gro')
        self.loadGro(Grofile)

        self._check_file(Topfile, '.top')
        self.loadTop(Topfile)

        self._check_file(Xmlfile, '.xml')
        self.loadXml(Xmlfile)

        print("Files loaded in the system.")
        
    def _check_file(self, filename, ext):
        if not (filename.lower().endswith(ext)):
            raise ValueError('Wrong file extension: {} must to be {} extension'.format(filename, ext))

        
    def loadGro(self, Grofile):
        R"""Loads the  *.gro* file format in the OpenMM system platform. The inputs files are generated using SMOG2 software with the flag :code:`-openSMOG`. Details on how to create the files can be found in the `SMOG2 User Manual <https://smog-server.org/smog2/>`__.
        A tutorial on how to generate the inputs files for a C-alpha model simulation can be found `here <https://opensmog.readthedocs.io>`__.

        Args:

            Grofile (file, required):
                Initial structure for the MD simulations in *.gro* file format generated by SMOG2 software with the flag :code:`-openSMOG`.  (Default value: :code:`None`).
        """
        self.Gro = GromacsGroFile(Grofile)
        
    def loadTop(self, Topfile):
        R"""Loads the  *.top* file format in the OpenMM system platform. The inputs files are generated using SMOG2 software with the flag :code:`-openSMOG`. Details on how to create the files can be found in the `SMOG2 User Manual <https://smog-server.org/smog2/>`__.
        A tutorial on how to generate the inputs files for a C-alpha model simulation can be found `here <https://opensmog.readthedocs.io>`__.

        Args:

            Topfile (file, required):
                Topology *.top* file format generated by SMOG2 software with the flag :code:`-openSMOG`. The topology file lists the interactions between the system atoms expect for the "Native Contacts" potential that is provided to OpenSMOG in a *.xml* file. (Default value: :code:`None`).
        """
        self.Top = GromacsTopFile(Topfile)
        self.system = self.Top.createSystem(nonbondedMethod=CutoffNonPeriodic,nonbondedCutoff=self.rcutoff)
        nforces = len(self.system.getForces())
        for force_id, force in enumerate(self.system.getForces()):                  
                    if nforces == 7: 
                        if force_id <=4:
                            force.setForceGroup(force_id)
                            self.forcesDict[self.forceNamesCA[force_id]] = force
                            self.forceCount +=1
                        else:
                            force.setForceGroup(30)
                    elif nforces == 8:
                        if force_id <=5:
                            force.setForceGroup(force_id)
                            self.forcesDict[self.forceNamesAA[force_id]] = force
                            self.forceCount +=1
                        else:
                            force.setForceGroup(30)

        
    def _splitForces(self):
        n_forces =  len(self.data[3])

        forces = {}
        for n in range(n_forces):
            forces[self.data[3][n]] = [self.data[0][n], self.data[1][n], self.data[2][n]]
        self.contacts = forces
        
    def _customSmogForce(self, name, data):
        #first set the equation
        contacts_ff = CustomBondForce(data[0])

        #second set the number of variable
        for pars in data[1]:
            contacts_ff.addPerBondParameter(pars)

        #third, apply the bonds from each pair of atoms and the related variables.
        pars = [pars for pars in data[1]]

        for iteraction in data[2]:
            atom_index_i = int(iteraction['i'])-1 #check where start the polymer
            atom_index_j = int(iteraction['j'])-1
            parameters = [float(iteraction[k]) for k in pars]

            contacts_ff.addBond(atom_index_i, atom_index_j, parameters)

        self.forcesDict[name] =  contacts_ff
        contacts_ff.setForceGroup(self.forceCount)
        self.forceCount +=1

    def loadXml(self, Xmlfile):
        R"""Loads the  *.xml* file format in the OpenMM system platform. The inputs files are generated using SMOG2 software with the flag :code:`-openSMOG`. Details on how to create the files can be found in the `SMOG2 User Manual <https://smog-server.org/smog2/>`__.
        A tutorial on how to generate the inputs files for a C-alpha model simulation can be found `here <https://opensmog.readthedocs.io>`__.

        Args:

            Xmlfile (file, required):
                The *.xml* file that contains the information on the "Contacts" potential. The *.xml* file is generated by SMOG2 software with the flag :code:`-openSMOG` and accepts Custom Potential forms. (Default value: :code:`None`).
        """

        def validate(Xmlfile):
            path = "share/openSMOG.xsd"
            pt = os.path.dirname(os.path.realpath(__file__))
            filepath = os.path.join(pt,path)

            xmlschema_doc = etree.parse(filepath)
            xmlschema = etree.XMLSchema(xmlschema_doc)

            xml_doc = etree.parse(Xmlfile)

            result = xmlschema.validate(xml_doc)
            #print("xml validation:", result)
            return result
                  
        def import_xml2OpenSMOG(file_xml):
            XML_potential = ET.parse(file_xml)

            Expression = []
            Parameters = []
            Pairs = []
            Force_Names= []

            root = XML_potential.getroot()

            for i in range(len(root[0])):

                for name in root[0][i].iter('contacts_type'):
                    Force_Names.append(name.attrib['name'])

                for expr in root[0][i].iter('expression'):
                    Expression.append(expr.attrib['expr'])
                    

                internal_Param=[]
                for par in root[0][i].iter('parameter'):
                    internal_Param.append(par.text)
                Parameters.append(internal_Param)

                internal_Pairs=[]
                for atompairs in root[0][i].iter('interaction'):
                     internal_Pairs.append(atompairs.attrib)
                Pairs.append(internal_Pairs)


            return Expression,Parameters,Pairs,Force_Names
        if not (self.forceApplied):
            if not validate(Xmlfile):
                raise ValueError("The xml file is not in the correct format")

            
            self.data = import_xml2OpenSMOG(Xmlfile)
            self._splitForces()
        
            for force in self.contacts:
                print("creating force {:} from xml file".format(force))
                self._customSmogForce(force, self.contacts[force])
                self.system.addForce(self.forcesDict[force])
            self.forceApplied = True

        else:
            print('\n Contacts forces already applied!!! \n')
        
    def createSimulation(self):

        R"""Creates the simulation context and loads into the OpenMM platform.
        """

        if not self.loaded:
            self.simulation = Simulation(self.Top.topology, self.system, self.integrator, self.platform, self.properties) 
            self.simulation.context.setPositions(self.Gro.positions)
            self.simulation.context.setVelocitiesToTemperature(self.temperature)
            self.loaded = True
        else:
            print('\n Simulations context already created! \n')
        
    def createReporters(self, trajectory=True, energies=True, forces=False, interval=1000):
        R"""Creates the reporters to provide the output data.

        Args:

            trajectory (bool, optional):
                 Whether to save the trajectory *.dcd* file containing the position of the atoms as a function of time. (Default value: :code:`True`).
            energies (bool, optional):
                 Whether to save the energies in a *.txt* file containing five columns comma-delimited. The header of the files shows the information of each collum: #"Step","Potential Energy (kJ/mole)","Kinetic Energy (kJ/mole)","Total Energy (kJ/mole)","Temperature (K)". (Default value: :code:`True`).
            forces (bool, optional):
                 Whether to save the potential energy for each applied force in a *.txt* file containing several columns comma-delimited. The header of the files shows the information of each collum. An example of the header is: #"Step","eletrostastic","Non-Contacts","Bonds","Angles","Dihedrals","contact_1-10-12". (Default value: :code:`False`).
            interval (int, required):
                 Frequency to write the data to the output files. (Default value: :code:`10**3`)
        """

        if trajectory:
            dcdfile = os.path.join(self.folder, self.name + '_trajectory.dcd') 
            self.simulation.reporters.append(DCDReporter(dcdfile, interval))

        if energies:
            energyfile = os.path.join(self.folder, self.name+ '_energies.txt') 
            self.simulation.reporters.append(StateDataReporter(energyfile, interval, step=True, 
                                                          potentialEnergy=True, kineticEnergy=True,
                                                            totalEnergy=True,temperature=True, separator=","))
        if forces:
            forcefile = os.path.join(self.folder, self.name+ '_forces.txt')
            self.simulation.reporters.append(forcesReporter(forcefile, interval, self.forcesDict, step=True)) 
            
    def run(self, nsteps, report=True, interval=10**4):
        R"""Run the molecular dynamics simulation.

        Args:

            nsteps (int, required):
                 Number of steps to perform the simulation. (Default value: :code:`10**7`)
            report (bool, optional):
                Whether to print the simulation progress. (Default value: :code:`True`).
            interval (int, required):
                 Frequency to print the simulation progress. (Default value: :code:`10**4`)
        """

        if report:
            self.simulation.reporters.append(StateDataReporter(stdout, interval, step=True, remainingTime=True,
                                                  progress=True, totalSteps=nsteps, separator="\t"))
        self.simulation.step(nsteps)
