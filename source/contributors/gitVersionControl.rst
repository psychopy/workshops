.. _gitBasics:

Version control with git
=====================================

There are lots of tutorials on the web for this, but we'll look at the basics

What is it?
------------

Version control means:

- not having to label documents
    - mydoc_final
    - mydoc_FINAL
    - mydoc_reallyFINALFINAL
    - ...
- being able to combine work of others with your own
- keeping track of what changed, when and why

.. nextslide::

By far the most widely used package for this is `Git`

- developed by Linus Torvalds (Mr Linux) in 2005 (before that SVN and CVS were the norm)
- there are a huge number of possible commands and some not very intuitive, but now many user-friendly tools on top
- unlike SVN and CVS, Git supports "distributed" version control meaning you don't need a server
- it's very fast, even for large repositories
- it's really designed for text files (don't use this for version control of Word docs or images)

What is GitHub?
------------------

GitHub is a website that allows you so work on Git repositories together. It provides a really nice user interface, and project management tools, that make it easy to collaborate on code. 

To get an idea of what Git and GitHub, together, provide take a look at:

- `the history of commits to PsychoPy's release branch <https://github.com/psychopy/psychopy/commits/release>`_
- `the current list of issues (needs work!) <https://github.com/psychopy/psychopy/issues>`_
- `the current requests for changes that need accepting/rejecting <https://github.com/psychopy/psychopy/pulls>`_
- `the contents, history and "blame" for a specific file <https://github.com/psychopy/psychopy/blob/dev/psychopy/visual/button.py>`_

Wide choice of free tools?
-------------------------------

From most flexible to easiest (some of which we can demo):

- Command line: this is "raw" git and allows everything

    - Common commands are quick to master, but some are very strange
    - It's nice being explicit - fewer errors?
    - Might be annoying to set up (e.g log in details, especially if you use 2FA on GitHub) whereas the graphical tools will do this more for you

We're going to refer to those commands to teach the basics in a moment

.. nextslide::

Graphical options:

- GitKraken: a pure Git tool, very visual and relatively easy. Faithful to Git terminology
- PyCharm: more complex editor and more complex git support. Very little you can't do here, but often with new names. If you like PyCharm for coding then you will like it for git!
- Visual Studio Code: Quite handy if you're working within
- git gui (also known as git cola): comes from the command line but then opens a simple app
- GitHub Desktop: gives you some of the features of git, enough to do basic tasks like. To start with, probably all you need
  
.. nextslide::

The great thing is that these all interact happily using the same files so you can use one or more and change your mind whenever

Jon typically uses git gui to create commits (selecting files/lines) and then command line to push/pull/branch...

Basic git concepts/terms
-------------------------


Git *can be* used just by you on your own machine to version control text files (e.g. data/analysis files):

- `git init` creates a repo
- `git add` allows you to 'stage' files ready to 'commit' (Jon uses `git gui` instead)
- `git commit` allows you to organise chunks of effort with a comment
- `git tag` allows you to keep track of particular points in your work
- `git log` to look back at the commit messages
- `git checkout` to go back/forwards in time

.. nextslide::

Git can also be used by you with your own remote repo (e.g. on GitHub, GitLab or Pavlovia)

Same commands as local use but now also:

- `git clone` to fetch the remote repo to your local machine (rather than init a new one)
- `git push` and `git pull` allow you to fetch and send your local work to the server
- `git rebase` (not really needed) if you want to insert other changes *before* your local changes

.. nextslide::

Lastly you might use Git to contribute to a larger project (like PsychoPy). The key thing here is that you probably 
don't have access to 'push' directly to the repository, so you need your own copy and then connect to both 'remote' locations.

e.g. to set up my copy of psychopy on a new machine I will do

.. code:: bash

    git clone https://github.com/peircej/psychopy.git
    cd psychopy
    git remote add upstream https://github.com/psychopy/psychopy.git
    git checkout dev
    git pull upstream dev

Then, when starting work I fetch changes from `upstream`, push to `origin` and then create a pull request (using GitHub) back to the upstream repository.

.. nextslide::

So, in a standard set up. Most people will fork the PsychoPy repository on github and then 

- remote: the server location(s) where the copy(s) of your git repo lives 
- fork: to copy an existing repo to your own space on GitHub
- origin: usually the remote that you own (e.g. your fork of github.com/peircej/psychopy)
- upstream: usually the remote that you don't own (e.g. your fork of github.com/peircej/psychopy)
- clone: to fetch a git repo to your local machine
  
Most often you create a GitHub fork of a project, then you 