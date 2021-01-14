
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

To run in the browser your python experiment is translated to Javascript (PsychoJS). Not everything you use in python can be autotranslated to JS (e.g. whole python libraries such as numpy). 

.. nextSlide::

General tips for getting online
````````````````````````````````

1. Always check the status of online options `status of online options <https://www.psychopy.org/online/status.html>`_ *before* making your experiment
2. Push your experiment little and often (don't make your full experiment perfectly locally and then try to push it online)
3. Read the `crib sheet <https://discourse.psychopy.org/t/psychopy-python-to-javascript-crib-sheet/14601>`_
4. Check out the `psychoJS documentation <https://psychopy.github.io/psychojs/>`_

The forum is always there!

.. nextSlide::

Common errors
````````````````````````````````

*Undefined* errors::

	feedbackText = ' target hit! %.2f seconds'%(mouse.time[0])

.. nextSlide::

.. image:: /_images/notDefinedErr.png
    :align: right

This means that although something was defined when you ran in python, that variable didn't make it to the JS code..

.. nextSlide::

.. image:: /_images/functionErrorRound.png
    :align: right

Sometimes we might get an error that doesn't refer to a variable, but it refers to a function or library we tried to use. 

Resources
````````````````````````````````

If we encounter a translation error. There are several places we should check for support:

- `The psychopy to JS crib sheet <https://docs.google.com/document/d/13jp0QAqQeFlYSjeZS0fDInvgaDzBXjGQNe4VNKbbNHQ/edit#>`_
- `The psychoJS API <https://psychopy.github.io/psychojs/module-visual.Polygon.html>`_
- `The forum <https://discourse.psychopy.org/>`_

.. nextSlide::

e.g. If we search 'round' in the crib sheet, we can see that the JS version of this is provided::

	round = function(num, n=0) {    
	    return +(Math.round(num + ("e+" + n))  + ("e-" + n));
	}

Adding JS code
````````````````````````````````

Add a code component in your first routine 'initJS'. Then let's try and run online again.

.. image:: /_images/defineRoundJS.png
    :align: center

.. nextSlide::

There are several handy functions you might want to include at the start of your experiment in a .JS component which might make things easier in the long run:
    - append - for adding to lists
    - thisExp - for adding data to the experiment handler
    - shuffle - for shuffling and randomly selecting items from lists


*Group Exercise*
````````````````````````````````
Let's try and push the experiment we made yesterday online and talk through any errors we encounter. 

Add ons we might also want to discuss:
    - counterbalancing online
    - bot checkers and online checks (e.g. has our participant walked away? is our participant pressing the same key repeatedly?)

Other errors
````````````````````````````````

We have already seen that the variable "t" can be used to refer to the current time in the trial. But what if we want seperate clocks that run independantly relative to something else, locally we would use::

	myClock = core.Clock()

.. nextSlide::

But online, that causes an error. 

.. image:: /_images/constructorErr.png
    :align: center


Exercise: What's wrong? How to we fix it? (Hint: crib sheet)

.. nextSlide::

Solution (note the code type here):

.. image:: /_images/clockConstructorFix.png
    :align: right

.. nextSlide::

Fnding errors: Developer tools
-------------------------------

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

Other useful tools
-------------------
There are several other tools that can be useful including:

- `counterbalancing online <https://discourse.psychopy.org/>`_ through using sequential participant IDs.

- `The psychopy to JS crib sheet <https://docs.google.com/document/d/13jp0QAqQeFlYSjeZS0fDInvgaDzBXjGQNe4VNKbbNHQ/edit#>`_ also has seceral useful references for daisychaining with qualtrics:

- `Scaling your screen <https://pavlovia.org/Wake/screenscale>`_

Next up!
-----------------

Let's practice debugging errors, then play with advanced plugins we can use online ( :ref:`advancedOnline`).

Then we will try :ref:`firstExperiment`.

