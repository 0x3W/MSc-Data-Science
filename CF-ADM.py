#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb  6 10:00:24 2017

@author: Dovla
"""
import time
start = time.time()
start1 = time.time()

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

def rmse(prediction, ground_truth):
    prediction = prediction[ground_truth.nonzero()].flatten() 
    ground_truth = ground_truth[ground_truth.nonzero()].flatten()
    return sqrt(mean_squared_error(prediction, ground_truth))

def rmse1(prediction, ground_truth):
    prediction = prediction[ground_truth.nonzero()].flatten() 
    ground_truth = ground_truth[ground_truth.nonzero()].flatten()
    return np.sqrt(((prediction - ground_truth) ** 2).mean())

df1 = pd.read_csv('/Users/Dovla/Downloads/BX-CSV-DUMP/BX-Book-Ratings.csv', sep=';', encoding='latin1')
df2 = pd.read_csv('/Users/Dovla/Downloads/BX-CSV-DUMP/BX-Books.csv', sep=';', encoding='latin1', error_bad_lines=False, warn_bad_lines=False)
df3 = pd.read_csv('/Users/Dovla/Downloads/BX-CSV-DUMP/BX-Users.csv', sep=';', encoding='latin1', error_bad_lines=False, warn_bad_lines=False)

df1.drop(df1[df1['Book-Rating'] < 1].index, inplace=True)

gr1 = df1.groupby(df1['User-ID'], as_index=False)['Book-Rating'].count()
gr1 = gr1.sort_values(['Book-Rating'], ascending=False)
#usersTop = gr1['User-ID'].head(5)
df11 = pd.merge(df1,gr1, how='left', on='User-ID')
#usersTop = gr1[gr1['Book-Rating'] > 10]

gr2 = df1.groupby(df1['ISBN'], as_index=False)['Book-Rating'].count()
gr2 = gr2.sort_values(['Book-Rating'], ascending=False)
#booksTop = gr2['ISBN'].head(5)
booksTop = gr2[gr2['Book-Rating'] > 20]

#df2 = df1(df1['User-ID'],index=True).isin(usersTop)

#usersTop2 = df1[df1['User-ID'].isin(usersTop['User-ID'])]
booksTop2 = df11[df11['ISBN'].isin(booksTop['ISBN'])]

df2 = pd.DataFrame(booksTop2[booksTop2['Book-Rating_y'] > 20])

colnames = ['User-ID','ISBN','Book-Rating', 'Count']
df2.columns = colnames

df4 = df2
df4['User-ID'] = pd.Categorical(df4['User-ID'])
df4['Ucode'] = df4['User-ID'].cat.codes

df4['ISBN'] = pd.Categorical(df4['ISBN'])
df4['Icode'] = df4['ISBN'].cat.codes

n_users = df4['Ucode'].unique().shape[0]
n_items = df4['Icode'].unique().shape[0]

n_usersStat = df1['User-ID'].unique().shape[0]
n_itemsStat = df1['ISBN'].unique().shape[0]
totRatdf1 = df1['Book-Rating'].count()

df5 = df4.reset_index(drop=True)
df5['Index'] = df5.index

errTot = []
kfolds = 5
subsetSize = len(df5)/kfolds
end = time.time()
print("Data consists of " + str(n_users) + "users(" + str(round((n_users/n_usersStat),2)) + "%) who rated " + str(n_items) + "books(" + str(round((n_items/n_itemsStat*100),2)) + "%)" + " with " + str(df5['Book-Rating'].count())+"ratings(" + str(round((df5['Book-Rating'].count()/totRatdf1*100),2)) + "%).")             
print("Data consists of " + str(n_users) +  " who rated " + str(n_items)  +" books with " + str(df5['Book-Rating'].count())+" ratings.")             

print("Data prep to loop: " + str(round((end-start),2)) + " seconds")

for i in range(kfolds):

    start = time.time()
    start2 = time.time()

    test_dataMy = df5.iloc[int(subsetSize)*i:int(subsetSize)*(i+1)]
    train_dataMy = df5[~df5['Index'].isin(test_dataMy['Index'])]

    train_data_matrix1 = np.zeros((n_users, n_items))
    for line in train_dataMy.itertuples():
        train_data_matrix1[line[5]-1, line[6]-1] = line[3]/2 
    
    test_data_matrix1 = np.zeros((n_users, n_items))
    for line in test_dataMy.itertuples():
        test_data_matrix1[line[5]-1, line[6]-1] = line[3]/2
    
    longMatArr = np.array(train_data_matrix1)
    longMatArrFl = longMatArr.astype('float')
    longMatArrFl[longMatArrFl == 0] = 'nan' # or use np.nan
    
    longMatMean = np.nanmean(longMatArrFl,axis=1)
    longMatMinMean = longMatArrFl - longMatMean[:,np.newaxis]
    
    longDf = pd.DataFrame(longMatArrFl)
    longDfZ = np.nan_to_num(longDf)
    longDfMinMean = pd.DataFrame(longMatMinMean)
    longDfMinMeanZ = np.nan_to_num(longDfMinMean)    
    end = time.time()
    print("Data prep in loop: " + str(round((end-start),2)) + " seconds")

    start = time.time()
    sim = fast_similarity(longDfMinMeanZ)
    sim1 = sim.clip(min = 0)

    end = time.time()
    print("Cos similarity done: " + str(round((end-start),2)) + " seconds")
    start = time.time()

    predictStep1 = sim1.dot(longDfZ)
    temp1 = longDfZ.clip(max=1)
    temp2 = sim1.dot(temp1)
    predict = (predictStep1 + 0.0000001) / (temp2 + 0.0000001) # - 1
    
    end = time.time()
    print("CF prediction done: " + str(round((end-start),2))+ " seconds")

    start = time.time()
    
    err = rmse1(predict, test_data_matrix1)
    errTot.append(err)
    print ('\n CF RMSE: '+ str(round(err,4)))

    end = time.time()
    print("\nRound completed: " + str(i+1) + " of " + str(kfolds)) 
    print("Total time for round: " + str(round((end - start2),2)) + " seconds")
    print("=====================================================")

print("\nAverage RMSE: " + str(round(sum(errTot)/len(errTot),4)))
#print("Total time for 5-fold CV CF prediction model: " + str(round((end - start1),2)) + " seconds")
