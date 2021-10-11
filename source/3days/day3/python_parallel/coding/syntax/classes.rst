.. _classes:

Classes
================

Everything in Python is an 'object'. Everything has data stored inside it and has methods that allow that data to be accessed or modified. For instance, a string is an object whose data are the values of the letters and whose methods are `upper()`, `lower()`, `split()`.

We can make our own classes of object too! This is Object-Oriented Programming (OOP).

Do I really need this?
-------------------------------

A class is just a collection of functions and variables to store/retrieve/modify related data.

Classes aren't essential for most programming of experiments, but if you're comfortable with this object-oriented concept of programming, and comfortable with how to create functions already then classes provide you with a way to create your own custom objects, or to modify existing classes of object. (If you aren't yet comfortable with function definitions then leave this section until another day!)

What is a class?
---------------------

A class defines a type of object. You then create instances of the object class that are each different.

In the real world there is a class of object called bike and there are certain attributes that relate to all bikes (color, wheel size..., handlebar shape, etc.)

There are also some common *methods*, things you can *do* with all bikes (ride them, fix them, etc.)

There is also *your* bike, which has a particular set of the parameters.


.. nextslide::

In object-oriented programming it's the same. We define a class of object and that definition says what things describe individual objects of this class (usually called "instances")::

  myGrating = visual.GratinStim(win, sf=5, ori=45)

Here, ``myGrating`` is an instance of the ``GratingStim`` class

Creating Classes
---------------------

.. note::

    In Python functions that start with _ indicate internal functions/attributes that the user should probably ignore. Methods start/end with __ indicate functions that typically have special meanings to the language. For instance `__init__` is a function that is run when an object is created, `__str__` is a function that is run if an object is being converted to a string representation etc.

Let's define a simple class to represent a moving dot (we'll stick to one axis of motion for simplicity).

We'll give our class two methods, one to initialise it and another to report the position for a point in time.

To know where a dot is at any point in time we would need to know its start position and rate of motion.

I usually give class names a capital letter so, when I do dir() on my modules, I immediately know which things are classes and which are simple functions.

.. nextslide::

::

    class Dot:
        def __init__(self, startPos, speed):
            self.startPos = startPos
            self.speed = speed
        def getPos(self, t):
            """Get the location of the dot at a given time"""
            pos = self.startPos + t*self.speed
            return pos

    dot1 = Dot(2.0, 1.5) #this is really just a call to the Dot.__init__() function
    print(dot1.getPos(3.0)) #after 3 secs this dot should be at pos=6.5
    print(dot1.speed) #the value of self.speed can be accessed like this
    dot2 = Dot(2.0, -1.5) #each instance of the Dot is independent
    print(dot2.getPos(3.0))
    print(dir(dot2)) #what attributes does a Dot instance have?

.. nextslide::

Every class has a special function called ``__init__`` that isn't called by the user, but determines how the object is created.

Also, note that every function within the class there's an extra input argument called ``self``. ``self`` allows you to set/retrieve variables that are associated with your object. So a class method with 3 arguments should be called with 2 (``self`` is going to be given automatically).

.. nextslide::

It might be useful to have the dot keep track of time. Then we could find its current pos without having to tell it a time. Or we could use a built-in clock unless the user requests a specific time::

    import time #the time module built in to Python

    class Dot:
        def __init__(self, startPos, speed):
            self.startPos = startPos
            self.speed = speed
            self.t0 = time.time() #the current time
        def getPos(self, t=None):
            """Get the location of the dot at the current time (or
            any time, if given)"""
            if t == None:#if we were given a value for t use that, otherwise...
                t = time.time()-self.t0 #the time since t0
            pos = self.startPos + t*self.speed
            return pos

    dot1 = Dot(2.0, 1.5)
    time.sleep(1.5) #pause the script for 1.5 secs
    print(dot1.getPos()) #with no args get the current pos
    print(dot1.getPos(5.0)) #pos at some given point in time

Sub-classing
------------------

One big advantage of classes is that you can take an existing class and modify just one part of it::

    class NewStr(str):
        def sentence(self):
            #capitalise the first character
            new = self.replace(self[0], self[0].upper())
            #add a full stop
            if not new.endswith('.'):
                new = new+'.'
            return new

    x = NewStr('hello everyone')
    print(x.sentence())
    print(dir(x)) #compare this with dir of a normal string

.. nextslide::

That code created a subclass of string that has all the methods of normal strings but adds the additional method of returning itself as a `sentence()`. All other methods (including `__init__`) are untouched.

You can also replace existing methods in exactly the same way.

.. ifslides::

  That's it
  ----------------

  Go back to :ref:`day1sched`
