.. ifslides::

    .. image:: /_static/OST600.png
        :align: left
        :scale: 25 %
        
.. _advancedOnline:

Advanced online
=================================

Advanced online
---------------------------------

PsychoJS can be used in combination with many JS plugins, which allows a broad range of possibilities for making exciting online studies. You don’t need to be a pro JS coder to use these. Several basic demos are available and a key skill is knowing how to adapt and use these demos. In this exercise, we will focus on how to adapt the eye-tracking demo available on pavlovia.org, which uses the webgazer package for eye tracking.

.. nextSlide::

Some of the tools we can use online:
	- Eye tracking (using webgazer)
	- Your device sensors (e.g. gyroscope)

*Exercise*
`````````````````````````````````
In your breakout rooms work through this stepby-step guide to implement some adaptations to an eye tracking demo. 

.. nextSlide::

1.	Search for “demo_eye_tracking” in pavlovia.org  We want the version loaded by tpronk. Click ‘view code <>’
2.	Click ‘fork’ (next to clone) and select the name space you want to fork this too. 
3.	Go to Dashboard> Experiments, find your newly forked project and set its’ status to running. Click ‘Run’ and check that it works on your own set up (you may be asked for webcam permissions the first time you run the demo). 
4.	From your local PsychoPy. Select the ‘search pavlovia’ icon  (central globe icon in the top tool bar) and search ‘demo_eye_tracking’. Find the version that you just forked to your own namespace **Important: make sure it is the copy from your own namespace**

.. nextSlide::

OK so now we have our own copy of an eye tracking demo! Let’s make some edits! An important part of this exercise is that we don’t *need* to know JS in order to use this demo (but we can learn some bits along the way if we want!). We just need to know how to navigate code and what is possible. We are going to adapt the ‘tracking_trial’ routine .

.. nextSlide::

1.	Add a polygon component to the ‘tracking_trial’ routine and position it in the top right corner of your screen, set it to appear for infinite duration. 

*Note: Because this uses Javascript code, your local psychopy won’t run it. So, to check your changes have been made you will need to run it in the browser. In your ‘trials’ loop set ‘Selected Rows’ temporarily  to 1, click ‘sync to pavlovia’ (second globe from the right) then check that your polygon appears where you want it on screen (notice, the tracking won’t work well following one calibration trial, but that is fine for now).*

.. nextSlide::

2.	Add a code component called ‘checkTarget’ to the ‘tracking_trial’ routine. In the ‘each frame’ tab write

.. code-block:: python

	if polygon.contains(tracking_square):
    	thisCol = 'red'
	else:
    	thisCol = 'white'

.. nextSlide::

3.	Right click your ‘checkTarget’ component and select ‘move up’ so that it appears above the polygon in the routine. 
4.	In your polygon component. Select Advanced> Color and set the color field to read ‘$thisCol’ with the field set to ‘set every frame’

.. nextSlide::

5.	Sync it online – see what happens! Your polygon should change colour when you look at it.


.. nextSlide::

**if there is time...**
Ok imagine we want several trials, where each trial ends when the participant looks at the target.

1.	Make a conditions file that has one column for the x coordinate and one for the y coordinate of your polygon on each trial. 
2.	Add a loop around the ‘tracking_trial’ routine and feed in the conditions file you made.
3.	In your ‘checkTarget’ code component make the following edit

.. code-block:: python

	if polygon.contains(tracking_square):
    	thisCol = 'red'
    	continueRoutine = False
	else:
    	thisCol = 'white'
