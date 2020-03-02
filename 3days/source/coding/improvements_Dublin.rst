.. P4N 2014 slides file, created by
   hieroglyph-quickstart on Tue Mar  4 20:42:06 2014.

.. _Improve:

Improvements
============================================

In this session we'll work through ways of improving the task we made earlier.

Improvements
------------------------

Previously we mentioned a few problems that we will work on in this session:

    - we should time our stimulus presentations by number of frames, for brief stimuli, not by a clock
    - a very fast response gets ignored because we only start looking at the keyboard after the probe has gone
    - we don't have any practice trials (to learn that the cue is 'informative')

Recording fast responses
------------------------

**setAutoDraw()**

This will allow you to say if you want to draw something on each frame, and allows you to stop
drawing something by setting to False.

.. nextslide::

Replacing .draw() should present something pretty similar, but we still miss quick responses::

    probe.setAutoDraw(True)
    win.flip()
    core.wait(info['probeTime'])
    kb.clearEvents ()
    kb.clock.reset()
    got_keypress = False
    while not got_keypress:
        keys =  kb.getKeys(keyList = ['left','right','escape'], clear=True)
        if 'escape' in keys:
            core.quit()
        if len(keys)>0:
            print(keys[0].name, keys[0].rt, keys[0].duration)
            rt = keys[0].rt
            resp = keys[0].name
            got_keypress = True
    print('RT (seconds):', rt)

.. nextslide::

We can stop drawing the probe when the probe time is up::

    while not got_keypress:
        if kb.clock.getTime()>info['probeTime']:
            probe.setAutoDraw(False)
            win.flip()

Timing stimuli using frames
------------------------

Currently ::

	info['probeTime']=0.2

On a 60Hz Monitor this is 12 frames.

Remember the duration of stimuli are limited to integers of the monitors frame rate.

.. nextslide::

To present something for 12 frames we would say::

	probe.setAutoDraw(True)
	for frameN in range(12):
		win.flip()
	probe.setAutoDraw(False)
	win.flip()

.. nextslide::

To ease the transition from time to frames we can set up a function to 
figure out how many frames are needed for our desired timing (sec) through measuring the
monitors frame rate::


	def sec_to_frame(sec, tol=0.1):
		frame_time = (sec)/(1/win.getActualFrameRate())
		frame_time_int= int(round(frame_time))
		if abs(frame_time - frame_time_int) < tol:
			return frame_time_int
		else:
			raise Exception('Desired timing not divisible by frame rate. Please reset')

*Note:* It is still better to plan your stimuli to be an integer of your frame rate. Here 
you might want to warn the user of timing discrepancies. 

.. nextslide::

Then we would use this function to convert our stimulus timings to frames::

	fixTime=sec_to_frame(info['fixTime'])
	cueTime=sec_to_frame(info['cueTime'])
	probeTime=sec_to_frame(info['probeTime'])
	trial_frames = fixTime+cueTime+probeTime

.. nextslide::

In our trial loop we then present stimuli like this::

    for frameN in range(trial_frames):
        if frameN<=fixTime:
            fixation.setAutoDraw(True)
        elif fixTime<frameN<=fixTime+cueTime:
            fixation.setAutoDraw(False)
            cue.setAutoDraw(True)
        else:
            cue.setAutoDraw(False)
            probe.setAutoDraw(True)
        win.flip()
    probe.setAutoDraw(False)
    win.flip()

.. nextslide::

Reset the response key clock when the probe is drawn and fetch the keys at the end of 
the trial::

    for frameN in range(trial_frames):
        if frameN<=fixTime:
            fixation.setAutoDraw(True)
        elif fixTime<frameN<fixTime+cueTime:
            fixation.setAutoDraw(False)
            cue.setAutoDraw(True)
        elif fixTime+cueTime==frameN:
            cue.setAutoDraw(False)
            probe.setAutoDraw(True)
            win.callOnFlip(kb.clearEvents)
            win.callOnFlip(kb.clock.reset) # sets t=0 to stim pres time
        win.flip()
    probe.setAutoDraw(False)
    win.flip()

.. nextslide::

If a response has not been made by the end of the trial time wait for a key press::

    while not keys:
        keys =  kb.getKeys(keyList = ['left','right','escape'], 
        		clear=True)
    if 'escape' in keys:
        core.quit()
    if len(keys)>0:
        print(keys[0].name, keys[0].rt, keys[0].duration)
        rt = keys[0].rt
        resp = keys[0].name
        got_keypress = True
    print('RT (seconds):', rt)


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
