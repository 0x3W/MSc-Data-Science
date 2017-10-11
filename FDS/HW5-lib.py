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

def closest(L):
    d = np.infty
    for i in range(len(L)):
        for j in range(len(L)):
            if i != j:
                if cldist(L[i],L[j]) < d:
                    d = cldist(L[i],L[j])
                    a, b = i, j
    return(a, b)

def single_linkage(L, k):
    seq = [[i] for i in range(len(L))]
    points2 = L.copy()
    while len(seq) > k:
        fir, sec = closest(points2)
        seq[fir] = seq[fir] + seq[sec]
        del seq[sec]
        points2[fir] = points2[fir] + points2[sec]
        del points2[sec]
    return seq
