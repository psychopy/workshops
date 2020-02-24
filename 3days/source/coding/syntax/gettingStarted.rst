.. _gettingStarted:

Getting started
-----------------------------

Python versions
~~~~~~~~~~~~~~~~~~~~~~~

You might have been somewhat overwhelmed by the versions of Python and PsychoPy:

.. rst-class:: build

    - Python2 to **Python3** introduced various nice features (e.g. better string handling) but some incompatibilities (eg. print statement)
    - PsychoPy2 to **PsychoPy3** introduced web experiments and Pavlovia.org sync tools

PsychoPy has been providing Python2 and Python3 versions for about a year, but stick to Python3 if possible.

The Coder Shell window
~~~~~~~~~~~~~~~~~~~~~~~

This is a great place just to try out a quick command and see what happens. You can check a little Python syntax and see the results of commands instantly.

Let's type some commands into the shell panel and see what happens::

    >>> a = 3
    >>> b = a + 2
    >>> b
    5
    >>> b == 5
    True

.. nextslide::

Comments
~~~~~~~~~~~~~

*NB Programmers can spend far more time reading code than writing it. Future-you will think of well-written comments as love letters from current-you.*

In Python comments are usually indicated by the `#` symbol.

Short variable names need comments:
    >>> # I hope I remember what this means later:
    >>> a = 5 # participant age

Descriptive variable names become their own comments, and can be understood regardless of where they appear in the code:
    >>> age = 5
    >>> adjustedAge = age + 2

.. nextslide::

.. rst-class:: build

    - Remember, you’ll read these variable names more often than you type them, so take an extra second or two to make them descriptive, while saving on typing comments.
    - Use `camelCase` or `under_scores` as you prefer, but be consistent.
    - `R` programmers? **No, you can't use dots in variable names.** They mean something in Python, analogous to the $ symbol in `R`.

.. note::

    Annoyingly a British Mac keyboard doesn't show you where the `#` is, but you can get it using `Alt-3` if you're running under OS X. If you're using a British Mac keyboard under Windows you need `Ctrl+Alt+3`. Sigh!

Long comments
~~~~~~~~~~~~~
You can start/end a multi-line comment with three double-quotes::

    """This is a potentially long piece of text that
    will be ignored. If it occurs at the start of a
    function it becomes the help for that function
    """

In the PsychoPy Coder window you can comment out lines with ``Ctrl-'`` and undo that with ``Shift-Ctrl-'``
If you forget, it’s listed in the `Edit` menu

Shortcuts
~~~~~~~~~~~~~

In the shell window you can see available code-completion options by starting to type a command. Type these lines gradually, taking note of what happens when you type the '.' in the second line:

    >>> name = 'Jessica'
    >>> name = name.upper()
    >>> name
    JESSICA

To repeat a previous command hit ``Alt-P`` on your keyboard.
e.g. Repeat the ``name = 'Jessica'`` statement to go back to its original value.


Editing Scripts
~~~~~~~~~~~~~~~~~~~~~

Although the shell is a handy place to check a quick command, it's often desirable to be able to repeat a set of commands without retyping them. Type this into the editor window and save the script somewhere (e.g. firstScript.py)::

    a = "hello"
    print(a)
    b = ' world'
    a + b

Switch the bottom panel of the Coder view to show the `Output` from the script. Hit the `Run` button (or press ``Ctrl-R``). You might have expected to see ``hello world`` but it didn't appear. That's because in running scripts nothing is printed to the output unless you explicitly request it. Change the last line to ``print(a+b)``.

.. nextslide::

Strings in Python can be defined using either ``'`` or ``"``.
To actually include one of these marks within a string, enclose it in the other one, for example::

    >>> text1 = "I don't like ham"
    >>> text2 = 'She said "hello".'

If you don't match your quotes in pairs, you'll notice all of your code turn pink.

.. ifslides::


  .. nextslide:: That's it

  Let's look at creating and manipulating :ref:`variables`
