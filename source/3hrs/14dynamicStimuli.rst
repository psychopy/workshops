
.. _dynamic:

Making things dynamic
===================================

What is dynamic?
---------------------

In PsychoPy everything is organised in reference to time

  - We don't have "slides" that simply follow each other like in some packages
  - Things overlap in time
  - Things can *change* their attributes in time

Why is that useful?
----------------------------------------

You could use this, for instance, to:

  - gradually reveal an object
  - make an object move to make the task harder
  - make an object more interesting for participants (e.g. developmental)

    - rainbow text
    - throbbing heart

Code as arguments
---------------------

Most dialog entries have the option to take raw Python code if you start your entry with `$` (or have that by default).

You can use this as more than a variable from your conditions file e.g.:

    - set stimulus position to travel in a circle with :code:`$[ sin(t*2*pi), cos(t*2*pi) ]` and set this to `update every frame`

NB. If you actually need a dollar symbol to be in your text, do one of:
    - `$"You won $5"`  [include quotes]
    - `You won \\$5`

.. nextSlide::


Let's create a task where text is gradually revealed.

Think of a Routine like this:

.. image:: /_images/routineTextReveal.png

The text object could be any long piece of text. You might need to make sure the wrap length is set to be the full width of the screen to fit on one line.

.. nextSlide::

.. image:: /_images/revealMaskProperties.png
    :align: right

Your mask is a square that moves (note the size and the pos settings).

..  _quizShowFaces:

Quiz show faces
----------------------------

- Let's take some faces and make them shrink and rotate while participants try to detect the face.

- The psychological point of this isn't clear(!), but it used to be popular in quiz shows.

- "Have I got News For You" still does it.

..  _heartThrob:

Create a pulsating heart
----------------------------

Download an image of a "love" heart, preferably one with a transparent background.

Let's put that into a PsychoPy experiment and set its size to vary on every frame.

.. image:: /_images/heart_red.png
    :align: center
    :scale: 10

Equation for a pulse
-----------------------

Getting the maths to look right here is going to be the key.

It's something based on a sinusoid. Recall that `sin(t)` varies smoothly
between -1 and 1:

  - `sin(t)` :  too small
  - `50*sin(t)` : big enough (50 pixels) but it goes negative
  - `100+50*sin(t)` : varying nicely between 50 and 150 pixels

That's a good start. If we want to make it more pulse-like we need to
raise the value to a power before scaling it up:

  - `100+50*sin(t)**4`

More ideas and working code
-----------------------------

Inside the examples zip file, look under::

  builder/dynamic

You'll find working examples of a range of these stimulus setups

Coming next
---------------

:ref:`blockDesigns`
