
.. _mouse:

Mouse inputs
=================================

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

Dot to Dot Demo
---------------------------------------------

We need:

- A number of polygons
- A mouse
- The 'brush' component (our pencil to join the dots)
- A code component to turn the polygons red when the mouse is clicked in their location

.. nextslide::

We have already seen how we can use 'conditional if' statements in python. And we could just use several of these statements to check if the mouse is in each polygon individually. 

Alternatively, we could use a 'for' loop... 

.. nextslide::

For loops allow us to repeat the same set of code over a predifined n or over a set of objects. e.g.::

  polygons=[polygon1, polygon2, polygon3]
  for polygon in polygons:
    if mouse.isPressedIn(polygon):
        polygon.color = 'red'

OK so once we have this, let's try and take this online.

.. nextslide::

When getting this online, we might notice this doesn't quite look as we expect. In these cases, there are several places we could look for support:

- `The psychopy to JS crib sheet <https://docs.google.com/document/d/13jp0QAqQeFlYSjeZS0fDInvgaDzBXjGQNe4VNKbbNHQ/edit#>`_
- `The psychoJS API <https://psychopy.github.io/psychojs/module-visual.Polygon.html>`_
- `The forum <https://discourse.psychopy.org/>`_

.. nextslide::

If something works locally, but not online, this is typically a JS translation issue. so we can change the JS side of our code e.g.::
  
  polygon.fillColor = new util.Color("red");

instead of::

  polygon.color = 'red'

What next?
---------------------------------------------

OK so we have covered the basics of making a task and how to do exciting dynamic things with the mouse. Let's touch on a relatively new response type...

:ref:`typedResponses`

An exercise (time pending)
---------------------------------------------

Practice what we learnt earlier to present several trials of our task:

-repeat our trial 3 times and present the dots in new locations on each trial.
- use a second mouse component with a clickable button to end each trial