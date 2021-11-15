# -*- coding: utf-8 -*-
"""
Created on Sun Feb 14 18:34:03 2021

@author: Krish Nath
"""
from datetime import datetime
import copy
f = open('SCC.txt', 'r')
graph_a = {}
lines = f.readlines()
lines_length = len(lines)
key = 1
curr = []
#remaining=[]
index=-1
explored = []
put_in_result = []
in_keys = []
largest_key = 0
now = datetime.now()
current_time = now.strftime("%H:%M:%S")
print(current_time, ': Starting graph creation')
for i in range(1000000):
    in_keys.append(0)
    
for l in lines:
    index+=1
    if ((index% 400000) == 0):
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        print(current_time, ': Working on line:', index)
    #print('new',l)
    curr_line = l.split()
    new_key = int(curr_line[0])
    new_val = int(curr_line[1])
    
    if (new_key > largest_key):
        largest_key = new_key
    if (new_val > largest_key):
        largest_key = new_val
        
    if (in_keys[new_key - 1] == 0):
        in_keys[new_key - 1] = 1
        graph_a[new_key] = []
        
    curr = graph_a[new_key]
    curr.append(new_val)
    graph_a[new_key] = curr

now = datetime.now()
current_time = now.strftime("%H:%M:%S")
print(current_time, ': Starting to work on remaining, largest key found =', largest_key)
for s in range(largest_key):
    if (in_keys[s] == 0):
        in_keys[s] = 1
        graph_a[s + 1] = []

now = datetime.now()
current_time = now.strftime("%H:%M:%S")
print(current_time, ': Completed creating the graph')

#print('Graph', graph_a)
#de = 4/(3-3)
#graph_a = {1:[4,3],2:[3,1],3:[],4:[2]}
graph_b = {1:[2,11],2:[],3:[2,4],4:[],5:[6],6:[7],7:[8],8:[9],9:[],10:[9,11],11:[]}
# make function
stack = []
result = []

def dfs_forest(graph_g, vertices, result_list):
    # in a while loop, keep looking for vertices that are still unvisited, 
    # and call dfs on each
    for w in vertices:
        if (explored[w-1]==0):
            # start with the first unvisited vertex s
            dfs(graph_g, w, result_list)
            now = datetime.now()
            current_time = now.strftime("%H:%M:%S")
            print(current_time, ': Dfs Forset - 1 DFS call done')
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
            print(current_time, ': Count:', count, ', Result_len',len(result_list),', Stack_len',len(dfs_stack),', Explored_len',len(explored),'element',n)
        #print("Popped", n)
        if (explored[n-1]== 1):
            if (put_in_result[n-1] == 0):
                result_list.append(n)
                put_in_result[n-1] = 1
                #print("1 Appending", n)
            continue
        #mark	n	as	explored	
        explored[n-1]=1
    	#for every edge	(n, v)	:
        #print('dfs', graph_g.get(n))
        val = graph_g.get(n)
        if (val == [] or val == None):
            result_list.append(n)
            put_in_result[n-1] = 1
            #print("2 Appending", n)
            continue
        dfs_stack.append(n)
        for q in val:
            #if	v	unexplored
            # if ((q > 853359) or (q < 1)):
            #     print("Disaster!!!!!!!!!!")
            #     print(q)
            if (explored[q-1]==0):
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
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    print(current_time, ': Graph Len:', graph_lenth)
    #print(graph_lenth)
    for s in range(largest_key):
        reverse_graph[s + 1] = []
    # Make a list of all vertices
    for i in graph_g:
        vertices.append(i)
    for i in range(largest_key):
        explored.append(0)
        put_in_result.append(0)
    #print('Length of explored',len(explored))
    
    dfs_forest(graph_g, vertices, stack)
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    print(current_time, ': DFS 1 comlete')
    #print('explored',explored)
    for i in range(largest_key):
        explored[i-1] = 0
        put_in_result[i-1] = 0
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
    
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    print(current_time, ': Graph_reversal complete at time')
    #print('Reverse Graph', reverse_graph)
    #return
    answer = []
    num = graph_lenth
    while (num != -1):
        #print(num, 'num')
        num -= 1
        use = stack[num]
        #print('explored1', explored)
        if (explored[use-1]==0):
            #print(use, 'looking')
            result.clear()
            #print(result, 'result')
            dfs(reverse_graph, use, result)
            #print(result, 'result2')
            #print('old', answer)
            copied_result = copy.deepcopy(result)
            answer.append(copied_result)    
            #print("SCC:", result)
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    print(current_time, ': DFS 2 comlete')
    return answer
# import sys
# import threading
# threading.stack_size(67108864)
# sys.setrecursionlimit(2**20)
# thread = threading.Thread(target=kosaragu_algoratim(graph_g))
# thread.start()
answer_list = kosaragu_algoratim(graph_g)
#print(answer_list)
list_of_sublist_lengths = []
for sublist in answer_list:
    sublist_length = len(sublist)
    list_of_sublist_lengths.append(sublist_length)
print('Unsorted:', list_of_sublist_lengths)
list_of_sublist_lengths.sort()
print('Sorted:', list_of_sublist_lengths)
list_len = len(list_of_sublist_lengths)
for e in range(list_len - 1, list_len - 6, -1):
    print(list_of_sublist_lengths[e])
