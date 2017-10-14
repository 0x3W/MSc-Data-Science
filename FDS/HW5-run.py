#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 24 15:41:56 2016

@author: Dovla
"""

import sys
import lib1772953 as lib

files = sys.argv[1:-2]
filter = sys.argv[-2]
nrClst = int(sys.argv[-1])

points = []
for f in files:
    points.append([lib.charfreq(f, filter)])
    
clusters = lib.single_linkage(points, nrClst)
for i in range(len(clusters)):
    namedClst = []
    for j in clusters[i]:
        namedClst.append(files[j])
    print(namedClst)
