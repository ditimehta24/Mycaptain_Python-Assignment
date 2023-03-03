# -*- coding: utf-8 -*-
"""
Created on Fri Mar  3 18:02:53 2023

@author: Diti Mehta
"""

def most_frequent(string):
    print("Please enter a string:")
    dict={}
    for char in string:
        if char in dict:
            dict[char]+=1
        else:
            dict[char]=1
    list=[(key, value) for key, value in dict.items()]
    list.sort(key=lambda x: x[1],reverse=True)
    for item in list:
        print(item[0],":",item[1])
