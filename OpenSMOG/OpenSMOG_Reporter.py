# Copyright (c) 2020-2021 The Center for Theoretical Biological Physics (CTBP) - Rice University
# This file is from the OpenSMOG project, released under the MIT License. 

R"""  
The :class:`~.OpenSMOG_Reporter` class stores the potential energy information for each force applied in the system.
"""

from simtk.openmm.app import *
from simtk.openmm import *
from simtk.unit import *
import os
import warnings
from sys import stdout

class forcesReporter(StateDataReporter):
    def __init__(self, file, reportInterval, forces=None, **kwargs):
        super(forcesReporter, self).__init__(file, reportInterval, **kwargs)
        self._forces = forces
    
    def _constructHeaders(self):
        headers = super()._constructHeaders()

        for n in self._forces:
            headers.append(str(n))

        return headers
    def _constructReportValues(self, simulation, state):

        values = super()._constructReportValues(simulation, state)

        for i,n in enumerate(self._forces):
            values.append(simulation.context.getState(getEnergy=True, groups={i}).getPotentialEnergy().value_in_unit(kilojoules_per_mole))

        return values