
.. PEP 2014 slides file, created by
   hieroglyph-quickstart on Tue Mar  4 20:42:06 2014.

.. _clocksAndTrialCounders:

Clocks and trial counters
===============================

Clocks
==============================

Keeping track of time is really important to most experiments. In PsychoPy there are many useful clocks that live "under the hood", which we can use in our experiment:

*	:code:`routineClock` : Every routine has it's own clock with this naming convention e.g. a routine called "trial" would have a clock called "trialClock".
*	:code:`t` : We might not need the routineClock, because the variable `t` represents the time since the start of the current routine anyway!

Making custom clocks
-----------------------------

If we want to use a custom clock (e.g. to measure the time across several routines) we can always make a clock wihin a code component::

	myClock = core.Clock()

.. note::
	If we are working online we will need to change our code component "type" to be "Both" and use :code:`myClock = util.Clock()` on the JS side - this is because the 'Clock' class lives in different modules in PsychoPy and PsychoJS. 

Useful methods for use with clocks
-----------------------------------

Once we have our clock there are several useful methods we might want to know about. 

*	:code:`.getTime()`: fetches the time on the current clock (note that we don't need to do this for :code:`t` because t represents the time on the current routine clock rather than a clock itself)
*	:code:`.reset()` : resets a clock - note that this is OK on our custom clocks, but it is best that we don't reset any of PsychoPy's inbuilt clocks. 


Adding a timer to your experiment
-----------------------------------

Now that we know how to make a clock and how to access the time on it, we can easily add a timer to our experiment to show our participant how far into a trial, or the experiment they are. 

.. nextslide::

Add a text component to your trial routine and position it in the top right corner (in height units you will want something like `pos = (0.4,0.4)`. Then in the `text` field all we need is to write :code:`$t` and **set every frame**. 

.. note::
	Depending on your PsychoPy version you might need to use :code:`t` - omiiting the dollar sign. Remember that you only need a $ at the start of a field if there is not already a $ int he parameter name. 

.. nextslide::

The properties of the text component should look like this:

.. image:: /_images/timer_properties.png
    :align: left
    :scale: 50 %

.. nextslide::

OK now you should have a timer to show participants how far through a trial they are!! If you wanted to show them how far into the experiment they are you could add a code component and in the `Begin Experiment` tab write :code:`expClock = core.Clock()`. Then in your text component replace :code:`t` with :code:`expClock.getTime()`.

Ending a trial early 
-----------------------------------

Imagine we want to end the experiment early if your participant takes too long to respond (this might be particularly important for online studies!). Now we know how to time each trial we can use those clocks to end the task early if a trial takes too long. 

.. nextslide::

Add a code component and in the "Each Frame" tab write::

	threshold = 10 # number of seconds before we end the experiment
	if t > threshold:
		continueRoutine = False # end the current routine
		trials.finished = True # exit the current loop 

.. nextslide::

If we have any routines that follow this we will also want to make sure we end those too, so we might also want to extend this code a little::

	threshold = 10 # number of seconds before we end the experiment
	endTask = False
	if t > threshold:
		continueRoutine = False # end the current routine
		trials.finished = True # exit the current loop 
		endTask = True

Then add a code component to all routines following this and int he "Begin Routine" tab type::

	if endTask:
		continueRoutine = False

This way all following routines would also be ended if the participant took too long to respond. 

Trial counters
====================================
How is PsychoPy counting trials?
------------------------------------

Each loop we add to our experiment will automatically be counting the number of trials that have occured already (as well as how many repetitions of our trials list have occured!). Run your experiment and have a loop at the output. You will see some useful information in the headers of your file.

.. nextslide::

*	:code:`trials.thisRepN` - the current repetition of your conditions file
*	:code:`trials.thisTrialN` - the current trialN within this repetition
*	:code:`trials.thisN` - the current trialN regardless of repetition
*	:code:`trials.thistrialIndex` - the index of the current trial from within our trialList (the conditions spreadsheet).

Adding a trial counter
------------------------------------

Now we know how PsychoPy counts trials, we can use this info to add a trial counter and show how far through the experiment participants are. Add a text component and position it in the top left (in height units pos = (-0.4, 0.4)). In the text field add :code:`$trials.thisN`. 

trial counters online
------------------------------------

Currently (PscyhoPy version 2021.1.4) the trial counter variables exist in PsychoPy but not PsychoJS (but they will do soon!). Instead, we can use our own custom trial counters. Add a code component and in the "Begin Experiment" tab type :code:`trialCounter = 0`, then in the "Begin Routine" tab type :code:`trialCounter += 1`. Finally, replace the text in your text component with :code:`$trialCounter` and **set every repeat**. 


Quick Exercise
------------------------------------

Try to end the experiment on trial 5 using a code component.

What next?
------------------------------------

We can make more flexible and dynamic experiments using code, including:
   - :ref:`addingFeedback`
   - :ref:`mouse3days`
