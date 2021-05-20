
.. ifslides::

    .. image:: /_static/OST600.png
        :align: left
        :scale: 25 %
        
.. _debuggingOnline:

Debugging online
=================================

Debugging online
----------------------------------

So your task was running perfectly offline, then you pushed it online, and it doesn't work - why?

To run in the browser your python experiment is translated to Javascript (PsychoJS). Not everything you use in python can be autotranslated to JS (e.g. whole python libraries such as numpy). 

.. nextSlide::

General tips for getting online
----------------------------------

1. Always check the status of online options `status of online options <https://www.psychopy.org/online/status.html>`_ *before* making your experiment
2. Push your experiment little and often (don't make your full experiment perfectly locally and then try to push it online)
3. Read the `crib sheet <https://discourse.psychopy.org/t/psychopy-python-to-javascript-crib-sheet/14601>`_
4. Check out the `psychoJS documentation <https://psychopy.github.io/psychojs/>`_

The forum is always there!

.. nextSlide::

Common errors
----------------------------------

***Undefined errors***
These usually mean that something "exists" in Python that does not "exist" in Javascript. This commonly happens with python libraryies e.g. *"np is not defined"* We recommend taking a look at the `crib sheet <https://discourse.psychopy.org/t/psychopy-python-to-javascript-crib-sheet/14601>`_ in cases like this, where there is a handy list of python terms and there equivilant javascript term. 

.. note::
    Remember that PsychoJS is ALOT younger than PsychoPy, so it needs a bit of time to catch up - which is why not all terms that exist in python exist in PsychoJS - we're working on it though!


How do we fix errrors?
----------------------------------
For these undefined errors we recommend adding a code component to the first routine where we "tell" javascript what we mean by providing the JS alternatives to anything undefined. 

.. image:: /_images/JSsnippet.png
    :align: center

.. note::

For things like numpy we also need to change code type to "Both" and make sure to use the new method (average) instead of refering to :code:`np.average`. 

.. image:: /_images/both_average.png
    :align: center

Want to explore Javascript?
----------------------------------

Remember that you can always export your experiment to it's underlying Javascript code as well, this can be useful in learning how some things are defined differently in PsychoPy versus PsychoJS (but remember that this is a one way street! don't be tempted to alter the JS code if you want to continue making edits in builder!)

Fnding errors: Developer tools
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

- `Scaling your screen <https://pavlovia.org/Wake/screenscale>`_

- The `assignment <https://gitlab.pavlovia.org/tpronk/assignment_stroop_cep_2021_may19-21>`_ we will complete! (fork the task then find the bugs...)

Next up!
-----------------

Let's practice debugging errors, then play with advanced plugins we can use online ( :ref:`advancedOnline`).

Then we will try :ref:`firstExperiment`.

