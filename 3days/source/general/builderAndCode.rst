
.. PEP 2014 slides file, created by
   hieroglyph-quickstart on Tue Mar  4 20:42:06 2014.

.. _builderAndCode:

Extending Builder with code
===============================

Using Builder to create your experiment
------------------------------------------

Generating 'standard' paradigms in Builder is generally easier than writing the code yourself. Being able to write code helps you do things that a graphical interface can't.

Go to the Builder view and open the Stroop demo. Take a look around.

.. _scriptOutput:

Viewing the Builder script
-----------------------------

As a first step to combining your code with a Builder

.. image:: /_images/compileScriptButton.png

Compare this with scripts you've written:

    - much more code than we needed
    - especially more complicated code to
        - start/stop each stimulus/component
        - determine whether all the components are finished (i.e. trial is over)
    - rather little re-use of code

Builder doesn't know your intentions so plans for everything

.. nextslide::

Many similar concepts:

    - similar imports
    - initialisation of objects
    - creating a dialog box from a dictionary
    - TrailHandler(s) and ExperimentHandler

It can be useful:

    - to get ideas for how to do things
    - to find out what variables a Builder experiment 'knows' about e.g.:
        `t` is always the current time in sec since the start of the Routine

One-way streets
~~~~~~~~~~~~~~~~~~~~~~~

You could save and run this exported script (that's what Builder does each time you press run).

You could tweak this code and see the effects your edits have on the running of the experiment.

If you do your changes will **NOT** be reflected back in the Builder experiment.

Hacking the script is useful to see how things work but it's better to add your edits back into the Builder view.

.. _codeComponents:

Code as arguments
---------------------

Most dialog entries have the option to take raw Python code if you start your entry with `$` (or have that by default).

You can use this as more than a variable from your conditions file e.g.:

    - set stimulus position to be :code:`$[ sin(t*2*pi), cos(t*2*pi) ]` and set this to `update every frame`
    - set a text object to have text :code:`"ABC"[randint(3)]` and have it `update every repeat`

NB. If you actually need a dollar symbol to be in your text, do one of:
    - `$"You won $5"`  [include the quotes]
    - `You won \$5`

Code Components
---------------------

This goes to the next step in integrating code with your experiment

A Code Component allows you to add multi-line arbitrary Python code at 5 different points in the script:
    - start of the experiment
    - start of the current Routine
    - every frame
    - end of the Routine
    - end of the Experiment

.. nextslide::

Let's try and create a 'Feedback' Routine for the basic stroop task (requires a Code Component to decide whether the last response was correct or not).
    - open the Stroop demo from Builder >demos
    - create a new Routine that goes immediately after `trial` on the flow

**More advanced:** go and open the demo called 'BART', the Balloon Analog Risk Task. That requires lots of code:

    - what is the current size of the balloon?
    - did the subject press the 'pump' key?
    - did we exceed our maxPumps for this balloon?
    - ...

Understanding the order of execution
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Each entry of your Routine has multiple Components and their code /for each part of the experiment/  is run in the order of the components.

Do you want you custom code executed before or after your stimulus?

Custom Components
---------------------

If you know how to write :ref:`codeComponents` then you're also most of the way to writing your own, reusable, *custom component* which will appear in the Components Panel of the Builder interface.
