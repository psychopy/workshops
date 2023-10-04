
.. _session13Days:

Building better experiments
==============================


What makes a PsychoPy experiment?
--------------------------------------

A builder experiment has three main sections. To start making an experiment we add routines to our flow and add components to our routines.

.. image:: /_images/builder_terms.png

Creating a routine
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

A Routine is the basic building block of PsychoPy experiments. You can add routines to your flow by selecting "insert routine" on your flow panel > new > name your routine and insert on the flow. 

.. image:: /_images/routines_basics.png
	:width: 90%
	:align: center

.. nextslide::

The next step is to add components to your routine. Think about what your trial will present, and how long each stimulus is on the screen for. For example, we might want some text (you can find this in the stimuli section) and a keyboard response (you can find this in the responses section).

Gather participant info
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Every experiment starts with a dialog box to gather some info about the participant/experiment. By default "participant" and "session" are gathered - and these are used to set the filename of that participant. 

.. image:: /_images/exp_info.png
	:width: 80%
	:align: center

.. note::
	In the current release (2023.2.2) check box options are not yet supported online.


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

.. _keyboardAccuracy:

Storing accuracy 
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

To store accuracy, we need to consider what is the correct key press on each trial. We can therefore add a column to our conditions spreadsheet to indicate what is the correct answer on each trial (in the example below the participant is asked on each trial which number is numerically larger, the correct asnwer is indicated by "corrAns")

.. figure:: /_images/keyboard_acc_spreadsheet.png


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

Think of nReps as a way of turning on or off different routines on your flow, if nReps is 0 then that routine will not be presented. 

.. image:: /_images/case2_blocks.png


Presenting blocks in a set order
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

To make blocks appear in a set order, we would set our loop type to "sequential".

To introduce each block you can add a routine inside the blocks loop, but outside of the trials loop i.e. to introduce each set of trials.

.. image:: /_images/block_intro.png


.. _counterbalancedDesigns3Days:

Counterbalanced designs
--------------------------------------

Counterbalancing your blocks involves presenting blocks in a particular order for each group.

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



