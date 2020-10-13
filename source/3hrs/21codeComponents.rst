
.. _codeComponents:

Code Components
=====================

This goes to the next step in integrating code with your experiment

.. slide::
  :level: 2

  A Code Component allows you to add multi-line arbitrary Python code at 5 different points in the script:
      - start of the experiment
      - start of the current Routine
      - every frame
      - end of the Routine
      - end of the Experiment

.. ifnotslides::

  A Code Component allows you to add multi-line arbitrary Python code at 5 different points in the script:
      - start of the experiment
      - start of the current Routine
      - every frame
      - end of the Routine
      - end of the Experiment

Create a feedback Routine
----------------------------

Let's create a 'Feedback' Routine for the basic task we created earlier (requires a Code Component to decide whether the last response was correct or not).
    - create a new Routine, `feedback`, that goes immediately after `trial` on the flow
    - we need a Code Component (from the 'Custom' section) with a message that differs according to the response
    - then we'll use that message in a Text Component

.. nextSlide::

In your Code Component select the tab for `Begin Routine` and type in::

    if resp.corr:
      msg="Correct! RT=%.3f" %(resp.rt)
    else:
      msg="Oops! That was wrong"

Code Components are obviously something that could get super-complex but you can accomplish a lot with quite simple Python commands.

.. nextSlide::

Now create a Text Component:

    - name = `feedbackTxt` (or something)
    - text = `$msg` and make sure you **set every repeat**

That's all you need.

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

Formatted strings
~~~~~~~~~~~~~~~~~~~~~~

Sometimes you need to combine numbers and strings.

You've seen this in the reaction time feedback and you can see it in the setting of the filename for data file (in Experiment Settings).

.. nextslide::

You can simply convert numbers into strings and "add" them to a string::

    filename = subj + str(cond) + ".txt"

but that doesn't provide much control of the formatting of the number. For example, if you wanted a certain number of decimal places it couldn't set that.

.. nextslide::

In the following the `%i`, `%f` and `%s` indicates that Python go and find a variable in the following list and insert it with the specified representation. Any other text just looks like itself(!). If you've ever used formatted string operations in C or Matlab these will make sense pretty quickly, but otherwise they could take some time::

    "%i" %(23)
    "an int:%i" %(5)
    "a float:%f" %(5)
    "before%i_after" %(200)
    "%s.txt" %(subj) #assuming subj was still defined
    filename = "%s%i.txt" %(subj, cond)

.. nextslide::

Now the real advantage of formatted strings is that you can control the number of decimal places, and padding with zeros. Try these out::

    "%04i" %(9)
    "%4i" %(9)
    "%.2f" %(9)
    "%s%03i.txt" %(subj, cond)
    "That took %f seconds" %(32.5432143)
    "That took %.2f seconds" %(32.5243553)

.. nextslide::

There's a new way to do the same sort of thing::

		"{}".format(23)
		"an int:{:d}".format(5)  # it's d now, not i
		"a float:{:f}".format(5)
		"{:4i}".format(9)
		"{:04d}".format(9)

It has some advantages in being able to name the entry::

		filename = "{subj}{cond:02d}.txt".format(subj='jwp', cond=1)

.. ifnotslides::

    These formatted strings may seem cumbersome to start with but they're very powerful when you get the hang of them (and they're roughly the same in most languages). There are many more variants on these operations but those are the main ones that you'll need.

    For more see:

    http://docs.python.org/2/library/stdtypes.html#string-formatting-operations

If... statements and code blocks
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

What gets included in an `if...` statement (or a `for...` loop) is determined by indentation. There is no `end` statement in Python::

  if 'x' in keys:
    corr = 1
    continueRoutine = False
  elif 'y' in keys:
    print('invalid key')
  else:
    corr = 0
  print('done')

Understanding the order of execution
--------------------------------------

Each entry of your Routine has multiple Components and their code *for each part of the experiment* is run in the order of the components.

Do you want you custom code executed before or after your stimulus?

For our feedback we needed the Code component to create the `msg` variable before the Text Compenent updated its message.

Storing variables for later use
----------------------------------------

Often you'll need to store variables to keep track of things, such as how many times your participant has got the answer correct.

Let's take a look at the BART demo (included in PsychoPy Builder).


Branching and terminating Routines early
------------------------------------------

Basically, you can use an `if...` statement on each frame (or somewhere else) and set a variable to stop on next repeat.

  - `continueRoutine`
    can be set to False to exit the current Routine at the next screen refresh

  - `trials.finished` (where `trials` is the name of a loop) can be set to  `False` and that loop will terminate on its next iteration. This doesn't abort the current Routine(s) before that

  - `core.quit()`

