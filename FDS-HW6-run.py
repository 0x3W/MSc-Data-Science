#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 30 10:56:10 2016

@author: Dovla
"""
# Functions and libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import sys

def z(x):
    """Evaluate the sigmoid function at x."""
    return 1.0/(1.0 + np.exp(-x))

def h(Theta, X):
    """Evaluate the sigmoid function at each element of <Theta,X>."""
    return np.array([z(np.dot(Theta, x)) for x in X])

def gradient(Theta, X, Y):
    """Compute the gradient of the log-likelihood of the sigmoid."""
    pX = h(Theta, X) # i.e. [h(x) for each row x of X]
    return np.dot((Y - pX), X)

def logfit(X, Y, alpha=1, itr=10):
    """Perform a logistic regression via gradient ascent."""
    Theta = np.zeros(X.shape[1])
    for i in range(itr):
        Theta += alpha * gradient(Theta, X, Y)
    return Theta

