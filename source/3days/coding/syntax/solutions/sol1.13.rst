.. _sol1.11:

Exercise 1.13 - using classes with PsychoPy
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python
	from psychopy import visual, sound, event
	from psychopy.sound import Sound


	class PianoKey:
	    def __init__(self, win, note, octave, pos):
	        # Rect component to represent the key on screen
	        self.rect = visual.Rect(
	            win, 
	            size=(0.05, 0.5), pos=pos, units="height",
	            fillColor="white"
	        )
	        # Mouse component to get clicks
	        self.listener = event.Mouse(
	            win
	        )
	        # Sound component to play note
	        self.sound = Sound(
	            value=note, octave=octave, volume=1,
	            secs=10 # (10s is short enough that it doesn't take forever to load, but longer than any note is likely to be played for)
	        )
	        # Start off unclicked
	        self.wasClicked = False
	    
	    def update(self):
	        # Draw rect
	        self.rect.draw()
	        # Check for clicks
	        isClicked = self.listener.isPressedIn(self.rect)
	        # Play sound on first frame of click
	        if isClicked and not self.wasClicked:
	            self.sound.play()
	            # Take note that the key was clicked for the next frame
	            self.wasClicked = True
	        # Stop playing when click is released
	        if self.wasClicked and not isClicked:
	            self.sound.stop()
	            # Take note that the key was released for the next frame
	            self.wasClicked = False
