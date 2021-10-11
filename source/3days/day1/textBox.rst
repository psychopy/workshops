.. _typedResponses3days:

Typed responses
=================
PsychoPy now has an editable text box component to get typed responses. It is under development, but worth touching on.

textBox
----------------------------------
The texbox component is very similar to the text stimulus, except that we can make it 'editable'

You can find the textbox component under the 'responses' section of the compontent panel.

.. nextslide::

When asking participants to submit a response, remember all keys will be watched by the textbox. So, if you don't want any keys to end the trial use a mouse click to submit the response and end the trial.

If you want speeded responses, perhaps you want to use a key repsonse component and end the routine when a specific key is pressed (e.g. 'return')

.. nextslide::

We can check the accuracy of responses, but usually this will be via a string comparison. e.g::

	if textbox.text == corrAns:
		feedback = 'correct!'
	else:
	    feedback= 'incorrect'


This means we should be very careful as checks will be case and space sensitive.


*Exercise*
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Make a digit span task. Participants will see 3 numbers and type their response. We need:

- A routine to show the digits one by one in a random order
- A routine to gather the responses. Participants type a response and click a button to end the routine.
- Both of these routines to repeat 5 times 

What next?
----------------------------------

:ref:`builderAndCode`
