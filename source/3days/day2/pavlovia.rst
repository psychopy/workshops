
.. ifslides::

    .. image:: /_static/OST600.png
        :align: left
        :scale: 25 %
        
        
.. _pavloviaEnv:

The Pavlovia environment and getting online
=================================

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
* A gitbased version control system.
* A huge open access library of experiments (that you can add to!)

Finding openly shared experiments
----------------------------------

There are two ways we can find and use existing experiments from Pavlovia:

*   From within pavlovia itself using the `explore <https://pavlovia.org/explore>`_ tab. 
*   From within PsychoPy itself using the search globe. 

.. nextSlide::

We could directly fork an experiment on pavlovia.

.. image:: /_images/fork_online0.png
    :align: left

.. nextSlide::

Then, search for that inside PsychoPy and sync it to our desktop. We could actually fork + sync in PsychoPy itself!

.. image:: /_images/fork_local0.png
    :align: left

.. nextSlide::

*Side Tip*

Why might we fork inside pavlovia instead of using fork + sync in PsychoPy? Isn't this more work? 

*   You can avoid some errors by deleting the data folder from the forked project *before* you clone/sync it locally (Web IDE > ... > delete > commit)
*   Can be easier for use with groups (online you can fork to a group, locally the project will always be forked to your namespace)

Syncing our own study to pavlovia
----------------------------------

If the task that you need doesn't already exist - push your own! Before you get started try to make sure you:

*    Have a fresh folder that contains only **one .psyexp file and the resources needed by that file**. 
*   It can also be helpful to make sure your folder is not in a location already under git version control. 

.. nextSlide::

Once you have made your experiment and made sure that your local folders are organised neatly ( **with one .psyexp file in this location**) you're ready to sync your project to pavlovia!. 

.. image:: /_images/sync_to_pav.png
    :align: left

.. nextSlide::

Once you have synced your study you will find it in your Dashboard on pavlovia.org under "Experiments". 

.. image:: /_images/experiment_dashboard.png
    :align: left

.. nextSlide::

*   *Piloting versus running* - piloting will produce a token that lets you run your study for free for one hour, a data file will automatically download so that you can inspect it. Running will generate a URL to share with participants - no data will be downloaded locally using that link.
*   *CSV or DATABASE* - csv will generate a csv file per participant that will be sent to your gitlab repository (so it will be public if you make the repo public). Database will append all participants data to a single file (it will not be sent to gitlab).


.. nextSlide::

Inside the experiment settings of PsychoPy you can configure the online settings of your experiment. 

.. image:: /_images/online_tab.png
    :align: left

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

Pavlovia uses a git based system for version conrol called "gitlab". You can see when the last changes were made to the task by looking at the commit history.

.. image:: /_gifs/git_control.gif
    :align: center
    :scale: 100%


.. nextSlide::


If you click on the change you can see deletions and insertions. You can browse the repository at that point in history to retrieve past files!

.. image:: /_images/gitlabComChange0.png
    :align: cener
    :scale:70%

.. image:: /_images/gitlabBrowse0.png
    :align: center
    :scale:50%

Adding team members
--------------------------

To add members to your own project, you can use the settings>members option where you can search and invite collaborators.

.. image:: /_gifs/add_member.gif
    :align: center

Making your task public
--------------------------

You can change the visibility of your task at any time under permissions. **Remember** Once you make your project "public" the data file stored there will also be public. 

.. image:: /_gifs/gitlab_privacy.gif
    :align: center

.. nextSlide::


*Exercises (10-15 mins)*
--------------------------

Let's get some practice using pavlovia.org!

1. try forking a task you like (hint: those in the 'demos' group can be useful)
2. try searching that project from your local psychopy 
3. make a small edit 
4. upload and see if the change shows on gitlab!
5. add someone else in your breakout room as a team member

NB. don't forget to give stars to the projects you like! this could help future researchers picking tasks!


