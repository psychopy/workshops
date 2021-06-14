
.. _codeComponents:

Code Components
=====================

Integrating code with your experiment is not necissary, but can allow greater flexibility in your experiments (and allows you to learn some code!)

Code Components
----------------------------

  A Code Component allows you to add multi-line arbitrary Python code at 6 different points in the script:
      - before the exmperiment
      - start of the experiment
      - start of the current Routine
      - every frame
      - end of the Routine
      - end of the Experiment


.. nextSlide::

You can also set the code 'type':

- Py: python code (local use)
- JS: Java script (code you will only need executing online)
- Both: allows you to simultaneously edit and add both Py and JS
- Auto -> JS: type in python, autotranslated to JS

I tend to keep the default (Auto-> JS) and then switch to 'Both' if I need to make edits for online. But keeping seperate JS and Py can help keep things 'modular'

Create a feedback Routine
----------------------------

Let's create a 'Feedback' Routine for the basic task we created earlier. We could just use some "code as argument". i.e. you can add code to the field of any component by starting that field with a $ sign. 

Add a text component and in the 'text' field add::

  $"RT=" + str(round(resp.time[0], 3))

and 'set to every repeat'

.. nextSlide::

Imagine we want something a bit more complex. We want the colour of the feedback to change depending on how fast the participant was. For this we need to:

    - we need a Code Component (from the 'Custom' section) with a message/colour that differs according to the response
    - then we'll use that colour in the Colour field of our text

.. nextSlide::

In your Code Component select the tab for `Begin Routine` and type in::

    if resp.time[0]<.5:
      thisCol='green'
    else:
      thisCol='red'
Then inside your test component under Appearance > Color type :code:`thisCol` and "set every repeat"

Code Components could get super-complex but you can accomplish a lot with quite simple Python commands.

Common coding issues
----------------------------

Locally, syntax errors can be common. If you have your code type set to Auto ->JS you might notice when these errors can occur, but it is also useful to understand why these can occur. 

Basic Python syntax
--------------------------------------

There are so many potential things to learn about Python code and we really can't teach much of it.

Assigning variables is done like::

  a = 5 # an int
  b = "some text" # a string

NB strings can use "" or '' as long as the quotes match (and the other quote can be a character inside the string).

.. nextslide::

You can also have groups of variables like a list::

  a = [1, 2, 3]
  b = ['a', 'b', 21]

Accessing the contents of a list (or array or string is done like this)::

  firstEntry = a[0]  # indices start at zero!!
  lastEntry = a[-1]
  firstLetter = 'my long string'[0]
  middleLetters = 'my long string'[5:8]

.. nextslide::

Or use a dictionary (dict)::

  a = {}
  a['name'] = 'jon'
  a['gender'] = 'male'
  a['age'] = 21

and access like this::

  name = a['name']

.. nextslide::

One very useful dictionary is the `expInfo` dictionary which contains all the info from your initial dialog box::

  print(expInfo['participant'])

Try adding some variables to your Experiment Info dialog (in Experiment Settings) and then use it as the text in a Text Component like::

  $expInfo['participant']

You *may* need to convert your info object to a string first like this::

  $str(expInfo['consented'])

If... statements and code blocks
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

What gets included in an `if...` statement (or a `for...` loop) is determined by indentation. There is no `end` statement in Python, recall our earlier component::

    if resp.time[0]<.5:
      thisCol = 'green'
    else:
      thisCol = 'red'

Understanding the order of execution
--------------------------------------

Each entry of your Routine has multiple Components and their code *for each part of the experiment* is run in the order of the components.

Do you want you custom code executed before or after your stimulus?

For our feedback we needed the Code component to create the `msg` variable before the Text Compenent updated its message.

Storing variables for later use
----------------------------------------

Often you'll need to store variables to keep track of things e.g. keeping track of RTs to give feedback at the end::

    RTlist = []

and add to that list at the end of each routine::

    RTlist.append(resp.time[0])

NB: append is 'push' in JS

.. nextslide::

