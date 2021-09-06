
.. ifslides::

    .. image:: /_static/OST600.png
        :align: left
        :scale: 25 %


.. _session1:

Building better experiments
==============================

Using Builder
----------------------------------

All the base knowledge we assume at the start of this workshop can be learnt from this `15 minute video <https://www.youtube.com/watch?v=fIw1e1GqroQ>`_

This shows you how to make the 'posnerTargets' demo available from `previous examples <https://workshops.psychopy.org/psychopy_examples.zip>`_

What makes a PsychoPy experiment?
----------------------------------

Open the posnerHand.psyexp file. An experiment in Builder has:

- a single *Flow* (specifies the order in which things occur and whether they repeat in a *Loop*)
- one or more *Routines* that are combined in the *Flow*
- several *Components* that are combined to form *Routines*


The conditions file
----------------------------------

Open the conditions.xlsx file...

If you are going to change something on every repeat of a routine (e.g. stimulus location changes on each trial) you can use a *Conditions* file. This is fed into the loop surrounding the routine.

Each header is a parameter, each row corresponds to the value of that parameter on each repeat/trial.

Making edits
----------------------------------

As a basic first step let's add some instructions. Select "insert routine" and then click on your flow to add this to the start of your experiment. Click on the routine and add:

- A Text component for your instructions
- A keyboard, mouse or button component to end the routine when your participant has finished reading. 

.. note::
	As a general styling tip, we suggest to *keep the number of routines to a minimum*. Got several sets of instructions? use a loop!

Let's practice making edits to make sure we are comfortable with builder view. 

Exercises (10 minutes)
----------------------------------

- add 2 more trials to the conditions file; on one trial a 'neutral' arrow image will be presented on the left on the other the 'neutral' arrow image will be presented on the right
- add a routine to thank participants for taking part at the end
- in the thanks routine, ask participants to press a button to end the task.

:ref:`online`
