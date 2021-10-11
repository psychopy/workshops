.. _variables:

Variables and common types
=================================

Assigning variables
--------------------------------

You've already seen variables being assigned using =. You can also assign multiple things at once. Type these in and then check to see what each variable looks like afterwards::

	a = b = 2

	a, b = 2, 3 # try what happens if the number of vals doesn't match

	myString = 'Hello World'

	firstWord, secondWord = myString.split() # also try splitting by 'o'

	listOfTwoWords = myString.split()

Comparing variables
--------------------------------

In some programming languages, the '=' sign is used both to assign a value to a variable and to compare variables for equality.

In Python, we use '==' to test if two things are equal::

    >>> a = 2 # make a equal 2
    >>> b = a # make b equal a
    >>> b == a # compare b to a
    True

Types of variable
--------------------------------

In Python almost everything is an `object`. There are a number of built-in objects that are very widely used:

    * integers and floats
    * booleans
    * strings (and unicodes)
    * tuples and lists
    * dicts

.. nextslide::

Objects can be much more complicated.

PsychoPy adds a bunch of other object types, such as::

    Window # something to draw stimuli in

    GratingStim # something psychophysicists love to draw in windows

    DotStim # lots of random dots that move by themselves

    Clock # control timing

    ExperimentHandler # control trials & save data

    ParallelPort # send signals to hardware like EEGs

.. note::
    An individual object is an `instance` of a `class`. That is, a class is a set of code and specifications which defines what an object created from it can do. We create a specific object by `instantiating` it using the class as a recipe. This terminology perhaps won't make sense until you see the more sophisticated PsychoPy classes being used.

.. nextslide::


You can find out what an object is using the ``type()`` function::

    type('Hello')
    type('Hellø')  # in Python3 a string is "unicode" format
    type(5)
    type(5.0)
    type([1, 2, 3])
    type(True)

.. nextslide::

Finding out the type can be essential if things look the same when printed but aren't the same.
*Sprinkling print statements like this throughout your code is often a key part of debugging in Python/PsychoPy*::

    a = 5
    b = '5'
    print(a, b)
    print(a == b)
    print(type(a), type(b))

But there are a huge number of additional objects and you can make your own too.

Integers and floats
^^^^^^^^^^^^^^^^^^^^^^^^^

Integers and floats (floating point numbers) are just 2 different types of number. Integers don't store anything after the decimal place.

**If you're using Python2**  beware that dividing a pair of integers gives you back an integer::

    print(1/3) # surprise!
    print(1.0/3)
    print(1/3.0)

In Python3 dividing integers returns a float if needed, and you can get the same in Python2 by adding this to your script::

    from __future__ import division

Strings
^^^^^^^^^^^^^^^^^^^^^^^^^

Python has fantastic string handling options. Try these methods that are attached to strings::

    a = 'hello world'
    a.title()
    a.split()
    a.endswith('world')
    len(a) # you'll probably use this function a lot

.. nextslide::

You can also combine strings in nice, simple ways::

    image = 'cat'
    suffix = '.jpg'
    fileName = image + suffix # you can add or 'concatenate' strings
    text = image * 2 # yes, this is valid
    text = image * 2.0 # but this isn't
    image + image.upper()

.. _slicing:

Slicing
-------------

Often you need to fetch a subset of an object, like a string or a list.

.. warning::

    If you're used to `Matlab` or `R` then be warned: in Python the first element of an array or a list is zero, not one. This will catch you out sooner or later!!

>>> a = 'Nottingham'
>>> a[0]
>>> a[2:4]
>>> a[2:]
>>> a[:]
>>> a[-1]
>>> a[2:-2].upper()

Converting (aka coercing)
------------------------------

You can convert between these different types of objects where they make sense::

    a = int(1.5)
    b = int('1')
    c = str(1.5)
    d = float(1)

but not where they don't::

    float('f1')
    int([1,2])

.. _formattedStrings:

Formatted strings
--------------------

Sometimes you need to combine numbers and strings. Imagine I wanted to make a filename to save my data. Maybe in my script I had a variable to store my subject name and another to store a stimulus attribute which was 10, 50, 100, 200 on different runs. I might try and save the data filename like this::

    subj = 'jwp'
    cond = 50.0
    filename = subj + cond + ".txt"

You get an error because cond is a number and your trying to add it to a pari of strings (subj and ".txt") and Python doesn't know what way you want them combined.

.. nextslide::

You could convert cond into a string and have no error::

    filename = subj + str(cond) + ".txt"

