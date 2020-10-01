
.. _builderToPavlovia:

Launching your studies on Pavlovia
=================================

The plan
-----------------

Today we are going to practice what we learnt in builder, but focus on getting online. 

We are going to make a new task - an asteroid blast game (AKA response time task). 


Make your builder file
-----------------
Make a folder called "targetHitTask", open builder view and save the file in our folder. 


Add a stimulus
-----------------

Download an image you want (preferably with a transparent background e.g. .png) and save it as 'targetIm'.

.. nextSlide::

Exercise: 

On each trial we will present our image. We want to present our image in a different location on each trial. How do we do that?

.. nextSlide::

Answer:

We create a conditions file containing the desired X and Y coordinates on each trial, and set our stimulus position to update. 

.. image:: /_images/targetImSettings.png
    :align: right

Gather a response
-----------------

Exercise: 

On each trial, we want to gather responses from the mouse.

The participant should only be able to click the target.

The image should stay on the screen untill clicked.

.. nextSlide::

Answer:

	- add a mouse component
		- duration: infinate (blank)
		- end routine: "valid click"
		- clickable stimuli: "targetIm"
	- set the duration field of our image to be empty (infinate)

.. nextSlide::

On a tablet, mouse clicks are translated to screen touches. 

.. image:: /_images/mouseProperties1.png
    :align: right

Add more routines
-----------------

Add some instructions and a thank-you message - then let's get this online!

NB: when deciding what kind of response to use to end a routine (e.g. instructions) remember this is going online, and not all devices have keyboards...

Push it online
-----------------

To load the task to pavlovia.org we can either use the "run online" or the "sync to pavlovia" icons. The former will then try to run our task in the browser. For now let's use sync. 

.. image:: /_images/syncWithPav.png
    :align: right

.. nextSlide::

Next we create a pavlovia project, select what group we load the project to and add details on the task.

.. image:: /_images/pavCreateProject.png
    :align: right


.. nextSlide::

If we then go to our Experiments in the pavlovia Dashboard, we should see our task uploaded. We can see that currently it is inactive, change the status to pilot and then click "pilot" next to the View code option. 

.. nextSlide::

There we have it! our first basic task in pavlovia!! 

In reality, things are not always smooth. Next we will build on this task to cover some tips in :ref:`debuggingOnline`