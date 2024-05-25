#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Aug  7 10:57:48 2022

@author: felipems
"""

import numpy as np
import math as math


# x_1 + (x_2 - x_1)/2 is used to avoid error from round-off.
# (x_1 + x_2) / 2 can return a value out of [x_1,x_2] interval
def middle_point(x_1, x_2):
    return x_1 + (x_2 - x_1)/2


def find_section(f, a, b):
    m = middle_point(a, b)
    if (f(m) == 0):
        return a, b
    elif (np.sign(f(m))*np.sign(f(b)) < 0):
        return m, b
    else:
        return a, m


def bisection_method(f, interval, tolerance):
    a_i = interval[0]
    b_i = interval[1]
    c = middle_point(b_i, a_i)
    error = abs(f(c))
    iterations = 0
    while not (error < tolerance):
        iterations += 1
        a_i, b_i = find_section(f, a_i, b_i)
        c = middle_point(b_i, a_i)
        error = abs(f(c))
    return c, error, iterations


# Receives the function f, interval [a,b], tolerance (op) and interval steps to
# find zeros
def main_bisection_method(f, a, b, tolerance=1.0e-5, interval_steps=0.005):
    intervals = find_intervals(f, a, b, interval_steps)

    if not intervals:
        print("No change of sign found in [{}, {}]".format(a, b))
        return

    f_sig_figures = math.ceil(-np.log10(tolerance))
    result = []

    for i, interval in enumerate(intervals):
        a = interval[0]
        b = interval[1]
        c, f_error, iterations = bisection_method(f, interval, tolerance)
        x_error, x_sig_figures = bisection_max_error(a, b, iterations)
        result.append("{}:\n x = {} +/- {};\n f(x) = {} +/- {};"
                      "\n Number of iterations = {};".format(
                       i+1, round(c, x_sig_figures),
                       round(x_error, x_sig_figures+1),
                       round(f(c), f_sig_figures),
                       round(f_error, f_sig_figures+1),
                       iterations))
    return result


def bisection_max_error(a, b, iterations):
    x_error = (b-a)/2**iterations
    sig_figures = math.ceil(- np.log10(x_error))
    return x_error, sig_figures


def find_intervals(f, a, b, dx=0.005):
    points = np.arange(a, b, step=dx)
    sections = [(x, x+dx) for x in points
                if np.sign(f(x))*np.sign(f(x+dx)) <= 0]

    return sections
