import numpy as np
import time
import sys
import copy
from methods import *
e=1

prob=" ".join(sys.argv[1:]).split('.')[0]
fil=prob+'.npz'

npzfile = np.load(fil)
npzfile.files
m=npzfile['m']
n=npzfile['n']
s=npzfile['s']
d=npzfile['d']
f=npzfile['f']
c=npzfile['c']

print ('m:',m,' n:',n)
print ('s:',s)
print ('d:',d)
print ('f:',f)
print (c)

t1=time.time()
x=np.zeros((m,n),dtype=int)
y=np.zeros((m),dtype=int)

ss=copy.deepcopy(s)
dd=copy.deepcopy(d)

while sum(dd)>0:
    # find facility, find customer, send, at min cost
    # set x and y
    # deduct from ss and dd, 
    # --------
    break


print(c.sum(axis=1)/n)
demand = d.sum()
counter = 0
supply = -np.sort(-s, kind ='mergesort')

indexes = getleastnrgreedyfactories(c.sum(axis=1),demand, s)
for i in indexes:
    y[i] = 1
cf = c[indexes]

print(cf)

while sum(dd)>0:
    bestindex = getMinAndIncrease(cf, n)
    currentsupply = ss[bestindex[0]]
    currentdemand = dd[bestindex[1]]
    print(currentdemand,currentsupply)
    if(currentsupply < currentdemand):
        cf[bestindex[0]] = np.iinfo(cf.dtype).max
        ss[bestindex[0]] -= currentsupply
        dd[bestindex[1]] -= currentsupply
        x+=
    else:
        cf[:,bestindex[1]] = np.iinfo(cf.dtype).max
        ss[bestindex[0]] -= currentdemand
        dd[bestindex[1]] -= currentdemand
    print(cf)
    
   






elapsed = time.time() - t1
print ('Tid: '+str('%.4f' % elapsed))

cost=sum(sum(np.multiply(c,x))) + e*np.dot(f,y)
print ('Problem:',prob,' Totalkostnad: '+str(cost))
print ('y:',y)
print ('Antal byggda fabriker:',sum(y),'(av',m,')')