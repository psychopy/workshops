.. _ex1.13:

Exercise 1.13 - using classes with PsychoPy
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Make a "PianoKey" class which contains:

	- A `visual.Rect` object to represent the key on screen
	- A `event.Mouse` object to listen to clicks
	- A `sound.Sound` object to play a sound when pressed

Then add an `update` method to be called each frame, which:

	- Checks for clicks
	- Plays the sound if clicked
	- Stops the sound when click is released
	- Draws the rectangle

If successful, you should be able to copy and paste your class definition above this code and run it:

.. code-block::python
	from psychopy import core, visual

	# Setup window and clock
	win = visual.Window()
	clock = core.Clock()

	# Make key
	key = PianoKey(
	    win=win, 
	    note="C", octave=4, 
	    pos=(0, 0)
	)

	# Each frame...
	while clock.getTime() < 10:
	    # Update key
	    key.update()
	    # Flip window
	    win.flip()

Things to keep in mind:
	
	- What needs to be imported for this to work?
	- What input will the class need in its `__init__` function?
	- How will it use these inputs?