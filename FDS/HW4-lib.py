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

def bag(wc, treshold=10):
    d1 = [k for k, v in wc.items() if v > treshold] 
    return d1
    
def jaccard(s1,s2):
    sUnion = s1.union(s2)
    sInter = s1.intersection(s2)
    
    lenUnion = len(sUnion)
    if not lenUnion:
        return 0
    
    return len(sInter)*1.0/lenUnion

def single_linkage(D, k):
    count = len(D) - k
    i = 1
    D[D == 0] = 1
    unRavels=[]
    while (i <= k):
        #print ("The count is:", i)

    # Get everything for rows
    # Unravel rows
        temp1 = np.unravel_index(D.argmin(), D.shape)
        #print(temp1)

    # Unravel columns
        temp2 = temp1[::-1]

    # Select min rows, and find min of them
        #print("Minimum rows")
        finMat2 = D[np.ix_(temp1)]                
        tempMatR = np.amin(finMat2, axis=0)
        #print(tempMatR)

    # Select min columns, and find min of them
        #print("Minimum columns")
        finMat3 = D[np.ix_(temp2)]
        #print(finMat3.T)
        tempMatC = np.amin(finMat3, axis=0)
    #tempMatC1 = np.transpose(tempMatC)
        #print(tempMatC)

    #Add character due to larger rows
        #print("TryOut")
        addOne = np.array([1])
        #print(addOne)
        addOneTo = np.hstack((tempMatC,addOne))
        #print(addOneTo)
        addOneTo1 = addOneTo.reshape((-1, 1))
        #print(addOneTo1)

        #print("stacked mins for rows")
        tempMat2 = np.vstack((D,tempMatR))
        #print(tempMat2)

    # Try to combine on new matrix
        #print("stacked mins for cols")
        combLarge = np.hstack((tempMat2,addOneTo1))
        #print(combLarge)

    #Deleting
        #print(temp1)
        #print("Deleted excess from first iter, row")
        tempMat3 = np.delete(combLarge, np.ix_(temp1), axis=0)
        #print(tempMat3)

        #print(temp2)
        #print("Deleted excess from first iter, column")
        tempMat4 = np.delete(tempMat3, np.ix_(temp2), axis=1)
        #print(tempMat4)
        unRavels.append(temp1)
        D = tempMat4
        #print(D)
        i = i + 1
    return D, unRavels

def single_linkage2(D, k):
    min_point = np.argmin(D, axis=1)
    points = [(row, p) for row, p in enumerate(min_point)]
    index1 = np.arange(len(D))
    
    #posit1 = np.arange(a-1)

    points1 = []
    for c in range(len(points)):
        points1.append(D[points[c]])
    

    pdf1 = pd.DataFrame(
    {'lst1Tite': points,
     'lst2Tite': points1,
     'lst3Tite': index1,
    })
    #print(pdf1)

    pdf2 = pdf1.sort_values(by=['lst2Tite'], ascending=[1])
    #print(pdf2)

    pdf2list = pdf2['lst3Tite'].tolist()
    #print(len(pdf2list))
    mlt = len(pdf2list)//k
    new_list = [pdf2list[i:i+mlt] for i in range(0, len(pdf2list), mlt)]
    return new_list
