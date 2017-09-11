#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec  1 16:10:48 2016
"""

import pandas as pd
import csv
import libADM as lb
import math

#%% load files
print("I'm loading kernel...")
dict_ingr = dict()
f = open('dict_ingr.csv')
for row in csv.reader(f):
    dict_ingr[row[0]] = row[1]
f.close()

print("I'm loading BBC downloaded data...")
ricette = pd.DataFrame.to_dict(pd.DataFrame.from_csv('df_ricepes.csv'), orient = 'index')

print("I'm loading Inverted Index...")
norm_data = pd.DataFrame.from_csv('InvertedIndex.csv')
#%%

#my_dict = dict()
#for k in ricette.keys():
#    query = str(ricette[k]['Ingredients']).lower()
#    l = []
#    for v in dict_ingr.keys():
#        pos = query.find(v)
#        if pos > 0:
#            l.append(int(dict_ingr[query[pos:pos+len(v)]]))
#            my_dict[k] = l

my_dict = dict()
f = open('my_dict.csv')
for row in csv.reader(f):
    a = ','.join(row[1:]).strip(',,').split(',')
    a = list(map(float, a))
    a = list(map(int, a))
    my_dict[row[0]] = a
f.close()
#%%
import string


exclude = set(string.punctuation)

#request

#myset = set()

req = input("Ready, what are you looking for?\n")

req = ''.join(ch for ch in req if ch not in exclude).lower()

myset = set()
for k in my_dict.keys():
    title = ricette[k]['Name'].lower()
    title = ''.join(ch for ch in title if ch not in exclude)
    lista = [title.find(word) for word in req.split()]
    count = 0
    for i in lista:
        if i > 0:
            count += 1
    if count/len(lista) >= 0.55:
        myset.add(k)

req_ingr = []
for k in dict_ingr.keys():
    pos = req.find(k)
    if pos > 0:
        req_ingr.append(k)

if len(req_ingr) > 0:
    myset = myset.union(lb.find_recipes_with(dict_ingr,my_dict,req_ingr[0]))
    for i in req_ingr:
        myset = myset.intersection(lb.find_recipes_with(dict_ingr,my_dict,i))
#%% find light recipes

fat_ingr= ['butter','margarine', 'coconut oil', 'cake', 'sugar', 'cocoa butter', 'fat', 'lard','bacon', 'suet','brown sugar','corn syrup', 'glucose', 'honey', 'peanut', 'peanut butter', 'mincemeat', 'egg yolk', 'lardons', 'panettone', 'chocolate', 'cream', 'banana', 'beer', 'biscuit', 'brandy', 'whisky', 'banana bread', 'brandy butter', 'brioche', 'buttercream icing']
health_words = ['healthly', 'health','light', 'lightly']

fat_recipes = set()
if ( sum(req.find(i) for i in health_words) != -len(health_words) ) :
    for i in fat_ingr:
            fat_recipes = fat_recipes.union(lb.find_recipes_with(dict_ingr,my_dict,str(i)))
    if len(myset) == 0:
        myset = set(ricette.keys()).difference(fat_recipes)
    else:
        myset = myset.difference(fat_recipes)

#%% find quick recipes

quick_recipes = set()
quick_words = ['quick', 'quickly', 'speed', 'speedy', 'fast', 'faster', 'rapid', 'rapidly', 'swift']

if( sum(req.find(i) for i in quick_words) != -len(quick_words) ):
    for k in ricette.keys():
        if( (ricette[k]['CookTime'] == 'no cooking required' or ricette[k]['CookTime'] == 'less than 10 mins') and ( ricette[k]['PrepTime'] == 'less than 30 mins') ):
            quick_recipes.add(k)
    if len(myset) == 0:
        myset = quick_recipes
    else:
        myset = myset.intersection(quick_recipes)

#%%

lact_ingr = ['cheese', 'milk', 'butter','yogurt', 'yoghurt', 'chocolate', 'ice cream', 'pudding']
lactoses = []
for k in dict_ingr.keys():
    for i in lact_ingr:
        if k.find(i) != -1:
            lactoses.append(k)
lact_words = ['lactose', 'without lactose']
lactose_recipes = set()
if ( sum(req.find(i) for i in lact_words) != -len(lact_words) ) :
    for i in lactoses:
            lactose_recipes = lactose_recipes.union(lb.find_recipes_with(dict_ingr,my_dict,str(i)))
    if len(myset) == 0:
        myset = set(ricette.keys()).difference(lactose_recipes)
    else:
        myset = myset.difference(lactose_recipes) 
    
#%%
vgt_recipes = set()

if req.find('vegetarian') > 0:
    for k in ricette.keys():
        if ricette[k]['Dietary'] == 'vegetarian':
            vgt_recipes.add(k)
    if len(myset) == 0:
        myset = vgt_recipes
    else:
        myset = myset.intersection(vgt_recipes)


#%% print result
recipes_found = set()
if len(myset) == 0:
    print("I'm sorry, your research didn't give any result")
else:
    for i in myset:
        recipes_found.add(ricette[i]['Name'])
        print(ricette[i]['Name'])
    print('I found ', len(myset), ' recipes\nIf you are interested in one them press "y", else press "n"')
    cnt = str
    while cnt != 'y' or cnt != 'n':
        cnt = input()
        if cnt == 'y':
            print('Copy and past the name of the recipe of interest to see how to prepare it')
            y = input()
            while y not in recipes_found:
                print('Ops, be sure to copy it well, check capital letters')
                y = input()
            for k in ricette.keys():
                if ricette[k]['Name'] == str(y):
                    print('Title of recipe: ',ricette[k]['Name'])
                    print('Written by ', ricette[k]['Author'],'\n')
                    print('People served: ', ricette[k]['Serves'])
                    print('Time of preparation: ', ricette[k]['PrepTime'])
                    print('Time of cooking: ', ricette[k]['CookTime'],'\n')
                    print('Ingredients you need: ', ricette[k]['Ingredients'],'\n')
                    print('Method: ', ricette[k]['Method'],'\n')
                    print('Is it enough? If you want to find recipes similar to it press "find": ')
                    cnt = input()
                    if cnt == 'find':
                        lst = []
                        for x in norm_data:
                            a = norm_data[k].values
                            b = norm_data[str(x)].values
                            cos = lb.cosine_similarity(a,b)
                            lst.append([x, cos])
                        lst.sort(key = lambda x: x[1], reverse = True)
                        for x in lst[:10]:
                            if math.fabs(x[1]) > 0.50 and x[0] != k:
                                print(ricette[x[0]]['Name'],' is similar at: ', x[1])
            break
        else:
            if cnt == 'n':
                print('Thanks anyway')
                break
        print('Opss, something goes wrong, try again (y/n): ')
       
