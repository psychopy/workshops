
.. PEP 2014 slides file, created by
   hieroglyph-quickstart on Tue Mar  4 20:42:06 2014.

.. _generalPurpose:

General purpose programming
============================================

Although Python is great for doing neuroscience and psychology, one of its strengths is that it's a really useful general purpose scripting language.

Python script to rename some files
---------------------------------------

In the :ref:`dataAnalysis` section you learned how to use :func:`psychopy.gui.fileOpenDlg` to load a set of files and :func:`os.path` commands to rename them.

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

Use the same script as before but for our loop we'd like::

    for fileN, thisFilename in enumerate(filenames):
        ...
        folder, filenameAndExt = path.split(thisFilename)
        outName = "%s/face%03i.jpg" %(folder, fileN)
        thisImg.save(outName)

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

Resampling statistics
---------------------------------------

A scripting language like Python is also great for doing resampling statistics procedures (bootstrapping, Monte Carlo simulations etc). Not everyone knows about those so we'll need to go through the logic of one such test while we create some code. This one is called a 'permutation test'.

.. nextslide::

Take the heights of 7 dwarfs and 13 smurfs::

    smurfs = [13.6, 10.3, 10.0, 16.0, 12.4, 9.1, 14.5, 10.2,
            8.9, 11.1, 15.9, 9.5, 10.4]
    dwarfs = [11.0, 8.9, 8.0, 14.0, 11.4, 8.1, 18.5]

I have a hypothesis that smurfs are just dwarfs painted blue. If so then they are really one population. We could test whether their heights are significantly different.

.. nextslide::

To get the difference in mean heights::

    import numpy as np
    smurfMean = np.mean(smurfs)
    dwarfMean = np.mean(dwarfs)

    print("smurfs=%.1f, dwarfs=%.1f" %(smurfMean, dwarfMean))

Was that unlikely to occur by chance?

.. nextslide::

Our Null Hypoth is that smurfs and dwarfs are the same. They are one population::

    popn = smurfs+dwarfs

    np.random.shuffle(popn) #this shuffles the population 'in place'
    resampSmurfs = popn[0:len(smurfs)] #from 0:13
    resampDwarfs = popn[len(smurfs):] #from 13:end
    print(len(resampSmurfs), resampSmurfs)
    print(len(resampDwarfs), resampDwarfs)

If smurfs and dwarfs are the same, this resample is as likely as the original sample

.. nextslide::

Given how easy it is to create a loop in Python, we could create thousands of those resamples and find out how unlikely our original was, according to the Null Hypoth::

    nResamples = 5000
    allDiffs = []
    for sampN in range(nResamples):
        np.random.shuffle(popn) #this shuffles the population 'in place'
        resampSmurfs = popn[0:len(smurfs)] #from 0:13
        resampDwarfs = popn[len(smurfs):] #from 13:end
        #find the difference in means
        thisDiff = np.mean(resampSmurfs) - np.mean(resampDwarfs)
        allDiffs.append(thisDiff)

    plt.hist(allDiffs)
    plt.show()

.. nextslide::

After our loop we can process the set of differences we measured and see what
distribution of values occurs (this is the Null Distribution)::

  origDiff = dwarfMean-smurfMean
  # 2-sided test is about the prob of being bigger magnitude (unsigned)
  # so we take abs() of the
  nGreater = sum(np.abs(allDiffs) > np.abs(origDiff))
  pPermTest = nGreater/nResamples

  print('permutation test: p=%.3f (two tails)' %(pPermTest))

.. nextslide::

We could compare the result we got with that from a traditional t-test::

    from scipy import stats  # add this to top of script?
    #for comparison let's do an independent-samples t-test
    t, p = stats.ttest_ind(smurfs, dwarfs)
    print('t-test: t=%.3f p=%.3f' %(t, p))

With programming skills, computing either the traditional or resampling estimates of `p` is easy

.. nextslide::

Note that:

    - the permutation test does not assume normal distribution
    - should agree, if there **is** a normal distribution
    - does not give you the (incorrect) belief that there is a single 'true' probability value (all estimates of p are simply estimates)
    - means nothing if your data are not representative (as with t-test but most people have forgotten)
    - needs thought to get right (maybe this is a good thing?)


Learning more about Python
---------------------------------------

Practice, practice, practice. Treat this as fun problem solving!

Using Python as a general programming language is a great way for you to get comfortable with syntax, so use it widely for any batch task you can think of.

Find ways to check that your code gives the right answers. e.g. try to analyse things multiple ways first time you run a script, or use a dataset where you know the 'real' answer.

.. nextslide:: Other resources

You should:

  - use the demos menus (in both Builder and Coder views)
  - buy `Building Experiments in PsychoPy <https://uk.sagepub.com/en-gb/eur/building-experiments-in-psychopy/book253480>`_ (Peirce and MacAskill) out very soon
  - use the forum https://discourse.psychopy.org (but learn about giving a good question)
  - google everything. Typically takes you to

    - PsychoPy reference manual
    - StackOverflow
    - PsychoPy forum
