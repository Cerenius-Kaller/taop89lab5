from GreedyExponentialWeightedMean import GreedyExponenialWeightedMean
from BinarySearchGreedyExponenialWeightedMean import BinarySearchGreedyExponenialWeightedMean

tests = [("floc1", 3880,2),("floc2",15252,7),("floc3",244101,3),("floc4",118802,9),("floc5",141630,10),("floc6",106668,12),("floc7",174760,11),("floc8",314657,30)]

average = 0
delimeter = ","

print("Test",delimeter,"Optimum",delimeter, "Herustic", delimeter, "%", delimeter, "Time")
for (test, opt, opty) in tests:
    (cost, y, t) = GreedyExponenialWeightedMean("./data/"+test+".npz",2.6)
    procent = (cost/opt)-1
    average += procent
    print(test,delimeter,opt,"("+str(opty)+")",delimeter,cost,"("+str(y)+")",delimeter,str('%.4f' % procent),delimeter,str('%.4f' % t))

# print("Average", average/len(tests))