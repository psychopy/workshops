
.. ifslides::

    .. image:: /_static/OST600.png
        :align: left
        :scale: 25 %
        
        
.. _pavloviaEnv:

The Pavlovia environment and getting online
==============================================

What is PsychoJS?
----------------------------

When we make an experiment in PsychoPy builder, it is writing our experiment in Python code under the hood. Now it also writes our experiment to JavaScript via PsychoPy's sister library `PsychoJS <https://psychopy.github.io/psychojs/>`_.

.. image:: /_images/psychopy_js_pav.png

.. nextSlide::

If you prefer to write experiments in pure code, you can use Javascript using PsychoJS.

But, in general it will be faster, less bug prone and easier to share with non-coders if you use Builder. 

What is Pavlovia?
----------------------------

Once we have our experiment written in JS, we need a way to "host" it online.  `Pavlovia <https://pavlovia.org/>`_ is:

* A secure server for running experiments and storing data.
* A git based version control system.
* A huge open access library of experiments (that you can add to!)

What is our "Buisiness model"?
--------------------------------
We have a unique model to try and sustain open source software, whilst trying to be as low cost as possible.

.. image:: /_images/Buisiness_model.png
    :align: left

So.. how do we use pavlovia.org?
----------------------------------

We might want to use Pavlovia.org to:

* Find and reuse others studies
* Launch our own study in browser

Finding openly shared experiments
----------------------------------

There are two ways we can find and use existing experiments from Pavlovia:

*   From within pavlovia itself using the `explore <https://pavlovia.org/explore>`_ tab. 
*   From within PsychoPy itself using the search globe. 

.. nextSlide::

We could directly download an experiment on pavlovia.

.. image:: /_images/fork_online0.png
    :align: left


.. nextSlide::

Or we could search for that experiment and download it directly in PsychoPy:

.. image:: /_images/fork_local0.png
    :align: left

.. _pavloviaLaunch:

Syncing our own study to pavlovia
----------------------------------

If the task that you need doesn't already exist - push your own! Before you get started try to make sure you:

*    Have a fresh folder that contains only **one .psyexp file and the resources needed by that file**. 
*   It can also be helpful to make sure your folder is not in a location already under git version control. 

.. nextSlide::

Once you have made your experiment and made sure that your local folders are organized neatly ( **with one .psyexp file in this location**) you're ready to sync your project to pavlovia!. 

.. image:: /_images/sync_to_pav.png
    :align: left

.. nextSlide::

Once you have synced your study you will find it in your Dashboard on pavlovia.org under "Experiments". 

.. image:: /_images/experiment_dashboard.png
    :align: left

.. nextSlide::

*   *Piloting versus running* - piloting will produce a token that lets you run your study for free for one hour, a data file will automatically download so that you can inspect it. Running will generate a URL to share with participants - no data will be downloaded locally using that link.
*   *CSV or DATABASE* - csv will generate a csv file per participant that will be sent to your gitlab repository (so it will be public if you make the repo public). Database will append all participants data to a single file (it will not be sent to gitlab).

.. _additionalResources:

Configuring online settings
----------------------------

Inside the experiment settings of PsychoPy you can configure the online settings of your experiment. 

.. image:: /_images/online_tab.png
    :align: left

*Exercise (5-10 mins)*
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Let's quickly make a basic experiment and put it online:

1. Make a new .psyexp file with some text that simply reads "Hello, I'm online!"
2. Sync that experiment to pavlovia.org 
3. Go to your experiment dashboard to find your experiment 
4. Change your study to piloting and check that it runs by changing it to pilot mode and select "pilot".
5. Redirect your participant to PsychoPy.org when they have completed the task, redirect them to pavlovia.org if they do not complete the task.

Let's push our task online!
-------------------------------

Let's try putting the task we made in day 1 online and getting some data together!


.. _debuggingOnline:

Debugging online
=================================

Why do we need to debug?
----------------------------------

So your task was running perfectly offline, then you pushed it online, and it doesn't work - why? There are lot's of reasons something might not work online, but the most common errors are coding errors. 

