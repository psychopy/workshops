.. ifslides::

    .. image:: /_static/OST600.png
        :align: left
        :scale: 25 %


.. _online:

Running online studies
=================================

So now we have a very simple experiment that works locally, let's see how we would get that online. 

Before we take our study online it is important for us to understand a bit about how PsychoPy generates an experiment that can be read by your browser (using PsychoJS) as well as how we can host the study online (using pavlovia.org)


What is PsychoJS?
----------------------------

When we make an experiment in PsychoPy builder, it is writing our experiment in Python code under the hood. Now it also writes our experiment to JavaScript via PsychoPy's sister library `PsychoJS <https://psychopy.github.io/psychojs/>`_.

.. image:: ../_images/psychopy_pav_psychojs.png
    :align: center
    :scale: 25 %

.. nextSlide::

If you prefer to write experiments in pure code, you can use Javascript using PsychoJS.

But, in general it will be faster, less bug prone and easier to share with non-coders if you use Builder. 

What is Pavlovia?
----------------------------

Once we have our experiment written in JS, we need a way to "host" it online.  `Pavlovia <https://pavlovia.org/>`_ is:

* A secure server for running experiments and storing data.
* A gitbased version control system.
* A huge open access library of experiments (that you can add to!)



Launching your studies on Pavlovia
=================================

Syncing our own study to pavlovia
----------------------------------

If the task that you need doesn't already exist - push your own! Before you get started try to make sure you:

*    Have a fresh folder that contains only **one .psyexp file and the resources needed by that file**. 
*   It can also be helpful to make sure your folder is not in a location already under git version control. 

.. nextSlide::

Once you have made your experiment and made sure that your local folders are organised neatly ( **with one .psyexp file in this location**) you're ready to sync your project to pavlovia!. 

.. image:: ../_images/sync_to_pav.png
    :align: left

.. nextSlide::

Once you have synced your study you will find it in your Dashboard on pavlovia.org under "Experiments". 

.. image:: ../_images/experiment_dashboard.png
    :align: left

.. nextSlide::

*   *Piloting versus running* - piloting will produce a token that lets you run your study for free for one hour, a data file will automatically download so that you can inspect it. Running will generate a URL to share with participants - no data will be downloaded locally using that link.
*   *CSV or DATABASE* - cav will generate a csv file per participant that will be sent to your gitlab repository (so it will be public if you make the repo public). Database will append all participants data to a single file (it will not be sent to gitlab).


.. nextSlide::

Inside the experiment settings of PsychoPy you can configure the online settings of your experiment. 

.. image:: ../_images/online_tab.png
    :align: left


The Pavlovia environment
=================================

Finding openly shared experiments
----------------------------------

There are two ways we can find and use existing experiments from Pavlovia:

*   From within pavlovia itself using the `explore <https://pavlovia.org/explore>`_ tab. 
*   From within PsychoPy itself using the search globe. 


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

Gitlab
--------------------------

Benefits of GitLab (the important bits):
 - Fork existing projects
 - Version control
 - Add lab members to projects to work on the same files
 - Easy sharing of your task (open science) 


Making your task public
--------------------------

You can change the visibility of your task at any time under permissions. 

.. image:: ../_images/gitlabPermissions.png
    :align: center


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


OK what next?
----------------------------------

So we have created a basic experiment, pushed it online and learnt about how we could share it. 

But what if we want something more complex?

Let's talk about some other types of responses we can get and how these can make our experiment more flexible.

:ref:`blockDesigns`

:ref:`codeComponents`

:ref:`mouse`

:ref:`typedResponses`