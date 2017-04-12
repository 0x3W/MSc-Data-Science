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

# RMSE is root mean squared error calculated between each test value, and 
# actual predicted score. Its cruical that only values that exist in test
# are calculated hence nonzero function used.
def rmse1(prediction, test):
    prediction = prediction[test.nonzero()].flatten() 
    test = test[test.nonzero()].flatten()
    return np.sqrt(((prediction - test) ** 2).mean())
# ============================================================                 
# Read all three datasets
ratings = pd.read_csv('/Users/Dovla/Downloads/BX-CSV-DUMP/BX-Book-Ratings.csv', sep=';', encoding='latin1')
books = pd.read_csv('/Users/Dovla/Downloads/BX-CSV-DUMP/BX-Books.csv', sep=';', encoding='latin1', error_bad_lines=False, warn_bad_lines=False)
users = pd.read_csv('/Users/Dovla/Downloads/BX-CSV-DUMP/BX-Users.csv', sep=';', encoding='latin1', error_bad_lines=False, warn_bad_lines=False)
# Drop zero ratings as they represent nothing really
ratings.drop(ratings[ratings['Book-Rating'] < 1].index, inplace=True)
# Count how many books each user rated
ratingsUserGroup = ratings.groupby(ratings['User-ID'], as_index=False)['Book-Rating'].count()
# Sort starting with users with highest number of ratings
ratingsUserGroupSort = ratingsUserGroup.sort_values(['Book-Rating'], ascending=False)
# Add user rating count to ratings data
ratingsAndUserCount = pd.merge(ratings,ratingsUserGroupSort, how='left', on='User-ID')

# Count how many times each book is rated
ratingsISBNGroup = ratings.groupby(ratings['ISBN'], as_index=False)['Book-Rating'].count()
# Sort starting with books with highest number of ratings
ratingsISBNGroupSort = ratingsISBNGroup.sort_values(['Book-Rating'], ascending=False)
# Select books that are rated more than X times, 10 as optimal speed/quality contraint
topBooks = ratingsISBNGroupSort[ratingsISBNGroupSort['Book-Rating'] > 20]
# Select same topBooks but with data about user rating count
topBooksAllData = ratingsAndUserCount[ratingsAndUserCount['ISBN'].isin(topBooks['ISBN'])]
# From topBooks select only those users who rated more than X books, 10 as optimal speed/quality constraint
filteredRatings = pd.DataFrame(topBooksAllData[topBooksAllData['Book-Rating_y'] > 20])
#Clean columns names
colnames = ['User-ID','ISBN','Book-Rating', 'UserRatingCount']
filteredRatings.columns = colnames
#Generate catcodes for User ID so that it can be used for generating matrix 
# based on its index and later retrivied particular book/user if needed
filteredRatings['User-ID'] = pd.Categorical(filteredRatings['User-ID'])
filteredRatings['Ucode'] = filteredRatings['User-ID'].cat.codes
#Generate catcodes for ISBN ID so that it can be used for generating matrix 
# based on its index and later retrivied particular book/user if needed
filteredRatings['ISBN'] = pd.Categorical(filteredRatings['ISBN'])
filteredRatings['Icode'] = filteredRatings['ISBN'].cat.codes
# Number of unique users
nUsers = filteredRatings['Ucode'].unique().shape[0]
# Number of unique books
nItems = filteredRatings['Icode'].unique().shape[0]
# Add index columns to be used for selecting test/train data
completeData = filteredRatings.reset_index(drop=True)
completeData['Index'] = completeData.index

# ============================================================                 
# Create empty variable to store rmse for each round
errTot = []
# specify number of data folds (20% hence 5)
kfolds = 5
# calculate subset size in each fold
subsetSize = len(completeData)/kfolds
# Print basic data info
print("Data consists of " + str(nUsers) +  " who rated " + str(nItems)  +" books with " + str(completeData['Book-Rating'].count())+" ratings.")             
for i in range(kfolds):
    start = time.time()
# Split data into train and test based on size of kfolds
    testData = completeData.iloc[int(subsetSize)*i:int(subsetSize)*(i+1)]
# Take all data except what is in test
    trainData = completeData[~completeData['Index'].isin(testData['Index'])]

# Generate utility matrix for train data, by indexing on newly generated catCodes
    trainMatrix = np.zeros((nUsers, nItems))
    for line in trainData.itertuples():
        trainMatrix[line[5]-1, line[6]-1] = line[3]/2 

# Generate utility matrix for test data, by indexing on newly generated catCodes    
    testMatrix = np.zeros((nUsers, nItems))
    for line in testData.itertuples():
        testMatrix[line[5]-1, line[6]-1] = line[3]/2

# ============================================================                 
# The following ~20 lines are used to prepare data for calculation of cosine similarity
# Make sure train matrix is array 
    trainMatrixArr = np.array(trainMatrix)
# Make sure array is of type float
    trainMatrixArrFl = trainMatrixArr.astype('float')
# Turn all 0 into nans
    trainMatrixArrFl[trainMatrixArrFl == 0] = 'nan'
# Calculate row means (note 0s are not included)
    trainMatrixMean = np.nanmean(trainMatrixArrFl,axis=1)
# Subtract mean from rating (generate mean normalized ratings)
    trainMatrixMinMean = trainMatrixArrFl - trainMatrixMean[:,np.newaxis]  
# Create a dataframe copy of data
    trainMatrixDf = pd.DataFrame(trainMatrixArrFl)
# Convert all nans to 0s 
    trainMatrixDfZ = np.nan_to_num(trainMatrixDf)
# Create a dataframe copy of data
    trainDfMinMean = pd.DataFrame(trainMatrixMinMean)
# Convert all nans to 0s 
    trainMatrixDfMinMeanZ = np.nan_to_num(trainMatrixMinMean)    

# ============================================================
# generate cosine similarity matrix
    sim = fast_similarity(trainMatrixDfMinMeanZ)
# Set minimum value in similarity at 0 (negatives turned to 0)
    simMinZero = sim.clip(min = 0)

# ============================================================
# Following ~10 lines used for prediction ratings in two steps
# First step, generate similarity weighted sum of ratings via dot product
    predictStep1 = simMinZero.dot(trainMatrixDfZ)
# Set all ratings to 1, necessery for next calculation step
    temp1 = trainMatrixDfZ.clip(max=1)
# Get only similarities that are used in data (0 rating, 0 sim)
    temp2 = simMinZero.dot(temp1)
# Second step, predict average similarity based rating
    predict = (predictStep1 + 0.0000001) / (temp2 + 0.0000001) # - 1

# ============================================================
# Calculate and print rmse, and append it to total rmse for later calc of avg rmse
    err = rmse1(predict, testMatrix)
    errTot.append(err)
    print ('\n CF RMSE: '+ str(round(err,4)))
# Print which round it is, and how long it took to complete it.
    end = time.time()
    print("\nRound completed: " + str(i+1) + " of " + str(kfolds)) 
    print("Total time for round: " + str(round((end - start),2)) + " seconds")
    print("=====================================================")

# Calculate and print average RMSE for the kfold specified rounds
print("\nAverage RMSE: " + str(round(sum(errTot)/len(errTot),4)))
