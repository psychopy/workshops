
.. PEP 2014 slides file, created by
   hieroglyph-quickstart on Tue Mar  4 20:42:06 2014.

.. _customRandomisation:

Randomising with constraints
===============================

Making custom randomised orders
----------------------------------------------

We have already seen that by default builder allows you to present trials in one of three orders, including:

- Random
- Sequential
- Full Random

From this we know that if we want a pre-specified order, the best way to do this is to use the 'sequential' option and specify that order in our conditions file. But what if we want more "custom", "on-the-fly" randomisation. 

Using loops for loading stimuli/conditions
----------------------------------------------

Loops don't just have to be used to present trials/repeat stimuli, they can also be used to load in your conditions file, and manipulate it how you want:

- Make a conditions file with the header 'Word' and a list of words to present
- Add a routine to your experiment and call it 'loading'. 
- Add a code component to this routine and at under *Begin Routine* use :code:`print(Word)

.. nextslide::

Once we know how to load our stimuli, we can use our python skills to manipulate the order of words from within our experiment itself. 

Some cases where this can be useful:

- You want some stimuli to be presented at fixed trials (e.g. 5th, 10th, 15th) trial is fixed, but with the interleaving trials selected randomy.
- You want to randomly pick a subset of the to-be-presented words in some practice trials.

and many more! We will practice with the first case example. 

Setting up our conditions file
----------------------------------------------

In this example, we are going to make sure every 5th word is presented in a fixed order, with the other words presented randomly. First, set up your conditions file to be something like this (but with more words). 

+----------+-------------+-------------+
| Word     | Fixed       | N           |
+==========+=============+=============+
| Cat      | 0           | 1           |
+----------+-------------+-------------+
| Dog      | 0           | 2           |
+----------+-------------+-------------+
| Fish     | 0           | 3           |
+----------+-------------+-------------+
| Owl      | 0           | 4           |
+----------+-------------+-------------+
| Tree     | 1           | 5           |
+----------+-------------+-------------+

.. nextslide::

Here our column "Word" is the word that will be presented and the column "Fixed" indicates if we want that word to be in a fixed location. 

+----------+-------------+-------------+
| Word     | Fixed       | N           |
+==========+=============+=============+
| Cat      | 0           | 1           |
+----------+-------------+-------------+
| Dog      | 0           | 2           |
+----------+-------------+-------------+
| Fish     | 0           | 3           |
+----------+-------------+-------------+
| Owl      | 0           | 4           |
+----------+-------------+-------------+
| Tree     | 1           | 5           |
+----------+-------------+-------------+


Accessing the "fed in" trial info
----------------------------------------------

We could load these variables into our experiment in several ways. Remember that the ` Trial Handler <https://www.psychopy.org/api/data.html#psychopy.data.TrialHandler>`_ loads in a conditions file as a list of dictionaries. Infact, we can access that list directly using :code:`trials.trialList` where :code:`trials` is the name of our loop. Or we could access a single trial dictionary using :code:`trials.trialList[n]` where *n* is the index. 

.. note::
	There are several inbuilt fuctions that can be handy for use with trialHandler:

	:code:`trials.getCurrentTrial()` - fetches the current trial info
	:code:`trials.getFutureTrial(n)` - fetches the info of the trial n ahead
	:code:`trials.getEarlierTrial(n)` - fetches the info of the trial n back

Making a custom trial list
----------------------------------------------

Once we have acess to the list of trials we can pick out our random trials::

	oldTrials = myLoop.trialList

	randomTrials = []
	for myTrial in oldTrials:
		if not myTrial['Fixed']:
			randomTrials.append(myTrial)

.. nextslide::

Then we can piece our trialList back together by randomly sampling without replacement from the :code:`randomTrials` list::

	newTrials = []

	for myTrial in oldTrials:
		if myTrial['Fixed']:
			# Use this trial
			newTrials.append(myTrial)
		else:
			# resample without replacement
			shuffle(randomTrials)
			newTrials.append(randomTrials[-1])
			randomTrials.pop()
	print(newTrials)

Working through a custom trial list in builder
----------------------------------------------

Once we have our custom randomised trial list we need to use that in Builder. Usually we wrap a loop around a routine and feed in a conditions file. Then :code:`nReps` corresponds to the number of times we repeat that file. This time we need to do it a little differently.....

.. nextslide::

Add a routine called 'showWords' and inside it add a simple textBox component that lasts for 0.5 seconds. Wrap a loop around the routine and call it 'trials'. This time we want nReps to correspond to the length of our custom trialList ('newTrials'). So you can type :code:`len(newTrials)` in the nReps field. 

.. note::
	Online :code:`len()` might not smoothly translate in the nReps field. If that happens make a custom variable after the creation of 'newTrials' and use that instead in teh nReps field, e.g. :code:` myNReps = len(newTrials) will smoothly translate in a code component. 

.. nextslide::

OK finally, we need to use the trial info from each run in our textBox component. In the Text field of the component type :code:`newTrials[trials.thisN]` and make sure to *set every repeat*. 

.. note::
	Online :code:`trials.thisN` might not smoothly translate (but it should do *very* soon). In place, you can use a code component to count the iterations, in the 'Begin Experiment' tab type :code:`trialCount = 0` then in the 'End Routine' tab type :code:`trialCount +=1` then use 'trialCount' in place of 'trials.thisN'.

.. nextslide::

If you ran that now you might be surprised to see a full dictionary printed out on each trial. Remember *each trial is a dictionary* we need to access the value corresponding to the key 'Word'. So for the final touch update :code:`newTrials[trials.thisN]` to :code:`newTrials[trials.thisN]['Word']`

Exercise (15 mins)
----------------------------------------------

Present a list of numbers and alternate numbers between odd and even.

*Hint: remember how we can seperate out specific conditions (e.g. randomTrials) and how we can sample without replacement using :code:`shuffle()` and :code:`pop()`

