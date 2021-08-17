.. _addingFeedback:

Adding feedback
===============================

Adding feedback
-------------------------------

Let's try and create a 'Feedback' Routine for the Posner task we want to:

- Add trial by trial feedback on response times 
- Adjust the colour of the feedback based on RT
- Give feedback at the end on average RT overall, on valid trials and on invalid trials.

What can we give feedback on?
-------------------------------

We can explore the variables available to us by examining the data output of our experiment. If we used a mouse component for example, we can see that there is usually: 

*   :code:`mouse.time` - the time(s) of the mouse click(s)
*   :code:`mouse.clicked_name` - the name(s) of the object(s) clicked by the mouse.

We can also store other things from our mouse component by adding parameters to the *Store params for clicked* field.

.. nextslide::

We can use any of these variables to then provide trial-by trial feedback. Imagine our trial has a Mouse Component called `resp`. 

We would need to add a routine called "feedback", in this feedback routine add a text component and in the text field we could write::

    $'RT was ' + 'str(resp.time)' + ' ms'

Here we are concatinating strings using the + operator and we are also converting our resp.time variable to a string using the :code:`str()` method (we can't concatinate strings and numbers!).

.. nextslide::

The problem here is that 1) the resp.time value is actually a list, so we may want to index either the first or last element 2) we probably want to round the value to be a bit prettier::

    $'RT was ' + 'str(round(resp.time[0], 3))' + ' ms'

An alternative way of doing this in python would be to use a "formatted string" (this is better practice for python, but it might not translate so smoothly online)::

    $f'RT was {resp.time[0] : .3f} ms'

feedback dependant stimuli
-------------------------------

We can make feedback response dependant by using simple :code:`if` statements.
To adjust feedback colour based on response time we need a code component::

    if resp.time[0] < 0.5:
        feedbackCol = 'green'
    else:
        feedbackCol = 'red'

Providing overall feedback
-------------------------------

To give feedback at the end for each condition let's learn about lists. We want three lists to keep track of RTs::

    allRTList=[]
    validRTList=[]
    invalidRTList=[]

.. nextslide::

Some useful *Python* methods

- .append() - adds to a list
- np.average() - returns average of a list using the numpy (np) library. 

.. nextslide::

We can use these to give feedback at the end of our experiment to summarise performance.

On each trial we add to the list::

    if label == 'valid':
        validRTList.append(thisRT)
    elif label == 'invalid':
        invalidRTList.append(thisRT)

At the end of the experiment we can average these lists::

    validAv = np.average(validRTList)


*Exercise*
---------------------

1. Add a feedback tone that varies in frequency depending on if the RT is fast (e.g. <.05) or slow.
2. Add a text component to the end routine to tell participants if they showed a Posner cueing effect.
3. IF participants show a posner cueing effect, tell them how large their effect was in ms. 

What next?
---------------------

Code components allow us to extend mouse responses in some fun ways. So let's talk about  :ref:`mouse3days`. 



