
.. PEP 2014 slides file, created by
   hieroglyph-quickstart on Tue Mar  4 20:42:06 2014.

.. _generalPurpose:

General purpose programming
============================================

Although Python is great for doing neuroscience and psychology, one of its strengths is that it's a really useful general purpose scripting language.

Python script to rename some files
---------------------------------------

In the :ref:`plottingPosner` section you learned how to use :func:`psychopy.gui.fileOpenDlg` to load a set of files and :func:`os.path` commands to rename them.

Let's apply that, and Python's nice string handling, to another scenario. Say I've collected a set of images from the web that are all faces, but they've come from many sources and have different filenames. I want them to be called 'face001.jpg', face002.jpg',...

Find a few images and save them into a folder.

.. nextslide::

Let's fetch images and save as new filename::

    from os import path
    from psychopy import gui
    from PIL import Image

    filenames = gui.fileOpenDlg(allowed="*.*")
    for thisFilename in filenames:
        print(thisFilename)
        fileNoExt, fileExt = path.splitext(thisFilename)
        thisImg = Image.open(thisFilename)
        thisImg.save(fileNoExt+'NEW.jpg')

.. nextslide::

But we wanted to rename our files. To do that:

    - it's handy to have the index of the filename
    - we want to use a 'formatted string' to set our filename to 001, 002, 003...
    - we will use 'rename' from the os library

.. nextslide::

Use the same script as before but at the start of the loop insert::

  from os import path, rename

Then, for our loop we'd like::

    for fileN, thisFilename in enumerate(filenames):
        ...
        folder, filenameAndExt = path.split(thisFilename)
        outName = "%s/face%03i.jpg" %(folder, fileN)
        rename(thisFilename, outName)

Python script to manipulate images
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Take any format and re-save it

Save a blurred as well as a standard copy. As before but now change our import to::

    from PIL import Image, ImageFilter

Create a filter to use (at any point in the script)::

    gaussBlur = ImageFilter.GaussianBlur(radius=2)

.. nextslide::

Use that filter on each image and save both::

    filtered = thisImg.filter(gaussBlur)
    outName = "%s/face%03i.jpg" %(folder, fileN)
    blurName = "%s/face%03i_blur.jpg" %(folder, fileN)
    thisImg.save(outName)
    filtered.save(blurName)

Sampling from the webcam
---------------------------------------

PsychoPy includes all the libraries you need to record from your webcam and present the video as a stimulus!

To record from your webcam you just need::

  import cv2  # this is the OpenCV library for computer vision
  video = cv2.VideoCapture(0)  # connect to the zeroth video camera

.. nextslide::

To present that as a PsychoPy image stimulus you need to grab the frame, convert the colors and then provide that as an image to ImageStim::

  # create your stimulus (top of script)
  camView = visual.ImageStim(win, size=[0.5, 0.5], pos=[-0.5, 0.5],
                             flipVert=True)  # webcam reads bottom to top

  for n in range(1000):
    # get a frame from the camera
    returnVal, frame = webCam.read()
    # convert color to psychopy format
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)/255.0
    camView.image = frame
    camView.draw()
    win.flip()

Making and presenting movies
---------------------------------------

Open the demos misc>makeMovie and stimuli>MovieStim. Copy the code from these demos and and save them to a new file location (so that we can edit them).

Using these demos, we are going to record the webcam, and playback the recording. 

.. nextslide::

Exercise: which lines can we steal from 'makeMovie' to record the webcam demo? (Hint: it is 2 lines)

.. nextslide::

Exercise: how can we playback the recording that we just took?

.. nextslide::

We could even manipulate the feedback from the webcam. The image taken from the webcam is just an 'imageStim', which means we can change any of the properties in `imagestim <https://www.psychopy.org/api/visual/imagestim.html>`_

What's more, we could change these dynamically.... let's make our image spin


Learning more about Python
---------------------------------------

Other examples :ref:`resampling`

Practice, practice, practice. Treat this as fun problem solving!

Using Python as a general programming language is a great way for you to get comfortable with syntax, so use it widely for any batch task you can think of.

Find ways to check that your code gives the right answers. e.g. try to analyse things multiple ways first time you run a script, or use a dataset where you know the 'real' answer.

.. nextslide:: Other resources

You should:

  - use the demos menus (in both Builder and Coder views - and pavlovia!!)
  - buy `Building Experiments in PsychoPy <https://uk.sagepub.com/en-gb/eur/building-experiments-in-psychopy/book253480>`_ (Peirce and MacAskill)
  - use the forum https://discourse.psychopy.org (but learn about giving a good question)
  - google everything. Typically takes you to

    - PsychoPy reference manual
    - StackOverflow
    - PsychoPy forum
