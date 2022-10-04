
.. ifslides::

  .. image:: /_static/OST600.png
    :align: left
    :scale: 25%

.. _introduction3Hours:

Introductions
----------------

The Team!
=========================

PsychoPy is an Open Source project, the users have access to the code and can contribute at any time! That kind of means the team is technically huge!

.. figure:: _images/team_slide.png


.. nextslide::

In terms of the "core team" , thanks to Pavlovia users and grants we can now fund staff to work on developing the tools and supporting users.

.. figure:: /_images/team2022.png
    :scale: 80%
    
About the workshop
~~~~~~~~~~~~~~~~~~~~~~

We can't teach you all of PsychoPy. This intro is aimed to give you a basic intro and inspire ideas on what's possible. 


Getting to know PsychoPy
============================

What is PsychoPy?
~~~~~~~~~~~~~~~~~~

It's `Psychology software in Python`

PsychoPy is a Python library, an script editor (Coder) an application with a GUI (Builder)

It is, itself, entirely written in Python
    * 2002-2003: Jon began work on this for his own lab (visual neruoscience)
    * 2003-2017: a purely volunteer-driven, evenings and weekends project
    * 2017-now: still open source and free to install but with professional support (funded by grants and Pavlovia)

Goal of PsychoPy
~~~~~~~~~~~~~~~~~~

The aim is to enable scientists to run as wide a range of experiments as possible, as easily
as possible, with standard computer hardware.

A single piece of software:
    - precise enough for psychophysics
    - intuitive enough for undergraduate psychology
    - flexible enough for everything else
    - capable of running studies in the lab or online

Choice of interface
~~~~~~~~~~~~~~~~~~~~~

It's hard to make something easy enough for undergrads and novices but flexible enough for everything else.

PsychoPy provides two main options, coder view and builder view. But you can also use code inside builder view - which is what we recommend.

.. nextslide::

.. figure:: /_images/coder_small.png

   The Coder view is used to create experiments from Python scripts

.. nextslide::

.. figure:: /_images/builder.png

   The Builder view is used to create experiments visually

Why do people *Code*?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* To implement more complex experimental designs/procedures(?)
* To know exactly what the code is doing(?)
* To break out of the "trials/blocks" structure or drawing loop cycle
* To program things that aren't psychology experiments. (e.g. stats, simulations, analyses etc.)

Why do people *Build*?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* It is far faster to develop experiments!
* You can still understand (and build on) your experiment next year
* You'll probably have fewer bugs
* Code Components can be used in nearly all places where Builder isn't enough
* Your Builder experiment will also compile to a web (JS/HTML) experiment!

What do **we** do?
~~~~~~~~~~~~~~~~~~~~~~~~~~

Our *experiments* are almost always in Builder, with added Code Components. I don't ever break out and switch to pure code. 

I do use code for other things, like making my 'conditions' .csv files, making stimuli and customizing the experiments.

PsychoPy versions
~~~~~~~~~~~~~~~~~~~~~~~~~~

PsychoPy is changing rapidly, especially now it has full-time programmers

You *don't* want your study to change part-way through, but you *do* want to be able to update your software

PsychoPy experiments have a setting called `useVersion` that works for Builder/Python/JS experiments. Ideally:

- Install the latest stable version
- Develop your experiment in that
- When you start running "for real" set the useVersion to the specific version you tested on


Going further
~~~~~~~~~~~~~~~~~~~~~~

Builder interface:
    - `Building Experiments in PsychoPy (Second Edition) <https://uk.sagepub.com/en-gb/eur/building-experiments-in-psychopy/book273700>`_ by Peirce, Hirst and MacAskill (2022, Sage Publications)

Python programming (for experimental psych) but these are a bit outdated:
    - `Programming Visual Illusions for Everyone <http://www.springer.com/gb/book/9783319640655>`_ by Marco Bertamimi (2017, Springer) 
    - `Python for Experimental Psychologists <https://www.amazon.co.uk/Python-Experimental-Psychologists-Edwin-Dalmaijer/dp/1138671576>`_ by Edwin Dalmaijer (2017, Routledge)

So, let's go on and learn some :ref:`builder3Hrs`...
