# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import sys
import node.py
import graph.py

def read_input():
    
    #lê e constroi grafo (filhos)? e lista de launches?
    #conta vertices para v_total
    #constroi problema
    v_total = 0
    
    graph = graph()     #graph
    launches = {}
    pieces = {}   #dicionario com id ligado ao peso
    
    for line in open(sys.argv[2], 'r'):
        words = line.split()
        if len(words):
            
            letter = words[0][0]
            
            if letter == 'V':
                pieces[words[0]]= words[1]
            elif letter == 'L':
                launches[words[0]] = launch(words[1], words[2],words[3])
            elif letter == 'E':
                graph.add_edge(words[1], words[2])
                
          
    problem=problema(0,launches,pieces,graph) 

    return problem

def strategy_f(search_type):
    
    if search_type == '-u':
        uninformed() = pai 
        
    else:
        informed() = pai
    
    explored.append(pai)
    frountier.delete(pai)   #???
    #retorna e remove da frountier
    return pai;
        
def goal_check(v_sent,v_total):
    if v_sent==v_total:
        return 1
    return 0
        
def g_function(pai):
    cost = pai.cost+launch[y].ci*filhos[x].weight
    return cost

def general_search(problem,search_type):
    #escrever no fout! o que esta no expanded?
   
    checked=list()
    frontier=list() #queue
    pai=node()  #.....
    
    i_state=node(problem.cost,problem.state)
    frontier.append(i_state)
    #explored.append(i_state)??
    
    pai=i_state;
    while True:
        
        strategy_f(search_type,pai) = pai     
            
        if pai == NULL:
            return 1
        
        if goal_check(v_sent,len(problem.pieces))==1 :#vai ser o optimal?
            return 0    #escrever fich out
        else:
            
            v_sent +=1  #nao vai ser smp 1!
            
            for x in range(len(edges)):  #que nivel do edges?
                
                cost=g_function()
                frontier=organize(edges[x],pai)
                    #verifica se já existe em explored ou frontier --sim->verifica custo e substitui se menor
                                            #--nao->insere
    return 1    
            
            
def main():

    v_sent=0
    solution=sys.argv[0:-3]+'.out'
    file_out = open(solution, 'w')
    
    problem = read_input()
    
    general_search(problem,sys.argv[1])
    
    file_out.close()