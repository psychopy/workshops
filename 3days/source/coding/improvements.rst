.. P4N 2014 slides file, created by
   hieroglyph-quickstart on Tue Mar  4 20:42:06 2014.

.. _Improvements:

Improvements
============================================

In this session we'll work through ways of improving the task we made earlier.

Improvements
------------------------

Previously we mentioned a few problems that we will work on in this session:

    - we should time our stimulus presentations by number of frames, for brief stimuli, not by a clock
    - a very fast response gets ignored because we only start looking at the keyboard after the probe has gone
    - we don't have any practice trials (to learn that the cue is 'informative')

Presenting stimuli by frames
------------------------

Previously we used the::

    probe.draw()
    win.flip()

This is fine, but as soon as you flip the window again, the stimulus will disappear.  **setAutoDraw()** allows you to continue drawing on every frame.

.. nextslide::

We could draw something on a set number of frames using a 'for' loop::

    for Nframes in range(5):
        probe.setAutoDraw(True)
        win.flip()
    probe.setAutoDraw(False)

This should look pretty similar when we run it.
Exercise: Reset our stimulus timings by adapting our 'info' dictionary.

.. nextslide::

We could use several for loops OR we could use one large for loop with 'if' statements::

    for frameN in range(totalFrames):
        if frameN<info['fixTime']:
            fixation.setAutoDraw(True)
        elif info['fixTime']<=frameN<info['fixTime']+info['cueTime']:
            fixation.setAutoDraw(False)
            cue.setAutoDraw(True)
        else:
            cue.setAutoDraw(False)
            probe.setAutoDraw(True)
        win.flip()
    probe.setAutoDraw(False)
    win.flip()

Getting an early keypress
------------------------

For more precise keypress measurements, we can use the Keyboard class rather than the event module.

.. nextslide::

**hardware.keyboard.Keyboard.getKeys()**

Uses python-psychtoolbox lib and has some advantages:

    * polling is performed and timestamped asynchronously with the main thread (times relate to when the key was pressed, not when the call was made)
    * it's faster
    * can detect the KeyUp events (enabling) keypress duration
    * on Linux and Mac you can distinguish between different keyboard devices (see getKeyboards())

.. note:: On 32 bit installations and Python2 older psychopy.event.getKeys() is used.

.. nextslide::

**hardware.keyboard.Keyboard.getKeys()**::

    #at the start of your script
    from psychopy.hardware import keyboard
    kb = keyboard.Keyboard()

.. nextslide::

We can reset this clock and get keypresses using::

    kb.clock.reset()
    keys = kb.getKeys(keyList = ['left','right','escape'])


If a response has not been made by the end of the trial time wait for a key press::

    while not keys:
        keys =  kb.getKeys(keyList = ['left','right','escape'], 
        		clear=True)
    resp = keys[0].name
    rt = keys[0].rt

This will function much like our old code... we need to position the first call to getKeys to make a response earlier.

.. nextslide::

Exercise: Where do we reposition the call to getKeys in order to measure response time from the time the probe is first drawn?

To check your solution, try changing the duration of the fixation, cue and probe to check you can respond before or when the probe appears

Try printing the response time ...

.. nextslide::

You may notice that we are getting some negative rts... this is because a response is logged before the clock is reset... why? We might need to clear the event buffer::

            elif frameN==info['fixTime']+info['cueTime']:
                #reset clock and listen for keypress
                kb.clearEvents()
                kb.clock.reset()
                keys = kb.getKeys(keyList = ['left', 'right', 'escape'])

.. nextslide::

Final solution::
        for frameN in range(totalFrames):
            if frameN<info['fixTime']:
                fixation.setAutoDraw(True)
            elif info['fixTime']<=frameN<info['fixTime']+info['cueTime']:
                fixation.setAutoDraw(False)
                cue.setAutoDraw(True)
            elif frameN==info['fixTime']+info['cueTime']:
                #reset clock and listen for keypress
                kb.clearEvents()
                kb.clock.reset()
                keys = kb.getKeys(keyList = ['left', 'right', 'escape'])
            else:
                cue.setAutoDraw(False)
                probe.setAutoDraw(True)
            win.flip()
        probe.setAutoDraw(False)
        win.flip()
        #if a key hasn't been pressed already wait untill one is
        while not keys:
            keys =  kb.getKeys(keyList = ['left','right','escape'])
        resp = keys[0].name
        rt = keys[0].rt

.. nextslide::

Practice trials
------------------------

We want a practice block, in which one trial for each condition is presented. For this, 
we can use our Experiment Handler::

	#Before our trial loop
	#Create an outerloop that acts as a block (2 blocks; practice and main)
	outerLoop = data.TrialHandler(trialList=[], nReps=2, name='Block',
					 method='random')
	thisExp.addLoop(outerLoop)

.. nextslide::

Then, put our trial loop inside a block loop (indent the whole block), create 
the trial list at the start of the block and add it to the experiment handler::

	block_count=0
	for block in outerLoop:  # the outer loop doesn't save any data
		if block_count==0:
			trials = data.TrialHandler(trialList=conditions, 
					nReps=1, name='practiceBlock')
		else:
			trials = data.TrialHandler(trialList=conditions, 
					nReps=2, name='mainBlocks')
		block_count=block_count+1
		thisExp.addLoop(trials)
		for thisTrial in trials:

Now lets run that and look at the output...

.. nextslide::

**Exercise** We want a message at the start to show task instructions, and 
a message after the practice trials to check if participants are OK to move on to the 
main trials...

*Hint* See Demos > textStimuli.py

.. nextslide::

**Solution** Make some text stimuli::

	#When creating your stimuli
	#Task instructions and continue messages
	Instructions = visual.TextStim(win,
		units='norm', height = 0.1,
		pos=(0, 0), text='In this task you will see a green circle on either the left or the right\nPress the left arrow if the circle is on the left\n press the right arrow if it is on the right\nPress space for a practice round',
		color='White')

	Continue = visual.TextStim(win,
		units='norm', height = 0.1,
		pos=(0, 0), text='That was the end of the practice, are you ready to continue?\nPress the left arrow if the circle is on the left\n press the right arrow if it is on the right\nPress space to start',
		color='White')

.. nextslide::

**Solution** present the text stimuli in the relevant places::

	#Before your block loop 
	Instructions.draw()
	win.flip()
	event.waitKeys()

	#At the start of your block loop
	for block in outerLoop:  # the outer loop doesn't save any data
		if block_count ==0:
			trials = data.TrialHandler(trialList=conditions,
						nReps=1, method = 'random', name='PracticeBlock')
		else:
			trials = data.TrialHandler(trialList=conditions,
						nReps=5, method = 'random', name = 'MainBlock')
		if block_count==1:
			Continue.draw()
			win.flip()
			event.waitKeys()
		block_count=block_count+1

Further improvements
------------------------

There are many further tweaks we may want to make:

	- Providing feedback
	- Counterbalancing

And many more specific to your experiment requirements...

Next we will cover :ref:`plottingPosner` 

Time permitting we might cover :ref:`syntax` (but you will have picked a lot of this up 
already!)

.. toctree::
    :hidden:
    :maxdepth: 1

    syntax/index_Dublin
    arraysAndPlotting_Dublin
