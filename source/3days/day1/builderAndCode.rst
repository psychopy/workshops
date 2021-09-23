
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

This goes to the next step in integrating code with your experiment. You can add code in either python or JavaScript (JS). By default, python code will be **tranpiled** into Javascript. 

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


What can we do with code in our experiments?
---------------------

We can make more flexible and dynamic experiments using code, including:
   - :ref:`clocksAndTrialCounders`
   - :ref:`addingFeedback`
   - :ref:`mouse3days`
