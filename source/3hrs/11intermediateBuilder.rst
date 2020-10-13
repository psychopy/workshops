
.. ifslides::

    .. image:: /_static/OST600.png
        :align: left
        :scale: 25 %


.. _session1:

Building better experiments
==============================

Using Builder
-----------------

All the base knowledge we assume at the start of this workshop can be learnt from this `15 minute video <https://www.youtube.com/watch?v=fIw1e1GqroQ>`_

This shows you how to make the 'posnerHand' demo available from `previous examples <https://workshops.psychopy.org/psychopy_examples.zip>`_

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
    - Add a routine to 'familiarise' participants with the stimuli

.. _onlineStudies:

Running online studies
=================================

So now we have a very simple experiment that works locally, let's see how we would get that online. 

This is where the globe symbols come in, which represet online functionality. 

Running online studies
-----------------

To get our study online, we check that we are signed into our pavlovia acount. Then we 'sync' our project. 

As we create the project we have the options to:
    - select which 'group' we want to push a project to
    - add a description that will appear on the 'Experiment' page online
    - add keywords to help future users find your task (if you make it public)
    - choose if we want the task to be public*

*we can change the visibility of our task later

.. nextSlide::

To view your study online, log into pavlovia.org, you will see your experiment under Dashboard > Experiments.


Let's get some data! 

Next
----------

OK we have now seen the basics of running a study online. Let's talk about some other aspects of the pavlovia environment...

:ref:`pavloviaEnv3Hrs`
