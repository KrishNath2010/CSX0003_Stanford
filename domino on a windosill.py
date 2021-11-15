# -*- coding: utf-8 -*-
"""
Created on Thu Mar 18 11:02:49 2021

@author: Krish Nath
"""

tralis=int(input())
answer_list=[]
for d in range(tralis):
    numbers_1=input().split()
    numbers_2=input().split()
    n=int(numbers_1[0])
    k_1=int(numbers_1[1])
    k_2=int(numbers_1[2])
    w=int(numbers_2[0])
    b=int(numbers_2[1])
    geretor=None
    if k_1>=k_2:
        geretor=k_1
    else:
        geretor=k_2
    diff=abs(k_2-k_1)
    possible_w=(geretor-diff)+(diff//2)
    b_1=n-k_1
    b_2=n-k_2
    geretor_b=None
    if b_1>=b_2:
        geretor_b=b_1
    else:
        geretor_b=b_2
    diff_b=abs(k_2-k_1)
    possible_b=(geretor_b-diff_b)+(diff_b//2)
    if possible_w>=w and possible_b>=b:
        answer_list.append('YES')
    else:
        answer_list.append('NO')
for s in answer_list:
    print(s)
    
    
    