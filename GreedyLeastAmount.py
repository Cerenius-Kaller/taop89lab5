import numpy as np
import time
import sys
import copy
from methods import *
e=1

def GreedyExponenialWeightedMean(fil,factor):
    npzfile = np.load(fil)
    npzfile.files
    m=npzfile['m']
    n=npzfile['n']
    s=npzfile['s']
    d=npzfile['d']
    f=npzfile['f']
    c=npzfile['c']

    # print ('m:',m,' n:',n)
    # print ('s:',s)
    # print ('d:',d)
    # print ('f:',f)
    # print (c)

    t1=time.time()
    x=np.zeros((m,n),dtype=int)
    y=np.zeros((m),dtype=int)

    ss=copy.deepcopy(s)
    dd=copy.deepcopy(d)

    #Choose factory
    indexes = getleastnrgreedyfactories(c.sum(axis=1),d.sum(), s)

    for i in indexes:
        y[i] = 1

    cf = copy.deepcopy(c)
    cf[np.setdiff1d(range(m), indexes)] = np.iinfo(cf.dtype).max


    while sum(dd)>0:
        bestindex = getMinAndIncrease(cf, n)
        currentsupply = ss[bestindex[0]]
        currentdemand = dd[bestindex[1]]
        if(currentsupply < currentdemand):
            cf[bestindex[0]] = np.iinfo(cf.dtype).max
            ss[bestindex[0]] -= currentsupply
            dd[bestindex[1]] -= currentsupply
            x[bestindex] = currentsupply
        else:
            cf[:,bestindex[1]] = np.iinfo(cf.dtype).max
            ss[bestindex[0]] -= currentdemand
            dd[bestindex[1]] -= currentdemand
            x[bestindex] = currentdemand
        # print(cf)
        


    elapsed = time.time() - t1
    cost=sum(sum(np.multiply(c,x))) + e*np.dot(f,y)
    return (cost,sum(y),elapsed)