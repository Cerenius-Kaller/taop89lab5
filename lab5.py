# TAOP89 David Cerenius and Martin Kaller
import numpy as np
import time
import sys
import copy
from math import floor
from methods import *

e = 100

# Get the max value the array type can hold
# Can be used to "punish" values in matrix/vector by making them the most expensive
def getUpperLimit(array):
    return np.iinfo(array.dtype).max

# Choose the cheapest factories based on the average sending cost
# and calculates the least number required to meet the demand and
# return the indexes of these factories.
def getLeastAmountGreedyFactories(cavg, demand, supply):
    sum = 0
    indexs = []
    cavg2 = copy.deepcopy(cavg)
    while sum < demand:
        index = np.argmin(cavg2)
        sum += supply[index]
        cavg2[index] = getUpperLimit(cavg2)
        indexs.append(index)
    return (indexs)

# Get the 2D index of the smallest value in matrix
def getMin(cf, n):
    index = cf.argmin()
    a = floor(index/n)
    b = index - a*n
    return (a, b)

# Choose the "amount" cheapest factories based on the average sending cost
# and returns the indexes of these factories. 
def getGreedyFactoriesByAmount(cavg, amount):
    indexs = []
    cavg2 = copy.deepcopy(cavg)
    for i in range(amount):
        index = np.argmin(cavg2)
        cavg2[index] = getUpperLimit(cavg2)
        indexs.append(index)
    return (indexs)


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

t1=time.time()
x=np.zeros((m,n),dtype=int)
y=np.zeros((m),dtype=int)

ss=copy.deepcopy(s)
dd=copy.deepcopy(d)

# Average cost to send to every customer for each factory
cavg = c.sum(axis=1)
# Total demand for all customers
dsum = d.sum()

# Get indexes for lowest possible number of factories to meet the total demand.
# The factories choosen are the cheapest (to send) on average.
indexes = getLeastAmountGreedyFactories(cavg,dsum, s)

#Average demand multiplied with the average cost to send divided by average build cost.
tmp = c[indexes]
willingnessToBuildFactor = d.mean()*tmp.mean()/(f.mean()*e)


# Use the willingness to build factor to determine how many extra factories should be built
# compared to the previous (getLeastAmountGreedyFactories) amount.
amount = ((m-len(indexes))/m) * willingnessToBuildFactor**2.6  + len(indexes)

# Don't build more than possible
if amount > m:
    amount = m

indexes = getGreedyFactoriesByAmount(cavg,int(amount))

# Set factories built
for i in indexes:
    y[i] = 1

# Remove factories which aren't selected (by making cost to send the highest possible (almost inf))
cf = copy.deepcopy(c)
cf[np.setdiff1d(range(m), indexes)] = getUpperLimit(cf)

while sum(dd)>0:
    # Choose the cheapest route to send of all (selected) factories 
    bestindex = getMin(cf, n)
    currentsupply = ss[bestindex[0]]
    currentdemand = dd[bestindex[1]]
    if(currentsupply < currentdemand):
        # If the choosen factory can't satisfy customer demand, take as much as possible
        # Remove the factory
        cf[bestindex[0]] = getUpperLimit(cf)
        ss[bestindex[0]] -= currentsupply
        dd[bestindex[1]] -= currentsupply
        x[bestindex] = currentsupply
    else:
        # If factory can meet demand, satisfy customer demand
        # Remove customer
        cf[:,bestindex[1]] = getUpperLimit(cf)
        ss[bestindex[0]] -= currentdemand
        dd[bestindex[1]] -= currentdemand
        x[bestindex] = currentdemand

elapsed = time.time() - t1
print('Tid: '+str('%.4f' % elapsed))
cost = sum(sum(np.multiply(c, x))) + e*np.dot(f, y)
print('Problem:', prob, ' Totalkostnad: '+str(cost))
print('y:', y)
print('Antal byggda fabriker:', sum(y), '(av', m, ')')
