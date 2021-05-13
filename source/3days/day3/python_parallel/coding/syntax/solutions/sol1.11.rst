.. _sol1.11:

Exercise 1.11 - make a 'Food' class
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

1.11 a)
=========

::

	class Food:
    def __init__(self, name, calories):
        self.name = name
        self.calories = calories


1.11 b)
=========

Add the attribute 'hungry' to the object initialisation, then ::

    def feed(self, food):
        if food.calories>100:
            self.hungry = False
