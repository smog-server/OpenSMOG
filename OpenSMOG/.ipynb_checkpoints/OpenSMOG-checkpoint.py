# Copyright (c) 2020-2021 The Center for Theoretical Biological Physics (CTBP) - Rice University
# This file is from the OpenSmog project, released under the MIT License. 

R"""  
The :class:`~.OpenSmog` classes perform Molecular dynamics using Structure-based Models for Biomolecules.
"""

from simtk.openmm.app import *
from simtk.openmm import *
from simtk.unit import *
import os
import numpy as np
import xml.etree.ElementTree as ET
from sys import stdout


class SBM:

    R"""  
    The :class:`~.SBM` classes perform Molecular dynamics using Structure-based Models for Biomolecules.
    """
    
    def __init__(self, 
        name = "SBM",
        dt = 0.002,
        gamma = 1.0,
        rcutoff = 1.5,
        temperature = 1):
        
            self.name = name
            self.dt = dt * picoseconds
            self.gamma = gamma / picosecond
            self.rcutoff = rcutoff * nanometers  
            self.temperature = temperature * 120.0 * kelvin
            self.forceApplied = False
            self.loaded = False
            self.folder = "."
            
    def setup_openmm(self, platform='cuda', precision='mixed', GPUindex='default', integrator="langevin"):
        
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
        
    def saveFolder(self, folder):       
       
    
        if os.path.exists(folder) == False:
            os.mkdir(folder)
        self.folder = folder    
        
    def loadGro(self, Grofile):
        self.Gro = GromacsGroFile(Grofile)
        
    def loadTop(self, Topfile):
        self.Top = GromacsTopFile(Topfile)
        self.system = self.Top.createSystem(nonbondedMethod=CutoffNonPeriodic,nonbondedCutoff=self.rcutoff)
        
    def _splitForces(self):
        n_forces =  len(self.data[3])

        forces = {}
        for n in range(n_forces):
            forces[self.data[3][n]] = [self.data[0][n], self.data[1][n], self.data[2][n]]
        self.contacts = forces
        
    def customSmogForce(self, name, data):
       

        #first set the equation
        contacts_ff = CustomBondForce(data[0])

        #second set the number of variable
        for pars in data[1]:
            contacts_ff.addPerBondParameter(pars)

        #third, apply the bonds from each pair of atoms and the related variables.
        pars = [pars for pars in data[1]]
        #print(pars)
        for iteraction in data[2]:
            atom_index_i = int(iteraction['i'])-1 #check where start the polymer
            atom_index_j = int(iteraction['j'])-1
            parameters = [float(iteraction[k]) for k in pars]
            #print(atom_index_i, atom_index_j, parameters)
            contacts_ff.addBond(atom_index_i, atom_index_j, parameters)

        self.forceDict[name] =  contacts_ff
        
    def loadXml(self, Xmlfile):        
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
            self.data = import_xml2OpenSMOG(Xmlfile)
            self._splitForces()
        
            for force in self.contacts:
                print("creating force {:} from xml file".format(force))
                self.customSmogForce(force, self.contacts[force])
                self.system.addForce(self.forceDict[force])
            self.forceApplied = True
        else:
            print('\n Contacts forces already applied!!! \n')
        
    def createSimulation(self):
        if not self.loaded:
            self.simulation = Simulation(self.Top.topology, self.system, self.integrator, self.platform, self.properties) 
            self.simulation.context.setPositions(self.Gro.positions)
            self.simulation.context.setVelocitiesToTemperature(self.temperature)
            self.loaded = True
        else:
            print('\n Simulations context already created! \n')
        
    def createReporters(self, trajectory=True, energies=True, dt_files=1000):
        if trajectory:
            dcdfile = os.path.join(self.folder, self.name + '_trajectory.dcd') 
            self.simulation.reporters.append(DCDReporter(dcdfile, dt_files))

        if energies:
            energyfile = os.path.join(self.folder, self.name+ '_energies.txt') 
            self.simulation.reporters.append(StateDataReporter(energyfile, dt_files, step=True, 
                                                          potentialEnergy=True, kineticEnergy=True,
                                                            totalEnergy=True,temperature=True, separator=","))
            
    def run(self, nsteps, report=True, interval=500):
        if report:
            self.simulation.reporters.append(StateDataReporter(stdout, interval, step=True, remainingTime=True,
                                                  progress=True, totalSteps=nsteps, separator="\t"))
        self.simulation.step(nsteps)
