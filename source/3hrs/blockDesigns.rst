
.. _blockDesigns:

Block designs and counterbalancing
=====================================

Randomised block designs
--------------------------------------

A block design is where we have sets of similar trials organised into blocks rather than having trials interleaved.

e.g.
  - a block of faces to recognise or a block of houses
  - a faces oriented correctly and faces inverted
  - a block of Stroop task in English and a block in French

Note: these are all cases where the components would be identical between blocks.

The natural error
`````````````````````````````````````````

The biggest error that people make with this is to create a Routine (and a loop) for each block of trials:

.. image:: /_images/flowBlocksWrong2020.png

Then they ask on the forum, "How do I shuffle the blocks on my Flow?"

That is the wrong way to think about it (for blocks with identical components).


The right way
`````````````````````````````````````````

Instead of a Routine for each block, create a Routine for all your trials and make it behave differently across the blocks:

.. image:: /_images/flowBlocksRight2020.png

Then you can set the conditions files in your blocks loop to control the block-level changes.

The outer "blocks" loop then takes a (meta) "conditions" file that specifies which of the conditions files will be loaded in each block.

.. nextslide::

Imagine we want to extend our Posner task to include a block where invalid trials occur on a higher proportion of trials. 

We need to create a total of 3 conditions files:

- conditionsA.xlsx
- conditionsB.xlsx
- blocks.xlsx

.. nextslide::


blocks.xlsx:

.. image:: /_images/posnerBlocks.png

The `label` variable isn't technically needed but it could be used to tell people what block they are about to enter. The point is that you can still use other variables here, defined at the block level of the program.

.. nextslide::

Now we need to set up the variables inside our experiment:

- the inner (trials) loop will have a conditions file = `$conditions` which is defined in the `blocks.xlsx` file
- the outer (blocks) loop will have conditions file = `blocks.xlsx`

.. nextslide::

.. image:: /_images/blocksMethodB_blockLoop2020.png

.. nextslide::

We could also tell the participants what kind of block they are about to enter, we can add a text object that takes::

    $label

.. image:: /_images/blocksMethodBFullFlow2020.png

.. nextslide:: Randomised block design complete!

You've sorted out block designs in a relatively neat fashion.

Just keep clear what differs from one block to the next (for a conditions file) and what stays the same (for the Routine definition).

Exercise (10 mins)
`````````````````````````````````````````

In the psychopy examples folder you downloaded, open builder > counterbalancingExercises > exercise 1. Here we have a design containing one block where pictures of cats are presented and one where images of dogs are presented. Turn this into a randomised block design... 

Counterbalancing 
--------------------------------------

Counterbalancing your blocks is really just an extension of the blocking scenario, except that you set the blocks to operate in a particular order rather than leaving PsychoPy to randomise them.


Setting the order
`````````````````````````````````````````

At the moment, PsychoPy doesn't handle the ordering for you - you need to decide how to create the orders and how to assign participants.

So, you need a file per conditions order (e.g. A -> B and B-> A) and then set the blocks loop to be `sequential` rather than `random` to preserve the order you set.


How to assign participants to a group
`````````````````````````````````````````

Easiest way is by hand at the start of the run for the participant. The steps are:

- In Experiment Settings add a field for `group` (which will be A, B, C... for however many orders you need)
- For the block loop use that value by calling `expInfo['group']` using one of the alternatives below::

	$"block" + expInfo['group'] + ".xlsx"
	$"block{}.xlsx".format( expInfo['group'] )

*Note: This second kind of formatting is termed an 'fstring' in python - we will talk about that more later.*

*Exercises (10 mins)*
`````````````````````````````````````````

In the psychopy examples folder you downloaded, open builder > counterbalancingExercises > exercise 1. You should have already turned this into a randomised block design in the last exercise, now turn this into a counterbalanced design. So that group A see cats first and group B see dogs first. (You should be able to input group in the GUI at the start)

When you are finished, come back to the main session, if you run into any error messages please share them (on slack) and we can discuss them.


Counterbalancing subtasks
--------------------------------------

Sometimes we might have to counterbalance subtasks (i.e. routines that contain very different sets of components)

You can wrap a loop around any set of routines and control if it presents using nReps. 

.. nextslide::

In the below we could control create the order C->B->A by using a conditions file where the nReps of each subloop are set per iteration of the outerloop. 

.. image:: /_images/counterbalancesubs.png

.. nextslide::

e.g. using a conditions file like this...

+----------+-------------+-----------+
| nRepsA   | nRepsB      |  nRepsC   |
+==========+=============+===========+
| 0        | 0           | 1         |
+----------+-------------+-----------+
| 0        | 1           | 0         |
+----------+-------------+-----------+
| 1        | 0           | 1         |
+----------+-------------+-----------+

Where the nReps argument of each subloop is set using something like '$nRepsA' ect.


*Exercise*
`````````````````````````````````````````

Open exercise 2 in the counterbalanceExercises folder. This is very similar to our last task, but this time our two routines present different kinds of components, so we need to use a different method of counterbalancing. 

We want a design where groupA sees cat images first and group B sees cat words first. Counterbalance this flow using the nReps arguments in the loops.

All done
--------------------------------------

You can now create trials and blocks in any order, fixed or random.

You're in complete control (but you need to understand what orders you want!)

For online use we could also use this handy tool for `generating sequential participant IDs <https://moryscarter.com/vespr/pavlovia.php>`_

What next?!
--------------------------------------

:ref:`blockDesigns`

:ref:`codeComponents`

:ref:`mouse`

:ref:`typedResponses`
