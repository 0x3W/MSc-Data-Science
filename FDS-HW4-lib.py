#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov  9 17:26:44 2016

@author: Dovla
"""
#punc = ['<','>','/','?',';',':',',','.','"','’','[',']','{','}','|','=','+','-','_','(',')','*','&','^','%','$','#','@','!','‘','~','\\','\t','\n','\r']
import numpy as np
import pandas as pd

def wordcount(filename):
    file1 = open(filename)
    text = file1.read()
    pun = '<>/?;:,."“”’[]{}|=+-_()*&^%$#@!‘~\\\t\n\r'
    for p in pun:
        text = text.replace(p, " ")
    text1 = text.split()
    textLower = [item.lower() for item in text1]
     
    wordsBag={}
    for word in textLower:
        if word not in wordsBag.keys():
            wordsBag[word]=1
        else:
            count=wordsBag[word]
            wordsBag[word]=count+1
    return wordsBag