Instead, we can use a formatted string or "f-string" in Python3 (we'll mention the Python2 options later)::

    filename = f"{subj}{cond}.txt"

.. nextslide::

You can also specify the format of numbers. Try some of these::

    f"{subj}{cond}.txt"  # default format for that object type
    f"{subj}{cond:.3f}.txt"
    f"{subj}{cond:.0f}.txt"
    f"{subj}{cond:6.0f}.txt"
    f"{subj}{cond:06.0f}.txt"
    f"{subj}{cond:+06.0f}.txt"

These would often be used in feedback messages too::

    rt = 0.63445345
    msg = f"Well done {subj}! Your reaction time was {rt:.3f}"

.. nextslide::

You can even run simple code snippets inside these formatted strings!::

    f"{subj.upper()}.txt"

.. nextslide::

The above system of formatting is only for Python3.6+ but there are other systems too (use these if you need Python2 compatibility).

Like the new f-strings::

	filename = "{}{:03}.txt".format(subj, cond)

Like older C-style formats::

	filename = "%s%03i.txt" %(subj, cond)

For more see on those two see: https://pyformat.info/

.. ifslides::

    Now you know about simple variables let's store them in :ref:`containers`

Containers
-----------------

Very often you need variables that store more than one value and keep them organised in some way. The two most common are lists and dictionaries.

Lists
^^^^^^^^^^^^^^^^^^^^^^^^^

For storing things that have a defined order::

	a = [30, 20, 10]
	b = ['a', 1, 1.0]
	b.append('blah')
	a.append(3.0)

Slicing works just the same as with strings::

	a[0] # remember, Python starts at zero
	a[4] # so this won't work
	a[-1] # this will
	b[-1]
	b[-1][-1]

.. nextslide::

Mathematical operators::

	a + a # this might be a surprise (unlike in Matlab/R)
	a + b
	b * 3

For those who have come from Matlab backgrounds, these lists might look like Matlab matrices, but they aren't. These aren't designed for mathematical operations. There is a similar object which *is* very much like Matlab matrices, which we'll explore when we look at :ref:`dataAnalysis`

.. nextslide::

Other methods::

	print(dir([])) # go and explore some of the other methods of lists
	a.pop() # pull off the last element of a
	a.append(b) # add all of b as the last element of a
	a.extend(b) # add all of the elements of b individually
	a.index(30) # where is the value 30?


Dictionaries (dicts)
^^^^^^^^^^^^^^^^^^^^^^^^^

At times you want to keep things with something that identifies what each element is. That's where you'll use a dict. These can be created in various ways::

    stim1 = {'word':'red','ori':90,'duration':0.5}

    # or just create it and add the entries afterwards:
    stim2 = {}
    stim2['word'] = 'blue'
    stim2['ori'] = 90
    stim2['duration'] = 0.3
    print(stim1['word'])

.. nextslide::

Then you can access the contents in a similar way::

    print(stim1['ori'])
    print(stim2['fail']) # error?

Explore what some of the different dict methods do::

    dir(stim1)
    stim1.keys()
    stim1.values()

To test if a dictionary has a particular key::

    'word' in stim1  # True
    'blue' in stim1  # False

.. nextslide::

Dictionaries are important in PsychoPy. They are often used to hold the information specifying parameters of a trial::

    trial1 = {'distractor':True,
              'image':'cat.jpg',
              'duration':0.5}

*NB. if a line ends in a comma you can break the line without breaking the code*

Nesting objects within each other
--------------------------------------

Often containers are nested within each other. You might well have a list of dicts, or a dict containing lists etc.::

    #a list of dicts
    stimuli = [stim1, stim2, stim3]
    stimuli[0]['word'] # this is stim1 because we start at zero!!
    thisStimulus = stimuli[2]
    thisStimulus == stim3

.. nextslide::

or a list of lists::

    coordinates=[[0,0], [2,3], [8,0]]
    responses = [ [1, 1, 0, 0],
        [1,1,1,0],
        [0,1,1,1]]
    print(responses)
    print(responses[2][3]) #the 4th entry of 3rd list (STARTS AT ZERO)

    #or we could have done this
    responses = []
    cond1 = [1, 1, 0, 0]
    responses.append(cond1) #etc.

You can nest objects as deeply as you like. The limit is your own brain being able to keep track of what you're doing!

Indentation
----------------

One of the unusual things in Python is that indentation (whitespace) is actually important. Try to use a genuine programmer's text editor and set it to insert spaces in place of tabs (it's hard to spot errors when you have a mixture of tabs and spaces). Many editors, will try to help you get indentation right::

    if response == 'y':
       print('Yes')
    else:
       print('No')
    print('Whatever')

.. nextslide::

Type the following into the editor after your other text::

    name = 'Jessica'
    for thisLetter in name:
        print(thisLetter)
        print(thisLetter.upper())
        print('done')

.. note::

    ``upper()`` is a ``method`` that all strings have. Let's find out what else they have by using the ``dir()`` function. Add ``print(dir(name))`` to the last line.

Now, that probably didn't do what you expected. In Python the code that is included as part of the for-loop is indicated by the level of indentation, so ``print('done')`` was repeated for each repeat.

.. nextslide::

Select the last few lines of code and press `Ctrl-[` to get this::

    for thisLetter in name:
        print(thisLetter)
    print(thisLetter.upper())
    print('done')
    print(dir(name))

Now the code will print each of the letters in their lower case. Then the loop ends. ``thisLetter`` still exists but it isn't changing any more. It gets printed just once in upper case, followed by the other commands.

.. nextslide::

``print`` can print multiple objects at once (if you insert commas), and you can suppress the line endings. With old-style `print`::

    for thisLetter in name:
        print thisLetter, thisLetter.upper(),
    print 'end of the loop'
    print 'done'

