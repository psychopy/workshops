
.. _mouse:

Mouse inputs
=================

There are some neat aspects to the mouse that can make for interesting interactive experiments

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

.. nextslide::

The stimulus that you test can be moving and that's fine too. The `.contains()` method doesn't care if the position is changing!

The "stimulus" can also be invisible (so you're effectively just using it to define an "area" rather than a stimulus).

Creating a button
---------------------------------------------

Using the fact that we can easily work out where a mouse is we can create dynamic "buttons" with a bit of code as well:

  - create a stimulus
  - test whether the mouse is contained in that stimulus
  - test whether the mouse button(s) are being pressed

You can even make your button change when it has been pressed (e.g. stimuli that disappear once you click them?) or when you hover over them
