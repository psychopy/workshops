.. ifslides::

    .. image:: /_static/OST600.png
        :align: left
        :scale: 25 %
        
.. _advancedOnline:

Advanced online
=================================

What "Advanced" online options are available?
------------------------------------------------

If there is an open JS library for it, then it can be imported into PsychoPy and used on pavlovia. This allows a broad range of possibilities for making exciting online studies. You don’t need to be a pro JS coder to use these. Several basic demos are available and a key skill is knowing how to adapt and use these demos. In this exercise, we will focus on how to adapt the eye-tracking demo available on pavlovia.org, which uses the webgazer package for eye tracking.

.. image:: /_gifs/posner-eye-gif.gif
    :align: center

.. nextSlide::

Some of the tools we can use online:
	- `Eye tracking <https://gitlab.pavlovia.org/demos/demo_eye_tracking2>`_
        -Archived (run on PsychoPy versions pre 2021.2): Examples using the `Posner task <https://run.pavlovia.org/lpxrh6/posner_eyetracking_test/>`_, and another for tracking `basic left right eye movements <https://run.pavlovia.org/lpxrh6/demo_eye_tracking/>`_)
	- Your device sensors such as the `Gyroscope <https://run.pavlovia.org/tpronk/demo_gyroscope/>`_

*Exercise*
------------------------------------------------
In your breakout rooms work through this stepby-step guide to implement some adaptations to an eye tracking demo. This builds on the skills we learned from Mouse tracking.

.. nextSlide::

**Step 1: Forking the demo**

1.	Search for and :ref:`forking` the `demo_eye_tracking2 <https://gitlab.pavlovia.org/demos/demo_eye_tracking2>`_ project in demos.
2.	Click `fork <https://workshops.psychopy.org/3days/day2/pavlovia.html#finding-shared-experiments-from-pavlovia-itself>`_ and select the name space you want to fork this too. 
3.	Go to Dashboard> Experiments, find your newly forked project and set its’ status to running. Click ‘Run’ and check that it works on your own set up (you may be asked for webcam permissions the first time you run the demo). 
4.	From your local PsychoPy. Select the ‘search pavlovia’ icon  (central globe icon in the top tool bar) and search ‘demo_eye_tracking’. Find the version that you just forked to your own namespace **Important: make sure it is the copy from your own namespace**

.. nextSlide::

**Step 2: Making local edits**

OK so now we have our own copy of an eye tracking demo! Let’s make some edits! An important part of this exercise is that we don’t *need* to know JS in order to use this demo (but we can learn some bits along the way if we want!). We just need to know how to navigate code and what is possible. We are going to adapt the ‘tracking_trial’ routine .

.. nextSlide::

1.	Add a polygon component to the ‘trackingTrial’ routine and position it in the top right corner of your screen, set it to appear for infinite duration. 

.. note::
    Because this uses Javascript code, your local psychopy won’t run it. So, to check your changes have been made you will need to sync it and run it in the browser from pavlovia. 

.. nextSlide::

2.	Add a code component called ‘checkTarget’ to the ‘tracking_trial’ routine. In the **each frame** tab write
::
        if polygon.contains(tracking_square):
            thisCol = 'red'
	else:
            thisCol = 'white'

.. nextSlide::

3.	Right click your ‘checkTarget’ component and select ‘move up’ so that it appears above the polygon in the routine. 
4.	In your polygon component. Select Appearance> Color and set the color field to read :code:`$thisCol` with the field set to **set every frame**

.. nextSlide::

5.	Sync it online – see what happens! Your polygon should change colour when you look at it.

.. image:: /_gifs/eyetracking-polygon.gif
    :align: center

.. nextSlide::

**if there is time...**

Ok imagine we want several trials, where each trial ends when the participant looks at the target.

1.	Make a conditions file that has one column for the x coordinate and one for the y coordinate of your polygon on each trial. 

2.	Add a loop around the ‘tracking_trial’ routine and feed in the conditions file you made.

3.	In your ‘checkTarget’ code component make the following edit
::

    if polygon.contains(tracking_square):
        thisCol = 'red'
        continueRoutine = False
    else:
        thisCol = 'white'


