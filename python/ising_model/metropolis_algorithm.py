#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 10 13:42:43 2022

@author: felipems
"""

import numpy as np

# -----------------------------------------------------------------------------
# Calculates the energy diference------------------------------------------
# nn is a np.array with nearest neighbors
def energy_change_metropolis(lattice, site, nearest_neighbors_function):
    # Calls the nearest_neighbors function to find the nn.
    nn = lattice.nearest_neighbors_square(site)

    # Sums all nn spins
    aux_nn = np.sum(nn)

    # Calculates the energy change if the spin is flipped
    dE = -2*lattice.coupling_const_j*lattice[site]*aux_nn

    return dE
# -------------------------------------------------------------------------


# Metripolis algorthim ----------------------------------------------------
def metropolis(lattice, nearest_neighbors_function):
    # Randomly chooses one site
    site = [np.random.randint(0, lattice.size) for i in range(lattice.dimension)]
    # calls the energy function
    dE = energy_change_metropolis(lattice, site, nearest_neighbors_function)

# Accept or not the change
    prob = np.exp(-lattice.beta*dE)
    if prob > 1:
        lattice[site] = - lattice[site]
    else:
        aux = np.random.uniform(0, 1)
        if prob > aux:
            lattice[site] = - lattice[site]
# -------------------------------------------------------------------------
