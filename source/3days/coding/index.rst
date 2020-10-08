
.. P4N 2014 slides file, created by
   hieroglyph-quickstart on Tue Mar  4 20:42:06 2014.

.. _firstExperiment:

Coding a full experiment
============================================

In this session we'll create an experiment from scratch using only Python code.

The Posner Cuing task
------------------------

Synopsis of the study:

    - Present a probe to the left or right of fixation
    - Participants have to respond to the presence of the probe as quickly as possible
    - Precede the probe with a cue
    - Usually the cue predicts the probe location
    - We can measure the effect of attention by the difference in reaction times between correct and incorrect cues


How do we even start?
------------------------

Don't be tempted to try and write a script from beginning to end in one go! Break it down into chunks that you can manage. e.g.:

.. rst-class:: build

    - create a trial
        - create window
        - create fixation, cue and probe stimuli
        - set up the timing of the trial
    - set up conditions
        - need to alter probe location
        - need to alter cues
    - make sure data are being saved

Create a window
---------------------

First we need to import the necessary libraries. For an experiment we nearly always need to import the `visual`, `event`, `data` and `core` modules from PsychoPy::

    from psychopy import visual, event, core, data

then creating a window is another single line. We'll use units of pixels for the window for simplicity. Then all our stimulus dimensions will be in pixels::

    win = visual.Window([1024,768], fullscr=False, units='pix')

Save your experiment and run it to make sure a window flashes up.

Our trial starts with a fixation
------------------------------------

Immediately after creating our window we usually initialise objects like stimuli and clocks::

    #initialise some stimuli
    fixation = visual.Circle(win, size = 5,
        lineColor = 'white', fillColor = 'lightGrey')

Later (on each trial) we'll need to draw the fixation point and then flip the screen so that the drawing becomes visible::

    #run one trial
    fixation.draw()
    win.flip()

Create your probe stimulus
-----------------------------

Just for variety, let's create a Gaussian spot for the probe. You need this code where your stimuli are being initialised (doesn't matter if it's before or after probe)::

    probe = visual.GratingStim(win, size = 80, # 'size' is 3xSD for gauss,
        pos = [300, 0], #we'll change this later
        tex = None, mask = 'gauss',
        color = 'green')

After drawing the fixation point and flipping, we need to do the same for the probe::

    probe.draw()
    win.flip()

We also need a cue
------------------------------------

We could use some image of an arrow for this. Or we could create some shape of our
own with custom vertices::

    cue = visual.ShapeStim(win,
        vertices = [[-30,-20], [-30,20], [30,0]],
        lineColor = 'red', fillColor = 'salmon')

Also add draw() code like the other objects. Again, it doesn't matter the order we initialise it, but the drawing needs to be between the fixation and the probe.

Understanding `Window.flip()`
-------------------------------

    - All the `draw()` commands operate on a memory buffer called the 'back buffer' on the graphics card.

    - When you `flip()` the window it causes everything in that 'back buffer' to become visible on the physical screen.

    - The flip() command waits until the next screen refresh to present your stimuli (every 1/60s, so about 16.6ms)

    - It will then wait until the physical screen refresh occurs (if possible with your graphics card settings)

.. nextslide::

This has various knock-on effects:

    - That means your screen flips (and intervening code) are tied to a fixed rate of 1/60s

    - It is physically impossible to draw your stimulus for partial frames (e.g. 25ms) on a 60Hz screen

    - Also, if Python/PsychoPy has to run too much code between flips you might 'drop' a frame (fail to get it drawn by the time of the screen refresh)

    - If you don't call `flip()` for a while, or if you drop a frame, the screen will stay as it is for another frame

Set some timing parameters
-----------------------------

If you run now the objects will be presented for a single frame each (1/60th of sec). That's too short for us to see. We need to set times for our objects. we can achieve that with the `core.wait()` function.

Possible: "hard code" the values by typing them where needed.

Better: store them as variables at the top of the script

Even better: store them in a *dictionary* that we can save easily in the data files::

    info = {} #a dictionary
    info['fixTime'] = 0.5 # seconds
    info['cueTime'] = 0.2
    info['probeTime'] = 0.2

Pause after flipping the window for each object
----------------------------------------------------------

Add a line to wait after each flip of the window::

    # run one trial
    fixation.draw()
    win.flip()
    core.wait(info['fixTime'])

    cue.draw()
    win.flip()
    core.wait(info['cueTime'])

    probe.draw()
    win.flip()
    core.wait(info['probeTime'])

This is not actually a very precise way to control timing, but it's very easy!

Drawing two objects at the same time
----------------------------------------------------------

