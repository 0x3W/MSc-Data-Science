#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 24 15:58:52 2016

@author: Dovla
"""

import numpy as np
def charfreq(filename, filter):
    dc = {c:0 for c in filter}
    f = open(filename, "r")
    for line in f:
        for ch in line:
            if ch in dc:
                dc[ch] +=1
    f.close()
    fv = np.zeros(len(filter))
    for i in range(len(filter)):
        fv[i] = dc[filter[i]]
    return fv/fv.sum() if fv.sum() > 0 else fv

def euc(x, y):
    return np.sqrt(np.sum((x - y)**2))

def cldist(c1, c2):
    d = np.infty
    for x in c1:
        for y in c2:
            d = min(d, euc(x,y))
    return d

