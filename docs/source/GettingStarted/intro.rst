.. _intro:

============
Introduction
============

OpenSMOG is a Python library for performing molecular dynamics simulations using Structure-Based Models :cite:p:`noel2016smog`. OpenSMOG uses the `OpenMM <http://openmm.org/>`_ Python API that supports a wide variety of potential forms, which includes the most commonly employed C-alpha :cite:p:`clementi2000topological` and All-Atom :cite:p:`whitford2009all` models.
The input files are generated using SMOG2 software with the flag :code:`-openSMOG`. Details on how to create the files can be found in the `SMOG2 User Manual <https://smog-server.org/smog2/>`__.

.. image:: ../images/OpenSMOG_pipeline.jpg

.. bibliography::
    :style: unsrt
