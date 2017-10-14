#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 12 17:41:33 2016

@author: Dovla
"""
import sys
import random
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import lib1772953 as lib

data = pd.read_csv(sys.argv[1])
args = sys.argv[2:]

datap = pd.DataFrame.pivot(data, index=data.columns[0], 
                           columns=data.columns[1], values=data.columns[2])
datap.fillna(datap.mean(axis=0), axis=0, inplace=True)

r = random.sample(range(0,datap.shape[0]), 250)


plt.ion()
plt.grid()    
for i in args:
    lib.first(r,datap,int(i))
plt.show(block=True)
