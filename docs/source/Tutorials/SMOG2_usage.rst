.. _SMOG2_usage:

=====================================================================
Using SMOG2 to generate  C-alpha and All-Atom Structure-Based models
=====================================================================


This tutorial should take between 5 to 10 minutes to complete. Here, we will use the **SMOG2** software pacakge to generate the SBM (Structure-Based Model) input files that will be used to perform a simulation with **OpenSMOG**. To install SMOG2, please check the installation notes in the SMOG 2 user manual, or use the guide `here <https://opensmog.readthedocs.io/en/latest/GettingStarted/install.html#installing-smog2>`_. Details of SMOG2 usage and options are described in the `manual <https://smog-server.org/smog2/>`_. It is assumed that the executable **smog2** is in your path.


Preparing your PDB file
===============================

The following instructions will use a PDB file of CI2 protein (`2ci2.pdb <https://www.rcsb.org/structure/2CI2>`_).

First, download the PDB file:

.. code-block:: bash

    wget http://www.rcsb.org/pdb/files/2ci2.pdb


Then, it is necessary to clean up the file and only keep information needed to define a structure-based model. In this case, let us keep only the ATOM lines:

.. code-block:: bash

    grep "^ATOM" 2ci2.pdb > 2ci2.atoms.pdb

.. note:: Sometimes, you also want HETATMs. This is up to the user. HETATMs can be things that we don't want to include (e.g. HOH), or things that we may want to included (e.g. posttranslational modifications). In this case, we only want ATOM lines.


Next, add an END line to the file 2ci2.atoms.pdb:

.. code-block:: bash

    sed -i -e "\$aEND" 2ci2.atoms.pdb

Adjust the file, so that the naming convention conforms with the default SMOG models: 

.. code-block:: bash

    smog_adjustPDB -i 2ci2.atoms.pdb -o 2ci2.adj.pdb

Generate OpenSMOG input files for a C-alpha model
==================================    
Use the adjusted file to generate your input CA model:

.. code-block:: bash

    smog2 -i 2ci2.adj.pdb -CA -dname 2ci2.CA -OpenSMOG

Generate OpenSMOG input files for an all-atom model
==================================

To generate input files for the all-atom model, you only need to change the flag -CA to -AA:

.. code-block:: bash

    smog2 -i 2ci2.adj.pdb -AA -dname 2ci2.AA -OpenSMOG

.. note:: When running the simulation in OpenSMOG, there are differences in the simulation protocols and settings. For example, in the case of AA, the cutoff is typically much shorter than the values used with the CA model. However, larger timesteps can typically be used with the AA model. Please, check the `C-alpha <https://opensmog.readthedocs.io/en/latest/Tutorials/SBM_CA.html>`_  and `All-Atom <https://opensmog.readthedocs.io/en/latest/Tutorials/SBM_AA.html>`_ simulation tutorial pages.
