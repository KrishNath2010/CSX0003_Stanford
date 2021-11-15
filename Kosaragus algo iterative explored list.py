# -*- coding: utf-8 -*-
"""
Created on Sun Feb 14 18:34:03 2021

@author: Krish Nath
"""
from datetime import datetime
import copy
f = open('SCC1.txt', 'r')
graph_a = {}
lines = f.readlines()
lines_length = len(lines)
key = 1
curr = []
remaining=[]
index=-1
explored = []
for l in lines:
    index+=1
    #print('new',l)
    curr_line = l.split()
    new_key = int(curr_line[0])
    new_val = int(curr_line[1])
    if (new_key == key):
        #print('made',key)
        curr.append(new_val)
        if (new_val not in graph_a.keys()) and (new_val not in remaining):
            remaining.append(new_val)
    else:
        graph_a[key] = curr
        curr = []
        key += 1
        #print('key',key)
        while (new_key != key):
            key+=1
            #print(key,int(curr_line[0]))
            #if (key>20):
                #print((2/0))
        curr.append(new_val)
        if (index==(lines_length-1)):
            graph_a[key] = curr
            #print('all_keys',graph_a.keys())
            if (new_val not in graph_a.keys()):
                remaining.append(new_val)
                #print('in')
#print(graph_a)
#print('remaining initial', remaining)
graph_keys = graph_a.keys()
#print('keys', graph_keys)
rlen = len(remaining)
index=0
for i in range(rlen):
    r = remaining[index]
    
    if (r in graph_keys):
        remaining.remove(r)
    else:
        index += 1
#print('remaining final', remaining)
for r in remaining:
    graph_a[r] = []

#print('Graph', graph_a)
#de = 4/(3-3)
graph_a = {1:[4,3],2:[3,1],3:[],4:[2]}
graph_b = {1:[2,11],2:[],3:[2,4],4:[],5:[6],6:[7],7:[8],8:[9],9:[],10:[9,11],11:[]}
print(len(explored))
# make function
stack = []
result = []

def dfs_forest(graph_g, vertices, result_list):
    # in a while loop, keep looking for vertices that are still unvisited, 
    # and call dfs on each
    for w in vertices:
        if (w not in explored):
            # start with the first unvisited vertex s
            dfs(graph_g, w, result_list)
            now = datetime.now()
            current_time = now.strftime("%H:%M:%S")
            print("Dfs Forset Current Time =", current_time)
    return
def dfs(graph_g, s, result_list):
    #print(s, explored)
    dfs_stack = []
    count=0
    dfs_stack.append(s)
    while (dfs_stack != []): 
        count+=1
        n = dfs_stack.pop()
        if ((count% 4000) == 0):
            now = datetime.now()
            current_time = now.strftime("%H:%M:%S")
            print("Current Time =", current_time, ", Count:", count, ', Result_len',len(result_list),', Stack_len',len(dfs_stack),', Explored_len',len(explored),'element',n)
        #print("Popped", n)
        if (n in explored):
            if (n not in result_list):
                result_list.append(n)
                #print("1 Appending", n)
            continue
        #mark	n	as	explored	
        explored.append(n)
    	#for every edge	(n, v)	:
        #print('dfs', graph_g.get(n))
        val = graph_g.get(n)
        if (val == [] or val == None):
            result_list.append(n)
            #print("2 Appending", n)
            continue
        dfs_stack.append(n)
        for q in val:
            #if	v	unexplored	
            if (q not in explored):
                # do dfs
                #print("calling for", q)
                dfs_stack.append(q)
                #print("back")
    return

graph_g = graph_a

def kosaragu_algoratim(graph_g):
    vertices = []
    reverse_graph = {}
    graph_lenth = len(graph_g)
    print('Graph Len:', graph_lenth)
    #print(graph_lenth)
    for s in range(graph_lenth):
        reverse_graph[s + 1] = []
    # Make a list of all vertices
    for i in graph_g:
        vertices.append(i)
    dfs_forest(graph_g, vertices, stack)
    print('dfs 1 comlete')
    #print('explored',explored)
    explored.clear()
    #print("stack:", stack)
    #return 0
    # key = 0
    # for w in graph_g.values():
    #     print('w', w)
    #     key += 1
    #     for q in w:
    #         print('q', q, 'key', key)
    #         reverse_graph[q].append(key)
    for w in graph_g:
        #print('Key:', w)
        val = graph_g.get(w)
        #print('Value:', val)
        for v in val:
            reverse_graph[v].append(w)
    
    print('graph_reversal complete')
    #print('Reverse Graph', reverse_graph)
    #return
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

    