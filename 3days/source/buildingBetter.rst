
.. _session1:

Building better experiments
==============================

Using Builder
-----------------

.. slide:: Overview

    * :ref:`builderInterface`
    * :ref:`conditionsBuilder`
    * :ref:`trials`
    * :ref:`responsesBuilder`
    * :ref:`data`

.. _builderInterface:

The Builder interface
~~~~~~~~~~~~~~~~~~~~~~~~

An experiment in Builder has:

    - a single *Flow*
    - one or more *Routines* that are combined in the *Flow*
    - several *Components* that are combined to form *Routines*

The Flow
~~~~~~~~~~~~~~~~~~

This is really simply a flow diagram. It only specifies the order in which things occur and whether or not they repeat in a "Loop".

.. figure:: /_images/flowStroop2020.png

The Flow (usually) doesn't know how long things will last or what happens within them. It simply runs a *Routine* until that *Routine* has finished and then moves onto the next until the experiment finishes.

In the case of the Stroop task we have 3 Routines that run in turn and the 'trial' Routine is repeated a number of times in a loop.

Routines
~~~~~~~~~~~~~~~~~~

These define how *Components* interact in time. They allow one or more stimuli to be displayed and repsonses to be collected at defined times relative to the start of the Routine.

A typical Routine would be a trial (present one or more stimuli and get a response) but it might be something else like the presentation of instructions.

Also, a trial could be comprised of multiple Routines.

.. nextSlide::

Let's take a look at the `trial` Routine for the Stroop task.

.. image:: /_images/routineStroop2020.png

The 'trial' Routine in the basic Stroop task. You can see there are just two thing comprising the trial, a `Text Component` and a `Keyboard Component`

.. nextSlide::

You can see that the Routine has a time view, like a track editor for movie/audio editing software, so Components can be controlled independently in time. Maybe a fixation point would stay on for your entire trial but the stimulus would just appear for a short period.

In the stroop demo the stimulus and keyboard both start at 0.5s after the beginning of the Routine. They both last an infinite duration (the time bar extends beyond the screen).

Components
~~~~~~~~~~~~~~~~~~

.. image:: /_images/componentsView2020.png
    :align: right

There are many Components that could be added to a Routine. These are shown in the right-hand panel with different categories.

On the toolbar
~~~~~~~~~~~~~~~~~~

The first few icons are probably obvious (New experiment, Open, Save, Undo, Redo).

With the others, if you hover you'll get a tooltip telling you what they do.

The first two concern the Monitor centre (which controls screen parameters and callibration) and Experiment settings.

.. image:: /_images/monitorExpSettings.png
    :align: right

.. nextSlide::

The next set of icons allow you to compile your programme to a (slightly complicated) python .py file and run your programme (optionally through "Runner view").

.. image:: /_images/compileRunnerRun.png
    :align: right

Runner view
~~~~~~~~~~~~~~~~~~

.. image:: /_images/runnerView.png
    :align: right

Shows which file you are running, gives helpful alerts (to save time "fixing" things!) and gives a print out (stdout) of info as your task runs. The red cross force quits experiments (without saving any data!)

On the toolbar
~~~~~~~~~~~~~~~~~~

The final set of icons cover the run online options (we will cover these later!).

.. image:: /_images/onlineIcons.png
    :align: right

Your first study
---------------------

We'll build the [Erikson]_ flanker task. The task involves a central target with irrelevant objects, that may or may not match the target, on either side. The question is whether the reaction time differs according to whether the flankers match.

.. _conditionsBuilder:

Define your conditions
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The first thing we need to do when creating a task is to set up the conditions. Think about what differs from one trial to the next:

    - Do you need different filenames?
    - Different "correct" answers?
    - Different stimulus durations?

In the flanker task we basically need 4 trial variants:

.. code-block:: python

   < < < < <  # left congruent
   > > < > >  # left incongruent

   > > > > >  # right congruent
   < < > < <  # right incongruent

.. nextSlide::

For now we'll just use text characters as the stimuli, but they could be anything. We'll do a version with images afterwards.

Open a spreadsheet application (e.g. MS Excel) and create this set of entries:

    ==========     ========  =======
      stim          corrAns   congr
    ==========     ========  =======
    < < < < <       left     1
    > > < > >       left     0
    > > > > >       right    1
    < < > < <       right    0
    ==========     ========  =======

