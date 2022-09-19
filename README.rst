========
OpenSMOG
========

|Citing OpenSMOG|
|PyPI|
|conda-forge|
|ReadTheDocs|
|SMOG server|
|Update|
|GitHub-Stars|

.. |Citing OpenSMOG| image:: https://img.shields.io/badge/cite-OpenSMOG-informational
   :target: https://opensmog.readthedocs.io/en/latest/Reference/citing.html
.. |PyPI| image:: https://img.shields.io/pypi/v/OpenSMOG.svg
   :target: https://pypi.org/project/OpenSMOG/
.. |conda-forge| image:: https://img.shields.io/conda/vn/conda-forge/OpenSMOG.svg
   :target: https://anaconda.org/conda-forge/OpenSMOG
.. |ReadTheDocs| image:: https://readthedocs.org/projects/opensmog/badge/?version=latest
   :target: https://opensmog.readthedocs.io/en/latest/
.. |SMOG server| image:: https://img.shields.io/badge/SMOG-Server-informational
   :target: https://smog-server.org/
.. |Update| image:: https://anaconda.org/conda-forge/opensmog/badges/latest_release_date.svg
   :target: https://anaconda.org/conda-forge/opensmog
.. |GitHub-Stars| image:: https://img.shields.io/github/stars/junioreif/OpenSMOG.svg?style=social
   :target: https://github.com/junioreif/OpenSMOG


`Documentation <https://opensmog.readthedocs.io/>`__
| `Install <https://opensmog.readthedocs.io/en/latest/GettingStarted/install.html>`__
| `Tutorials <https://opensmog.readthedocs.io/en/latest/Tutorials/SBM_CA.html>`__

Overview
========

OpenSMOG is a Python library for performing molecular dynamics simulations using Structure-Based Models. OpenSMOG uses the  `OpenMM <http://openmm.org/>`_. Python API, which supports a wide variety of potential energy functions, including those that are commonly employed in C-alpha and all-atom models.
While it is possible to use this library in a standalone fashion, it is expected that users will generate input files using the SMOG2 software (version 2.4, or later, with the flag :code:`-OpenSMOG`). Details on how to generate OpenSMOG-compatible force fields files can be found in the `SMOG2 User Manual <https://smog-server.org/smog2/>`__.

.. raw:: html

    <p align="center">
    <img align="center" src="./docs/source/images/OpenSMOG_pipeline.jpg">
    </p>



Citation
========

When using **OpenSMOG** and **SMOG2**, please `use the following references
<https://opensmog.readthedocs.io/en/latest/Reference/citing.html>`__.



Installation
============

The **OpenSMOG** library can be installed via `conda <https://conda.io/projects/conda/>`_ or `pip <https://pypi.org/>`_, or compiled from `source (GitHub) <https://github.com/junioreif/OpenSMOG>`_.

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
These requirements can be met by installing the following packages from the `conda-forge channel <https://conda-forge.org/>`__:

.. code-block:: bash

    conda install -c conda-forge openmm
    
The following are libraries **required** for installing **OpenSMOG**:

    - `Python <https://www.python.org/>`__ (>=3.6)
    - `NumPy <https://www.numpy.org/>`__ (>=1.14)
    - `lxml <https://lxml.de/>`__ (>=4.6.2)

Installing SMOG2
================

The inputs **OpenSMOG** simulations are generated using `SMOG2 <https://smog-server.org/smog2>`_ (version 2.4 and later). Here, there is a quick installation guide based on `conda <https://conda.io/projects/conda/>`_ (Linux and Windows-WSL only).

First, download SMOG 2 (v2.4, or later) at `smog-server.org <https://smog-server.org/smog2/>`__

Second, create a new conda environment and activate it (called smog2.4, but name as appropriate):

.. code-block:: bash

    conda create --name smog2.4 perl
    
.. code-block:: bash

    conda activate smog2.4

Next, it is necessary to install a few **Perl** modules:

.. code-block:: bash

    conda install -c bioconda perl-xml-simple perl-xml-libxml java-jdk

.. code-block:: bash

    conda install -c eumetsat perl-pdl

.. code-block:: bash

    perl -MCPAN -e 'install XML::Validator::Schema'

Add the **Perl** and **smog2** path into the configure.smog2 file (described in the README that comes with SMOG 2).

.. hint:: Use the following command line to find out which installed **Perl** is being used.

.. code-block:: bash

    which perl

Then load and test the **smog2** installation:

.. code-block:: bash

    source configure.smog2
    
.. code-block:: bash

    ./test-config
    
As described in the SMOG 2 manual, it is highly recommended that you also download smog-check and run all checks before using the SMOG 2 software.

Verifying your installation
=========

After you have installed OpenSMOG (and optionally SMOG 2), you can check to see that the code is functioning properly using OpenSMOGcheck. To run the check, you just need to run the following commands (from within python):

.. code-block:: bash

    from OpenSMOG import SBM
    SBM.opensmogcheck()

If smog2 is in your path, then this script will check compatibility of SMOG2 and OpenSMOG.  If smog2 is not in your path, it will simply evaluate the energies for representative models/configurations and compare them to reference values.

Resources
=========

- `Reference Documentation <https://opensmog.readthedocs.io/>`__: Examples, tutorials, and class details.
- `Installing OpenSMOG <https://opensmog.readthedocs.io/en/latest/GettingStarted/install.html#installing-opensmog>`__: Instructions for installing **OpenSMOG**.
- `Installing SMOG2 <https://opensmog.readthedocs.io/en/latest/GettingStarted/install.html#installing-smog2>`__: Instructions for installing **SMOG2**.
- `Issue tracker <https://github.com/smog-server/OpenSMOG/issues>`__: Report issues/bugs or request features.