Or new-style (Python3 or using `from __future__ import print`)::

    for thisLetter in name:
        print(thisLetter, thisLetter.upper(), end="")
    print('end of the loop')
    print('done')

Importing modules:
----------------------

Python functions beyond its basic set are organised into `modules` and `packages` (`PsychoPy` is a set of such modules). We need to explicitly  import such packages to be able to access their functions::

    >>> import os # handy system and path functions

You can find out what's in a module using the function ``dir()``::

    >>> dir(os)

.. note::

    Note that in the shell if the command `returns` a value and you didn't provide anything to receive/store that value then it gets printed to the screen instead (this is not the case for scripts run from the editor).

Import statement variants
----------------------------

Having functions in modules allows us to avoid name space collisions, such as functions that have the same name. Different import styles allow different naming::

    import numpy # access like:  numpy.sin(0)
    import numpy as np # np.sin(0)
    from numpy import sin, cos, tan # sin(0)
    from numpy import * # often frowned upon

    from numpy.random import random, randint, shuffle

    # can now say shuffle(mylist) rather than
    # numpy.random.shuffle(myList)

PsychoPy imports:
-------------------------

    >>> from psychopy import visual, core, data, event, sound, gui

    >>> from psychopy.constants import * # like STARTED, FINISHED


Common mistakes & error messages
-----------------------------------------

To follow is a list of simple, common mistakes. Remember:
    - every character counts. A single typo/omission causes the script to crash.
    - the script runs from the top and down. Things not defined yet cannot be referenced (used).

Python is helpful in letting you debug errors.
    - in every error, the top line tells you the line at which the error
      occurred. You probably mis-typed something.
    - in every error, the bottom line tells you the type of error.

Approaching Errors
^^^^^^^^^^^^^^^^^^^^^^^^^

.. rst-class:: build

A general strategy for approaching errors is:

1. **Look up the line that caused the error!**

	- Did you type everything correctly?
		- Do all your parenthesis, brackets, and quotes *match*?

	- Did you do something you shouldn't have?
		- Did you call for a class that doesn't exist, wasn't imported, or hasn't been set yet?

	- Is something not what you thought it was?
		- Was a value possibly redefined when you "weren't looking" or did a variable have a misleading name, like a number called "subject_name"?

.. nextslide::

2. **Look at the error type if you still haven't found the error!**

- The type of error tells you exactly why python thinks what you've done is wrong, even if you think it's right.


NameError
^^^^^^^^^^^^^^^^^^^^^^^^^

The variable is not defined (yet)::

    >>> myVariable = 2
    >>> print(myvariable)

::

    Traceback (most recent call last):
    File "<stdin>", line 1, in <module>
    NameError: name 'myvariable' is not defined

.. ifnotslides::

    `myvariable` doesn’t exist because Python is case-sensitive.

.. nextslide::

An error as output from PsychoPy::

    ## Running: /Users/michael/Desktop/PsychoPy test/test_lastrun.py ###

    Traceback (most recent call last):

    File "/Users/michael/Desktop/PsychoPy test/test_lastrun.py",

    line 96, in <module>

    print(aVariableThatIHaventDefinedYet)

    NameError: name 'aVariableThatIHaventDefinedYet' is not defined

TypeError
^^^^^^^^^^^^^^^^^^^^^^^^^

The variables are of the wrong type for what you tried to do to them::

    >>> subject = 'Emma'
    >>> trialNum = 2
    >>> print(subject + trialNum)
    TypeError: cannot concatenate 'str' and 'int' objects


.. rst-class:: exercise

    Revision: *How do you concatenate a string and an integer?*


SyntaxError
^^^^^^^^^^^^^^^^^^^^^^^^^

Your statements don’t follow the Python syntax. Because of this, the error message can't give helpful details except where the error occurred (via the line number and caret ^ symbol.

    >>> my Variable = 2
    File "<stdin>", line 1
    my Variable = 2
         ^
    SyntaxError: invalid syntax

.. ifnotslides::

    Cause: Variable names cannot contain spaces.

.. nextslide::

Another syntax error example::

    >>> for i in range(10)
    >>>    print(i ** 2)

    for i in range(10)
                     ^
    SyntaxError: invalid syntax


.. ifnotslides::

    Cause: Omitted colon.

IndexError
^^^^^^^^^^^^^^^^^^^^^^^^^

You tried to access an element of a list using an index which is out of bounds.

    >>> a = [10, 20, 30]
    >>> a[3]
    IndexError: list index out of range

.. ifnotslides::

    Did you remember the zero-based indexing?

KeyError
^^^^^^^^^^^^^^^^^^^^^^^^^

You tried to access an entry in a dictionary using a key that doesn’t exist.

    >>> details = {'name': 'jonas'}
    >>> print(details['age'])
    KeyError: 'age'

Error resources
^^^^^^^^^^^^^^^^^^^^^^^^^

    - Try this flow chart: http://i.imgur.com/WRuJV6r.png
    - For the pros, see http://stackoverflow.com/questions/1011431/common-pitfalls-in-python

