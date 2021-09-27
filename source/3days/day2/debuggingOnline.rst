
.. ifslides::

    .. image:: /_static/OST600.png
        :align: left
        :scale: 25 %
        
.. _debuggingOnline:

Debugging online
=================================

Why do we need to debug?
----------------------------------

So your task was running perfectly offline, then you pushed it online, and it doesn't work - why? There are lot's of reasons something might not work online, but the most common errors are coding errors. 

Remember that locally PsychoPy runs a compiled python experiment. Online, pavlovia runs your compiled *Javascript* experiment which uses the `PsychoJS library`<https://github.com/psychopy/psychojs>_. 

.. nextSlide::

The PsychoJS library doesn't yet contain everything in PsychoPy, for several reasons:

*	Does a component "make sense" online? e.g. Grating stimuli ideally require a luminance calibrated monitor. Does your participant have a photometer at home? Input/Output components to connect with EEG might not make sense online either..
*	PsychoJS is younger than PsychoPy! But we

Transpiling 
----------------------------------

When we add code components we have the choice to add code as either:

*	*Py* - pure Python
*	*JS* - pure JavaScript
*	*Both* - Python and Javascript independantly
*	*Auto -> JS* - automatically *transpile* python code to javascript. 

The last option is very cool and useful - but it can catch people out if something doesn't translate smoothly!

.. nextSlide::

General tips for getting online
----------------------------------

1. Always check the status of online options `status of online options <https://www.psychopy.org/online/status.html>`_ *before* making your experiment
2. Push your experiment little and often (don't make your full experiment perfectly locally and then try to push it online)
3. Read the `crib sheet <https://discourse.psychopy.org/t/psychopy-python-to-javascript-crib-sheet/14601>`_
4. Check out the `psychoJS documentation <https://psychopy.github.io/psychojs/>`_
5. Update to the latest release! Version 2021.2. improved transpiling alot and you can save *alot* of manual debugging online using that version. 

The forum is always there!

.. nextSlide::

Common errors
----------------------------------

***Undefined errors***
These usually mean that something "exists" in Python that does not "exist" in Javascript. This commonly happens with python libraries e.g. *"np is not defined"* We recommend taking a look at the `crib sheet <https://discourse.psychopy.org/t/psychopy-python-to-javascript-crib-sheet/14601>`_ in cases like this, where there is a handy list of python terms and there equivilant javascript term. 

How do we fix errrors? 
----------------------------------

**Pre 2021.2.2**

Before PsychoPy 2021.2, there were lot's of things that did not transpile smoothly from python to Javascript. If you update you will save alot of headaches. For these undefined errors we recommend adding a code component to the first routine where we "tell" javascript what we mean by providing the JS alternatives to anything undefined. 

.. image:: /_images/JSsnippet.png
    :align: center

**Still relevant to 2021.2.2**

Even though we've improved the transpiler, there are some things that either still need updating or that we can't expect to transpile i.e. whole python libraies like numpy. So if you are using specific functions you will need to find the JS equivilent and add that to your experiment. We would also thenneed to change code type to "Both".

The developers console
----------------------------------

This is the equivilent to your "StdOut" window in runner view. In fact, it's alot more than that - it's a shell where you can type and try out bits of JavaScript. You can access developer tools in most browsers by right clicking the browser and selecting "inspect" then clicking console. 

*For faster access look up the keyboard shortcut for your specific operating system/browser!*

Finding errors: Developer tools
-------------------------------

Sometimes you might not get an error message, but things "don't work" - what do we do here?

.. image:: /_images/initialisingScreen.png
    :align: center

.. nextSlide::

you can open developer tools in your browser (the `crib sheet <https://discourse.psychopy.org/t/psychopy-python-to-javascript-crib-sheet/14601>`_) gives tips how to do this on different browsers/operating systems)
This will tell us where our (which line) error is occuring

.. image:: /_images/developerTools.png
    :align: center

.. nextSlide::

If you are ever unsure where to look in your builder experiment for an error, you can look for the line that indicates what routine this code is being executed in. 

.. image:: /_images/navigate_console_error.png

Clearing your browser cache
----------------------------------

If you ever make a change in your experiment and it isn't reflected in your online experiment, it is very likely you need to clear your browser cache. How this is dont can vary browser to browser - so do search how to do that on your specific operating system/browser.

Useful Javascript commands
----------------------------------

- :code:`console.log()`: The equivilent of :code:`print()` in python. Useful for when a variable doesn't appear as you expect - you can print out values to your console and check they are updating as you expect. 
- :code:`window.object = object`: pass an object to the window for inspection e.g. pass a component by replacing :code:`object` with the name of your component. Useful for seeing what attributes and methods an object has.

Want to explore Javascript?
----------------------------------

Remember that you can always export your experiment to it's underlying Javascript code as well, this can be useful in learning how some things are defined differently in PsychoPy versus PsychoJS (but remember that this is a one way street! don't be tempted to alter the JS code if you want to continue making edits in builder!)

Other useful tools
-------------------
There are several other tools that can be useful including:

- Counterbalancing online using `sequential participant IDs <https://moryscarter.com/vespr/pavlovia.php>`_ 

- `Scaling your screen <https://pavlovia.org/Wake/screenscale>`_ (e.g. so that we can use cm units online).

- `Headphone checkers using huggins pitch <https://github.com/ChaitLabUCL/HeadphoneCheck_Test>`_ 

- `Embedding html forms <https://discourse.psychopy.org/t/new-web-app-form-to-html-for-pavlovia/22626>`_.

- `Eyetracking online <https://workshops.psychopy.org/3days/day2/advancedOnline.html>`_ using the webgazer library. **Note that in 2021.2.2 there is a different way of loading resources** 

Next up!
-----------------

Let's practice debugging errors, then play with advanced plugins we can use online ( :ref:`advancedOnline`).

Then we will try :ref:`firstExperiment`.

