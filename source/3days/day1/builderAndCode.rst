
.. PEP 2014 slides file, created by
   hieroglyph-quickstart on Tue Mar  4 20:42:06 2014.

.. _builderAndCode:

Extending Builder with code
===============================

Using Builder to create your experiment
------------------------------------------

Generating 'standard' paradigms in Builder is generally easier than writing the code yourself. Being able to write code helps you do things that a graphical interface can't.

.. _scriptOutput:

Compiling your experiment to python or JavaScript
---------------------------------------------------

A first step to combining your code with a Builder is to compile a builder script to coder and peek what's "under the hood".

.. image:: /_images/compile.png

.. nextslide::

Compare this with scripts you may have written:

- much more code than we needed
- especially more complicated code to
    - start/stop each stimulus/component
    - determine whether all the components are finished (i.e. trial is over)
- rather little re-use of code

Builder doesn't know your intentions so plans for everything

.. nextslide::

Many similar concepts:

- similar imports
- initialization of objects
- creating a dialog box from a dictionary
- TrailHandler(s) and ExperimentHandler

.. nextslide::

It can be useful:

- to get ideas for how to do things
- to find out what variables a Builder experiment 'knows' about e.g.:
    `t` is always the current time in sec since the start of the Routine

One-way streets
------------------

You could save and run this exported script (that's what Builder does each time you press run).

You could tweak this code and see the effects your edits have on the running of the experiment.

If you do your changes will **NOT** be reflected back in the Builder experiment.

Hacking the script is useful to see how things work but it's better to add your edits back into the Builder view.

.. _codeArguments:

Code "as arguments"
---------------------

Most dialog entries have the option to take raw Python code if you start your entry with `$` (or have that by default).

You can use this as more than a variable from your conditions file e.g.:

- set a random value (e.g. onset, position) :code:`random()`
- set a text object to have text :code:`"ABC"[randint(3)]` and have it `update every repeat`

NB. If you actually need a dollar symbol to be in your text, do:

- `$"You won $5"` [include the quotes]

.. nextslide::

Using code as arguments allows us to easily make stimuli 'dynamic' (i.e. things change their attributes in time). 

e.g. a shape that tracked the mouse by setting the shape position to be mouse.getPos()

.. nextslide::

Making things dynamic could allow you to, for instance:

- gradually reveal an object
- make an object move to make the task harder
- make an object more interesting for participants (e.g. developmental)

.. _codeComps:

Code Components
---------------------

This goes to the next step in integrating code with your experiment. You can add code in either python or JavaScript (JS). By default, python code will be **transpiled** into JavaScript.

.. image:: /_images/code_component.png

.. nextslide::

A Code Component allows you to add Python (and now JS) code at 6 different points in the script:

.. image:: /_images/code_component_sequence.png

.. nextslide::

The order of execution is important.

Each entry of your Routine has multiple Components and their code /for each part of the experiment/  is run in the order of the components.

Do you want you custom code executed before or after your stimulus?

.. note::
  Handy side tip. If you want to see what properties and methods an object has, you can  use :code:`dir()` for example to inspect the properties of the mouse you could use :code:`print(dir(mouse))`.

  If you want to learn more about a method in an object you can print the docstring for that method :code:`print(mouse.setVisible.__doc__)`

  *The dir() method is a python specific function - so be careful if you leave that in your code when pushing your experiment online!*


.. _addingFeedback:


Adding feedback
=========================

Trial-by-trial (from a key press)
-----------------------------------

When we use a keyboard component for our responses, there are a few variables returned on the key press:

- :code:`key_resp.keys`: Key name(s) that were pressed.
- :code:`key_resp.rt`: The response time(s) of key presses.
- :code:`key_resp.corr`: If a correct answer was provided to the component (under "Data" tab) this will return 1/0 for if the response was correct/incorrect.

.. nextslide::

Following this you could use a code component to give response dependent feedback::

   if key_resp.corr:
      feedback = ' Correct!'
   else:
      feedback = 'Incorrect'

Using :code:`$feedback` in a Text component. 


Overall feedback (from a key press)
-----------------------------------

Sometimes we might want to tell our participant how well they did overall. For example, we might want to tell them the percentage of correct answers they got. 

.. nextslide::

For this we would need two variables, the number of trials and the number of correct responses. 

In the Begin Experiment tab, we could use:

.. code::

   totalTrials = 0
   totalCorrect = 0

Then in the End Routine tab we could use:

.. code::

   totalTrials += 1
   totalCorrect += key_resp.corr

.. nextslide::

Finally, at the end of our experiment we could add a text component and use some code in the text field::
  
  $'You scored' + str((totalCorrect/totalTrials)*100) + '% correct!'.

If you want to be kind to future you, you could even save this summary variable to your data file by adding a code component to your last routine::
  
  thisExp.addData('percent_correct', (totalCorrect/totalTrials)*100)

.. nextslide::

We can also obtain similar feedback when :ref:`usingMouse` (but let's save that for later!)

*Exercise (20 mins)*
---------------------



* set the color of the feedback to be green if the response is correct and red if incorrect. 
* give trial-by-trial feedback on how fast the participant was. Hint: you can access response times from a keypress using  :code:`key_resp.rt` and convert numbers to strings using :code:`str(x)` where :code:`x` is your number. 
* *if there's time* download the images `here <https://gitlab.pavlovia.org/Hirst/workshopnumberstroop/tree/master/images>`_ to show a celebration image if correct, and a sad face if incorrect. 

More code examples
=========================

Inserting a timer
-------------------

To show the participant the time into a trial, we don't even need a code component. We can add a Text stimulus, and in the Text field write :code:`str(t)` (*t is a special variable that lives under the hood of PsychoPy, it indicates the time since the trial started*) then make sure to set the field *Each frame*. This is a good example of converting variable "types" in python:

- :code:`str()` : Converts to a string.
- :code:`int()` : converts to an integer.

.. nextslide::

This might return a value that is quite long, so, to round that we could use :code:`round(t, 3)`


Ending a set of trials early
-----------------------------------------------

Imagine we want a set of practice trials, that will end when your participant gets 5 correct. 

You can use the code :code:`trials.finished = True` to end a loop early. So, you could say::

   if totalCorrect >= 5:
      practice_trials.finished = True # practice_trials is the name of the loop

Ending or skipping a routine
-----------------------------------------------

Imagine we want to skip a routine/trial (for example to only show a routine on some trials). You can add a code component and use::

   continueRoutine = False

To end or skip a routine. 

.. nextslide::

This can be extended to insert a break. The modulus operator :code:`%` can be used to say if a number has any remainders following a division, so, if we want a break every 5th trial we could add a routine in our trial loop called "breakMsg" and add a code component with the following in the begin routine::

   if trials.thisN + 1 % 5 > 0:
        continueRoutine = False

Note that we add 1 because python indexing starts at 0.


Making a branched experiment
--------------------------------------
A branched experiment refers to an experiment in which one of two paths could be taken, depending on the response given. A *very* basic example of a branched experiment could be if the participant chooses to consent or not, if they do consent the experiment progresses, otherwise the experiment skips to a thank-you message. 

.. nextslide::

Add a Routine to the start of our experiment called "consent" and add two clickable images (one called "Yes" and one called "No"). Then add a code component, and in the *End Routine* tab, write::

   if consent_mouse.clicked_name[-1] == 'Yes':
      mainLoopReps = 1
   else:
      mainLoopReps = 0

Then add a loop around the rest of your experiment and use :code:`$mainLoopReps` in the :code:`nReps` field. This is a basic example, but you could imagine how this could be used for other branched experiments to show different parts of your experiment to different participants. 


Randomizing the position of stimuli (e.g. images)
---------------------------------------------------

Imagine you have 4 images to present in 4 locations. On each trial, you want the location for each image to be selected randomly. You could add a code component, and in the `Begin Routine` tab write::

   xList= [-.5, -.25, .25, .5]
   shuffle(xList)

Then in the position field of each image component  use :code:`[xList[0], 0]`, :code:`[xList[1], 0]` and so on... *making sure to set every repeat* 

Storing custom variables
--------------------------------------

It is really handy to be able to save custom variables to our data file. Following the example of randomizing image position, we could save the xlist to our data file using :code:`thisExp.addData('xList', xList)` the function :code:`addData()` takes 2 arguments - the first is the value for the column header in the output file, the second it the value of the variable to save. 

.. _clocksAndTrialCounters:

Clocks and trial counters
===============================

Clocks
--------

Keeping track of time is really important to most experiments. In PsychoPy there are many useful clocks that live "under the hood", which we can use in our experiment:

*	:code:`routineClock` : Every routine has it's own clock with this naming convention e.g. a routine called "trial" would have a clock called "trialClock".
*	:code:`t` : We might not need the routineClock, because the variable `t` represents the time since the start of the current routine anyway!

Making custom clocks
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

If we want to use a custom clock (e.g. to measure the time across several routines) we can always make a clock within a code component::

   myClock = core.Clock()

.. note::
   In the current release (2021.2.3) if we are working online we will need to change our code component "type" to be "Both" and use :code:`myClock = util.Clock()` on the JS side.

Useful methods for use with clocks
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Once we have our clock there are several useful methods we might want to know about. 

*	:code:`.getTime()`: fetches the time on the current clock (note that we don't need to do this for :code:`t` because t represents the time on the current routine clock rather than a clock itself)
*	:code:`.reset()` : resets a clock - note that this is OK on our custom clocks, but it is best that we don't reset any of PsychoPy's inbuilt clocks. 


Adding a timer to your experiment
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Now that we know how to make a clock and how to access the time on it, we can easily add a timer to our experiment to show our participant how far into a trial, or the experiment they are. 

.. nextslide::

Add a text component to your trial routine and position it in the top right corner (in height units you will want something like `pos = (0.4,0.4)`. Then in the `text` field all we need is to write :code:`$t` and **set every frame**. 

.. note::
   Depending on your PsychoPy version you might need to use :code:`t` - omitting the dollar sign. Remember that you only need a $ at the start of a field if there is not already a $ int he parameter name.

.. nextslide::

The properties of the text component should look like this:

.. image:: /_images/timer_properties.png
    :align: left
    :scale: 50 %

.. nextslide::

OK now you should have a timer to show participants how far through a trial they are!! If you wanted to show them how far into the experiment they are you could add a code component and in the `Begin Experiment` tab write :code:`expClock = core.Clock()`. Then in your text component replace :code:`t` with :code:`expClock.getTime()`.


Trial counters
-------------------------------

How is PsychoPy counting trials?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Each loop we add to our experiment will automatically be counting the number of trials that have occurred already (as well as how many repetitions of our trials list have occurred!). Run your experiment and have a loop at the output. You will see some useful information in the headers of your file.

.. nextslide::

*	:code:`trials.thisRepN` - the current repetition of your conditions file
*	:code:`trials.thisTrialN` - the current trialN within this repetition
*	:code:`trials.thisN` - the current trialN regardless of repetition
*	:code:`trials.thistrialIndex` - the index of the current trial from within our trialList (the conditions spreadsheet).

Showing trial progress
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Now we know how PsychoPy counts trials, we can use this info to add a trial counter and show how far through the experiment participants are. Add a text component and position it in the top left (in height units :code:`pos = (-0.4, 0.4)`). In the text field add :code:`$'Progress: ' + str(trials.thisN) + '/' + str(trials.nTotal)`. 


.. _usingMouse:

Using mouse/touchscreen responses
===================================

Mouse responses register as touch responses on touch screen devices, so they do make for a more portable online study. 

.. _mouseFeedback:

Feedback from a mouse
-----------------------------------

**Response time feedback from a mouse** 

In our example, we could use a mouse response by allowing the participant to click on one of the numbers. So long as the data from the mouse is set to save *On Click* (see data tab) this will return several values we can use for feedback:

- :code:`mouse.time` the time(s) of the mouse click(s). 
- :code:`mouse.clicked_name` the name(s) of the last object clicked

.. nextslide::

Adding a text component and writing :code:`$mouse.time[-1]` in the text field would show the time of the last mouse click. 

.. nextslide::

**Accuracy feedback from a mouse** 

Imagine we wanted to check our participant had selected the correct object. We could add a column to our conditions file e.g. "corrClick" then use a code component to check if this was correct::

    if mouse.clicked_name[-1] == corrClick:
        correct = 1
        print('correct!')
    else:
        correct = 0
        print('incorrect')

Note that we use :code:`[-1]` to retrieve the last object/time that was clicked. 



.. _mouse3days:

Making the most of mouse inputs
=================================

There are some neat aspects to the mouse that can make for interesting interactive experiments.


Stimuli that move with the mouse
----------------------------------

It's the easiest thing in the world to make a stimulus appear at the location of the mouse:

- add a Mouse Component (let's call it `mouse`)
- set the position of your stimulus to be at `mouse.getPos()` and **update on every frame**

Stimuli that act as buttons
----------------------------------

To turn a stimulus (almost any stimulus) into a button:

- Add a Mouse Component (let's call it `resp`)
- In the Mouse object, provide the names of stimuli that are "clickable"
- Optionally, insert whatever attributes about that stimulus you want to store

Is the mouse in *this* area?
---------------------------------------------

Most stimuli (except for text) have a method `.contains()` and so we can test whether the mouse is at that location.

Let's create a circle called `myStim` and an object that tracks the mouse, called `marker` and make `marker` change color if it goes inside the circle.

All we need is a Code Component with "Each Frame" set to::

  if myStim.contains(mouse):
    marker.color = 'red'
  else:
    marker.color = 'blue'

.. note::
  To take this online we need a slight edit::
  
    polygon.fillColor = new util.Color("red");

  instead of::

    polygon.color = 'red'


.. nextslide::

The stimulus that you test can be moving and that's fine too. The `.contains()` method doesn't care if the position is changing!

The "stimulus" can also be invisible (so you're effectively just using it to define an "area" rather than a stimulus).

Is the mouse "pressed in"
---------------------------------------------

You can continuously check if a mouse is pressed in an object using the mouse.isPressedIn(x) method. To check if the mouse is in the area of x and if one of the buttons is pressed in. 

Creating a button
---------------------------------------------

Using the fact that we can easily work out where a mouse is we can create dynamic "buttons" with a bit of code as well:

- create a stimulus
- test whether the mouse is contained in that stimulus
- test whether the mouse button(s) are being pressed

You can even make your button change when it has been pressed (e.g. stimuli that disappear once you click them?) or when you hover over them


What next?
---------------------------------------------

OK so we have covered the basics of making a task and how to do exciting dynamic things with the mouse. Let's touch on a relatively new response type...

:ref:`typedResponses3days`

*Exercise (time pending)*
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Let's practice what we know about mouse inputs to make a dot to dot demo. Participants will see a set of polygons and connect them (this allows us also to try the brush component!). When the mouse enters a polygon change it's colour.

.. nextslide::

We need:

- A number of polygons (keep the number small for now)
- A mouse
- The 'brush' component (our pencil to join the dots)
- A code component to turn the polygons red when the mouse is clicked in their location

.. nextslide::

*If you still have time* Repeat our dot-to-dot trial 3 times and present the dots in new locations on each trial. Use a clickable button to end each trial.

Side tip:
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
We have already seen how we can use 'conditional if' statements in python. And we could just use several of these statements to check if the mouse is in each polygon individually e.g.::

      if mouse.isPressedIn(polygon1):
        polygon1.color = 'red'
      if mouse.isPressedIn(polygon2):
        polygon1.color = 'red'
      if mouse.isPressedIn(polygon3):
        polygon1.color = 'red'

Alternatively, we could use a 'for' loop... 

.. nextslide::

For loops allow us to repeat the same set of code over a predefined n or over a set of objects. e.g.::

  polygons=[polygon1, polygon2, polygon3]
  for polygon in polygons:
    if mouse.isPressedIn(polygon):
        polygon.color = 'red'


.. note::
  To take this online we need a slight edit::
  
    polygon.fillColor = new util.Color("red");

  instead of::

    polygon.color = 'red'

  For useful tips on getting things online use:
    - `The psychopy to JS crib sheet <https://docs.google.com/document/d/13jp0QAqQeFlYSjeZS0fDInvgaDzBXjGQNe4VNKbbNHQ/edit#>`_
    - `The psychoJS API <https://psychopy.github.io/psychojs/module-visual.Polygon.html>`_
    - `The forum <https://discourse.psychopy.org/>`_

