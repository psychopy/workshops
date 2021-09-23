
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

Remember that locally PsychoPy runs a compiled python experiment. Online pavlovia runs your compiled *Javascript* experiment which uses the PsychoJS library. 

.. nextSlide::

The PsychoJS library doesn't yet contain everything in PsychoPy, for several reasons:

*	Does a component "make sense" online? e.g. Grating stimuli ideally require a luminance calibrated monitor. Does your participant have a photometer at home? Input/Output components to connect with EEG might not make sense online either..
*	PsychoJS is younger than PsychoPy!

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

Even though we've improved the transpiler, we can't expect to transpile whole python libraies (e.g. numpy). So if you are using specific functions you will need to find the JS equivilent and add that to your experiment. We might also need to change code type to "Both" and make sure to use the new method (average) instead of refering to :code:`np.average`. 

.. image:: /_images/both_average.png
    :align: center

Want to explore Javascript?
----------------------------------

Remember that you can always export your experiment to it's underlying Javascript code as well, this can be useful in learning how some things are defined differently in PsychoPy versus PsychoJS (but remember that this is a one way street! don't be tempted to alter the JS code if you want to continue making edits in builder!)

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

We can then open up our JS file and take a look further. 

.. image:: /_images/syntaxErrorJS.png
    :align: center

Other useful tools
-------------------
There are several other tools that can be useful including:

- Counterbalancing online using `sequential participant IDs <https://moryscarter.com/vespr/pavlovia.php>`_ 

- `Scaling your screen <https://pavlovia.org/Wake/screenscale>`_ (e.g. so that we can use cm units online).

- `Headphone checkers using huggins pitch <https://github.com/ChaitLabUCL/HeadphoneCheck_Test>`_ (e.g. so that we can use cm units online).

- `Embedding html forms <https://discourse.psychopy.org/t/new-web-app-form-to-html-for-pavlovia/22626>`_.

- `Eyetracking online <https://workshops.psychopy.org/3days/day2/advancedOnline.html>`_ using the webgazer library. **Note that in 2021.2.2 there is a different way of loading resources** 

- The `assignment <https://gitlab.pavlovia.org/tpronk/assignment_stroop_cep_2021_may19-21>`_ we will complete! (fork the task then find the bugs...)

Next up!
-----------------

Let's practice debugging errors, then play with advanced plugins we can use online ( :ref:`advancedOnline`).

Then we will try :ref:`firstExperiment`.

