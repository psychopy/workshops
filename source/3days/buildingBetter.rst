
.. _session1:

Building better experiments
==============================

Using Builder
-----------------

All the base knowledge we assume at the start of this workshop can be learnt from this `15 minute video <https://www.youtube.com/watch?v=fIw1e1GqroQ>`_

This shows you how to make the 'posnerHand' demo available from `previous examples <https://workshops.psychopy.org/examples2019.zip>`_

What makes a PsychoPy experiment?
-----------------

Open the posnerHand.psyexp file. An experiment in Builder has:

    - a single *Flow* (specifies the order in which things occur and whether they repeat in a *Loop*)
    - one or more *Routines* that are combined in the *Flow*
    - several *Components* that are combined to form *Routines*

The conditions file
-----------------

Open the conditions.xlsx file...

If you are going to change something on every repeat of a routine (e.g. stimulus location changes on each trial) you can use a *Conditions* file. This is fed into the loop surrounding the routine.

Each header is a parameter, each row corresponds to the value of that parameter on each repeat/trial.

Let's practice making minor edits
-----------------

    - Add some instructions
    - Gather some additional info (e.g. age)

Some warm up exercises (5-10 mins)
-----------------

    - Add a thanks message
    - Add a routine to familiarise participants with the stimuli. In this routine we want:
        - An image of the stimulus
        - Some text to tell the participant what that image is
        - A mouse click to end the routine
        - The routine will occur twice (once for each image)

When you are finished, come back to the main session and collect one run of your task so that we can talk through the data file.

.. _blockDesigns:

Block designs and counterbalancing
--------------------------------------

A block design is where we have sets of similar trials organised into blocks rather than having trials interleaved.

e.g.
  - a block of faces to recognise or a block of houses
  - a faces oriented correctly and faces inverted
  - a block of Stroop task in English and a block in French

The natural error
`````````````````````````````````````````

The biggest error that people make with this is to create a Routine (and a loop) for each block of trials:

.. image:: /_images/flowBlocksWrong2020.png

Then they ask on the forum, "How do I shuffle the blocks on my Flow?"

That is the wrong way to think about it.


The right way
`````````````````````````````````````````

Instead of a Routine for each block, create a Routine for all your trials and make it behave differently across the blocks:

.. image:: /_images/flowBlocksRight2020.png

Then you can set the conditions files in your blocks loop to control the block-level changes.

The outer "blocks" loop then takes a (meta) "conditions" file that specifies which of the conditions files will be loaded in each block.

.. nextslide::

Imagine we want to extend our Posner task to include a block where invalid trials occur on 80% or trials. 

We need to create a total of 3 conditions files:

  - conditions20.xlsx
  - conditions80.xlsx
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

We could also add a Routine called `blockReady` like an instructions Routine with:

  - a text object that says::

    $"This block will have a %s probability of invalid cues \n \n Press a key when ready" %(label)

  - a mouse object to advance to the next trial

.. image:: /_images/blocksMethodBFullFlow2020.png

.. nextslide:: Randomised block design complete!

You've sorted out block designs in a relatively neat fashion.

Just keep clear what differs from one block to the next (for a conditions file) and what stays the same (for the Routine definition).


.. _counterbalancedDesigns:

Counterbalancing
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Counterbalancing your blocks is really just an extension of the blocking scenario, except that you set the blocks to operate in a particular order rather than leaving PsychoPy to randomise them.


Setting the order
`````````````````````````````````````````

PsychoPy doesn't handle the ordering for you - you need to decide how to create the orders and how to assign participants.

Now, rather than a single file to specify the blocks you need one for each order that you want the blocks to appear in (and then set the blocks loop to be `sequential` rather than `random` to preserve the order you set)

For instance, the Posner task you might have groupA with alternating invalid cue probability, beginning with high prob, and the groupB participants might have the same but starting with low prob.

How to assign participants to a group
`````````````````````````````````````````

Easiest way is by hand at the start of the run for the participant. The steps are:

 - In Experiment Settings add a field for `group` (which will be A, B, C... for however many orders you need to create)
 - For the block loop use that value by calling `expInfo['group']` using one of the alternatives below:

  - `$"block" + expInfo['group'] + ".xlsx"`
  - `$"block{}.xlsx".format( expInfo['group'] )`

Some exercises (10-15 mins)
-----------------

    - Instead of changing the cue_image on each repeat. Manipulate the direction of the arrow using the 'Orientation' field of your cue component.
    - Add 2 new blocks (one 20% invalid cues the other 80% invalid) but, in these blocks, the target is instead presented above or below the fixation.
    - We will present the blocks in a randomised block design.

When you are finished, come back to the main session, if you run into any error messages please share them (on slack) and we can discuss them.

All done
-----------------

You can now create trials and blocks in any order, fixed or random.

You're in complete control (but you need to understand what orders you want!)

Next... :ref:`builderAndCode`

