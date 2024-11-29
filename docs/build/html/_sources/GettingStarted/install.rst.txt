.. _install:

============
Installation
============

Installing OpenSMOG
===================

The **OpenSMOG** library can be installed via `conda <https://conda.io/projects/conda/>`_ or `pip <https://pypi.org/>`_, or compiled from `source (GitHub) <https://github.com/smog-server/OpenSMOG>`_.

Install via conda
-----------------

The code below will install **OpenSMOG** from `conda-forge <https://anaconda.org/conda-forge/OpenSMOG>`_.

.. code-block:: bash

    conda install -c conda-forge OpenSMOG

Install via pip
-----------------

The code below will install **OpenSMOG** from `PyPI <https://pypi.org/project/OpenSMOG/>`_.

.. code-block:: bash

    pip install OpenSMOG

Install OpenMM
--------------

The **OpenSMOG** library uses `OpenMM <http://openmm.org/>`_ API to run the molecular dynamics simulations.
**OpenMM**  may be installed from the `conda-forge channel <https://conda-forge.org/>`__:

.. code-block:: bash

    conda install -c conda-forge openmm
    
The following libraries are **required** when installing **OpenSMOG**:

    - `Python <https://www.python.org/>`__ (>=3.6)
    - `NumPy <https://www.numpy.org/>`__ (>=1.14)
    - `ElementTree XML <https://docs.python.org/3/library/xml.etree.elementtree.html>`__ (>=2.2.0)

Installing SMOG2
================

The input files for **OpenSMOG** simulations are generated using `SMOG2 <https://smog-server.org/smog2>`_ (version 2.4, or newer). Here, there is a quick installation guide based on `conda <https://conda.io/projects/conda/>`_ (Linux and Windows-WSL only). Alternate installation options are described in the SMOG2 manual.

First, create a new environment and activate it:

.. code-block:: bash

    conda create --name smog2.4 perl
    
.. code-block:: bash

    conda activate smog2.4

Next, it is necessary to instal a few **Perl** modules (a complete list of modules is in the SMOG2 README file):

.. code-block:: bash

    conda install -c bioconda perl-xml-simple perl-xml-libxml java-jdk

.. code-block:: bash

    conda install -c eumetsat perl-pdl

.. code-block:: bash

    perl -MCPAN -e 'install XML::Validator::Schema'

Enter the **Perl** and **smog2** paths in the configure.smog2 file.

Then load and test your **smog2** configuration:

.. code-block:: bash

    source configure.smog2
    
.. code-block:: bash

    ./test-config
    
It is also **STRONGLY** recommended that you download **smog-check** (available at smog-server.org) and run all tests before using **smog2** for production calculations.
