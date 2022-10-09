#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct  9 12:18:34 2022

@author: felipems
"""

# Using ARCH(p) model in a time series

import pandas as pd
from arch import arch_model

df = pd.read_csv('MSFT_2006-01-01_to_2018-01-01.csv')
df.columns = ['date', 'open', 'high', 'low', 'close', 'volume', 'name']

time_serie = df.close[0:] - df.open[0:]

am = arch_model(time_serie, mean='Constant', vol='ARCH', p=2, dist='Normal')
results_arch = am.fit(update_freq=3)
results_arch.summary()
