# -*- coding: utf-8 -*-
"""
Created on Sun Feb 14 18:34:03 2021

@author: Krish Nath
"""
import copy
f = open('SCC.txt', 'r')
graph_a = {}
lines = f.readlines()
key = 1
curr = []
for l in lines:
    l = l.split()
    if (int(l[0]) == key):
        curr.append(int(l[1]))
    else:
        graph_a[key] = curr
        key += 1
        curr = []
graph_a = {1:[4,3],2:[3,1],3:[],4:[2]}
graph_b = {1:[2,11],2:[],3:[2,4],4:[],5:[6],6:[7],7:[8],8:[9],9:[],10:[9,11],11:[]}

# make function
explored = []
stack = []
result = []

def dfs_forest(graph_g, vertices, result_list):
    # in a while loop, keep looking for vertices that are still unvisited, 
    # and call dfs on each
    for w in vertices:
        if (w not in explored):
            # start with the first unvisited vertex s
            dfs(graph_g, w, result_list)
    return
def dfs(graph_g, s, result_list):
    #print(s, explored)
    if (s in explored):
        return 
    #mark	s	as	explored	
    explored.append(s)
	#for every edge	(s, v)	:
    #print('dfs', graph_g.get(s))
    for q in graph_g.get(s):
        #if	v	unexplored	
        if (q not in explored):
            # do dfs
            #print("calling for", q)
            dfs(graph_g, q, result_list)
            #print("back")
    result_list.append(s)
    return

graph_g = graph_a

def kosaragu_algoratim(graph_g):
    vertices = []
    reverse_graph = {}
    graph_lenth = len(graph_g)
    #print(graph_lenth)
    for s in range(graph_lenth):
        reverse_graph[s + 1] = []
    # Make a list of all vertices
    for i in graph_g:
        vertices.append(i)
    dfs_forest(graph_g, vertices, stack)
    #print('explored',explored)
    explored.clear()
    #print("stack:", stack)
    #return 0
    key = 0
    for w in graph_g.values():
        key += 1
        for q in w:
            reverse_graph[q].append(key)
    answer = []
    num = graph_lenth
    while (num != -1):
        #print(num, 'num')
        num -= 1
        use = stack[num]
        #print('explored1', explored)
        if (use not in explored):
            #print(use, 'looking')
            result.clear()
            #print(result, 'result')
            dfs(reverse_graph, use, result)
            #print(result, 'result2')
            #print('old', answer)
            copied_result = copy.deepcopy(result)
            answer.append(copied_result)    
            #print("SCC:", result)
    return answer
# import sys
# import threading
# threading.stack_size(67108864)
# sys.setrecursionlimit(2**20)
# thread = threading.Thread(target=kosaragu_algoratim(graph_g))
# thread.start()
print(kosaragu_algoratim(graph_g))

    