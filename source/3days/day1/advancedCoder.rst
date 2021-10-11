..under development

Code Components - Advanced
==================================

Go and open the demo called 'BART', the Balloon Analog Risk Task. That requires lots of code:

- what is the current size of the balloon?
- did the participant press the 'pump' key?
- did we exceed our maxPumps for this balloon?
- ...

First, everyone have a run through of this demo to familiarize yourself with the task. 

.. nextslide::

OK let's talk through the existing code components and the files in this demo. Then we are going to try some excercises to combine all of the skills we have learnt so far.

Exercises (20-30 minutes)
----------------------------------

1. Make the colour of the balloon change on every trial (either green or blue)
2. Add a new condition, where blue balloons have a high risk of popping early, whilst green balloons do not. 
3. Allow the researcher to assign participants to either group A or B - where group A will have the standard condition first, followed by block where colour predicts pop timing, and group B vice versa.
4. Set the colour of the baloon to be red if we are within 10 pumps of max pumps. 
5. Add a penalty - you loose earnings if the baloon pops..

Code Components - Advanced
----------------------------------

Sometimes you might want to end a routine or loop early if a certain condition is met. For example if a level of accuracy or a time limit has been reached. To do this we can use::

    continueRoutine = False # ends a routine
    trials.finished = True # ends the loop (trials = name of loop)

.. nextslide::

Make a simple routine with a text component that lasts 0.5 seconds add a loop to repeat that 5 times. 

Try accessing the properties of your loop object - see 'finished' is in the list. 
There is also some properties we see in our outputfile (e.g. thisN).

Let's try ending the routine at trial 3 instead of trial 5...
What happend if you do or do not use continueRoutine? 


.. note::

	Sometimes you might want to set the properties of multiple components at once. For this we could use a for loop (we will talk more about these on Friday)

Exercises (15-20 minutes)
-------------------------------------------------------
Painting shapes...

1. present 4 white polygons (circles, triangle, rectangle)
2. add a mouse component to click the polygons
3. if a polygon is clicked, set it's colour to green