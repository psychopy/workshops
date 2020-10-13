
.. _deeperChanges:

Making deeper changes (advanced)
============================================

You want to change PsychoPy itself?

 - **You can!** This is the beauty of Open Source
 - **It usually isn't even that hard!** This is the beauty of Python

What would I want to do?
----------------------------

Who knows? Maybe you want

 - a DotStim (RDK) that moves in a different way?
 - a whole "new" stimulus (e.g. a fixation point that's three rings)
 - a staircase that has a different selection method
 - a code component to be reusable

How to do it
----------------------------

First you have to work out what the Python code might look like from:

 - looking at existing code
 - searching online
 - importing other packages
 - ...

BUT then you also need to work out how to add this in a clean way so that you can still understand your study!

Classes and subclassing
--------------------------------------------

Let's imagine we're using dots in our study but we don't like DotStim. Fine:

 - Create a new DotStim that looks like the original and import that into your study.
 - Ideally your new DotStim is a subclass of the original and just overrides the methods you need
 - Now your study can use Builder just as before (easy to see what you're doing) but you import your own subclass and overwrite DotStim before it gets used
 
Similar solution for the change to the Staircase

Make your subclass re-usable
--------------------------------------------

If your class is going to be useful to multiple studies:

 - store it in a file in some central location (HOME/code/psychopyCompons)
 - add that location to the python path
 	- with a .pth file
 	- or in PsychoPy prefs (and then import psychopy)
 	- or by calling sys.path.append() in your script
 - now you can import that class in any study

Monkey-patching
--------------------------------------------

Sometimes you want to go even further and change something that you can't sub-class e.g. 

	- because PsychoPy creates it before you can insert code
	- because it's something that will be used globally

With "monkey patching" you can replace any command with something of your own, even builtin functions and even after classes have been created.

Custom Components
--------------------------------

If you know how to write Code Components then you're also most of the way to writing your own, reusable, *custom component* which will appear in the Components Panel of the Builder interface.

Not necessary but something for advanced technophiles to get into!

e.g. some users have added their own stimulus types, or hardware components (e.g. eyetracking) of their own