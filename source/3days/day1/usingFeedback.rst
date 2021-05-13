.. _addingFeedback:

Adding feedback
===============================

Adding feedback
-------------------------------

Let's try and create a 'Feedback' Routine for the Posner task we want to:

- Add trial by trial feedback on response times 
- Adjust the colour of the feedback based on RT
- Give feedback at the end on average RT overall, on valid trials and on invalid trials.

.. nextslide::

To add trial by trial feedback on response times create a feedback routine and add a text component. In the text field enter::
    
    $f'RT was {str(round(resp.time[0], 3))} ms'


.. nextslide::

To adjust feedback colour based on response time we need a code component::

    if resp.time[0]<.5:
        feedbackCol = 'green'
    else:
        feedbackCol = 'red'

.. nextslide::

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



