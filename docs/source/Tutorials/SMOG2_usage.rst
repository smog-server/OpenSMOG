.. _SMOG2_usage:

====================================
Using SMOG2 - C-alpha and All-Atoms
====================================

Creating Input files for OpenSMOG
==================================

This tutorial should take between 5 to 10 minutes of reading and generation the input files. Here, it will be used **SMOG2** software to generate the SBM (Structure-Based Model) input files for **OpenSMOG** simulations. To install SMOG2, please check the installation guide `here <https://opensmog.readthedocs.io/en/latest/GettingStarted/install.html#installing-smog2>`_ . Details of the usage of SMOG2 are described in the `manual <https://smog-server.org/smog2/>`_.


The following instructions will use a PDB file of CI2 protein (`2ci2.pdb <https://www.rcsb.org/structure/2CI2>`_).

First, download the `2ci2.pdb <https://www.rcsb.org/structure/2CI2>`_ file:

.. code-block:: bash

    wget http://www.rcsb.org/pdb/files/2ci2.pdb


Then, it is necessary to clean up the file to keep only the relevant information for building the model. In this case, let us keep only the ATOM lines:

.. code-block:: bash

    grep "^ATOM" 2ci2.pdb > 2ci2.atoms.pdb

.. note:: Note that, sometimes, you also want HETATMs. This is up to the user. HETATMs can be things that we don't want to include (e.g. HOH), or things that we may want to included (e.g. posttranslational modifications). In this case, we only want ATOM lines.


Next, add an END line to the 2ci2.atoms.pdb:

.. code-block:: bash

    sed -i -e "\$aEND" 2ci2.atoms.pdb

Adjust the file, so that the naming convention conforms with the default models: 

.. code-block:: bash

    smog_adjustPDB -i 2ci2.atoms.pdb -o 2ci2.adj.pdb

C-alpha model
-----------------    
Use the adjusted file to generate your input CA model:

.. code-block:: bash

    smog2 -i 2ci2.adj.pdb -CA -dname 2ci2.CA -openSMOG

All-Atoms model
-----------------

To generate the All-Atoms input files, only change the flag -CA to -AA:

.. code-block:: bash

    smog2 -i 2ci2.adj.pdb -AA -dname 2ci2.AA -openSMOG

.. note:: For running the simulations, there are differences in the simulation setup. For example, in the case of AA, the cutoff should be shorter than the CA model, and the timestep should be larger. Please, check the C-alpha and All-Atoms simulation tutorial pages.