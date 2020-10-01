.. _loops:

Loops
--------------

Repeating things is what computers are good at and humans find boring! Repetition is controlled with loops, which come in two varieties. :ref:`forLoops` are when you want something to repeat a known **number** of times, whereas :ref:`whileLoops` will run for an unspecified duration until some **condition** is met.

.. _forLoops:

for... loops
~~~~~~~~~~~~~~~

In many languages ``for`` is used for looping over some numbers, which you then use to index some other object (a string or an array).

Python loops are more flexible; you can loop over the contents directly without needing an index.

For instance, strings and lists both know how to 'iterate'::

    for thisLetter in 'hello':
        print(thisLetter)
    print('loop done')

    for thisInt in [1,2,3]:
        print(thisInt, thisInt*3)

.. nextslide::

In MATLAB, you might write:

.. code-block:: matlab

    subs = {'sub01' 'sub02' 'sub03'}
    for i = 1:3
        sub = subs{i}
        disp(sub)
    end

In Python this would be::

    subs = ['sub01', 'sub01', 'sub03']
    for sub in subs:
        print(sub)

.. nextslide::

.. rst-class:: build

* Each time through the loop, the next item is available as the variable after "for". Think of this as where "sub" or "thisTrial" are **defined**.

* You can use almost anything as your variable name, but it helps to be descriptive and meaningful.

* **PsychoPy style tip:** We quite often use 'this' to remind ourselves that a variable was being used in a loop. It can lead to confusing bugs if you refer to a variable after a loop has ended that was designed for use in the loop, because after the loop ends the variable still exists, but has the last value it had in the loop.

.. _enumerate:

Enumerate
~~~~~~~~~~~~~

Often you'll want to know not only the current value in a list, but also its location. For instance, if we run some trials like this. e.g. ::

    oris = [0,45,90,180]
    resps = [1, 1, 0, 1]
    RTs = [0.324, 0.454, 0.432, 0.123]

How do we print the ``resp`` and ``RT`` that is associated with the equivalent ``ori`` ?

.. nextslide::

We could go back to old-style and loop through a set of `indices` to fetch the values::

    for ii in range(len(resps)):
        thisOri = oris[ii]
        thisResp = resps[ii]
        thisRT = RTs[ii]
        print(ii, thisOri, thisResp, thisRT)

.. nextslide::

The need to know the current value AND its index in the list is so common that Python has a special function for it called ``enumerate``::

    for ii, thisOri in enumerate(oris):
        thisResp = resps[ii]
        thisRT = RTs[ii]
        print(ii, thisOri, thisResp, thisRT)


Common Use-cases
~~~~~~~~~~~~~~~~

Let's use a loop to create a list of dictionaries::

    myList=[]
    for thisInt in range(5):
        thisEntry = {}
        thisEntry['val']=thisInt
        thisEntry['X3']=thisInt*3
        myList.append(thisEntry)
    print('myList is now', myList)

    print('printing one entry per line:')
    for thisEntry in myList:
        print(thisEntry)


.. nextslide::

If you use a dictionary in a loop it will return each of the keys::

    man = {'name':'Jon', 'style':'geek', 'age':21}
    for thisKey in man:
        print(f"This man's {thisKey} is {man[thisKey]}")

Dictionaries also have an `items` method, which returns a list of key/value pairs. We could iterate over the list of pairs, which means we could do this::

    for thisKey, thisVal in man.items():
        print(f"This man's {thisKey} is {thisVal}")

Nesting loops
~~~~~~~~~~~~~~~~

You can nest one loop inside another (as deeply as you like). The inner loop will perform a full cycle on each pass through the outer loop::

    for thisNum in range(5):
        for thisChar in 'abc':
            print(thisNum, thisChar)

.. rst-class:: exercise

  **Exercise**: Switch the order of the two loops and try it again.

.. nextslide::

Remember **indentation** is key in deciding which of the loops a code line belongs to::

    for thisNum in range(5):
        print(f'------------starting run {thisNum}')
        for thisChar in 'abc':
            print(thisNum, thisChar)
            print('x')
        print(f'------------finished run {thisNum}')

**NB**: Be careful with looping - too many levels of nesting can be a sign of code that is too complicated. In that case, :ref:`functions` to the rescue!


.. _whileLoops:

while... loops
~~~~~~~~~~~~~~~~~

If you want your loop to end based on some condition, rather than based on a certain number or iterations, then you could use a while...loop. For instance, an experiment might be based something on time rather than on repeats::

    import time #time module is built into Python
    t0=time.time() #time in secs
    nReps = 0
    while (time.time()-t0) < 0.5: #continue this loop for 0.5s
        nReps = nReps+1 # (try using the shorthand n+=1 in the shell)
    print(f"we did {nReps:.0f} loops in 0.5s")

.. nextslide::

Or you might want to end the loop only when a valid response has occurred.::

    from numpy import random
    validKeys = 'az'
    availableKeys = 'azqwertyuiop'
    resp=None #None is a special value in Python for, well, none!
    while resp==None:
        ii = random.randint(0,len(availableKeys))
        keyPress = availableKeys[ii]
        if keyPress in validKeys:
            resp=keyPress
            print('At last')
        else:
            print(f"'{keyPress}' was not a valid key")
    print(f"subject responded with '{resp}'")


Other than that, ``while...loops`` are really similar to ``for...loops`` (personally I use them less).

`break` and `continue`
~~~~~~~~~~~~~~~~~~~~~~~~

Sometimes you need to end a loop, or this repeat of a loop, prematurely.

* ``break`` allows you to end a loop completely and move to the next code after it.

* ``continue`` means 'continue to the next iteration of the loop without finishing this one'.

They both only operate on the current loop - be careful if your loops are nested.


Loop Timing
~~~~~~~~~~~

A `for` loop can take a variable amount of time to execute depending on how many items are being iterated and how quickly each iteration completes.

A `while` loop can be held for a certain amount of time, especially when used with :class:`~psychopy.clock.Clock` and :class:`~psychopy.clock.CountdownTimer`

.. ifslides::

  That's it
  ~~~~~~~~~~~~~~~

  Go back to :ref:`day1sched`
