
.. ifslides::

    .. image:: /_static/OST600.png
        :align: left
        :scale: 25 %
        
.. _debuggingOnline3Hrs:

Debugging online
=================================

Debugging online
-----------------

So your task was running perfectly offline, then you pushed it online, and it doesn't work - why?

To run in the browser your python experiment is translated to Javascript (PsychoJS). Not everything you use in python can be autotranslated to JS. 

.. nextSlide::

Let's start by trying to push the task that we just made with our feedback code component and talk about some of the common errors we could encounter.

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
