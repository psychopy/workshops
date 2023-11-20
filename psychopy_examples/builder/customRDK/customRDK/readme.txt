Custom RDK
==================


In this version of the RDK "experiment" we've created a new class in the new_RDK.py file. What we actually did was create a sub-class of the original (from psychopy.visual.dot). We've left nearly all the code to work as in the original but we have override the existing _update_dotsXY function.

We ignore all the other attributes of the class and just make ALL the dots grow or shrink by a fixed amount by changing their "_verticesBase" (and then we make sure to call self._updateVertices() so that the changes are reflected onscreen).

To make use of our new class we create a Code Component in the experiment and overwrite the visual.DotStim class with our new one. As long as our new one doesn't change the structure of the calls then this works just fine!

The idea of this is just to show you that 