If you `draw()` two stimuli before a `win.flip()` then they both appear on the same frame. For the probe presentation let's have the fixation as well::

    fixation.draw()
    probe.draw()
    win.flip()
    core.wait(info['probeTime'])

If the stimuli overlap in space then the later draw() will occlude the earlier one. You can also set the degree of opacity of stimuli so that they are partially visible.

Let's run two trials
-----------------------

We could copy and paste the trial code to run repeated trials.

Try doing that so that you get two repeats of the trial.

That's very inefficient though, so undo it.

Exercise: Why not create a loop to run as many trials as you like? That would be more efficient. Add a for... loop and indent your trial code so that it is 'contained' in the loop. Set the loop to run for 5 'repeats'.

.. nextSlide::

Solution::

    for trial in range(5):
        fixation.draw()
        win.flip()
        core.wait(info['fixTime'])
    
        cue.draw()
        win.flip()
        core.wait(info['cueTime'])
    
        probe.draw()
        win.flip()
        info['probeTime']

.. _trialHandler:

TrialHandler
------------------------

This allows you to run multiple trials of different conditions in various ways (random or sequential etc.). It lives in the PsychoPy's `data` module, which we already imported.

To repeat our trials using the TrialHandler instead of the basic for loop we can do this::

    trials = data.TrialHandler(trialList=[], nReps=5)
    for thisTrial in trials:
        #code to run one trial here

For now we've set the `trialList` simply to an empty list, but later we'll change that.

The code above needs to come somewhere *after* you initialise your stimuli and it needs to include your trial code

Controlling conditions
------------------------

We need the stimuli to differ on each trial, which TrialHandler can also help us with. It expects to receive conditions (aka `trialTypes`) as a list of dictionaries, where one dictionary specifies the parameters for one condition. We could write that by code using a for...loop, but it might be easier this time to use a spreadsheet.

You could have achieved exactly the same as this using code to create a list of dictionaries with one dictionary for each type of trial in your conditions.

Create a conditions file
--------------------------------

We can import conditions from either *.xlsx* or *.csv* files.

