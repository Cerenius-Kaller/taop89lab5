from GreedyExponentialWeightedMean import GreedyExponenialWeightedMean
import numpy as np

tests = [("floc1", 3880),("floc2",15252),("floc3",244101),("floc4",118802),("floc5",141630),("floc6",106668),("floc7",174760),("floc8",314657)]

average = 0

def BinarySearchGreedyExponenialWeightedMean(fil):
    factor = 1
    delta = 1
    while(True):
        (cost, y,t) = GreedyExponenialWeightedMean(fil,factor)
        factors = [factor-delta, factor, factor+delta]

        (costL, y,t) =GreedyExponenialWeightedMean(fil,factor-1)
        (costR, y,t) = GreedyExponenialWeightedMean(fil,factor+1)

        costs = [costL,cost,costR]

        # print(costs)

        index = np.argmin(costs)
        factor = factors[index]
        delta -= 0.1

        if(delta < 0.01):
            return(costs[index])

BinarySearchGreedyExponenialWeightedMean("./data/floc3.npz")






