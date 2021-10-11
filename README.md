# workshops
Workshop materials for the PsychoPy team

## Build the slides/HTML/PDF

To build the output files from the `.rst` source files, navigate to the source folder that contains a `Makefile` that specifies how to build the documents from the source (e.g. the `3days` or `3hrs` folder), and in a terminal, type one or more of these to get the output you want:

    make html
    make slides
    make latexpdf

Building the slides (to check the layout) requires `sphinx` and `hieroglyph`:

https://www.sphinx-doc.org/en/master/
https://github.com/nyergler/hieroglyph

## Install with pip

    pip install sphinx hieroglyph

## Install with conda
The `conda` channel for `hieroglyph` doesn't seem to work:

    conda install sphinx
    pip install hieroglyph

## Possible build errors
If you receive an error like this:

    Could not import extension hieroglyph (exception: cannot import name 'copy_static_entry' from 'sphinx.util')

Your version of `sphinx` may be too recent for compatibility with `hieroglyph`, as it lacks the deprecated `copy_static_entry()` function. If so, force the installation of an older version. e.g.

    pip uninstall sphinx
    pip install sphinx==2.4

or:

    conda uninstall sphinx
    conda install sphinx=2.4

## Compiling to pdf

Note that using gif images may prevent the compilation process. To avoid this you can also make a static version of the image and use the syntax:
```
.. only:: html
    .. image:: /_images/coder_small.gif
       :width: 100 %

.. only:: latex
    .. image:: /_images/coder_small.png
       :width: 100 %
```
To make the latex file you can then use:

    make latex

And create the pdf in [texWorks](http://www.tug.org/texworks/) by opening the TEX file and running [pdfLatex](https://www.pdfconverters.net/how-to/convert-latex-to-pdf-in-windows/) to compile to pdf. 

In the source > conf.py file you will also want to change how the pdf is configured to show the date of compilation: 

    # JUST CHANGE THESE AND LET THE REST POPULATE
    year = "2021"
    release = 'September 2021'
    project = u'Workshops for PsychoPy {}'.format(year)
    copyright = u'{}, Open Science Tools'.format(year)
    authors = u'Open Science Tools'
    filebase = 'OST_Workshops'