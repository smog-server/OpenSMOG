########################################################
# opensmogcheck.py is a short script that will see if 
# OpenSMOG and (optionally) SMOG2 are working well
# together.  See smog-server.org for more information.
#
# Copyright (c) 2020, 2021, 2022 Center for Theoretical
# Biological Physics at Rice University and Northeastern
# University
########################################################

# try to find OpenSMOG
try:
	from OpenSMOG import SBM
except:
	print('Failed to import OpenSMOG libraries. Check your configuration.')
	sys.exit(1)


# with OpenMM 7.7.0, the import calls have changed. So, try both, if needed
try:
	try:
		# >=7.7.0
		import openmm.app as app
	except:
		# earlier
		print('Unable to load OpenMM as \'openmm\'. Will try the older way \'simtk.openmm\'')
		import simtk.openmm.app as app
except:
	print('Failed to load OpenMM. Check your configuration.')
	sys.exit(1)

import subprocess
import io
import os
import sys
import re as regex
from contextlib import redirect_stdout

# maxreldiff is the max relative deviation allowed
maxreldiff=0.00001
# maxabsdiff is the max absolute deviation allowed
maxabsdiff=0.002


# The name of each test is listed in tests/listoftests
# each line defines a test, which is a subdir of tests/
# each subdirectory has a "flags" file that gives the exact 
# flags used when calling smog2
# energies contains the gromacs-generated (or any reference 
# calculation) energies for the 10 frame..gro files

print(
'''
                       OpenSMOG-check
         For OpenSMOG v1.1.0 and SMOG v2.4.4 (or newer)

This script will use the version of SMOG2 that is found in the path
and try to generate OpenSMOG force fields. It will then calculate
the energy using the OpenSMOG force field with any available
version of OpenSMOG that is in the environment for reference 
configurations of each system. Finally, it will check if the 
potential energies are the same as a set of predefined reference 
values (typically from Gromacs).

There are currently no flags required.

For questions/suggestions email info@smog-server.org
''') 


##### subroutines #####

def alltests():
	# nummatch is the total number of energies that 
	# will need to be close, in order to pass
	# it is incremented as tests are applied
	nummatch=0
	# mcount is the number of matching energies
	mcount=0

	runsmog = which("smog2")
	print('What platform would you like to test?')
	print("\tOptions: OpenCL, HIP, CUDA, CPU, reference")
	plats = ['opencl', 'hip', 'cuda', 'cpu', 'reference']
	for line in sys.stdin:
		platform = line.rstrip()
		break
	if not (platform.lower() in plats):
		print('''Unrecognized platform! 
Options are (case-insensitive): 
OpenCL, HIP, CUDA, CPU, reference

Unable to perform tests.
''')
		sys.exit(1)	

	print("Will test platform \""+platform+"\"\n")

	list = open("tests/listoftests", "r")

	for testname in list:
		testname=testname.strip()

		PBC=False
		if regex.search(".PBC$",testname):
			PBC=True

		sysname = "tests/"+testname+"/"
		nummatch+=10
		print("STARTING TEST FOR SYSTEM IN "+testname)
		if runsmog:
			runSMOG(sysname)
		sbm_test = prepOpenSMOG(runsmog,sysname,platform,PBC)
		energies = open(sysname+"energies", "r")
		for frame in range(10):
			newgro = app.GromacsGroFile(sysname+"frame."+str(frame)+".gro")
			sbm_test.simulation.context.setPositions(newgro.positions)
			new=newgro.getPeriodicBoxVectors()
			sbm_test.simulation.context.setPeriodicBoxVectors(new[0],new[1],new[2])
			e_pot_frame = sbm_test.simulation.context.getState(getEnergy=True).getPotentialEnergy()
			num=str(e_pot_frame).split(" ",1)[0]
			openv=energies.readline()
			mcount += comparevalues(openv,num)
		print("COMPLETED TEST FOR SYSTEM IN "+testname+"\n")
                # these two lines can be uncommented, if we want to regenerate the reference templates for fall-back option
		#subprocess.run("cp opentest.xml "+sysname,shell=True)
		#subprocess.run("cp opentest.top "+sysname,shell=True)
                ##############
		if runsmog:
			subprocess.run('rm opentest*',shell=True)

	print(str(mcount) + " of " + str(nummatch) + " values matched")

	if nummatch == 0:	
		print("\n\nNO TESTS PERFORMED.  SOMETHING WENT WRONG!!!!\n\n")
		sys.exit(1)	
	elif mcount == nummatch:
		print("\n\nPASSED ALL CHECKS!!!!\n\n")
		sys.exit(0)	
	else: 
		print("\n\nFAILED CHECKS!!!!\n\n")
		sys.exit(1)	

def runSMOG(sysname):
	# based on the sysname, find the flags and run SMOG2
	with open(sysname+"smogcommands", "r") as f:
		for line in f:
			command = line.split()

			try:
				out=subprocess.run(command,stdout=subprocess.PIPE,stderr=subprocess.PIPE,check=True)	
			except subprocess.CalledProcessError as e:
				print("SMOG 2 failed to generate OpenSMOG input!!!!\n")
				print("STDERR:\n")
				print((e.stderr).decode())
				print("STDOUT:\n")
				print((e.stdout).decode())
				sys.exit(1)	


def prepOpenSMOG(runsmog,sysname,platform,PBC):
	# make and return a system.
	if runsmog:
		topname="opentest.top"
		xmlname="opentest.xml"
	else:
		topname=sysname+"opentest.top"
		xmlname=sysname+"opentest.xml"


	f = open(os.devnull, 'w')
	with redirect_stdout(f):
		sbm_test = SBM(name='testss', time_step=0.002, collision_rate=1.0, r_cutoff=2, temperature=0.1, pbc = PBC, warn = False)
		sbm_test.setup_openmm(platform=platform,GPUindex='default')
		sbm_test.saveFolder('.')
		sbm_test.loadSystem(Grofile=sysname+"frame.0.gro", Topfile=topname, Xmlfile=xmlname)
		sbm_test.createSimulation()
	return sbm_test

def comparevalues(ref,open):
	absdiff=abs(float(ref)-float(open))
	reldiff=abs(absdiff/float(ref))
	if absdiff < maxabsdiff or reldiff < maxreldiff:
		return 1
	else:
		print("BAD VALUES:"+ref.rstrip()+" (reference) and "+open+" (OpenSMOG)")
		return 0 

def which(exe):
	for dir in os.getenv("PATH").split(':'):
		if (os.path.exists(os.path.join(dir, exe))):
			print ('SMOG2 version found:%s/%s\n' % (dir, exe))
			return 1

	print ('''
NOTE: Did not find smog2 in path. Will test OpenSMOG library,
but not the generation of force fields with SMOG2.  Use
smog-check to ensure SMOG 2 is also functioning properly.
''')
	return 0
			
#end of subroutines

# call main program
alltests()
