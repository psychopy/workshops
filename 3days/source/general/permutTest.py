from __future__ import division
import numpy as np
from scipy import stats
import matplotlib.pyplot as plt

smurfs = [13.6, 10.3, 10.0, 16.0, 12.4, 9.1, 14.5, 10.2,
        8.9, 11.1, 15.9, 9.5, 10.4]
dwarfs = [11.0, 8.9, 8.0, 14.0, 11.4, 8.1, 18.5]
popn = smurfs+dwarfs

smurfMean = np.mean(smurfs)
dwarfMean = np.mean(dwarfs)

nResamples = 10000
allDiffs = []
for sampN in range(nResamples):
    np.random.shuffle(popn) #this shuffles the population 'in place'
    resampSmurfs = popn[0:len(smurfs)] #from 0:13
    resampDwarfs = popn[len(smurfs):] #from 13:end
    #find the difference in means
    thisDiff = np.mean(resampSmurfs) - np.mean(resampDwarfs)
    allDiffs.append(thisDiff)

origDiff = dwarfMean-smurfMean
nGreater = sum(np.abs(allDiffs) > np.abs(origDiff))
pPermTest = nGreater/nResamples
print('permutation test: p=%.3f (two tails)' %(pPermTest))

#for comparison let's do an independent-samples t-test
t, p = stats.ttest_ind(smurfs, dwarfs)
print('t-test: t=%.3f p=%.3f' %(t, p))

plt.hist(allDiffs)
#show the location of orig (from bottom to top of y axis)
ylims = plt.ylim()
plt.plot([origDiff, origDiff], ylims, 'r--')
#show the figure
plt.show()
