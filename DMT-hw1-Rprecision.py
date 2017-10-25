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

