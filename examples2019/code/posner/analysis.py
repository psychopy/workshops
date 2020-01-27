import pandas as pd
import glob
import scipy
from scipy import stats

"""Here we load one or more datafile(s) from psychopy, remove 
"""
filenames = glob.glob("posner/data/*.csv")
print(filenames)
for thisFilename in filenames:
    print(thisFilename)
    thisDat = pd.read_csv(thisFilename)
    
    #filter out RT>1.0s and incorrect response
    filtered = thisDat[ thisDat['rt']<=1.0 ]
    filtered = filtered[ filtered['corr']==1 ]
    print(filtered['rt'], len(filtered))
    
    #extract RTs based on condition
    conflict = filtered[filtered.descr == 'conflict']
    congruent = filtered[filtered.descr != 'conflict']
    
    #get mean/std.dev
    meanConfl = scipy.mean(conflict['rt'])
    sdConfl = scipy.std(conflict['rt'], ddof=1) # ddof=1 means /sqrt(N-1)
    meanCongr = scipy.mean(congruent['rt'])
    sdCongr = scipy.std(congruent['rt'], ddof=1)
    print("Conflict = %.3f (sd=%.3f)" %(meanConfl, sdConfl))
    print("Congruent = %.3f (sd=%.3f)" %(meanCongr, sdCongr))
    
    # can even run a t-test (this is testing within a single individual)
    t, p = stats.ttest_ind(conflict['rt'], congruent['rt'])
    print("Independent samples t-test: t=%.3f, p=%.4f" %(t, p))
    