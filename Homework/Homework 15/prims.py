#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 17 14:39:45 2019

@author: rcurry
"""
import random
import xlrd

def prims(V, E, c, start_node):
    
    #Defining the initial S set--This is the set of nodes in the list
    S = [start_node]
    
    #Defininig the initial S_bar set
    S_bar = [v for v in V if v not in S]
    
    #Prints out S and S-bar
    #print("Set S is equal to ", S)
    #print("\nSet S-bar is equal to ", S_bar)
    
    #initializing the total cost of the tree
    Tree_Cost = 0
    
    #Initalizing the list of edges in the tree
    Tree_Edges = []
    
    #Initializing the list of edges in the cut
    Cut = []
    
    #Complete this while loop while some nodes are not yet in the tree.
    while len(S_bar) != 0:
        
        #Determine the Cut set
        for i in S:
            for j in S_bar:
                if (i,j) in E:
                    
                    #Add (i,j) to Cut
                    Cut.append((i,j))
                    #print("\n arc (", (i,j), "is in the cut")
                if (j,i) in E:
                    Cut.append((j,i))
                    
                
            
        #Find the minimum cost edge in the cut-set
        min_cost_edge_value = 10000
        min_cost_edge_i = -1
        min_cost_edge_j = -1
        
        #Find the minimum cost edge in the cut-set
        for (i,j) in Cut:
            if c[i,j] < min_cost_edge_value:
                min_cost_edge_value = c[i,j]
                min_cost_edge_i = i
                min_cost_edge_j = j
                
        #print the edge to add to the tree
        print("\nAdd edge (", min_cost_edge_i, ",", min_cost_edge_j, ") to the Tree with cost", min_cost_edge_value)
        
        if min_cost_edge_i in S:
            #Add the new node to S
            S.append(min_cost_edge_j)
        else: 
            S.append(min_cost_edge_i)
        #Reset the set S-bar
        S_bar = [v for v in V if v not in S]
        
        #Print off the S and S-bar sets
        #print("\nSet S is equal to ", S)
        #print("\nSet S-bar is equal to ", S_bar)
    
        #update the cost of the tree, currently
        Tree_Cost = Tree_Cost + min_cost_edge_value
        
        #Update the min-cost cut edge to the set of tree edges
        Tree_Edges.append((min_cost_edge_i, min_cost_edge_j))
        
        #Print off the cost of the tree and the edges in the tree
        
        #Reset the cut-set
        Cut = []
        
    print("\nTotal tree cost = ", Tree_Cost)
    print("\nEdges in the tree are ", Tree_Edges)
            
    
    return Tree_Edges

def main():
    
    #Finds the Excel workbook with the data
    workbook = xlrd.open_workbook('Homework_13.xlsx')
    #Finds the specific Excel Sheet with the Data--when it's named Data
    worksheet= workbook.sheet_by_name('Data')
    
    #This finds the last column having a value in it. This helps us to know how many nodes are in the network.
    last_column = worksheet.ncols

    #We set the number of nodes equal to the number of non-empty columns
    num_nodes = last_column - 1
    
    #Initialize the V-set
    V = []
    
    #For loop to add nodes to the V-Set based on the number of nodes
    for i in range(num_nodes):
        V.append(i+1)
        
    #Initialize the set of edges E
    E = []
    
    #Initialize the cost parameter
    c={}
    
    #These for loops go through the table of data to 
    #figure out which edges are in the network
    #If the edge exists, then we add that edge to the set E
    #And, we set the set the cost of the edge 
    #equal to the value in the cell
    for i in V:
        for j in V:
            
            if worksheet.cell(j, i).value != "--":
                #ONly consider when i < j since this is the way to define 
                #the set of edges
                if i < j:
                    #set the cost of (i,j) equal to the integer value in the cell
                    c[i,j] = int(worksheet.cell(j,i).value)
                    #Adds (i,j) to the set E
                    E.append((i,j))
                
    #Runs Prims Algorithm
    prims(V, E, c, 1 )
    
    
if __name__ == '__main__':
    main()
