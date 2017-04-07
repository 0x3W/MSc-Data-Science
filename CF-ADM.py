#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb  6 10:00:24 2017

@author: Dovla
"""
import time
import pandas as pd
import numpy as np
import random
from random import randint
from sklearn.metrics import mean_squared_error
from math import sqrt

def fast_similarity(ratings, kind='user', epsilon=1e-9):
    # epsilon -> small number for handling dived-by-zero errors
    if kind == 'user':
        sim = ratings.dot(ratings.T) + epsilon
    elif kind == 'item':
        sim = ratings.T.dot(ratings) + epsilon
    norms = np.array([np.sqrt(np.diagonal(sim))])
    return (sim / norms / norms.T)

def rmse1(prediction, test):
    prediction = prediction[test.nonzero()].flatten() 
    test = test[test.nonzero()].flatten()
    return np.sqrt(((prediction - test) ** 2).mean())

ratings = pd.read_csv('/Users/Dovla/Downloads/BX-CSV-DUMP/BX-Book-Ratings.csv', sep=';', encoding='latin1')
books = pd.read_csv('/Users/Dovla/Downloads/BX-CSV-DUMP/BX-Books.csv', sep=';', encoding='latin1', error_bad_lines=False, warn_bad_lines=False)
users = pd.read_csv('/Users/Dovla/Downloads/BX-CSV-DUMP/BX-Users.csv', sep=';', encoding='latin1', error_bad_lines=False, warn_bad_lines=False)

ratings.drop(ratings[ratings['Book-Rating'] < 1].index, inplace=True)

ratingsUserGroup = ratings.groupby(ratings['User-ID'], as_index=False)['Book-Rating'].count()
ratingsUserGroupSort = ratingsUserGroup.sort_values(['Book-Rating'], ascending=False)
ratingsAndUserCount = pd.merge(ratings,ratingsUserGroupSort, how='left', on='User-ID')

ratingsISBNGroup = ratings.groupby(ratings['ISBN'], as_index=False)['Book-Rating'].count()
ratingsISBNGroupSort = ratingsISBNGroup.sort_values(['Book-Rating'], ascending=False)
topBooks = ratingsISBNGroupSort[ratingsISBNGroupSort['Book-Rating'] > 20]

topBooksAllData = ratingsAndUserCount[ratingsAndUserCount['ISBN'].isin(topBooks['ISBN'])]

filteredRatings = pd.DataFrame(topBooksAllData[topBooksAllData['Book-Rating_y'] > 20])

colnames = ['User-ID','ISBN','Book-Rating', 'UserRatingCount']
filteredRatings.columns = colnames

filteredRatings1 = filteredRatings
filteredRatings1['User-ID'] = pd.Categorical(filteredRatings1['User-ID'])
filteredRatings1['Ucode'] = filteredRatings1['User-ID'].cat.codes

filteredRatings1['ISBN'] = pd.Categorical(filteredRatings1['ISBN'])
filteredRatings1['Icode'] = filteredRatings1['ISBN'].cat.codes

nUsers = filteredRatings1['Ucode'].unique().shape[0]
nItems = filteredRatings1['Icode'].unique().shape[0]

completeData = filteredRatings1.reset_index(drop=True)
completeData['Index'] = completeData.index

errTot = []
kfolds = 5
subsetSize = len(completeData)/kfolds
print("Data consists of " + str(nUsers) +  " who rated " + str(nItems)  +" books with " + str(completeData['Book-Rating'].count())+" ratings.")             
for i in range(kfolds):
    start = time.time()

    testData = completeData.iloc[int(subsetSize)*i:int(subsetSize)*(i+1)]
    trainData = completeData[~completeData['Index'].isin(testData['Index'])]

    trainMatrix = np.zeros((nUsers, nItems))
    for line in trainData.itertuples():
        trainMatrix[line[5]-1, line[6]-1] = line[3]/2 
    
    testMatrix = np.zeros((nUsers, nItems))
    for line in testData.itertuples():
        testMatrix[line[5]-1, line[6]-1] = line[3]/2
    
    trainMatrixArr = np.array(trainMatrix)
    trainMatrixArrFl = trainMatrixArr.astype('float')
    trainMatrixArrFl[trainMatrixArrFl == 0] = 'nan' # or use np.nan
    
    trainMatrixMean = np.nanmean(trainMatrixArrFl,axis=1)
    trainMatrixMinMean = trainMatrixArrFl - trainMatrixMean[:,np.newaxis]
    
    trainMatrixDf = pd.DataFrame(trainMatrixArrFl)
    trainMatrixDfZ = np.nan_to_num(trainMatrixDf)
    trainDfMinMean = pd.DataFrame(trainMatrixMinMean)
    trainMatrixDfMinMeanZ = np.nan_to_num(trainMatrixMinMean)    

    sim = fast_similarity(trainMatrixDfMinMeanZ)
    simMinZero = sim.clip(min = 0)

    predictStep1 = simMinZero.dot(trainMatrixDfZ)
    temp1 = trainMatrixDfZ.clip(max=1)
    temp2 = simMinZero.dot(temp1)
    predict = (predictStep1 + 0.0000001) / (temp2 + 0.0000001) # - 1
        
    err = rmse1(predict, testMatrix)
    errTot.append(err)
    print ('\n CF RMSE: '+ str(round(err,4)))

    end = time.time()
    print("\nRound completed: " + str(i+1) + " of " + str(kfolds)) 
    print("Total time for round: " + str(round((end - start),2)) + " seconds")
    print("=====================================================")

print("\nAverage RMSE: " + str(round(sum(errTot)/len(errTot),4)))
