#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov  9 17:29:54 2016

@author: Dovla
"""

import sys
import numpy as np
import IDlibtest1 as mylib


a = len(sys.argv)
b = str(sys.argv)
#print(a,b)

bagsLength = []
jacResults = []
i = 1
for i in range(a):
    firstWc = mylib.wordcount(sys.argv[i])
    firstBag = mylib.bag(firstWc, treshold=200)
    bagsLength.append(len(firstWc))
    ii = 1
    for ii in range(a):
        secondWc = mylib.wordcount(sys.argv[ii])
        secondBag = mylib.bag(secondWc, treshold=200)
        jacResults.append(1-mylib.jaccard(set(firstBag),set(secondBag)))
        #print(jacResults)	
        if ii > a:
            break
        else:
            ii = ii + 1
    
    if i > a:
        break
    else:
        i = i + 1

print(sorted(bagsLength, reverse=True))

jacArr = np.array(jacResults)
shape = (a,a)
arr1 = jacArr.reshape(shape)
#print(arr1[0:,0:])
np.set_printoptions(precision=2)
print(arr1[1:,1:])
print(np.mean(arr1[1:,1:]))

finMat = arr1[1:,1:]

remPositions, clustPositions = mylib.single_linkage(finMat, k = 3)
#print(remPositions)
print(clustPositions)

impl2 = mylib.single_linkage2(finMat, k=3)
print(impl2)

