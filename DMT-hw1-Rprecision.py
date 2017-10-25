#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 13 01:14:50 2017

@author: Dovla
"""

import pandas as pd
groundTruth = pd.read_csv('/Cranfield_DATASET/cran_Ground_Truth.tsv', sep = '\t')

cDefStem = pd.read_csv('CountDefStem.tsv', sep='\t')
bDefStem = pd.read_csv('BM25DefStem.tsv', sep='\t')
tDefStem = pd.read_csv('TFIDFDefStem.tsv', sep='\t')

cEngStem = pd.read_csv('CountEngStem.tsv', sep='\t')
bEngStem = pd.read_csv('BM25EngStem.tsv', sep='\t')
tEngStem = pd.read_csv('TFIDFEngStem.tsv', sep='\t')

cEngStemStop = pd.read_csv('CountEngStemStop.tsv', sep='\t')
bEngStemStop = pd.read_csv('BM25EngStemStop.tsv', sep='\t')
tEngStemStop = pd.read_csv('TFIDFEngStemStop.tsv', sep='\t')

aggTextTitle = pd.read_csv('aggTextTitle.tsv', sep='\t')

maxQueries = 225 # final.Query_ID.max() 

def avgR(groundTruth, maxQueries, currentDF):
    rslt = []
    for i in range(maxQueries):
        temp10 = groundTruth.loc[groundTruth['Query_id'] == i+1]
        temp11 = currentDF.loc[currentDF['Query_ID'] == i+1]
        temp12 = temp10['Relevant_Doc_id'].isin(temp11['Doc_ID'])
        if temp12.empty:
            res = 0
            rslt.append(res)
        else:
            res = sum(temp12) / len(temp10)
            rslt.append(res)
    return sum(rslt)/len(rslt)


avgCDefStem = avgR(groundTruth, maxQueries, cDefStem)
avgBDefStem = avgR(groundTruth, maxQueries, bDefStem)
avgTDefStem = avgR(groundTruth, maxQueries, tDefStem)

avgCEngStem = avgR(groundTruth, maxQueries, cEngStem)
avgBEngStem = avgR(groundTruth, maxQueries, bEngStem)
avgTEngStem = avgR(groundTruth, maxQueries, tEngStem)
avgCEngStemStop = avgR(groundTruth, maxQueries, cEngStemStop)
avgBEngStemStop = avgR(groundTruth, maxQueries, bEngStemStop)
avgTEngStemStop = avgR(groundTruth, maxQueries, tEngStemStop)

avgAggTextTitle = avgR(groundTruth, maxQueries, aggTextTitle)

rPrecision = [avgCDefStem,avgBDefStem,avgTDefStem, avgCEngStem,avgBEngStem, avgTEngStem, avgCEngStemStop, avgBEngStemStop, avgTEngStemStop, avgAggTextTitle]
