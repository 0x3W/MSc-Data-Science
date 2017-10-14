#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 13 16:46:13 2016

@author: Dovla
"""

import numpy as np
import matplotlib.pyplot as plt

def euc(x,y):
    return np.sqrt(np.sum((x - y)**2))

def alldist(D):
    A = np.zeros((len(D),len(D)), dtype=np.float)
    B = []
    for i in D:
        for j in D:
            B.append(euc(i,j))
    C = np.asarray(B).reshape(len(D),len(D))
    return C

def achmat(D, d):
    return np.where(np.random.randn(D,d) < 0, -1, 1)

def reduce(X, d):
    A = achmat(X.shape[1], d)
    return np.dot(X, A) / np.sqrt(d)
ef distortion(dm1, dm2):
    return((dm1+1e-16)/(dm2+1e-16))

def first(r, data, redSize):

    dataRed = reduce(data,redSize)
    dataMat = data.as_matrix()
    arRed = []
    arData = []
    
    for i in r:
        arRed.append(dataRed[i])
        arData.append(dataMat[i])

    arRed = np.asarray(arRed)
    arData = np.asarray(arData)
   
    dist = []
    dist = distortion(alldist(arRed), alldist(arData))

    np.set_printoptions(precision=2)
    print((arData.nbytes / arRed.nbytes),round(dist.min(), 2),round(dist.mean(),2),round(dist.max(),2))
    plt.hist(np.ravel(dist), normed = True, bins = 100, histtype='step')

