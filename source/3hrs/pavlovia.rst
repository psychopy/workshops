
.. ifslides::

    .. image:: /_static/OST600.png
        :align: left
        :scale: 25 %
        
        
.. _pavloviaEnv3Hrs:

The Pavlovia environment
=================================

The Pavlovia environment
~~~~~~~~~~~~~~~~~~~~~~~~

Pavlovia is:

- A secure server to launch and run experiments
- An experiment repository

Pavlovia and the library used to run experiments in browser (PsychoJS) are relatively young (2018) - this means minor changes may occur as we develop and improve the platform (e.g. recently given option to not save incomplete data)


Pavlovia: Docs
-----------------

Here we can find important information that might be needed for ethics applications, documents on how to use the site ("Experiments") and info on credits and licensing.

.. image:: /_images/pavloviaEthics.png
    :align: right

Dashboard and Experiment pages
-------------------------------

This is where you will probably spend most of your time. You can view your experiments, check if you have credits etc. 

.. image:: /_images/pavloviaDashboard.png
    :align: right

.. nextSlide::

By clicking on one of your experiments, you can see the details of that project, set the state of your experiment and access the data. 

.. image:: /_images/pavloviaStatus.png
    :align: right

.. nextSlide::

You can save your output as .csv files or a database (data bases will not be shown on your gitlab page). You can also decide if you want to save incomplete results or not. 

.. image:: /_images/pavloviaSaving.png
    :align: right

Explore
-----------------

Here you can browse existing experiments. Try searching for an experiment in your field!

.. image:: /_images/pavloviaExplore.png
    :align: right
 

.. _gitlabBrief:

Gitlab
-----------------

Benefits of GitLab (the important bits):

- Version control
- Add lab members to projects to work on the same files
- Easy sharing of your task (open science)
- Others can fork, use and develop your task (more citations?)

Gitlab: version control
------------------------

You can see when the last changes were made to the task by looking at the commit history and see deletions (in red) and insertions (in green)

.. image:: /_images/gitlabComChange.png
    :align: right

Forking
-----------------

If you find an existing experiment you like you can make yourself a copy by forking, either locally from PsychoPy or online. 

To fork locally select the 'search' icon in builderview, search the project you want and select 'sync+fork'

.. nextSlide::

To fork online. From pavlovia, open the gitlab page by selecting 'View code (<>)'.

You can then fork that to make your own copy of the project and copy it to your 'namespace' or group. 

If you really like the task, give the original poster a star too!!

Gitlab: adding team members
----------------------------

You can either add members to a single project, or you can create a group where you can share several projects

To add members to your own project, you can use the settings > members option where you can search and invite collaborators.

.. image:: /_images/gitlabSettings.png
    :align: right


Gitlab: making your task public
---------------------------------

You can change the visibility of your task at any time under permissions. 

.. image:: /_images/gitlabPermissions.png
    :align: right

NB: once you make your project "public" the data file stored there will also be public. 
    - good as allows easy data sharing
    - Something to bare in mind if you are collecting protected data


OK what next?
-----------------

So we have created a basic experiment, pushed it online and learnt about how we could share it. 

But what if we want something more complex?

Let's talk about some other types of responses we can get and how these can make our experiment more flexible.

:ref:`mouse`

:ref:`typedResponses`