Create a file with:

    - headings that specify dictionary fields
    - (headings better with no spaces or punctuation, although that won't actually matter today)
    - one row per condition/trial-type
    - no missing columns or rows (e.g. don't leave a row between header and trials)


.. nextslide::

For the Posner task we *need* control of:

    - direction of cue (we could rotate the stimulus 180 deg to point the other way)
    - location of probe

For analysis it's handy also to store:

    - something to signal whether this trial is 'valid cue'
    - a description of this trial?

.. nextslide::

So we might have a sheet like this:

=======   =======   =======  =========
cueOri    probeX    valid    descr
=======   =======   =======  =========
0          300      1        right
180       -300      1        left
0          300      1        right
180       -300      1        left
0          300      1        right
180       -300      1        left
0          300      1        right
180       -300      1        left
180        300      0        conflict
0         -300      0        conflict
=======   =======   =======  =========

Save the file in `xlsx` or `csv` format. e.g. "conditions.csv"

Import that file and put it to use
------------------------------------

The `data` module in PsychoPy has a function to import such files. It gives a *list* of *dicts* that can be used directly in the TrialHandler::

    conditions = data.importConditions('conditions.csv')
    trials = data.TrialHandler(trialList=conditions, nReps=5)
    for thisTrial in trials:
        #code to run one trial here
        ...

This will run 5 repeats of our 10 trial types randomly. The way we've set this up we'll get 50 trials with 80% valid probes.

Updating stimuli
---------------------------

Each time through the loop the value `thisTrial` is a dictionary for one trial, with keys that have the column names::


    for thisTrial in trials:
        #code to run one trial here
        probe.setPos( [thisTrial['probeX'], 0] )
        cue.setOri( thisTrial['cueOri'] )

You can see the code changes here:

    - `repository: updating stimulus <https://github.com/psychopy/posner/commit/09e7057e0d243f5a211814453324efbd355b2d5e>`_

Collect responses
--------------------------

Now let's get a key-press after each trial and measure the reaction time (RT).

Before starting our trials we could create a clock/timer to measure response times::

    respClock = core.Clock()

Then when we present our stimulus we could reset that clock to zero::

    fixation.draw()
    probe.draw()
    win.flip()
    respClock.reset()
    ...

.. nextslide::

After our stimulus has finished we should flip the screen (without doing any drawing so it will be blank) and then wait for a response to occur::

    #clear screen
    win.flip()
    #wait for response
    keys = event.waitKeys(keyList = ['left','right','escape'])
    resp = keys[0] #take first response
    rt = respClock.getTime()

.. nextslide::

Check if that response was correct::

    if thisTrial['probeX']>0 and resp=='right':
        corr = 1
    elif thisTrial['probeX']<0 and resp=='left':
        corr = 1
    else:
        corr = 0

.. nextslide::

And store the responses in the TrialHandler::

    trials.addData('resp', resp)
    trials.addData('rt', rt)
    trials.addData('corr', corr)

(Note that we aren't saving the data file yet though!)

You can see the full set of code changes here:

`repository: collecting responses <https://github.com/psychopy/posner/commit/2aaebe7450d1828c3d0a28a8a84d8af5ebf55286>`_

(The 'view' button will fetch you the full script so far)

.. _experimentHandler:

Using the ExperimentHandler
-------------------------------

For today the `ExperimentHandler` isn't strictly needed, but it allows some nice things so we'll use it:

    - it allows multiple loops/handlers to be combined into one (e.g. we could have a loop of practice trials and another loop of main trials)
    - it saves data automatically in 3 formats even if there's an error:

        - log file for detail but not for analysis
        - csv file trial-by-trial is easy for analysis
        - psydat file contains more info about trials than csv file (and can regenerate the csv!)


.. nextslide::

All we need to do is:

    - create a base file name for our data files
    - create the `ExperimentHandler`
    - add our `trials` loop to it
    - tell it when one 'entry' is complete (one row in the data file, typically one trial)

Create a base filename
--------------------------

Let's create a filename using the participant name and the date. OK, so we'll need to get those!

For the username, we can easily create a dialog box that uses our `info` dictionary to store information (top of our script)::

    info = {} #a dictionary
    #present dialog to collect info
    info['participant'] = ''
    dlg = gui.DlgFromDict(info) #(and from psychopy import gui at top of script)
    if not dlg.OK:
        core.quit()
    #add additional info after the dialog has gone
    info['fixTime'] = 0.5 # seconds
    info['cueTime'] = 0.2
    info['probeTime'] = 0.2
    info['dateStr'] = data.getDateStr() #will create str of current date/time

.. nextslide::

Now we've collected the information there are various ways to create our filename string. All of these achieve the same thing, e.g. `data/jwp_2014_Apr_13_1406` ::

    filename = "data/" + info['participant'] + "_" + info['dateStr']
    filename = "data/%s_%s"%(info['participant'], info['dateStr'])
    filename = "data/{0}_{1}".format(info['participant'], info['dateStr'])
    filename = "data/{0['participant']}_{0['dateStr']}".format(info)
    filename = "data/{participant}_{dateStr}".format(**info)

You can see them looking increasingly obscure, but increasingly brief.

Create ExperimentHandler
--------------------------

After your code to create the TrialHandler loop::

    #add trials to the experiment handler to store data
    thisExp = data.ExperimentHandler(
            name='Posner', version='1.0', #not needed, just handy
            extraInfo = info, #the info we created earlier
            dataFileName = filename, # using our string with data/name_date
            )
    thisExp.addLoop(trials) #there could be other loops (like practice loop)

**AND** at the end of the response collection we need to inform the experiment handler that it's time to consider the trial complete::

    ...
    trials.addData('rt', rt)
    trials.addData('corr', corr)
    thisExp.nextEntry()


We can't quit during a run
----------------------------------------------------

Let's make it possible to end the experiment during a run using the 'escape' key

Where you checked your responses we need to add something to handle that::

    elif resp=='escape':
        trials.finished = True

Alternatives to `trials.finished=True` ::

    break #will end the innermost loop, not necessarily `trials`
    core.quit() #from psychopy lib will exit Python

NB: If you hit the red stop button in PsychoPy it issues a very severe abort and no data will be saved!


All done!
-------------

If I push these changes to pavlovia, you can see the changes we make to the task throughout task creation...

Improvements...
-----------------

There are a few problems with this version, that we could definitely improve on. Currently:

    - a very fast response gets ignored because we only start looking at the keyboard after the probe has gone
    - we should time our stimulus presentations by number of frames, for brief stimuli, not by a clock
    - we don't have any practice trials (to learn that the cue is 'informative')
    - our code is not very 'modular'
    - but it does work and took less than 100 lines!

Summary
----------------

Hopefully you've learned how to:
    - present stimuli
        - create them
        - set params as needed
        - draw each time you need to (or set autodraw to True)
        - update the window with `win.flip()`
    - control trials using the `TrialHandler`
    - set timings
    - receive responses from a keyboard
    - save data in various formats


.. nextslide::

What next? 
:ref:`Improvements`