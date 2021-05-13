
.. _resampling:

Resampling statistics
---------------------------------------

A scripting language like Python is also great for doing resampling statistics procedures (bootstrapping, Monte Carlo simulations etc). Not everyone knows about those so we'll need to go through the logic of one such test while we create some code. This one is called a 'permutation test'.

.. nextslide::

Take the heights of 7 dwarfs and 13 smurfs::

    smurfs = [13.6, 10.3, 10.0, 16.0, 12.4, 9.1, 14.5, 10.2,
            8.9, 11.1, 15.9, 9.5, 10.4]
    dwarfs = [11.0, 8.9, 8.0, 14.0, 11.4, 8.1, 18.5]

I have a hypothesis that smurfs are just dwarfs painted blue. If so then they are really one population. We could test whether their heights are significantly different.

.. nextslide::

To get the difference in mean heights::

    import numpy as np
    smurfMean = np.mean(smurfs)
    dwarfMean = np.mean(dwarfs)

    print("smurfs=%.1f, dwarfs=%.1f" %(smurfMean, dwarfMean))

Was that unlikely to occur by chance?

.. nextslide::

Our Null Hypoth is that smurfs and dwarfs are the same. They are one population::

    popn = smurfs+dwarfs

    np.random.shuffle(popn) #this shuffles the population 'in place'
    resampSmurfs = popn[0:len(smurfs)] #from 0:13
    resampDwarfs = popn[len(smurfs):] #from 13:end
    print(len(resampSmurfs), resampSmurfs)
    print(len(resampDwarfs), resampDwarfs)

If smurfs and dwarfs are the same, this resample is as likely as the original sample

.. nextslide::

Given how easy it is to create a loop in Python, we could create thousands of those resamples and find out how unlikely our original was, according to the Null Hypoth::

    nResamples = 5000
    allDiffs = []
    for sampN in range(nResamples):
        np.random.shuffle(popn) #this shuffles the population 'in place'
        resampSmurfs = popn[0:len(smurfs)] #from 0:13
        resampDwarfs = popn[len(smurfs):] #from 13:end
        #find the difference in means
        thisDiff = np.mean(resampSmurfs) - np.mean(resampDwarfs)
        allDiffs.append(thisDiff)

    plt.hist(allDiffs)
    plt.show()

.. nextslide::

After our loop we can process the set of differences we measured and see what
distribution of values occurs (this is the Null Distribution)::

  origDiff = dwarfMean-smurfMean
  # 2-sided test is about the prob of being bigger magnitude (unsigned)
  # so we take abs() of the
  nGreater = sum(np.abs(allDiffs) > np.abs(origDiff))
  pPermTest = nGreater/nResamples

  print('permutation test: p=%.3f (two tails)' %(pPermTest))

.. nextslide::

We could compare the result we got with that from a traditional t-test::

    from scipy import stats  # add this to top of script?
    #for comparison let's do an independent-samples t-test
    t, p = stats.ttest_ind(smurfs, dwarfs)
    print('t-test: t=%.3f p=%.3f' %(t, p))

With programming skills, computing either the traditional or resampling estimates of `p` is easy

.. nextslide::

Note that:

    - the permutation test does not assume normal distribution
    - should agree, if there **is** a normal distribution
    - does not give you the (incorrect) belief that there is a single 'true' probability value (all estimates of p are simply estimates)
    - means nothing if your data are not representative (as with t-test but most people have forgotten)
    - needs thought to get right (maybe this is a good thing?)