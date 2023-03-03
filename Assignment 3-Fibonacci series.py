# -*- coding: utf-8 -*-
"""
Created on Fri Mar  3 17:41:03 2023

@author: Diti Mehta
"""

n= int(input("How many terms? "))
n1,n2 = 0,1
count=0
if n==1:
   print("Fibonacci sequence upto",n,":")
   print(n1)
else:
   print("Fibonacci sequence:")
   while count<n:
       print(n1)
       nth = n1 + n2
       n1 = n2
       n2 = nth
       count=count+1
