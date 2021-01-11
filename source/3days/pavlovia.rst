
.. ifslides::

    .. image:: /_static/OST600.png
        :align: left
        :scale: 25 %
        
        
.. _pavloviaEnv:

The Pavlovia environment
=================================

The Pavlovia environment
----------------------------

.. image:: /_images/pavlovia.png
	:align: center

.. slide:: Overview

    * :ref:`pavloviaInterface`
    * :ref:`pavloviaDocs`
    * :ref:`pavloviaExplore`
    * :ref:`gitlabBrief`
    * :ref:`pavloviaDashboard`
    * :ref:`pavloviaExpPage`

.. _pavloviaInterface:

The Pavlovia environment
----------------------------

Pavlovia is:

- A secure server to launch and run experiments
- An experiment repository

Pavlovia and the library used to run experiments in browser (PsychoJS) are relatively young (2018) - this means minor changes may occur as we develop and improve the platform (e.g. recently given option to not save incomplete data)


.. _pavloviaDocs:

Pavlovia: Docs
----------------------------

To learn more about Pavlovia we can use the 'Docs' tab.

.. image:: /_images/pavloviaTabs.png
    :align: right

.. nextSlide::

Here we can find important information that might be needed for ethics applications, documents on how to use the site ("Experiments") and info on credits and licensing.

.. image:: /_images/pavloviaEthics.png
    :align: right

.. nextSlide::

PsychoPy is free. Using Pavlovia to share studies is free. Collecting data through pavlovia has a small cost (relative to commercial competitors). This cost is to ensure the sustainability of PsychoPy. 

.. image:: /_images/pavloviaPrices.png
    :align: right

.. nextSlide::

You can buy credits or site licences in the "Store" tab. Pavlovia accounts are free and you can pilot experiments for free. 

.. image:: /_images/pavloviaStore.png
    :align: right

.. _pavloviaExplore:

Pavlovia: Explore
----------------------------

Here you can browse existing experiments. Try searching for an experiment in your field!

.. image:: /_images/pavloviaExplore.png
    :align: right

.. nextSlide::

You can search a task, see what state it is currently in (Inactive, piloting or running), and either launch the task or take a look at the code, by clicking on the <> symbol. 

.. image:: /_images/pavloviaSearch.png
    :align: right

.. note::
    Pavlovia is another good place to start if you are looking to create a task that might already exist (in addition to the demos in PsychoPy!).

.. _gitlabBrief:

Gitlab
--------------------------

Viewing the code will take you to "gitlab". This allows similar features to GitHub (if you want them).

.. image:: /_images/gitlabPosner.png
    :align: right

.. nextSlide::

Benefits of GitLab (the important bits):
 - Fork existing projects
 - Version control
 - Add lab members to projects to work on the same files
 - Easy sharing of your task (open science)


Forking
````````````````````````````

If you find an experiment you like using 'explore' you can open the gitlab page by selecting 'View code (<>)'

You can then fork that to make your own copy of the project to work from (you can make a copy for your own 'namespace' or add it to a group). 

If you really like the task, give the original poster a star too!! 

Version control
````````````````````````````

You can see when the last changes were made to the task by looking at the commit history

.. image:: /_images/gitlabComHistory.png
    :align: right

.. nextSlide::

If you click on the change you can see deletions (in red) and insertions (in green)

.. image:: /_images/gitlabComChange.png
    :align: right

.. nextSlide::

You can browse the repository at that point in history:

.. image:: /_images/gitlabBrowse.png
    :align: right

Imagine you have a working task, you then make a bunch of changes, and it doesn't work. If you commit little and often you can easily revert those changes. 

Adding team members
````````````````````````````

To add members to your own project, you can use the settings>members option where you can search and invite collaborators.

.. image:: /_images/gitlabSettings.png
    :align: right

.. note::
    You can also make 'groups' inside gitlab

Making your task public
````````````````````````````

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
`````````````````````````

Let's get some practice using pavlovia.org!

1. in your breakout room make a group for you to share something. 
2. try forking a task you like (hint: those in the 'demos' group can be useful)
3. try searching that project from your local psychopy 
4. make a small edit 
5. upload and see if the change shows on gitlab!

NB. don't forget to give stars to the projects you like! this could help future researchers picking tasks!

.. _builderToPavlovia:

Launching your studies on Pavlovia
=================================

Launching studies on pavlovia
-----------------------------

To load the task to pavlovia.org we can either use the "run online" or the "sync to pavlovia" icons. The former will then try to run our task in the browser. For now let's use sync. 

.. image:: /_images/syncWithPav.png
    :align: right

.. nextSlide::

Next we create a pavlovia project, select what group we load the project to and add details on the task.

.. image:: /_images/pavCreateProject.png
    :align: right


.. nextSlide::

If we then go to our Experiments in the pavlovia Dashboard, we should see our task uploaded. We can see that currently it is inactive, change the status to pilot and then click "pilot" next to the View code option. 


.. _pavloviaDashboard:

Pavlovia: Dashboard
-----------------

This is where you can view your experiments, check if you have credits etc. 

.. image:: /_images/pavloviaDashboard.png
    :align: right

.. _pavloviaExpPage:

Pavlovia: Dashboard: Experiment page
-----------------

By clicking on one of your experiments, you can see the details of that project, set the state of your experiment and access the data. 

.. image:: /_images/pavloviaStatus.png
    :align: right

.. nextSlide::

Set to "Piloting" and click "Pilot".
     - you can share that URL for 1hr to try the task.
     - you will get a pilot .csv data file.

.. image:: /_images/pavloviaPilot.png
    :align: right

.. nextSlide::

Setting your task to "Running" will create a URL under the "recruitment" tab which will allow you to share and run the task!

.. image:: /_images/pavloviaRunning.png
    :align: right


.. nextSlide::

You can save your output as .csv files or a database. You can also decide if you want to save incomplete results or not. 

.. image:: /_images/pavloviaSaving.png
    :align: right


.. nextSlide::

In reality, things may not always translate online smoothly (but we are working on it!).Let's talk about how to get online confidently and some tips for translating experiments online in :ref:`debuggingOnline`
