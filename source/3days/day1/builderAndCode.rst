
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
~~~~~~~~~~~~~~~~~~~~~~~

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

.. _codeComponents:

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


Example uses of code in PsychoPy
================================

Inserting a break
-------------------

Imagine you want to insert a break every 10th trial. You could add a routine in your trial loop, then add a code component and use this in the *Begin Routine* tab::

	if not trials.thisN % 10:
		continueRoutine = False

.. nextslide::

A few handy bits of code are used here:

- :code:`%` : the modulus operator, returns the remainder of a value.
- :code:`.thisN` the current iteration number of this loop *Remember: python indexing starts at 0*.
- :code:`continueRoutine` : if :code:`False` the current routine will end and the experiment will progress. 

Inserting a timer
-------------------

To show the participant the time into a trial, we don't even need a code component. We can add a Text stimulus, and in the Text field write :code:`str(t)` then make sure to set the field *Each frame*. This is a good example of converting variable "types" in python:

- :code:`str()` : Converts to a string.
- :code:`int()` : converts to an integer.

.. nextslide::

This might return a value that is quite long, so, to round that we could use :code:`round(t, 3)


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

Randomizing the order of stimuli (e.g. images)
------------------------------------------------

Imagine you have 4 images to present in 4 locations. On each trial, you want the location for each image to be selected randomly. You could add a code component, and in the `Begin Routine` tab write::
	
	imageList = ['images/im1.jpg', 'images/im2.jpg', 'images/im3.jpg', 'images/im4.jpg']
	shuffle(imageList)

Then in your image components use :code:`$imageList[0]`, :code:`$imageList[1]` and so on... *making sure to set every repeat*


Storing custom variables
--------------------------------------

It is really handy to be able to save custom variables to our data file. Following the example of randomizing image order, we could save the image list to our data file using :code:`thisExp.addData('imageList', imageList)` the function :code:`addData()` takes 2 arguments - the first is the value for the column header in the output file, the second it the value of the variable to save. 

Adding feedback
--------------------------------------

**Response time feedback from a mouse** 

In our Posner example, we are using mouse responses. So long as the data from the mouse is set to save *On Click* (see data tab) this will return several values we can use for feedback:

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

**Response time feedback from a key press** 

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

In our experiment
---------------------

Following these examples, let's add different kinds of feedback to our Posner task - :ref:`addingFeedback`

We can make more flexible and dynamic experiments using code, including:
   - :ref:`clocksAndTrialCounders`
   - :ref:`mouse3days`
