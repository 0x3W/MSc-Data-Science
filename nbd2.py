#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 19 03:00:38 2017

@author: Dovla
"""
import networkx as nx
import pylab as plt
import numpy as np
import random

lenList = [1,2,3,4]
n = 100
r = 8
p = 8/(n-1)

erGraph = nx.gnp_random_graph(n,p)
rGraph = nx.random_regular_graph(r,n)

def maxR1(graph, nr,l):
    allR = []
    for i in range(nr):
        for j in range(nr):
            acc = graph
            #print(i,j)
            res = 0
            if i != j:
                while nx.has_path(acc,i,j):
                    n=nx.shortest_path(acc,i,j)
                    #print(res)
                    len1 = len(n)
                    if nx.shortest_path_length(acc,i,j) == l:
                        res = res + 1
                    if len1 > 1:
                        for ii in range(len1-1):
                            acc.remove_edge(n[ii],n[ii+1])
                #print(res)
                allR.append(res)
            else:
                continue
    return max(allR)

#2nd Evaluate rh
test2=[]
for k in lenList:   
    #print(k)
    #print(maxR1(erGraph.copy(),n,k))
    #print(maxR1(rGraph.copy(),n,k))
    th1 = k/maxR1(erGraph.copy(),n,k)
    th2 = k/maxR1(rGraph.copy(),n,k)
    print('For l: ',k,' th performance of ER is: ', th1)
    print('For l: ',k,' th performance of r-regular is: ', th2)
    test2.append([th1,th2])
plt.plot(lenList, test2)
plt.xlabel('l, length of disjoint paths')
plt.ylabel('TH')
plt.legend(['erGraph', 'rGraph'], loc='best')
plt.show()


#3rd Relability
def remove_edges(graph, p):    
    for node in graph.nodes():    
        # find the other nodes this one is connected to    
        connected = [to for (fr, to) in graph.edges(node)]    
        # probabilistically remove a random edge    
        if len(connected): # only try if an edge exists to remove    
            if random.random() < p:    
                remove = random.choice(connected)    
                graph.remove_edge(node, remove)    
    return graph   
   
failProbs = np.arange(0.01, 0.25, 0.02)
for k in lenList:
    test = []
    for f in failProbs:
        newErG = remove_edges(erGraph.copy(),f)
        th1 = k/maxR1(newErG.copy(), n, k)
        newRG = remove_edges(rGraph.copy(),f)
        th2 = k/maxR1(newRG.copy(), n, k)
        test.append([th1,th2])
    plt.plot(failProbs, test)
    plt.xlabel('Probability of failure')
    plt.ylabel('TH')
    plt.legend(['erGraph', 'rGraph'], loc='best')
    plt.show()
