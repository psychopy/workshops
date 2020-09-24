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

    for frameN in range(5):
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

	#Create two sets of trial handlers
	trials = data.TrialHandler(trialList=conditions, nReps=1, name='mainBlock')
    pracTrials = data.TrialHandler(trialList=conditions, nReps=1, name='practiceBlock')
    outerLoop = [pracTrials, trials]


.. nextslide::

Then, put our trial loop inside a block loop (indent the whole block), create 
the trial list at the start of the block and add it to the experiment handler::

    for trials in outerLoop:
        thisExp.addLoop(trials)
        for trial in trials:
            print(trials.name)#check this is the set of trials we were expecting

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

	for trials in outerLoop:
    thisExp.addLoop(trials)
    if trials.name=='mainTrials'
		Continue.draw()
		win.flip()
		event.waitKeys()

Further improvements
------------------------

Exercises:

	- Add trial-by-trial feedback on correctness and RT
	- End the practice trials early if the participant scores 5 correct in a row



Let's talk about :ref:`syntax` (but you will have picked a lot of this up 
already!) and then look at :ref:`plottingPosner` 

.. toctree::
    :hidden:
    :maxdepth: 1

    syntax/index_Dublin
    arraysAndPlotting_Dublin