Then in our final end message we could add a code component where we set some feedback text::

  feedbackText = 'Your average RT was'+average(RTlist)

Then in our text component add::

    $feedbackText

NB: we can't use specific python libraries (i.e. numpy) online so we find appropriate alternatives using JS resources.

Branching and terminating Routines early
------------------------------------------

Basically, you can use an `if...` statement on each frame (or somewhere else) and set a variable to stop on next repeat.

  - :code:`continueRoutine`
    can be set to False to exit the current Routine at the next screen refresh

  - :code:`trials.finished` (where `trials` is the name of a loop) can be set to  `False` and that loop will terminate on its next iteration. This doesn't abort the current Routine(s) before that


Sometimes you need multiple things

Prevent a Routine from occurring
------------------------------------------

You could use the code above to prevent a Routine form occuring.

You could set a variable that aborted the Routine (setting :code:`continueRoutine=False`) on the very first frame.

You can also skip a routine by setting nReps to 0! 

How to debug a code component
-------------------------------

Once you're adding custom code there are **many** things to go wrong. We'll look at some of the common issues.

Look carefully at the message and try google as well - most errors have been encountered by somebody before you! Look at the names of the variables that the error mentions and check the code relating to them.

:code:`print()` statements are really useful here but remove them when you're done. Lots of print commands can bring your script to a grinding halt!

Debugging `if...` statements
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

`if...` statements often cause problems for new programmers. Sometimes an entry never gets used, when you think it should be `True`

You may need to use `print()` to work out where in your `if...` statement your code gets to. For example imagine we didn't know mouse RTs were stored as a list and used::

    if resp.time<.5:

instead of::

    if resp.time[0]<.5:

.. nextslide::

By printing out what the value of `resp.time` was on the occasions that it goes wrong we can help you debug the code::

    print(resp.time)

.. nextslide::

Syntax errors
~~~~~~~~~~~~~~~~

These crop up when you haven't written valid code. Check the 'syntax' of your code against the examples carefully. For example::

  if x = 5:
    print('hello')

is a syntax error because you need **==** for a test (not **=**).

::

  if x==5
    print('hello')

is a syntax error because the colon is missing

Attribute errors
~~~~~~~~~~~~~~~~~~~

If you get an attribute error it usually means that something in one part of your script has been overwritten by another or that you are trying to access an attribute that doesn't exist. 

For example, if you had the spelling error::

  print(resp.tiem)

This would probably tell you that your response component doesn't have an attribute names that..

Type errors
~~~~~~~~~~~~~~~~

Type errors can occur when you try to do things with the wrong 'type' of object. For instance::

  print(age+name)

would give:

.. code-block:: none

  TypeError: unsupported operand type(s) for +: 'int' and 'str'

if age had defined as a number and name was a *string*. You would need to convert the number to a string (or vice versa) to add them

.. nextslide::

Type errors can also occur nowhere near the line of code where they were created (as with Attribute Errors) if you have overwritten another variable with your code.

Again, look at the line of code where the error is being generated and think about what you've done with similar variable names.

Index errors
~~~~~~~~~~~~~~~~

You can get an `IndexError` by referring to something that is too short (e.g. requesting the third entry in a list with only two entries).

For example a common error might be to try and index the first element of a list like this::

  print(resp.time[1])

And if you have set your mouse component to end the routine on a single click, there probably won't be an element in the 1th position.


How would I know what is possible!?
------------------------------------------

Of course, the code might be simple when you know it! How would you know that variables psychopy already 'knows' about?

We could compile our task to code and peak behind the scences. This is useful for clocks for example.

One-way streets
-------------------

You could save and run your exported script (as Builder does each time you press run).

You could tweak this code and see the effects your edits have on the running of the experiment.

If you do your changes will **NOT** be reflected back in the Builder experiment.

Hacking the script might be useful to see how things work but it's better to add your edits back into the Builder view.

What next
-------------------

Knowing how we can set the attributes of components on every frame, we can make some exciting experiments by :ref:`dynamic` as we can with mouse components.