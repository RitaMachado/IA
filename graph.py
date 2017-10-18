# -*- coding: utf-8 -*-
"""
Created on Wed Oct 18 16:13:40 2017

@author: ritam
"""


class node:

    def __init__(self, cost=0,state=None,previous=None):
        self.cost = cost
        self.state = state  #int? list?
        self.previous = previous
        
class graph :
    
    graph={}
        
    def add_adj(self,n_id):
        if n_id not in self.graph:
            self.graph[n_id]=list()
        
            
    def add_edge(self,id1,id2):
        
        self.add_adj(id1)
        self.graph[id1].append(id2)
        
        self.add_adj(id2)
        self.graph[id2].append(id1)
