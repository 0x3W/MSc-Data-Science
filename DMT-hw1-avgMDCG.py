#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr  7 23:51:10 2017

@author: Dovla
"""

import pandas as pd
import math

groundTruth = pd.read_csv('Cranfield_DATASET/cran_Ground_Truth.tsv', sep='\t')

cDefStem = pd.read_csv('CountDefStem.tsv', sep='\t')
bDefStem = pd.read_csv('BM25DefStem.tsv', sep='\t')
tDefStem = pd.read_csv('TFIDFDefStem.tsv', sep='\t')

cEngStem = pd.read_csv('CountEngStem.tsv', sep='\t')
bEngStem = pd.read_csv('BM25EngStem.tsv', sep='\t')
tEngStem = pd.read_csv('TFIDFEngStem.tsv', sep='\t')

cEngStemStop = pd.read_csv('CountEngStemStop.tsv', sep='\t')
bEngStemStop = pd.read_csv('BM25EngStemStop.tsv', sep='\t')
tEngStemStop = pd.read_csv('TFIDFEngStemStop.tsv', sep='\t')

maxQueries = groundTruth.Query_id.max()
k = [1,3,5,10]

def avgDCMG(ground, stemmer, k, maxQueries):
    rslt0 = []
    for kl in k:    
        rslt1 = []
        for i in range(maxQueries):
            temp1 = ground.loc[ground['Query_id'] == i+1]
            temp2 = stemmer.loc[stemmer['Query_ID'] == i+1]
            
            temp3 = temp2.head(kl)
            temp5 = temp3[temp3['Doc_ID'].isin(temp1['Relevant_Doc_id'])]
            temp6 = pd.merge(temp3, temp5, how='left', on=['Doc_ID'])
            temp7 = temp6.fillna(0)
            temp7.ix[temp7.Score_y>0, 'Score_y'] = 1
            
            if temp7.empty:
                res = 0
            else:
                if kl == 1:
                    res = temp7['Score_y'][0]
                    res = res / 1
                elif kl == 3:
                    res = temp7['Score_y'][0] + (temp7['Score_y'][1] / math.log2(2)) + (temp7['Score_y'][2] / math.log2(3))
                    res = res / 2.6309
                elif kl == 5:
                    res = temp7['Score_y'][0] + (temp7['Score_y'][1] / math.log2(2)) + (temp7['Score_y'][2] / math.log2(3)) + (temp7['Score_y'][3] / math.log2(4)) + (temp7['Score_y'][4] / math.log2(5))
                    res = res / 3.5616
                elif kl == 10:
                    res = temp7['Score_y'][0] + (temp7['Score_y'][1] / math.log2(2)) + (temp7['Score_y'][2] / math.log2(3)) + (temp7['Score_y'][3] / math.log2(4)) + (temp7['Score_y'][4] / math.log2(5)) + (temp7['Score_y'][5] / math.log2(6)) + (temp7['Score_y'][6] / math.log2(7)) + (temp7['Score_y'][7] / math.log2(8)) + (temp7['Score_y'][8] / math.log2(9)) + (temp7['Score_y'][9] / math.log2(10))
                    res = res / 5.09311
            rslt1.append(res)
        
        rsltAvg = sum(rslt1)/len(rslt1)
        rslt0.append(rsltAvg)
    return rslt0



    