.. nextSlide::

In this table:

    - The columns represent variables that we can refer to from PsychoPy
    - The variable names need to be unique and with no punctuation (case-sensitive)
    - The rows represent distinct trials (which we can randomise and repeat)
    - In our case `cong` isn't actually used by PsychoPy but it's useful for analysis

.. nextSlide::

Create a folder on the computer where you'll store the experiment.

Save your spreadsheet inside that folder as an Excel Workbook (*.xlsx* format), or comma-separated-value (*.csv*) file.

.. _trials:

Define your trials
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

For the flanker task (as we've defined it) all we need is a single Text Component on each trial and a Keyboard Component for participants to respond.

Open the PsychoPy Builder view and make sure you have an empty (New) experiment.

Save it straight away in the folder you created. (This creates a *.psyexp* file)

.. nextSlide::

We want about 0.5s inter-trial-intervals (ITI) so that participants don't feel too rushed. To achieve that all we need to do is start the stimulus/response Components after a period at the beginning of the Routine.

.. image:: /_images/textAdd2020.png
    :align: right

Create a new Text Component by clicking the button on the right.

NB: The buttons on the right create new objects, but you can edit an object by clicking on its icon in the Routine. You can remove an object by *right* clicking its icon in the Routine. You can also copy and past a component to a new routine. 

.. nextSlide::

.. figure:: /_images/textDlg1st2020.png

    Text dialog with contents for our stimulus

.. nextSlide::

Note, we changed:

    - the *start* time to 0.5 (seconds after Routine started)
    - the *stop* (duration) could be shorter?
    - the *text* became *$stim* where the name *stim* was one of our columns
    - the *text* has been set to *update every repeat* (of the Routine)

NB: Start and stop can be defined in different ways (times, frames, conditions) and a duration/stop that is left blank will last forever.

.. nextSlide::

*If you get an error message from your experiment that "stim is not defined" it means one of these things:*

    - you didn't tell PsychoPy to "set every repeat"
    - you have a typographical (e.g. capitals) error with your conditions file
    - you haven't told PsychoPy about your conditions file (like now)

.. nextslide::

To repeat trials (with variations as needed) we need to add a loop to your Flow.

Click ONCE on *Insert Loop* in the Flow panel:

.. image:: /_images/flowClickInsertLoop2020.png
    :align: center

Then click the start and the end points for your loop (it doesn't matter which you do first). If the is only one remaining valid place for your loop to go the other point will be added automatically.


.. image:: /_images/flowInsertLoopStart2020.png
    :align: center

.. nextslide::

When the start/end points are added a dialog will appear to allow you to control the settings.

.. image:: /_images/loopDlg2020.png
    :align: center

NB: Later, you can click on the loop name to get this dialog back.

.. nextSlide::

Press `Browse...` to find your conditions file, telling PsychoPy about each of your trials.

.. image:: /_images/loopDlgComplete2020.png
    :align: left

If you got your excel file right then you'll see a message telling you how many trial types and variables you created.

Press `OK`

.. nextSlide::

Your Flow should now look something like this:

.. image:: /_images/flowWithLoop2020.png
    :align: center

At this point you should be able to save your experiment and run the "study".

You'll see a dialog appear asking for the name of the participant and the "session".

When you run you should see different trials occuring. Press `Escape` anytime to quit (will save the data but not much will be in there).

.. _responsesBuilder:

Collecting responses
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Believe it or not we've nearly finished!

All we really need now is to collect reaction times.

Add a Keyboard Component to your study with:

    - start = `0.5` (seconds)
    - end = `<leave blank, meaning infinite>`
    - allowed keys = `'left','right'`
    - store correct = `True`
    - correct = `$corrAns`

.. nextSlide::

.. image:: /_images/keyboardDlg2020.png
    :align: left

For more information about the options you could press the help button.

.. nextSlide::

Your `trial` Routine should now look like this. Note the start times align at 0.5 but the keyboard option goes on forever. The trial only ends when a response is made in this study.

.. image:: /_images/routineFlankerText2020.png
    :align: center

Add some instructions
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

For instructions:
    - create a new Routine called `instructions`
    - insert that Routine into your Flow before the `trials` loop starts

.. image:: /_images/addRoutine.png

Click on that Routine (either in the Flow or in the Routine tabs at the top) to edit that.

.. nextSlide::

Add a text component to `instructions` Routine:
    - name = `instructText`
    - start = 0
    - duration = `<blank i.e. infinite>`
    - text = `<something useful here about the keys to press>`

Because we made the text last forever we need to provide something to end the Routine or we'll never get to the main experiment!

.. nextSlide::

Add a keyboard component:
    - name = `endInstr`
    - save = nothing
    - duration = `<blank i.e. infinite>`
    - forceEndRoutine = `True`
    - allowedKeys = `<blank i.e. any keys>`

NB: make sure the duration is blank. If the keyboard stops being checked after 1 second then PsychoPy will never spot that the key has been pressed. The user will have to press Esc and quit the study.

Add a slide to say "thanks"
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

If an experiment suddenly ends after a trial but gives you no message people worry that they broke something.

Add a Routine like your `instructions` that says something like "Finished! Thanks for taking part."

There isn't much to read so you could just put the text up for 1 or 2 seconds and not bother using a keyboard to get rid of the message.

Changing your info dialog
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. image:: /_images/settingsExp128.png
    :align: left

In the Experiment Settings dialog you can alter the information you collect at the beginning, as well as a variety of other options.

We don't care(?) about the "session" number for the participant so we could remove that row.

**Do keep the `participant` setting** (it gets used by default in creating the data filename).

You could add a row for gender? Is there anything else you want to be kept alongside the data?

NB: The order of the entries doesn't matter (will be alphabetical anyway)

.. nextSlide::

.. image:: /_images/expSettingsFlanker.png
    :align: center


.. _data:

Data options
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The main file output is the trial-by-trial csv file (which opens in Excel).

**Don't** bother about `summarised` formats and Excel (native) files. They don't add information and can slow things down.

**Do** keep the `log` file and the `psydat` file. You might not need those but they're a safety net in case things go wrong.

The format of the filename can be changed but that's a little easy to break if you don't know what you're doing.

Analyse your data
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

When we run the experiment PsychoPy will create a folder called data next to the `.psyexp` file. That will contain 3 files for each run of the study:
    - log file (a text file). Lots of detail. Open in Excel or something like Notepad++
    - psydat file (for doing analyses in Python scripts)
    - csv file. For most analysis methods.

The csv file is a simple comma-separated text file. It can be opened in anything (R, SPSS, Excel...)

My computer is set to open this in Excel if I double-click

.. nextSlide::

Open your data file in Excel and *save as an Excel Workbook*. This means that:
    - Excel will not keep asking if you want to change the format
    - you can add things like graphs and formulae and they will get saved
    - if you mess up your analysis here the original file (csv) will still be there to go back to!

.. nextSlide::

Each row represents one trial, organised chronologically.

For this particular analysis all you would need to do is sort by whether the target/flankers were congruent (I told you that would be useful!) and then take the average reaction time of each type of trial.

The reaction time can be found in the resp.rt column. This measures the time (in secs) from the beginning of the keyboard being available (which we aligned with the stimulus onset).

That's it! One study created, run and analysed!

.. ifslides::

    .. create a slide for references here. For pdf these are collected and added to end
    .. nextSlide:: References

.. [Erikson] Eriksen, B. A., Eriksen, C. W. (1974). Effects of noise letters upon identification of a target letter in a non- search task. *Perception and Psychophysics* 16: 143–149



.. _dynamic:

Making things dynamic
---------------------------

What is dynamic?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

In PsychoPy everything is organised in reference to time

  - We don't have "slides" that simply follow each other like in some packages
  - Things overlap in time
  - Things can *change* their attributes in time

Why is that useful?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

You could use this, for instance, to:

  - gradually reveal an object
  - make an object move to make the task harder
  - make an object more interesting for participants (e.g. developmental)

    - rainbow text
    - throbbing heart

Code as arguments
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

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
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- Let's take some faces and make them shrink and rotate while participants try to detect the face.

- The psychological point of this isn't clear(!), but it used to be popular in quiz shows.

- "Have I got News For You" still does it.

..  _heartThrob:

Create a pulsating heart
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Download an image of a "love" heart, preferably one with a transparent background.

Let's put that into a PsychoPy experiment and set its size to vary on every frame.

.. image:: /_images/heart_red.png
    :align: center
    :scale: 10

Equation for a pulse
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

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
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Inside the examples zip file, look under::

  builder/dynamic

You'll find working examples of a range of these stimulus setups



.. _blockDesigns:

Block designs and counterbalancing
--------------------------------------

A block design is where we have sets of similar trials organised into blocks rather than having trials interleaved.

e.g.
  - a block of faces to recognise or a block of houses
  - a faces oriented correctly and faces inverted
  - a block of Stroop task in English and a block in French

The natural error
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The biggest error that people make with this is to create a Routine (and a loop) for each block of trials:

.. image:: /_images/flowBlocksWrong.png

Then they ask on the forum, "How do I shuffle the blocks on my Flow?"

That is the wrong way to think about it.


The right way
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Instead of a Routine for each block, create a Routine for all your trials and make it behave differently across the blocks:

.. image:: /_images/flowBlocksRight.png

Then you can set the conditions files in your blocks loop to control the block-level changes.

The outer "blocks" loop then takes a (meta) "conditions" file that specifies which of the conditions files will be loaded in each block.

Example: Multilingual Stroop
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Let's create the Stroop using blocks of French and english

We need to create a total of 3 conditions files:

  - french.xlsx
  - english.xlsx
  - blocks.xlsx

.. nextslide::

english.xlsx:

======  =============   =========== ===========
word    letterColour    congruent   corrAns
======  =============   =========== ===========
red     red             1           left
red     green           0           down
green   green           1           down
green   blue            0           right
blue    blue            1           right
blue    red             1           left
======  =============   =========== ===========

.. nextslide::

french.xlsx:

======  =============   =========== ===========
word    letterColour    congruent   corrAns
======  =============   =========== ===========
rouge   red             1           left
rouge   green           0           down
vert    green           1           down
vert    blue            0           right
bleu    blue            1           right
bleu    red             1           left
======  =============   =========== ===========

.. nextslide::

blocks.xlsx:

============  ========
conditions    label
============  ========
english.xlsx  English
french.xlsx   French
============  ========

The `label` variable isn't technically needed but it could be used to tell people what block they are about to enter. The point is that you can still use other variables here, defined at the block level of the program, just as in Method A.

.. nextslide::

Now we need to set up the variables inside our experiment:

  - the inner (trials) loop will have a conditions file = `$conditions` which is defined in the `blocks.xlsx` file
  - the outer (blocks) loop will have conditions file = `blocks.xlsx`

.. nextslide::

.. image:: /_images/blocksMethodB_blockLoop.png

.. nextslide::

We could also add a Routine called `blockReady` like an instructions Routine with:

  - a text object that says::

    $"Ready to start a block of %s words?\\n\\n Press a key when ready" %(label)

  - a keyboard object to advance to the next trial

.. image:: /_images/blocksMethodBFullFlow.png

.. nextslide:: Randomised block design complete!

You've sorted out block designs in a relatively neat fashion.

Just keep clear what differs from one block to the next (for a conditions file) and what stays the same (for the Routine definition).


.. _counterbalancedDesigns:

Counterbalancing
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Counterbalancing your blocks is really just an extension of the blocking scenario, except that you set the blocks to operate in a particular order rather than leaving PsychoPy to randomise them.
)

Setting the order
`````````````````````````````````````````

PsychoPy doesn't handle the ordering for you - you need to decide how to create the orders and how to assign participants.

Now, rather than a single file to specify the blocks you need one for each order that you want the blocks to appear in (and then set the blocks loop to be `sequential` rather than `random` to preserve the order you set)

For instance, the bilingual Stroop task you might have groupA with alternating languages, beginning with English, and the groupB participants might have the same but starting with French.

How to assign participants to a group
`````````````````````````````````````````

Easiest way is by hand at the start of the run for the participant. The steps are:

 - In Experiment Settings add a field for `group` (which will be A, B, C... for however many orders you need to create)
 - For the block loop use that value by calling `expInfo['group']` using one of the alternatives below:

  - `$"block" + expInfo['group'] + ".xlsx"`
  - `$"block{}.xlsx".format( expInfo['group'] )`

All done
~~~~~~~~~~~~~~~~~~

You can now create trials and blocks in any order, fixed or random.

You're in complete control (but you need to understand what orders you want!)

Next... :ref:`codeComponents`

