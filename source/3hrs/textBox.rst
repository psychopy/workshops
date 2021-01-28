.. _typedResponses:

Typed responses
=================
PsychoPy now has an editable text box component to get typed responses. It is under development, but worth touching on.

textBox
----------------------------------
The texbox component is very similar to the text stimulus, except that we can make it 'editable'. It can therefore be found under both 'Stimuli' and 'Response' sections of the components panel. 

.. nextslide::

* To have a completely blank textbox type a space in the text field to act as a place holder. Then set that field to *set every repeat*
* If you want a speeded typed response, you might want to add a keyboard component to end the routine when a certain key is pressed otherwise use a mouse response to end the trial.

.. nextslide::

If you want to check that the typed string was correct you can add a code component and, in the "end routine" tab use ::
	
	if corAns in textbox.text:
		correct = 1
	else:
		correct = 0

This will test if the correct answer was within the typed string (e.g. ignoring any spaces after the response)

What next?
----------------------------------

There is alot more we could talk about:

:ref:`blockDesigns` are something many want to implement.

Time permitting we can talk more about
:ref:`codeComponents`