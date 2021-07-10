.. _installation:

============
Installation
============

Installing OpenSMOG
===================

The **OpenSMOG** library can be installed via `conda <https://conda.io/projects/conda/>`_ or pip, or compiled from source.

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

The **OpenSMOG** library uses OpenMM API.
These requirements can be met by installing the following packages from the `conda-forge channel <https://conda-forge.org/>`__:

.. code-block:: bash

    conda install -c conda-forge openmm
    
    
Install SMOG2
=============

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