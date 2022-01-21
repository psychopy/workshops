
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

Code as arguments
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

This goes to the next step in integrating code with your experiment. You can add code in either python or JavaScript (JS). By default, python code will be **tranpiled** into JavaScript. 

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

Finally, at the end of our experiment we could add a text component and use some code in the text field :code:`$'You scored' + str((totalCorrect/totalTrials)*100) + '% correct!'`. If you want to be kind to future you, you could even save this summary variable to your data file by adding a code component to your last routine :code:`thisExp.addData('percent_correct', (totalCorrect/totalTrials)*100)`

.. nextslide::

We can also obtain similar fedback when :ref:`usingMouse` (but let's save that for later!)

*Exercise (10 mins)*
---------------------



* Use a conditional (if/then) code component to set the color of the feedback to be green if the response is correct and red if incorrect. 
* Give trial-by-trial feedback on how fast the participant was. Hint: you can access response times from a keypress using  :code:`key_resp.rt` and convert numbers to strings using :code:`str(x)` where :code:`x` is your number. 

More code examples
=========================

Inserting a timer
-------------------

To show the participant the time into a trial, we don't even need a code component. We can add a Text stimulus, and in the Text field write :code:`str(t)` then make sure to set the field *Each frame*. This is a good example of converting variable "types" in python:

- :code:`str()` : Converts to a string.
- :code:`int()` : converts to an integer.

.. nextslide::

This might return a value that is quite long, so, to round that we could use :code:`round(t, 3)`


Ending a set of trials early
-----------------------------------------------

Imagine we want a set of practice trials, that will end when your participant gets 5 correct. 

You can use the code :code:`trials.finished = True` to end a loop early. So, you could say:

.. code::
	if totalCorrect >= 5:
		practice_trials.finished = True # practice_trials is the name of the loop

Ending or skippng a routine
-----------------------------------------------

Imagine we want to skip a routine/trial (for example to only show a routine on some trials). You can add a code component and use

.. code::
    continueRoutine = False

To end or skip a routine. 

.. nextslide::

This can be extended to insert a break. The modulus operator :code:`%` can be used to say if a number has any remainders following a division, so, if we want a break every 5th trial we could add a routine in our trial loop called "breakMsg" and add a code component with the following in the begin routine:

.. code::
    if trials.thisN + 1 % 5 > 0:
        continueRoutine = False

Note that we add 1 because pytohn indexing starts at 0. 


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


In our experiment
---------------------

Following these examples, let's add different kinds of feedback to our task - :ref:`addingFeedback`

We can make more flexible and dynamic experiments using code, including:
   - :ref:`clocksAndTrialCounders`
   - :ref:`mouse3days`