Sometimes you need multiple things

Prevent a Routine from occurring
------------------------------------------

You could use the code above to prevent a Routine form occuring.

You could set a variable that aborted the Routine (setting continueRoutine=False) on the very first frame.

Alternatively you could surround that Routine by a loop in the Flow and set the a variable for the number of repeats (like `$nReps`). Then just use code to set `nReps=0` and your loop will effectively skip.

How to debug a code component
-------------------------------

Once you're adding custom code there are **many** things to go wrong. We'll look at some of the common issues.

Look carefully at the message and try google as well - most errors have been encountered by somebody before you! Look at the names of the variables that the error mentions and check the code relating to them.

`print()` statements are really useful here but remove them when you're done. Lots of print commands can bring your script to a grinding halt!

Debugging `if...` statements
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

`if...` statements often cause problems for new programmers. Sometimes an entry never gets used, when you think it should be `True`

You may need to use `print()` to work out where in your `if...` statement your code gets to. For example::

  if resp.keys == 'k':
    print('got a k yippee!')
  else:
    print(resp.keys)

.. nextslide::

By printing out what the value of `resp.keys` was on the occasions that it goes wrong we can help you debug the code.

NB. In the case above `keys` is `['k']` not `'k'` so you never get to see 'yipee'. You needed::

  if 'k' in resp.keys:

to test whether *any* of the keys were 'k'

.. nextslide::

Also, make sure that your `if...` statement catches *all* the relevant options. For instance::

  if resp=='right' and stimPos=='right':
    correct = True
  elif resp=='left' and stimPos=='right':
    correct = False

Here we haven't defined what happens if, say, `resp=='left'` so we might then have a problem that 'correct' hasn't been defined (or it might be left as whatever happened on the previous trial!!)

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

If you get an attribute error it usually means that something in one part of your script has been overwritten by another.

If the error comes up not on a line of your own hand-written code then it might indicate that one of the variables you created in your code component has overwritten something else.

For instance, if you had an Image Component called `stimulus` but then you used code to create a variable `stimulus = 'myImage.jpg'` then you would probably get an error later on like:

.. code-block:: none

  if t >= 0.0 and stimulus.status == NOT_STARTED:
  AttributeError: 'str' object has no attribute 'status'

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

One of the most common times this happens with Builder Code Components is when you try to test whether the participant pressed a certain key.

For example you could test whether the first key they pressed was 'x' by doing::

  if resp.keys[0] == 'x':
      print('yes it was x')

.. nextslide::

but if the subject hasn't responded at all then this will yield:

.. code-block:: none

    if resp.keys[0]=='x' and corrAns=='x':
    IndexError: list index out of range

You need this instead::

  if len(resp.keys)>0 and resp.keys[0] == 'x':
      print('yes it was x')

Or::

  if 'x' in resp.keys:
      print('x was one of the keys')

The user forum
~~~~~~~~~~~~~~~~~~

The forum (discourse.psychopy.org) is fairly willing to help you fix issues but only if you make it easy:

  - if you have Code Components in your experiment **always** state that and try to give any relevant pieces
  - try to work out which bit of the Code Component is the problem by cutting bits out and trying again
  - always give the exact, complete error message (not just the last line)
  - if you need to upload the experiment to the forum, try to create a *minimal working example*

How would I know what is possible!?
------------------------------------------

Of course, the code might be simple when you know it! How would you know that the above are variables?

PsychoPy has many users, and therefore Google knows PsychoPy well. The documentation and the users forum have many answers, so google very often works.

Google for: `end a loop early psychopy` and see what happens (hit 1 and 4 both give you the answer above)

You can also compile any script...

.. _scriptOutput:

Compiling code from Builder
----------------------------------------

.. image:: /_images/compileScriptButton.png

We can see some Python code using the compile button. The scripts generated by Builder are particularly frightening to a non-programmer:

    - much more code than we needed
    - especially more complicated code to
        - start/stop each stimulus/component
        - determine whether all the components are finished (i.e. trial is over)
    - rather little re-use of code

.. nextslide::

Builder can't know your intentions so has to prepare for everything!

But the code can be useful:

    - to get ideas for how to do things
    - to find out what variables a Builder experiment 'knows' about e.g.:
        `t` is always the current time in seconds since the start of the Routine


One-way streets
-------------------

You could save and run your exported script (as Builder does each time you press run).

You could tweak this code and see the effects your edits have on the running of the experiment.

If you do your changes will **NOT** be reflected back in the Builder experiment.

Hacking the script might be useful to see how things work but it's better to add your edits back into the Builder view.

We'll see some better ideas in the section :ref:`mouse`