Remember that locally PsychoPy runs a compiled python experiment. Online pavlovia runs your compiled *JavaScript* experiment which uses the `PsychoJS library <https://github.com/psychopy/psychojs>`_. 

.. nextSlide::

The PsychoJS library `doesn't yet contain everything in PsychoPy <https://www.psychopy.org/online/status.html>`_ , for several reasons:

*   Does a component "make sense" online? e.g. Grating stimuli ideally require a luminance calibrated monitor. Does your participant have a photometer at home? Input/Output components to connect with EEG might not make sense online either..
*   PsychoJS is younger than PsychoPy! (but we're making good progress!)

Transpiling 
----------------------------------

When we add code components we have the choice to add code as either:

*   *Py* - pure Python
*   *JS* - pure JavaScript
*   *Both* - Python and Javascript independently
*   *Auto -> JS* - automatically *transpile* python code to javascript. 

The last option is very cool and useful - but it can catch people out if something doesn't translate smoothly!

.. nextSlide::

General tips for getting online
----------------------------------

1. **Update to the latest release!** Version 2021.2. improved transpiling alot and you can save *alot* of manual debugging online using that version. 
2. Always check the status of online options `status of online options <https://www.psychopy.org/online/status.html>`_ *before* making your experiment
3. Push your experiment little and often (don't make your full experiment perfectly locally and then try to push it online)
4. Read the `crib sheet <https://discourse.psychopy.org/t/psychopy-python-to-javascript-crib-sheet/14601>`_
5. Check out the `psychoJS documentation <https://psychopy.github.io/psychojs/>`_


The `forum <discourse.psychopy.org>`_ is always there!

.. _commonErrors:

Common errors
====================

There are several kinds of error we might encounter when getting online, but generally these fall in three categories (you can find a useful `tutorial here <https://gitlab.pavlovia.org/tpronk/assignment_stroop>`_)

.. _syntaxErrors:

Syntax errors: Initializing experiment
------------------------------------------

The experiment is stuck on an "initializing experiment" screen. This usually means that there is some invalid Javascript written - so the experiment code cannot run at all. For this we need to explore the :ref:`developerTools`

.. _semanticErrors:

Semantic errors: X is not defined
------------------------------------

"ReferenceError: X is not defined"

This means that you are referencing a variable that is not yet defined in your Javascript. There are several reasons this could occur...

.. nextSlide::

**Using python modules** 

Semantic errors commonly happen when researchers try to use python libraries or functions that don't exist in Javascript e.g. *"np is not defined"* We recommend taking a look at the `crib sheet <https://discourse.psychopy.org/t/psychopy-python-to-javascript-crib-sheet/14601>`_ in cases like this that need manually translating. Here, there is a handy list of python terms and there equivalent JavaScript term (A huge credit to `Wakefield Morys-Carter <https://uk.linkedin.com/in/wakecarter>`_ for compiling this). 

.. nextSlide::

**Declaring variables**

This is a rarer one, but handy to know about. Another reason a semantic error could occur is if you have created a variable in a loop, and PsychoPy hasn't "caught" that variable to declare it in JavaScript. An easy way to avoid this it to also declare that variable outside of the loop::

    thisVariable = 0
    
    things = [1, 2, 3]
    for thing in things:
        if thing == 2:
            thisVariable = 'FOUND NUMBER 2'


.. _networkErrors:

Network errors: Unknown Resource
----------------------------------

Generally PsychoPy will try to find all the resources you need automatically and load them, but there are some cases this might not work..

.. nextSlide::

**Incorrect file extension**

Your image is a ".jpeg" but you have accidentally used the extension ".png"

.. nextSlide::

**Resources defined through code**

If a resource is defined through code rather than from a conditions file or component field then PsychoPy can fail to "prepare" for the eventuality that resource is needed. In cases like this it is always a good idea to manually add any additional resources you might need to the *additional resources* section of the experiment settings when :ref:`additionalResources`. 

.. _typeError:

Type Error: X is not a constructor
-----------------------------------

A `type error <https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Errors/Not_a_constructor>`_ occurs when we refer to an object that does not exist.

This can also occur because something exists in PsychoPy that does not exist in PsychoJS. For example :code:`core.Clock()` is not a constructor in JS because Clock lives in the util module of PsychoJS i.e. :code:`util.Clock()`. The `crib sheet <https://discourse.psychopy.org/t/psychopy-python-to-javascript-crib-sheet/14601>`_ can be helpful in helping in these cases. 

How do we fix errors? 
----------------------------------

Let's find out...

.. _developerTools:

Developers console
----------------------------------

This is the equivalent to your "StdOut" window in runner view. In fact, it's alot more than that - it's a shell where you can type and try out bits of JavaScript. You can access developer tools in most browsers by right clicking the browser and selecting "inspect" then clicking console. 

*For faster access look up the keyboard shortcut for your specific operating system/browser!*

Finding errors: Developer tools
-------------------------------

The developer tools are particularly helpful for :ref:`syntaxErrors`, where there is no error message, but things "don't work".

.. image:: /_images/initialisingScreen.png
    :align: center

.. nextSlide::

You can open developer tools in your browser (the `crib sheet <https://discourse.psychopy.org/t/psychopy-python-to-javascript-crib-sheet/14601>`_) gives tips how to do this on different browsers/operating systems)
This will tell us where our (which line) error is occurring. Remember, exporting to code is a one-way street. So whilst it is useful to look into the code, we *really* recommend fixing errors back in builder where possible. 

.. image:: /_images/developerTools.png
    :align: center

.. nextSlide::

If you are ever unsure where to look in your builder experiment for an error, you can look for the line that indicates what routine this code is being executed in. 

.. image:: /_images/navigate_console_error.png

Clearing your browser cache
----------------------------------

If you ever make a change in your experiment and it isn't reflected in your online experiment, it is very likely you need to clear your browser cache. How this is done can vary browser to browser - so do search how to do that on your specific operating system/browser.

*Exercise 15-20 mins*
----------------------------------

Think Escape room, but with bugs...

I am going to give you an experiment with 4 levels, each level contains a bug. Use the skills that we have learnt to find each bug and progress to the next level. 

To start fork or download `this experiment <https://gitlab.pavlovia.org/Hirst/buggy_breakout>`_.

.. image:: /_images/lock.png


Useful JavaScript commands for debugging
-----------------------------------------

- :code:`console.log()`: The equivalent of :code:`print()` in python. Useful for when a variable doesn't appear as you expect - you can print out values to your console and check they are updating as you expect. 
- :code:`window.object = object`: pass an object to the window for inspection e.g. pass a component by replacing :code:`object` with the name of your component. Useful for seeing what attributes and methods an object has.

Useful JavaScript commands for other tricks
--------------------------------------------

- :code:`window.open('myURL')`: open a new window e.g. a questionnaire (note: can be blocked as a pop up by some mac users).
- :code:`alert()` Add a pop-up alert to the participant. 
- :code:`prompt('Please enter your name', 'default')` retrieve some info from the participant `via a pop-up <https://www.w3schools.com/jsref/met_win_prompt.asp>`_
- :code:`confirm('Please click OK!')` Display a pop-up box with OK or cancel.

.. note::
    If you are running your study in full screen mode these will break into window mode*

Want to explore JavaScript and PsychoJS?
------------------------------------------

Remember that you can always export your experiment to it's underlying JavaScript code as well, this can be useful in learning how some things are defined differently in PsychoPy versus PsychoJS, and finding variables that will exist "under the hood of your experiment. For example :code:`expInfo['OS']` and :code:`expInfo['frameRate']` might be useful for checking the participants Operating system or screen refresh rate.

.. note::
    Remember that this is a one-way street! don't be tempted to alter the JS code if you want to continue making edits in builder! implement code from within builder itself!*

.. _gitlabBrief:

Gitlab
=================================

Pavlovia uses a powerful git-based system for storage and version control. Some of the benefits of using this include:

*   Fork existing projects
*   Version control
*   Easy sharing of your task (open science) 
*   Add lab members to projects

Version control
--------------------------

Pavlovia uses a git based system for version control called "gitlab". You can see when the last changes were made to the task by looking at the commit history.

.. only:: html
    .. image:: /_gifs/git_control.gif
        :align: center
        :scale: 100%

.. only:: latex
    .. image:: /_gifs/git_control.png
        :align: center
        :scale: 100%

.. nextSlide::


If you click on the change you can see deletions and insertions. You can browse the repository at that point in history to retrieve past files!


.. image:: /_images/gitlabComChange0.png
    :align: center
    :scale: 70%


.. image:: /_images/gitlabBrowse0.png
    :align: center
    :scale: 50%


Adding team members
--------------------------

To add members to your own project, you can use the settings>members option where you can search and invite collaborators.

.. only:: html
    .. image:: /_gifs/add_member.gif
        :align: center

.. only:: latex
    .. image:: /_gifs/add_member.png
        :align: center

Making your task public
--------------------------

You can change the visibility of your task at any time under permissions. **Remember** Once you make your project "public" the data file stored there will also be public (unless you have your data saving mode set to database). 

.. only:: html
    .. image:: /_gifs/gitlab_privacy.gif
        :align: center

.. only:: latex
    .. image:: /_gifs/gitlab_privacy.png
        :align: center

Making suggested edits to a shared project
----------------------------------------------
A handy thing is that if you fork a project and edit *your own version of that project* you can later make a merge request to the original project to suggest changes, this can be handy if you are working as a team on the same experiment.


*Exercises (10-15 mins)*
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Let's get some practice using gitlab!

1. One person in your breakout room set their "Hello, I'm online!" example to public.
2. Another person in your breakout room find that task and fork + sync it so that you have it locally.
3. Make a small edit to that task and sync the change.
4. Pilot your newly updated task to check you can see the edit.
5. Add someone different in your room as a team member to your project.

NB. don't forget to give stars to the projects you like! this could help future researchers picking tasks!


.. _counterbalancingOnline:

Counterbalancing online
=========================

When we take a study online, it is often important to automate group assignment in some way. At the moment, Pavlovia does not have an "out-of-box" solution for this - but there are several ways to approach this.

The common error
-------------------

Quite often, researchers think that if they have several groups they will need several Pavlovia projects (one per group). This is often inefficient and can become quite confusing when collating the data. Instead, we can make a single experiment and start by using the principles we learned in :ref:`blockDesigns`.

.. _queryStrings:

Query strings
-------------------

When sharing a study with a participant, we can auto-complete fields in the startup GUI using `query strings <https://en.wikipedia.org/wiki/Query_string>`_. You can provide info to your experiment by appending your experiment URL with :code:`?participant=1&group=A` - where "participant" and "group" correspond to parameter names. 

.. nextSlide::

There is no limit on the number of parameter names that you provide, so long as each parameter is separated by an ampersand (:code:`&`)

.. image:: /_images/queryStrings.png

.. nextSlide::

Thanks to query strings we can generate several URLs for the same project but for each group. For example, you might have 4 groups and therefore share the URLs:

* https://run.pavlovia.org/Username/Task/?group=A
* https://run.pavlovia.org/Username/Task/?group=B
* https://run.pavlovia.org/Username/Task/?group=C
* https://run.pavlovia.org/Username/Task/?group=D

.. warning::
    If you are using this approach and sharing URLs on recruitment websites, you would need to be careful that the same participants do not complete several URLs (i.e. complete your study several times in different groups). If you are using `Prolific <https://prolific.co/>`_ for recruitment there is guidance on how to do this `here <https://researcher-help.prolific.co/hc/en-gb/articles/360009094374>`_.

Query strings: Using participant ID
------------------------------------

A slightly more efficient way might be to generate sequential participant IDs and use that to assign to groups. For this, Wakefield Morys-Carter has developed an `external app <https://moryscarter.com/vespr/pavlovia.php>`_ (Morys-Carter, 2021) to assist. 

So, If your experiment URL is *https://pavlovia.org/a/b* then use *https://moryscarter.com/vespr/pavlovia.php?folder=a&experiment=b/*

.. nextSlide::

Inside PsychoPy, we could then use the code component::

    if int(expInfo['participant']) % 2 == 0:
        expInfo['group'] = A # Assigns even ID's to group A 
    else:
        expInfo['group'] = B

We then would not need the parameter "group" in our experiment settings (because this parameter assignment through code would overwrite it anyway).

More than two groups online
------------------------------------

Counterbalancing with more than 2 groups online is a little more complex. We can use the sequential participant ID method but we need to be more careful. If we had **40 participants**, in python, we could write::

    # Makes a long list of length 4 * 10
    groups = ['A', 'B', C', 'D'] * 10
    # if python index starts at 0 but participant ID starts at 1 the first element 
    # will be skipped, so add a value to compensate
    groups.append('A')
    # use the participant ID to index from this list
    expInfo['group'] = groups[int(expInfo['participant'])]

*Problem*, the method of list extension used to make the groups list does not translate to JavaScript (as outlined in the `crib sheet <https://discourse.psychopy.org/t/psychopy-python-to-javascript-crib-sheet/14601>`_).

.. nextSlide::

For this reason we would need to change Code Type to "Both" and use the following on the JavaScript side::

    # Makes a long list of length 4 * 10
    groups = Array(10).fill(['A', 'B', 'C', 'D']).flat();
    # if  index starts at 0 but participant ID starts at 1 the first element 
    # will be skipped, so add a value to compensate
    groups.push('A');
    # use the participant ID to index from this list
    thisGroup = groups[Number.parseInt(expInfo["participant"])];
    expInfo["Group"] = thisGroup;

.. nextSlide::

Remember, we could sanity check that this is working using::
    console.log('Group: ', expInfo['group'])

The Study Portal
------------------------------------

*Problem* The tool described so far is great and is free, but it does not take into account how many participants *completed*. So, it is still important to manually check how many complete data sets you have for each group.

We do hope to have an out-of-box solution to this in future, but we are very grateful for alternative solutions contributed by the community. In particular, Wakefield Morys-Carter has developed a `Study Portal <https://moryscarter.com/vespr/portal/>`_ to help group counterbalancing. Taking into account participant completion is a paid feature, but at a low cost (£10).

.. warning::
    If you are using the licensed features of the Study Portal to assign participants to group - do not use code within your experiment to assign group based on participant ID. 

.. nextSlide::

This allows tracking of how many participants from each group have completed and how many timed out: 

.. image:: /_images/studyPortalGroups.png

.. nextSlide::

Other features the Study Portal could help with:

*   Anonymous withdrawal
*   Consent/debrief forms

You can watch a presentation of the portal `here <https://youtu.be/qFSGuZoVzaI>`_.

Useful tools
-------------------
There are several other tools that can be useful including:

- Counterbalancing online using `sequential participant IDs <https://moryscarter.com/vespr/pavlovia.php>`_ 

- `Scaling your screen <https://pavlovia.org/Wake/screenscale>`_ (e.g. so that we can use cm units online).

- `Headphone checkers using huggins pitch <https://github.com/ChaitLabUCL/HeadphoneCheck_Test>`_ 

- `Embedding html forms <https://discourse.psychopy.org/t/new-web-app-form-to-html-for-pavlovia/22626>`_.

- `Eyetracking online <https://workshops.psychopy.org/3days/day2/advancedOnline.html>`_ using the webgazer library. **Note that in 2021.2.2 there is a different way of loading resources** 

Next up!
-----------------

Let's practice debugging errors, then play with advanced plugins we can use online ( :ref:`advancedOnline`).

Then we will try :ref:`firstExperiment`.

References
----------
Morys-Carter, W.L. (2021, April 26). Participant IDs for Pavlovia. VESPR. https://moryscarter.com/vespr/pavlovia.php.
