# Extending Classes

Sometimes, when you define a class, you don't necessarily want to start from scratch. Let's say you're making a "piano key" class in PsychoPy - what you effectively want is a tall, thin, white rectangle which plays a noise when clicked. Why write your own class from scratch when there's already a perfectly good Rect class, which just needs a method adding to play a sound?

## How to extend a class

This is where extending classes comes into things. Rather than creating a new class, you can extend an existing class, like so:

```python
class PianoKey(Rect):
    def __init__(self, win):
        Rect.__init__(self, win=win)
```

Adding `Rect` in brackets tells Python that your new class should have all the same methods as Rect, unless you've made a new one with the same name (this is called "overloading" or "overwriting" a method). When you make your `__init__` method, telling it how to create an instance of your class, the first thing you'll want to do is make your object as a `Rect` - you do this by calling the `__init__` function from Rect, with the first input being the current object (`self`), meaning that the object which gets `__init__`ialised is your object.

Once you've made a Rect, you can add methods and properties and everything just as you would any other class!

## What is this demo?

This demo uses this method to create an octave of keys - in `Begin Experiment`, a `PianoKey` class is defined, complete with its own `Sound` child object and method for playing the sound on request. In `Begin Routine`, an instance of this class is created for a few notes in the octave. In `Each Frame`, a `Mouse` component (the finger) checks whether it is pressed on each key, and calls its `press` method if it is.

## Your challenge...

Only a few notes in the octave are covered, the rest are missing! See if you can make a complete octave of keys by creating more instances in the `Begin Routine` tab.

If you finish early, have a go at adding inputs to the `__init__` function of the `PianoKey` class to let you specify its octave as well as its note. You can find the inputs for a `Sound` component [here](https://psychopy.org/api/sound.html#sounddevice-sound), showing how to change the octave for the `Sound` component once you have the desired input.

