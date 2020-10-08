
.. ifslides::

    .. image:: /_static/OST600.png
        :align: left
        :scale: 25 %
        
.. _debuggingOnline:

Debugging online
=================================

Debugging online
-----------------

So your task was running perfectly offline, then you pushed it online, and it doesn't work - why?

To run in the browser your python experiment is translated to Javascript (PsychoJS). Not everything you use in python can be autotranslated to JS. 

.. nextSlide::

Let's start by adding some feedback in our experiment::

	feedbackText = ' target hit! %.2f seconds'%(mouse.time[0])

now push that online and try to run it.

.. nextSlide::

.. image:: /_images/notDefinedErr.png
    :align: right

This means that although something was defined when you ran in python, that variable didn't make it to the JS code..

.. nextSlide::

Indeed, we can see that our code component did not translate. So let's try a different approach.

.. image:: /_images/notTranslated.png
    :align: right

.. nextSlide::

If we try a different approach to inserting our variable to the string, our code translates. 

.. image:: /_images/feedbackTranslated.png
    :align: right

.. nextSlide::

But that feedback is a bit long, let's try and use the python "round" function to round this to 2 decimal places::

	feedbackText = ' target hit!'+str(round(mouse.time[0], 2))+'seconds'

First check that runs locally, if yes, try to run that online. 

.. nextSlide::

.. image:: /_images/functionErrorRound.png
    :align: right

This time our error doesn't refer to a variable, but it refers to a function we used. 

The crib sheet
-----------------

If we encounter a translation error. The first point of call is the crib sheet. 

	- https://discourse.psychopy.org/t/psychopy-python-to-javascript-crib-sheet/14601

If we search 'round' here, we can see that the JS version of this is provided::

	round = function(num, n=0) {    
	    return +(Math.round(num + ("e+" + n))  + ("e-" + n));
	}

Adding JS code
-----------------

Add a code component in your first routine 'initJS'. Then let's try and run online again.

.. image:: /_images/defineRoundJS.png
    :align: center

More mods..
-----------------

Imagine we want:
	- a limited amount of time to hit targets
	- to count how many targets are hit. 

Clocks
-----------------

First we want a clock, let's see what clocks are already going on in the background of our task. Compile your task to a python script and search 'clock'

We want a new clock, but we don't want the name of our new clock to conflict with anything that already exists.

.. nextSlide::

Add a code component to your instructions routine. 
In the "End routine" tab we want to start the clock::

	targetHitClock = core.Clock()

In the "Begin Experiment" tab, let's set our time limit (in seconds)::

	timeLimitSecs = 15

.. nextSlide::

In our trials loop, we want to continuously check the time and, if the time limit has been reached, end the loop early. 

Where do we add a code component if we want to check something continuously?

.. nextSlide::

Add a code component to your trial routine and on "Every frame"::

	if targetHitClock.getTime() > timeLimitSecs:
   	    continueRoutine = False
    	trials.finished = True

Run that locally, does it work? 

If yes, sync that to pavlovia, does it work online?

Common online errors
-----------------

.. image:: /_images/constructorErr.png
    :align: center



Exercise: What's wrong? How to we fix it? (Hint: crib sheet)

.. nextSlide::

Solution (note the code type here):

.. image:: /_images/clockConstructorFix.png
    :align: right

.. nextSlide::

OK now we want to count how many hits we get. To do this, we can create a list. We will add to this each time a target is hit. Let's make an empty list at the start of our experiment::

	nHits =[]

NB: we could also use nHits = 0, but let's learn about lists

Because our code component is set to 'Both' we will also have to add this to the JS side..

.. nextSlide::

After each hit we add to this list, in python we do this using append::

	nHits.append(1)

At the end of our task we can use::

	sum(nHits)

Exercise: Add feedback to our thanks routine telling us how many hits we achieved.

.. nextSlide::

Solution:

.. image:: /_images/sumFeedback.png
    :align: right

Does it run locally? Now let's try get that online. 


.. nextSlide::

.. image:: /_images/feedbackTextErr.png
    :align: right

Did we also define this variable at the start of our programme in JS? 

.. nextSlide::

.. image:: /_images/clocksStartCode.png
    :align: right

If our code component code type is 'Both' we need to check that variables are defined in both python and JS. 

OK let's try that online again...

.. nextSlide::

A new error!!

.. image:: /_images/appendErr.png
    :align: right

Is this function listed on the crib sheet? Try to fix this one.

.. nextSlide::

Solution ('append' is 'push' in JS):

.. image:: /_images/appendToPush.png
    :align: right

OK let's try again...

.. nextSlide::

ANOTHER new error...

.. image:: /_images/sumErr.png
    :align: right

Is this function listed on the crib sheet? Try to fix this one.

.. nextSlide::

Solution: Define sum at the start of the experiment in JS

.. image:: /_images/defineSumJS.png
    :align: right



Developer tools
-----------------

Sometimes you might not get an error message, but things "don't work" - what do we do here?

.. image:: /_images/initialisingScreen.png
    :align: center

.. nextSlide::

you can open developer tools in your browser (see crib sheet)
This will tell us where our (which line) error is occuring

.. image:: /_images/developerTools.png
    :align: center

.. nextSlide::

We can then open up our JS file and take a look further. 

.. image:: /_images/syntaxErrorJS.png
    :align: center


Take home messages
-----------------

	- Common errors are usually translation errors
	- Look at the crib sheet 
	- Use the developer tools 
	- You can get more help on discourse! 

So we have now already encountered some code, let's learn some more and :ref:`firstExperiment`.

Exercise
-----------------

Try to push the experiment we made yesterday online. List any bugs you find and how you fixed them. 