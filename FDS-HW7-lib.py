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

