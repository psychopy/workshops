.. _usingMouse:

Using mouse/touchscreen responses
===================================

Let's try and create a 'Feedback' Routine for the Posner task we want to:

- Add trial by trial feedback on response times 
- Adjust the color of the feedback based on RT
- Give feedback at the end on average RT overall, on valid trials and on invalid trials.

.. _mouseFeedback:

Feedback from a mouse
-----------------------------------

**Response time feedback from a mouse** 

In our Posner example, we are using mouse responses. So long as the data from the mouse is set to save *On Click* (see data tab) this will return several values we can use for feedback:

- :code:`mouse.time` the time(s) of the mouse click(s). 
- :code:`mouse.clicked_name` the name(s) of the last object clicked

.. nextslide::

Adding a text component and writing :code:`$mouse.time[-1]` in the text field would show the time of the last mouse click. 

.. nextslide::

**Accuracy feedback from a mouse** 

Imagine we wanted to check our participant had selected the correct object. We could add a column to our conditions file e.g. "corrClick" then use a code component to check if this was correct::

    if mouse.clicked_name[-1] == corrClick:
        correct = 1
        print('correct!')
    else:
        correct = 0
        print('incorrect')

Note that we use :code:`[-1]` to retrieve the last object/time that was clicked. 




