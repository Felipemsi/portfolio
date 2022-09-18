#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 29 10:04:14 2022

@author: felipems
"""
import numpy as np
import os
# from decimal import Decimal, getcontext

# -----------------------------------------------------------------------------
class Lattice():

    #--------------------------------------------------------------------------
    def __init__(self, dimension, size, spin_type=[-1, 1],
                 spin_prob=[0.5, 0.5], lattice_type='square',
                 temperature=1.0, H=0, J=-1.0):

        self.__dimension = dimension
        self.__size = size
        self.__num_spins = self.__size**self.__dimension
        self.__lattice_type = lattice_type

        dim = [self.__size for i in range(self.__dimension)]
        self.__lattice = np.empty(tuple(dim), dtype=int)
        del dim

        self.__energy = 0.0
        self.__mag = 0
        self.__energy_per_spin = 0
        self.__mag_per_spin = 0

        self.__spin = np.array(spin_type, dtype=int)
        self.__spin_prob = spin_prob
        self.__temperature = temperature
        self.__beta = 1.0/self.__temperature
        self.__coupling_const_j = J
        self.__mag_field_h = H

        self.random_conf()
        self.update_energy()
        self.update_magnetization()
    #--------------------------------------------------------------------------

    # Dunder method to atribute a new value to the site
    def __setitem__(self, site, new_spin_value):
        self.__lattice[tuple(site)] = new_spin_value

    # Dunder method to return the spin value of the site 
    def __getitem__(self, site):
        return self.__lattice[tuple(site)]

    # Dunder method to print the np.ndarray with Lattice 
    def __str__(self):
        return str(self.__lattice)

    # Dunder method to make Lattice class iterable 
    def __iter__(self):
        return np.nditer(self.__lattice)

    def update_energy(self):
        # Energy measure
        aux_site = np.zeros(self.__dimension, dtype=int)
        # aux_site is an np.array with some site indexes
        # dimension is  the current dimension in the loop
        index = 0
        self.__energy = 0  # Total Energy
        self.loop_over_lattice(aux_site, index, self.sum_energy_of_a_site)
        
    def update_magnetization(self):
        self.__mag = np.sum(self.__lattice)  # Magnetization

    # Creates a random lattice 
    def random_conf(self):
    # Creates the lattice
        aux = np.zeros(self.__dimension, dtype=int)
        index = 0
        self.loop_over_lattice(aux, index, self.random_site)
    # -------------------------------------------------------------------------

    # Chooses one spin for some site with p probability
    # site is an np.array with the site coordinations
    def random_site(self, site):
        self.__lattice[tuple(site)] = np.random.choice(self.__spin, 
                                                       p=self.__spin_prob)
    # -------------------------------------------------------------------------

    # Loop to run over all lattice in an arbitrary dimension-------------------
    # aux is an np.array with some site indexes
    # index is  the current index in the loop
    # function is a function that will operate in the aux site.
    def loop_over_lattice(self, aux, index, function=None):
        if index == self.__dimension - 1:
            for i in range(self.__size):
                aux[index] = i
                function(aux)
        else:
            for i in range(self.__size):
                aux[index] = i
                self.loop_over_lattice(aux, index + 1, function)
    # -------------------------------------------------------------------------

    # Measures energy E and magnetization M, then writes on output files ------
    def measure(self):
        # Energy measure
        self.update_energy()
        self.__energy_per_spin = self.__energy/self.__num_spins # Ener per spin

        # Magnetization measure
        self.update_magnetization()
        self.__mag_per_spin = self.__mag/self.__num_spins # Mag per spin
    # -------------------------------------------------------------------------

    # Finds the nearest neighbors ---------------------------------------------
    # site is an np.array with the site coordinations
    def nearest_neighbors_square(self, site):
        d = self.__dimension
        N = self.__size
        nn = np.zeros(2*d, dtype=int)
        for i in range(d):
            if site[i] == 0:
                aux = np.zeros(d, dtype=int)
                aux[i] = N - 1
                aux = aux + site
                nn[2*i] = self.__lattice[tuple(aux)]
                aux = np.zeros(d, dtype=int)
                aux[i] = 1
                aux = aux + site
                nn[2*i+1] = self.__lattice[tuple(aux)]
            elif site[i] == N-1:
                aux = np.zeros(d, dtype=int)
                aux[i] = -1
                aux = aux + site
                nn[2*i] = self.__lattice[tuple(aux)]
                aux = np.zeros(d, dtype=int)
                aux[i] = 1-N
                aux = aux + site
                nn[2*i+1] = self.__lattice[tuple(aux)]
            else:
                aux = np.zeros(d, dtype=int)
                aux[i] = -1
                aux = aux + site
                nn[2*i] = self.__lattice[tuple(aux)]
                aux = np.zeros(d, dtype=int)
                aux[i] = 1
                aux = aux + site
                nn[2*i+1] = self.__lattice[tuple(aux)]

        return nn
    #--------------------------------------------------------------------------

    # Sums the energy of the interaction of the site with its 
    # nearest neighbors nn
    # site is an np.array with the site coordinations
    def sum_energy_of_a_site(self, site):
        # Calls the nearest_neighbors function to find the nn.
        nn = self.nearest_neighbors_square(site)

        # Sums all nn spins
        aux_nn = np.sum(nn)
        aux_site = self.__lattice[tuple(site)]

        # Sums the nn-site energy to the E in Measure function
        # Notice that each interation is summed twice
        self.__energy += 0.5*self.__coupling_const_j*aux_site*aux_nn
        self.__energy -= self.__mag_field_h*aux_site
    # -------------------------------------------------------------------------

    @property
    def size(self):
        return self.__size

    @property
    def dimension(self):
        return self.__dimension

    @property
    def energy(self):
        return self.__energy

    @property
    def mag(self):
        return self.__mag

    @property
    def energy_per_spin(self):
        return self.__energy_per_spin

    @property
    def mag_per_spin(self):
        return self.__mag_per_spin

    @property
    def temperature(self):
        return self.__temperature

    @temperature.setter
    def temperature(self, new_temperature):
        self.__temperature = new_temperature
        self.__beta = 1/new_temperature

    @property
    def beta(self):
        return self.__beta

    @beta.setter
    def beta(self, new_beta):
        self.__beta = new_beta
        self.__temperature = 1/new_beta

    @property
    def mag_field_h(self):
        return self.__mag_field_h

    @mag_field_h.setter
    def mag_field_h(self, new_h):
        self.__mag_field_h = new_h

    @property
    def coupling_const_j(self):
        return self.__coupling_const_j

    @coupling_const_j.setter
    def coupling_const_j(self, new_j):
        self.__coupling_const_j = new_j

# End of Lattice class --------------------------------------------------------

