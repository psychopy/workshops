from __future__ import division
import numpy as np
from scipy import stats
import matplotlib.pyplot as plt
import seaborn # make graphs pretty (just by importing)

# This demonstrates how to do a simple resampling test in Python
# The test is called a "permutation test" and is equiv to a t-test

nResamples = 5000
smurfs = [18.6, 18.3, 18.0, 16.0, 18.4, 18.1, 19.5, 19.2,
        18.9, 17.1, 15.9, 19.5, 10.4]
dwarfs = [11.0, 8.9, 8.0, 14.0, 11.4, 8.1, 18.5]

smurfMean = np.mean(smurfs)
dwarfMean = np.mean(dwarfs)
print "Mean smurf: %.3f Mean Dwarf:%.3f" %(smurfMean, dwarfMean)
print "Mean difference :%.3f" %(smurfMean-dwarfMean)

popn = smurfs+dwarfs
meanDiffs = []
for n in range(nResamples):
    np.random.shuffle(popn)
    newSmurfs = popn[len(dwarfs):]
    newDwarfs = popn[:len(dwarfs)]
    thisDiff = np.mean(newSmurfs)-np.mean(newDwarfs)
    meanDiffs.append(thisDiff)

nMoreExtreme = sum(np.abs(meanDiffs)>(smurfMean-dwarfMean))
p = nMoreExtreme/nResamples
print("p={} based on permutation test".format(p))
t, pTraditional = stats.ttest_ind(smurfs, dwarfs)
print("p={} based on Student t-test".format(pTraditional))
plt.hist(meanDiffs)
plt.show()

