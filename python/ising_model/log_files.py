#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 10 13:45:28 2022

@author: felipems
"""
from datetime import datetime
import os

# Class to deal with output files----------------------------------------------
class Log():

    def __init__(self, file_name, location):
        self._location = location
        self.__file = open(os.path.join(location, file_name), 'w')

    def write(self, text):
        self.__file.write(text)

    def close(self):
        self.__file.close()

    def write_energy_measurement(self, lattice, step):
        self.__file.write("%10d   %10.3f   %8.6f\n" %
                          (step+1, lattice.energy, lattice.energy_per_spin))

    def write_mag_measurement(self, lattice, step):
        self.__file.write("%10d   %6d   %10.6f\n" %
                          (step+1, lattice.mag, lattice.mag_per_spin))

    def write_log_measurement(self, step_time, step):
        self.__file.write("--- Step {} took {} ---\n".format(
                          step+1, datetime.now() - step_time))
# -----------------------------------------------------------------------------
