#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 10 13:42:43 2022

@author: felipems
"""

from lattice import Lattice
from files import Log
from metropolis_algorithm import metropolis
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime
import os

# Main program ----------------------------------------------------------------
start_time = datetime.now()  # Variable with initial run time

# Parameters-------------------------------------------------------------------
d = 2                     # Square lattice dimension
N = 4                   # Lattice size N^d
T = 2.2                 # Temperature
#beta = 1.0            #
J = -1.0                  # Spins interation
step_measure = 20  # Number of step before measuring
num_measures = 30      # Number of measuments
termalization = 0  # Number of temalization steps
# -----------------------------------------------------------------------------

# Creating a lattice of an arbitrary dimension---------------------------------
lattice = Lattice(d, N, temperature=T, H=0, J=J)
# -----------------------------------------------------------------------------

# Opens output files on the same directory as .py -----------------------------
# Gets the path to current directory
__location__ = os.path.realpath(os.path.join(
    os.getcwd(), os.path.dirname(__file__)))

log_file = Log(file_name="Log_file_Ising_Model.txt", location=__location__)
ener_file = Log(file_name="Ener_file_Ising_Model.txt", location=__location__)
mag_file = Log(file_name="Mag_file_Ising_Model.txt", location=__location__)

# Writes the header of files
ener_file.write("Model de Ising %1d |n step  Energy   Energy per spin\n" % (d))
mag_file.write(
    "Model de Ising %1d |n step  Magnetization   Magnetization per spin\n"
    % (d))
# -----------------------------------------------------------------------------
# Executes the Metropolis algorithm for the number of steps
# A termalization period
termalization_time = datetime.now()

for i in range(termalization):
    metropolis(lattice, lattice.nearest_neighbors_square)

log_file.write("--- Termalization step took {} ---\n".format(
                                    datetime.now() - termalization_time))
del termalization_time, termalization
# End of termalization --------------------------------------------------------


# Runs Metropolis algorithm and measures E and M after an number of measuments
for i in range(num_measures):
    step_time = datetime.now()  # variable with the step initial time

    # Runs Metropolis algorithm step_measure times before performing a measure
    for j in range(step_measure):
        metropolis(lattice, lattice.nearest_neighbors_square)
    # -----------------------------------------------------

    lattice.measure()  # Measures
    # Writes the energy and magnetization to the output files
    ener_file.write_energy_measurement(lattice, i)
    mag_file.write_mag_measurement(lattice, i)
    log_file.write_log_measurement(start_time, i)

log_file.write("--- Execution time: {} ---\n".format(
                datetime.now() - start_time))
del step_time, step_measure, num_measures
# End of Metropolis run -------------------------------------------------------

# Closes all output files -----------------------------------------------------
log_file.close()
mag_file.close()
ener_file.close()
# -----------------------------------------------------------------------------
