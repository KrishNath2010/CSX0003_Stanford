# -*- coding: utf-8 -*-
"""
Created on Tue Mar 16 21:56:48 2021

@author: Krish Nath
"""

from heapq import heapify, heappush, heappop
 
# Creating empty heap
heap = []
heapify(heap)
 
# Adding items to the heap using heappush function
heappush(heap, 5)
heappush(heap, 3)
heappush(heap, 17)
heappush(heap, 10)
heappush(heap, 84)
heappush(heap, 19)
heappush(heap, 6)
heappush(heap, 22)
heappush(heap, 9)
 
# printing the value of minimum element
for q in range(6):
    print("Head value of heap : "+str(heap[0]))
     
    # printing the elements of the heap
    print("The heap elements : ")
    for i in heap:
        print(i, end = ' ')
    print("\n")
     
    element = heappop(heap)
    print('poped',element)
    # printing the elements of the heap
    print("The heap elements : ")
    for i in heap:
        print(i, end = ' ')