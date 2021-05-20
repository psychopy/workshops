
.. ifslides::

    .. image:: /_static/OST600.png
        :align: left
        :scale: 25 %
        
        
.. _pavloviaEnv:

The Pavlovia environment
=================================

What is PsychoJS?
----------------------------

When we make an experiment in PsychoPy builder, it is writing our experiment in Python code under the hood. Now it also writes our experiment to JavaScript via PsychoPy's sister library `PsychoJS <https://psychopy.github.io/psychojs/>`_.

.. image:: /_images/psychopy_pav_psychojs.png
    :align: center
    :scale: 25 %

.. nextSlide::

If you prefer to write experiments in pure code, you can write experiments purely in Javascript using PsychoJS, but in general it will be more flexible, less bug prone and easier to share with non-coders if you use Builder. 

What is Pavlovia?
----------------------------

Once we have our experiment written in JS, we need a way to "host" it online.  `Pavlovia <https://pavlovia.org/>`_. is a secure server for running experiments and storing data but it is also a good way to share your experiments publically with other researchers! Pavlovia is fully `GDPR complient <https://pavlovia.org/docs/home/ethics>`_.

.. ifslides::

    .. image:: /_images/psychopy_pav_psychojs.png
    :align: center
    :scale:50%

What is free, what costs and why? 
---------------------------------

There are many features that we can use for free in pavlovia such as :

*   Version control
*   Public sharing of experiments

But to support the ongoing development of PsychoPy (which has been developed for free for years by `dedicated contributors <https://github.com/psychopy/psychopy/graphs/contributors>`_) a `small cost <https://pavlovia.org/store>`_ is introduced for **storing data** from experiments you run.

Finding openly shared experiments
----------------------------------

There are two ways we can find and use existing experiments from Pavlovia:

*   From within pavlovia itself using the `explore <https://pavlovia.org/explore>`_ tab. 
*   From within PsychoPy itself using the search globe. 

Finding shared experiments from Pavlovia itself
-------------------------------------------------

In the  `explore <https://pavlovia.org/explore>`_. tab each experiment has it's own icon. You can choose to run the experiment (if it is set to running) or view the code :code:`<>`

.. image:: /_images/stroop_pavlovia.png
    :align: left
    :scale: 25 %

.. nextSlide::

We can then fork the experiment to our own "namespace" or a selected "gitlab group".

.. image:: /_images/fork_online.png
    :align: left

.. nextSlide::

Finally, we would use the search icon inside PsychoPy to search and sync:

.. image:: /_images/sync_local.png
    :align: left

Finding shared experiments from PsychoPy
-------------------------------------------------
Alternatively, we could just search from inside PsychoPy itself and "Fork +Sync" all at once

.. image:: /_images/fork_local.png
    :align: left

.. nextSlide::

Since the second method is easier than the first, you might wonder "why bother" with the first approach? 

*   You can avoid some errors by deleting the data folder from the forked project *before* you clone/sync it locally (Web IDE > ... > delete > commit)
*   Can be easier for use with groups (online you can fork to a group, locally the project will always be forked to your namespace)

.. _gitlabBrief:

Gitlab
--------------------------

Benefits of GitLab (the important bits):
 - Fork existing projects
 - Version control
 - Add lab members to projects to work on the same files
 - Easy sharing of your task (open science) 

Version control
--------------------------

.. image:: /_images/gitlabComHistory.png
    :align: center
    :scale: 70%

You can see when the last changes were made to the task by looking at the commit history.

.. nextSlide::


If you click on the change you can see deletions (in red) and insertions (in green)

.. image:: /_images/gitlabComChange.png
    :align: center

.. nextSlide::

You can browse the repository at that point in history:

.. image:: /_images/gitlabBrowse.png
    :align: center

Imagine you have a working task, you then make a bunch of changes, and it doesn't work. If you commit little and often you can easily revert those changes. 

Adding team members
--------------------------

To add members to your own project, you can use the settings>members option where you can search and invite collaborators.

.. image:: /_images/gitlabSettings.png
    :align: center

Making your task public
--------------------------

You can change the visibility of your task at any time under permissions. 

.. image:: /_images/gitlabPermissions.png
    :align: right

.. ifslides::
    .. nextSlide::

    One thing to note is that once you make your project "public" the data file stored there will also be public. 
        - good as allows easy data sharing
        - Something to bare in mind if you are collecting protected data

.. ifnotslides::
    .. note::
        Once you make your project "public" the data file stored there will also be public. 
            - good as allows easy data sharing
            - Something to bare in mind if you are collecting protected data


*Exercises (10-15 mins)*
--------------------------

Let's get some practice using pavlovia.org!

1. try forking a task you like (hint: those in the 'demos' group can be useful)
2. try searching that project from your local psychopy 
3. make a small edit 
4. upload and see if the change shows on gitlab!
5. add someone else in your breakout room as a team member

NB. don't forget to give stars to the projects you like! this could help future researchers picking tasks!


