
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

As a first step to combining your code with a Builder is to compile a builder script to coder.

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

A Code Component allows you to add multi-line arbitrary Python code at 6 different points in the script:

    - before the experiment
    - start of the experiment
    - start of the current Routine
    - every frame
    - end of the Routine
    - end of the Experiment

.. nextslide::

.. image:: /_images/codeComponent2020.png

.. nextslide::

Let's try and create a 'Feedback' Routine for the flanker task we made (requires a Code Component to decide whether the last response was correct or not).
    - rerun the task you created to create a data file
    - open the data file and look at the headers that are created
    - you can access these data to feedback to participants.

.. nextslide::
Create a new Routine that goes immediately after `trial` on the flow and add a code component.

.. image:: /_images/flankerFeedback.png

Exercises
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Try: 

    1. Changing the colour of the text based on feedback (green correct, red incorrect)
    2. Adding a feedback 'tone' that varies depending on if correct or incorrect
    3. Adding response time feedback. 

Understanding the order of execution
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Each entry of your Routine has multiple Components and their code /for each part of the experiment/  is run in the order of the components.

Do you want you custom code executed before or after your stimulus?

Code Components - Advanced
---------------------

Go and open the demo called 'BART', the Balloon Analog Risk Task. That requires lots of code:

    - what is the current size of the balloon?
    - did the participant press the 'pump' key?
    - did we exceed our maxPumps for this balloon?
    - ...

First, everyone have a run through of this demo to familiarize yourself with the task. 

.. nextslide::

OK let's talk through the existing code components and the files in this demo.

Exercises: 

    1. Change the balloon to be the blue baloon. 
    2. Set the colour of the baloon to be red if we are within 10 pumps of max pumps. 
    3. Add a penalty - you loose earnings if the baloon pops..

What next?
---------------------

Next we will talk about getting online and what happens with the 'JS' side of your code components. But first, let's explore the pavlovia environment!