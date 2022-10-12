from cmath import inf
from math import floor
import numpy as np
import copy
import sys
limit = -1

def getleastnrfactories(d, s):
    demand = d.sum()
    counter = 0
    supply = -np.sort(-s, kind ='mergesort')
    summa = 0
    for i in supply:
        summa+=i
        counter+=1
        if summa >= demand:
            break
def getleastnrgreedyfactories(cavg, demand, supply):
    sum = 0
   
    indexs = []
    cavg2 = copy.deepcopy(cavg)
    while sum < demand: 
        index = np.argmin(cavg2)
       
        sum += supply[index]
        cavg2[index] = np.iinfo(cavg2.dtype).max
        indexs.append(index)
    
    return (indexs)

def getMinAndIncrease(cf,n):
    index = cf.argmin()
    a = floor(index/n)
    b = index - a*n
    return (a,b)

def setmax(index,array):
    array[index] = np.iinfo(array.dtype).max
        