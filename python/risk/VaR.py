#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct  8 18:31:30 2022

@author: felipems
"""
# Example of VaR calculation and ploting

import matplotlib.pyplot as plt
import scipy.stats as stats
import numpy as np


def define_partion(f, cut_off, spacing, size):
    a = 0
    while not f.pdf(a) < cut_off:
        a -= spacing

    b = 0
    while not f.pdf(b) < cut_off:
        b += spacing

    return np.linspace(a, b, int(size))


# Calculates de Value at Risk from probability density function
def VaR(f, p, cut_off=10e-6, spacing=0.1, size=10000):
    x = define_partion(f, cut_off, spacing, size)
    for arg in x:
        if f.cdf(arg) >= p:
            var = arg
            break

    plot_VaR(f, x, var)

    return var


# Plots PDF graph with VaR
def plot_VaR(f, x, var):
    plt.xlabel('Asset Return', fontsize='x-large')
    plt.ylabel('PDF', fontsize='x-large')
    plt.title('Value at Risk Example', fontsize='xx-large')

    aux = np.array([arg for arg in x if arg <= var])

    plt.fill_between(aux, f.pdf(aux), color='red', alpha=0.45)
    plt.plot(x, f.pdf(x), color='black')
    plt.vlines(var, 0, f.pdf(var), color='black')

    plt.text(var*(1-0.1), f.pdf(var)*0.1, '$VaR = {}$'.format(-int(var)),
             color='blue', fontsize='xx-large')

    plt.show()
    return


# Example
example = VaR(f=stats.norm(0, 80), p=0.02)
print('VaR = {}'.format(example))
