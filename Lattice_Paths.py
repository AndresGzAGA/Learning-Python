# -*- coding: utf-8 -*-
'''
Starting in the top left corner of a 2×2 grid, and only being able to move to the right and down, there are exactly 6 routes to the bottom right corner.

How many such routes are there through a 20×20 grid?
'''

'''
def count(x):
    
    #Counts the number of 1's that a number has got.
    
    c=0
    for a in range(len(str(x))):
        if str(x)[a]=='1':
            c+=1
    return c
   
def bin1(x):
    
    #Adds 1 to a binary number.
    
    x='0b'+str(x)
    return int(bin(int(x,base=0)+1)[2:])

def BIN(x):
    
    #Converts from base 10 to base 2.
    
    return int(str(bin(x))[2:])

x=1048574 #11111111111111111110 base 2
c=0
while x<1099510579200:
    x+=1
    if count(BIN(x))==20:
        c+=1
print c
'''
from math import factorial

def PcR2(a):
    '''
    Permutaciones con repetición con 2*a elementos, cada uno se repite a veces.
    '''
    return factorial(2*a)/(factorial(a)**2)