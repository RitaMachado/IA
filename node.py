# -*- coding: utf-8 -*-
"""
Created on Fri Oct 13 14:43:31 2017

@author: ritam
"""
        
class vertice:  #necessario?
    
    def __init__(self, weight=0, ID):
        self.weight =  weight
        self.id = ID
    
class launch:
    
    p_in=list()
    
    def __init__(self, max_w=0,fixed_c=0,ci=0,p_in):    #current_w tem que tar nos argumentos?
        self.max_w =  max_w
        self.fixed_c = fixed_c
        self.ci = ci
        self.pieces_in = p_in
        self.current_w = 0
    
    def add_piece(self, pieces, p_id):  #adicionar fixed qnd 1º vez?
        self.pieces_in.append(p_id)
        self.current_w += pieces[p_id]

#    def delete_piece(self,p_id,pieces):
#        self.pieces_in.remove(p_id)
#        self.current_w -= pieces[p_id]
#

        
class problema:
    
    def __init__(self, cost=0,launches=None,pieces=None,graph=None):
        self.cost = cost
        self.initial_state = 0  
        self.goal_state = len(pieces)
        self.launches = launches
        self.pieces =pieces
        self.graph = graph
    
class state: #node tree
    
    def __init__(self, launches=None,previous=None,cost=0,pieces_sent = 0):
        self.launches = launches
        self.previous = previous
        self.cost = cost
        self.pieces_sent = pieces_sent