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

OpenSMOG is a Python library for performing molecular dynamics simulations using Structure-Based Models. OpenSMOG uses the  `OpenMM <http://openmm.org/>`_. Python API employing a wide variety of potential forms, including the most commonly employed models such as the C-alpha and All-Atoms.
The input files are generated using SMOG2 software with the flag :code:`-openSMOG`. Details on how to create the files can be found in the `SMOG2 User Manual <https://smog-server.org/smog2/>`__.

.. raw:: html

    <p align="center">
    <img align="center" src="./docs/source/images/OpenSMOG_pipeline.jpg">
    </p>

Resources
=========

- `Reference Documentation <https://opensmog.readthedocs.io/>`__: Examples, tutorials, and class details.
- `Installing OpenSMOG <https://opensmog.readthedocs.io/en/latest/GettingStarted/install.html#installing-opensmog>`__: Instructions for installing **OpenSMOG**.
- `Installing SMOG2 <https://opensmog.readthedocs.io/en/latest/GettingStarted/install.html#installing-smog2>`__: Instructions for installing **SMOG2**.
- `GitHub repository <https://github.com/junioreif/OpenSMOG/>`__: Download the **OpenMiChroM** source code.
- `Issue tracker <https://github.com/junioreif/OpenSMOG/issues>`__: Report issues/bugs or request features.


Citation
========

When using **OpenSMOG** to perform chromatin dynamics simulations or analyses, please `use this citation
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
    - `ElementTree XML <https://docs.python.org/3/library/xml.etree.elementtree.html>`__ (>=2.2.0)

Installing SMOG2
================

The inputs **OpenSMOG** simulations are generated using `SMOG2 <https://smog-server.org/smog2>`_ > 2.4. Here, there is a quick installation guide based on `conda <https://conda.io/projects/conda/>`_.

First, just create a new environment and activate it:

.. code-block:: bash

    conda create --name smog2.4 perl
    
.. code-block:: bash

    conda activate smog2.4

Next, it is necessary an installation of a few **Perl** modules:

.. code-block:: bash

    conda install -c bioconda perl-xml-simple perl-xml-libxml java-jdk

.. code-block:: bash

    conda install -c eumetsat perl-pdl

.. code-block:: bash

    perl -MCPAN -e 'install XML::Validator::Schema'

Add the **Perl** and **smog2** path into the configure.smog2 file.

.. hint:: Use the following command line to find out which installed **Perl** is being used.

.. code-block:: bash

    which perl

Then load and test the **smog2** installation:

.. code-block:: bash

    source configure.smog2
    
.. code-block:: bash

    ./test-config
