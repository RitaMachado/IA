# -*- coding: utf-8 -*-
"""
Created on Fri Oct 13 14:43:31 2017

@author: ritam
"""

class node:

    def __init__(self, cost=0,state=None,previous=None):
        self.cost = cost
        self.state = state  #int? list?
        self.previous = previous
        
class vertice:  #necessario?
    
    def __init__(self, weight=0, ID):
        self.weight =  weight
        self.id = ID
    
class launch:
    
    def __init__(self, max_w=0,fixed_c=0,ci=0):
        self.max_w =  max_w
        self.fixed_c = fixed_c
        self.ci=ci
        
        
class problema:
    
    def __init__(self, cost=0,state=None,launches=None,pieces=None):
        self.cost = cost
        self.initial_state = state  #int? list?
        self.launches=launches
        self.pieces=pieces
    