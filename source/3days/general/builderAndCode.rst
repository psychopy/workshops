
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

.. nextslide::

Using code as arguments allows us to easily make stimuli 'dynamic' (i.e. things change their attributes in time). 

e.g. our shape that tracked the mouse by setting the shape position to be mouse.getPos()

.. nextslide::

Handy side tip. If you want to see what properties and methods an object has, you can  use a print() statement, e.g.::

    print(dir(mouse))

If you want to learn more about a method in an object you can print the docstring for that method::

    print(mouse.setVisible.__doc__)

.. nextslide::

Making things dynamic could allow you to, for instance:

  - gradually reveal an object
  - make an object move to make the task harder
  - make an object more interesting for participants (e.g. developmental)

.. nextslide::

Let's create a task where text is gradually revealed (e.g. we want to control reading speed).

Think of a Routine like this:

.. image:: /_images/routineTextReveal2020.png

The text object could be any long piece of text. You might need to make sure the wrap length is set to be the full width of the screen to fit on one line.

.. nextSlide::

.. image:: /_images/revealMaskProperties.png
    :align: right

Your mask is a square that moves (note the size and the pos settings). 

Code Components
---------------------

This goes to the next step in integrating code with your experiment

A Code Component allows you to add Python (and now JS) code at 6 different points in the script:

    - before the experiment
    - start of the experiment
    - start of the current Routine
    - every frame
    - end of the Routine
    - end of the Experiment

.. nextslide::

.. image:: /_images/codeComponent2020.png

.. nextslide::

The order of execution is important.

Each entry of your Routine has multiple Components and their code /for each part of the experiment/  is run in the order of the components.

Do you want you custom code executed before or after your stimulus?

.. nextslide::

Let's try and create a 'Feedback' Routine for the Posner task we want to:
    - Add trial by trial feedback on response times 
    - Adjust the colour of the feedback based on RT
    - Give feedback at the end on average RT overall, on valid trials and on invalid trials.

.. nextslide::

To add trial by trial feedback on response times create a feedback routine and add a text component. In the text field enter::
    
    $'RT was '+str(round(resp.time[0], 3))+' ms'

NB: at the moment we use '+' to concatinate strings rather than python formatted strings (e.g. '%s'%(resp.time[0])). This is because the latter is not currently compatible with online studies. 

.. nextslide::

To adjust feedback colour based on response time we need a code component::

    if resp.time[0]<.5:
        feedbackCol = 'green'
    else:
        feedbackCol = 'red'

.. nextslide::

To give feedback at the end for each condition let's learn about lists. We want three lists to keep track of RTs::

    allRTList=[]
    validRTList=[]
    invalidRTList=[]

.. nextslide::

Some useful *Python* methods
    - .append() - adds to a list
    - np.average() - returns average of a list using the numpy (np) library. 

Exercises (15-20 minutes)
---------------------

Try: 

    1. Add a feedback tone that varies in frequency depending on if the RT fell in the desired time limit. 
    2. Add a text component to the end feedback routine to tell participants if they showed a Posner cueing effect.
    3. IF participants show a posner cueing effect, tell them how large their effect was in ms. 

Code Components - Advanced
---------------------

Go and open the demo called 'BART', the Balloon Analog Risk Task. That requires lots of code:

    - what is the current size of the balloon?
    - did the participant press the 'pump' key?
    - did we exceed our maxPumps for this balloon?
    - ...

First, everyone have a run through of this demo to familiarize yourself with the task. 

.. nextslide::

OK let's talk through the existing code components and the files in this demo. Then we are going to try some excercises to combine all of the skills we have learnt so far.

Exercises (20-30 minutes)
---------------------

    1. Make the colour of the balloon change on every trial (either green or blue)
    2. Add a new condition, where blue balloons have a high risk of popping early, whilst green balloons do not. 
    3. Allow the researcher to assign participants to either group A or B - where group A will have the standard condition first, followed by block where colour predicts pop timing, and group B vice versa.
    4. Set the colour of the baloon to be red if we are within 10 pumps of max pumps. 
    5. Add a penalty - you loose earnings if the baloon pops..

Code Components - Advanced
---------------------

Sometimes you might want to end a routine or loop early if a certain condition is met. For example if a level of accuracy or a time limit has been reached. To do this we can use::

    continueRoutine = False # ends a routine
    trials.finished = True # ends the loop (trials = name of loop)

.. nextslide::

Make a simple routine with a text component that lasts 0.5 seconds add a loop to repeat that 5 times. 

Try accessing the properties of your loop object - see 'finished' is in the list. 
There is also some properties we see in our outputfile (e.g. thisN).

Let's try ending the routine at trial 3 instead of trial 5...
What happend if you do or do not use continueRoutine? 


What next?
---------------------

Next we will talk about getting online and what happens with the 'JS' side of your code components. But first, let's explore :ref:`pavloviaEnv`! 

Additional note
---------------------

Sometimes you might want to set the properties of multiple components at once. For this we could use a for loop (we will talk more about these on Friday)

Exercises (15-20 minutes)
---------------------
Painting shapes...

    1. present 4 white polygons (circles, triangle, rectangle)
    2. add a mouse component to click the polygons
    3. if a polygon is clicked, set it's colour to green