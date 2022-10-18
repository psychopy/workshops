
.. _session13Days:

Building better experiments
==============================

Using Builder
--------------------------------------

Today we will work through making a `Numerical Stroop <https://run.pavlovia.org/Hirst/workshopnumberstroop/>`_  task in PsychoPy. (Try it on your phone!)

.. image:: /_images/number_stroop_qr.png
	:width: 40%
	:align: center

If your PsychoPy isn't open already - open it now!

What makes a PsychoPy experiment?
--------------------------------------

A builder experiment has three main sections. To start making an experiment we add routines to our flow and add components to our routines.

.. image:: /_images/builder_terms.png

Gather participant info
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Every experiment starts with a dialog box to gather some info about the participant/experiment. By default "participant" and "session" are gathered - and these are used to set the filename of that participant. 

.. image:: /_images/exp_info.png
	:width: 80%
	:align: center

.. note::
	In the current release (2022.2.4) check box options are not yet supported online.

Creating a routine
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

A Routine is the basic building block of PsychoPy experiments. They could be complex (e.g. a single trial) or simple (e.g. an Inter-Trial-Interval presenting a fixation cross). 

.. image:: /_images/routines_basics.png
	:width: 90%
	:align: center

To begin with, we want a routine to present two numbers on the screen.

Changing things trial-by-trial
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

To present several trials, add a loop around the routine to repeat. If something changes trial-by-trial, we make a spreadsheet. Each header is a variable, each row corresponds to the value of that variable on each trial.

.. figure:: /_images/loops_and_conditions.png
	
	Once we have inserted a loop we can add a spreadsheet of trials to the "conditions" field.

.. nextslide::

Then make sure to use that variable to set the parameter of a component on every repeat of your loop.

.. image:: /_images/set_every_repeat.png
	:width: 60%
	:align: center

Let's start by presenting a different pair of numbers on each trial and allowing the participant to press the left and right arrow keys to press a number.


*Warm up exercise (10 mins)*
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

- Make the size (letter height) of the numbers change trial.
- Add a column to the conditions spreadsheet to note if this trial is congruent (numerically larger number is also physically larger) or incongruent (numerically larger number is physically smaller). 
- Add an instructions routine and a thanks routine to the experiment. 

When you are finished, come back to the main session and collect one run of your task so that we can talk through the data file.

.. _keyboardAccuracy:

Storing accuracy 
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

It is very easy to store accuracy from a keyboard in PsychoPy. In our experiment, the participant can press either the left or right arrow key. So, we add a column to our spreadsheet to indicate what the correct answer is. 

.. figure:: /_images/keyboard_acc_spreadsheet.png

	In this example, the numerically larger number is the correct answer. The corrAns column tells us which key is the correct answer. 

.. nextslide::

In our keyboard component, we can then select "Store correct" and use the variable :code:`$corrAns` in the field. 

.. figure:: /_images/store_correct_keyboard.png
	
	The data tab of the keyboard component, to store the correct answer click "store correct" if the correct answer changes trial by trial use a variable that is set from the spreadsheet.


.. _blockDesigns3Days:


Block designs and counterbalancing
=========================================


Randomized block designs
--------------------------------------

A block design is where we have sets of similar trials organized into blocks rather than having trials interleaved.

e.g.
  - a block of faces to recognize or a block of houses
  - a block of Stroop task in English and a block in French
  - a block of valid trials versus a block of invalid trials

Note: these are all cases where the components would be identical between blocks.

The natural approach
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

When people have several "blocks" the natural move is to add separate routines for those blocks:

.. image:: /_images/natural_error.png
	:align: center

But then, how do we randomise the order of the blocks in the experiment?


Blocking: Case 1
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Instead of a Routine for each block, create one Routine and reuse it for different blocks. You can feed in a different spreadsheet per block by nesting your loops!:


.. image:: /_images/case1_blocks.png


Blocking: Case 2
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

If you do have two blocks that contain very different stimuli/components the approach to take is to control the number of times each block repeats using an outer-loop. 

.. image:: /_images/case2_blocks.png

Blocking: Our example
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Imagine we want our task to include a block of neutral trials and a block of congruent/incongruent trials. 

We need to create a total of 3 conditions files:

- neutral_conditions.xlsx - A spreadsheet with neutral trials.
- congruency_conditions.xlsx - A spreadsheet with con/incon trials.
- blocks.xlsx - A spreadsheet listing neutral_conditions.xlsx and congruency_conditions.xls


*Exercise (15 mins)*
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

- Rather than a randomised order of blocks, make it so that the neutral block always occurs first.
- Add a routine on your flow to introduce each block. 
- Add a column to your spreadsheet to present different text before each block e.g. "Block 1 of 2" or "Block 2 of 2"


Solution
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

To make blocks appear in a set order, we would set our loop type to "sequential".

For our block introduction, if a routine should be presented once per block, it would be inside the blocks loop, but *before* the trials loop. 

.. image:: /_images/block_intro.png


.. _counterbalancedDesigns3Days:

Counterbalanced designs
--------------------------------------

Counterbalancing your blocks is really just an extension of our exercise, where we've set the blocks to operate in a particular order rather than leaving PsychoPy to randomize them.

The only difference is, we need two (or more) orders, one per group.

The steps we need for counterbalancing
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. rst-class:: build

	* A spreadsheet listing the block orders for each group.
	* An input at the start of the experiment to determine which spreadsheet to use for this participant.
	* A way for the Loop to use the input from the startup dialogue, to select the right spreadsheet. 


How to assign participants to a group
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. image:: /_images/counterbalancing_loop.png

For the "Conditions" field in the block loop we access the "group" field from the start dialogue by refering to "expInfo" ::

	$"block" + expInfo['group'] + ".xlsx"

.. note:: 
	:code:`expInfo` is a python "dictionary" that stores all information from the startup GUI. Fields of a python dictionary are accessed using the format :code:`dictName['fieldName']`. It works the same locally and online and means you can set features of your experiment based on the input received at startup!



All done
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

You now know the building blocks to making basic and complex blocked designs! 

:ref:`Next <builderAndCode>`



