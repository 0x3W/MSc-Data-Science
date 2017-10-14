#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb  6 16:02:30 2017

@author: Dovla
"""

import time
start = time.time()

import pandas as pd
import numpy as np

df1 = pd.read_csv('/Users/Dovla/Downloads/BX-CSV-DUMP/BX-Book-Ratings.csv', sep=';', encoding='latin1')
books = pd.read_csv('/Users/Dovla/Downloads/BX-CSV-DUMP/BX-Books.csv', sep=';', encoding='latin1', error_bad_lines=False)

df1.drop(df1[df1['Book-Rating'] < 1].index, inplace=True)

gr1 = df1.groupby(df1['User-ID'], as_index=False)['Book-Rating'].count()
gr1 = gr1.sort_values(['Book-Rating'], ascending=False)
#usersTop = gr1['User-ID'].head(5)
df11 = pd.merge(df1,gr1, how='left', on='User-ID')
#usersTop = gr1[gr1['Book-Rating'] > 10]

gr2 = df1.groupby(df1['ISBN'], as_index=False)['Book-Rating'].count()
gr2 = gr2.sort_values(['Book-Rating'], ascending=False)
#booksTop = gr2['ISBN'].head(5)
booksTop = gr2[gr2['Book-Rating'] > 10]

#df2 = df1(df1['User-ID'],index=True).isin(usersTop)

#usersTop2 = df1[df1['User-ID'].isin(usersTop['User-ID'])]
booksTop2 = df11[df11['ISBN'].isin(booksTop['ISBN'])]

df2 = pd.DataFrame(booksTop2[booksTop2['Book-Rating_y'] > 10])

colnames = ['User-ID','ISBN','Book-Rating', 'Count']
df2.columns = colnames

import random
from random import randint

liss = random.sample(range(0,df2.shape[0]), 3)
lis = df2.iloc[liss]

temp60 = pd.merge(lis,books, how='left', on='ISBN')  
temp61 = temp60.drop_duplicates('ISBN')


#lis = df2.head(100)
lis1 = df2[df2['ISBN'].isin(lis['ISBN'])]
lis1add = df2[df2['User-ID'].isin(lis1['User-ID'])]

lis11 = df2[df2['ISBN'].isin(lis['ISBN'])]

df4 = lis1add.iloc[:,0:3]
df4['User-ID'] = pd.Categorical(df4['User-ID'])
df4['Ucode'] = df4['User-ID'].cat.codes
df4['ISBN'] = pd.Categorical(df4['ISBN'])
df4['Icode'] = df4['ISBN'].cat.codes

df5 = lis1.iloc[:,0:3]
df5['User-ID'] = pd.Categorical(df5['User-ID'])
df5['Ucode'] = df5['User-ID'].cat.codes
df5['ISBN'] = pd.Categorical(df5['ISBN'])
df5['Icode'] = df5['ISBN'].cat.codes
   
n_users = df4['Ucode'].unique().shape[0]
n_items = df4['Icode'].unique().shape[0]

n_users1 = df5['Ucode'].unique().shape[0]
n_items1 = df5['Icode'].unique().shape[0]

data_matrix1 = np.zeros((n_users, n_items))
for line in df4.itertuples():
    data_matrix1[line[4]-1, line[5]-1] = line[3]/2  

data_matrix2 = np.zeros((n_users1, n_items1))
for line in df5.itertuples():
    data_matrix2[line[4]-1, line[5]-1] = line[3]/2

temp50 = np.count_nonzero(data_matrix2,axis=1)
temp51 = temp50/int(n_items1)
temp52 = data_matrix1 * temp51[:,np.newaxis]

longMatArr = np.array(temp52)
longMatArrFl = longMatArr.astype('float')
longMatArrFl[longMatArrFl == 0] = 'nan' # or use np.nan
   
temp22 = np.nanmean(longMatArrFl, axis=0)
temp22 = pd.DataFrame(temp22)
temp22['Icode'] = temp22.index
      
temp36 = pd.merge(temp22,df4, how='inner', on='Icode')  
temp23 = temp36.drop_duplicates('Icode')

temp37 = pd.merge(temp23,books, how='left', on='ISBN')  
temp38 = temp37.drop_duplicates('ISBN')

temp40 = temp38[~temp38['ISBN'].isin(lis['ISBN'])]

colnames = ['Score','Icode','User-ID','ISBN','Book-Rating','Ucode','Book-Title','Book-Author','Year-Of-Publication','Publisher','Image-URL-S','Image-URL-M','Image-URL-L']
temp41 = pd.DataFrame(temp40)
temp41.columns = colnames

temp100 = temp41.sort_values('Score', ascending=False)

end = time.time()
print(end - start)
