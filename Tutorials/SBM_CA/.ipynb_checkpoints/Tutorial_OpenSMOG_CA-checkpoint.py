#!/usr/bin/env python
# coding: utf-8

# # C-alpha Structure-based Model simulation using OpenSMOG
# 
# This tutorial should take between 5 to 15 minutes of reading and performing simulations.

# The first step is to import the OpenSMOG module

# In[ ]:


from OpenSMOG import SBM


# SBM class sets the initial parameters of the simulation:<br>
# 
# `name="1hk0"` set the default name of each simulation *(this name is used as prefix for the outputs)* <br>
# `dt=0.002` **picoseconds** the time step used in integration <br>
# `gamma=5.0` **picoseconds** the collision rate of Langevin integrator  <br>
# `rcutoff=1.5` **nanometers** non-bonded cutoff <br>
# `temperature=1.0` **reduced units** the temperature in  
# 
# sbm_CA is a chosen variable name for the SBM object

# In[ ]:


sbm_CA = SBM(name='1hk0', dt=0.002, gamma=2.0, rcutoff =1.5, temperature=1.0)


# There are three hardware platform options to run the simulations: 
# 
# `platform="cuda"` <br>
# `platform="opencl"` <br>
# `platform="cpu"` <br>
# 
# if "cuda" or "opencl" is choosen the GPUindex can be define as "0" or "0,1" for multiples GPUS 
# 

# In[ ]:


sbm_CA.setup_openmm(platform='cuda', GPUindex='default')


# Sets the directory name where to save the simulation outputs

# In[ ]:


sbm_CA.saveFolder('output')


# Load the Gro file into the sbm_CA object
# 
# in this tutorial all input files are in input folder

# In[ ]:


sbm_CA.loadGro('input/1hk0_CA.gro')


# Load the Top file into the sbm_CA object 

# In[ ]:


sbm_CA.loadTop('input/1hk0_CA.top')


# Load the xml file into the sbm_CA objetc
# 
# this function return the name of each force added.
# 
# in this example, uses only the Lennard-Jones 10-12 potential 

# In[ ]:


sbm_CA.loadXml('input/1hk0_CA.xml')


# The Simultion context is created feeding by all information given in previous steps

# In[ ]:


sbm_CA.createSimulation()


# Create a reporters that will save data in output folder.
# 
# `trajectory=True` save trajectory in .dcd format. <br>
# `energies=True` save the energy in text format, each information is separed by a comma. <br>
# `dt_files=1000` The step interval to save both trajectory and energies data.

# In[ ]:


sbm_CA.createReporters(trajectory=True, energies=True, dt_files=1000)


# The run function receives the following parameters:
# 
# `nsteps=10**7` number os steps to perform the simulation. <br>
# `report=True` show information as output (Progress (%), Step and Time Remaining) <br>
# `interval=10**4` The step interval to show the informations 

# In[ ]:


sbm_CA.run(nsteps=10**7, report=True, interval=10**4)


# When finished the output files can be finded in output folder
