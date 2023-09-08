.. _setting up version control:

Setting up version control
===============================

- many tutorials on the web for this
- just the basics here

What is *version control*?
------------------------------

- Similar to *Google Drive* and *MS 365*
    
  - each such document (e.g., a *Google Doc*) contains a *version history* 
    
    - go back and forth "in time" to look at (and even revert to) older versions of the document

- What about mulitiple files and folders?
  
  - *Git* and *GitHub*
  - You can also go "back and forth in time"
    
    - More complex as they account for multiple documents
    
What is *Git*?
----------------

- the most dominant tool worldwide for tracking and managing changes to software code and documentation

  - tracks an entire folder (not just a single file)
  
    - *repository* 
    
      - the folder (and all its subfolders) that you're tracking 
- runs on your computer (not online)


**NOTE**: *Git* works best with plain-text documents (UTF-8 encoding included), but not binary files like *Microsoft Word* or *Excel* documents

What is *GitHub*?
------------------

- a web-based service (not on your computer)
- centralizes *Git* repositories in the cloud
  
  - (literally an online *hub* for *Git* repositories) 
- simplifies collaboration

Basic *Git* workflow and terminology
--------------------------------------

.. image:: ../_images/openSourceGitFlow.png
  :align: center
  :width: 500
  :alt: Image of a typical, seven-step workflow for open-source software projects, from initial setup to pull requests (Creative Commons license, courtesy of openclipart.org, image `278845`, git-opensource-workflow, by developingo)

..

(Creative Commons license, courtesy of openclipart.org, image `278845`, git-opensource-workflow, by developingo)

Step-by-step
----------------

Now we'll go through setting up the *Git* workflow for |PsychoPy|

Step 1: Get *Git* and *GitHub* working
----------------------------------------

* *Git* is free software for your computer
* *GitHub* is an free online system, for which you need to sign up

Step 1a: Install *Git*
------------------------

- download *Git* |downloadGitHere| 

  - (the binary installer is easiest)
  - You can just choose the defaults 

- If you need it, the following |watchHere| quickly shows you how to do this on both Mac and Windows
  
  - The Windows installation process involves clicking through more screens

.. |downloadGitHere| raw:: html

  <a href="https://git-scm.com/downloads" target="_blank">here</a>

.. |watchHere| raw:: html

  <a href="https://youtu.be/F02LEVYEmQw" target="_blank">YouTube video</a>

Step 1b: Sign up for *GitHub*
------------------------------

- Go to |gitHubOnline|
- Click the following button: ``Sign up for GitHub``
- Provide your email, then create a password and username
- Verify that you're a human
- Enter the launchcode that was sent to your email
- You can accept the defaults through the rest of the options
  
  - If asked *How many team members will be working with you*
  
    - Just answer with: ``Just me`` 

.. |gitHubOnline| raw:: html

  <a href="https://github.com/" target="_blank">GitHub online</a>

Step 2: *Fork* the *psychopy* repository
------------------------------------------

- What is *forking* on *GitHub*?

  - for most users

    - just copying an existing repository already on *GitHub* somewhere
    - and making it your own, on your own, online *GitHub* account

**NOTE**: Technically and more generally, it's copying a repository, while also disconnecting it from previous committers

Step 2a: Find the *psychopy* repository
-----------------------------------------

- While logged in to *GitHub*
    
  - Go to the search box at the upper left
    
    - type in: `psychopy`
  - You should see the following at the top of the search list: `psychopy/psychopy` 
  - Click it
  - You should land here: ``https://github.com/psychopy/psychopy``

Step 2b: Ensure you are on the *release* branch
------------------------------------------------
**NOTE**: more on *branches* later

- |PsychoPy| has two branches: *dev* and *release*
- How to check you are on the *release* branch: 

  - The pull-down menu near the upper left should say *release*, not *dev* (or anything else for that matter)

.. image:: ../_images/trnslWkshp_releaseBranchBeforeForking.png
  :align: center
  :width: 300
  :alt: Screenshot of what the upstream repository at psychopy/psychopy should look like when the release branch is selected

..

Step 2c: *Fork* the *release* branch
----------------------------------------

- Find the ``Fork`` pull-down menu located near the upper right corner

.. image:: ../_images/trnslWkshp_findForkMenu.png
  :align: center
  :width: 300
  :alt: Screenshot of where the pull-down menu is to fork a repository

..

- Choose the following: ``+ Create a new fork``
- Check the box labeled as follows: ``Copy the release branch only``

What is a *fork*?
------------------

- a *fork* is your own (online) copy (on *GitHub*) of the all the code required to build the current (in this case, *release*) version of |PsychoPy|
- it is "yours" in the sense that...
  
  - it is now disconnected from all other users
  - you are free to modify it 
  
    - for your own purposes (it's open source, after all); or
    - in order to contribute back to the project (more common)
  
    - The latter is what you'll be doing as translators

Caveat: How it's *not* yours
---------------------------------

Keep in mind that |PsychoPy| is **not** yours in the sense that you still need to abide by the the particular |license-for-use| that applies to |PsychoPy|

.. |license-for-use| raw:: html

  <a href="https://psychopy.org/about/index.html#license-for-use" target="_blank">license</a>

Why the *release* branch?
--------------------------------

- the *dev* branch

  - for *major* changes to |PsychoPy| that need to be tested extensively so that they don't "break" the software (e.g., new features, deprecation, etc.)
  - Changes to the *dev* branch are released about twice a year only 
    
**NOTE 1**: At the end of this workshop, I will cover a situation when you might want to move your focus over to the *dev* branch 

**NOTE 2**: You yourself can create branches as well. Normally, you would do this only when you are working on very different aspects of a project (e.g., both translations and bug fixes)

What is the *release* branch then?
------------------------------------

- The *release* branch 

  - for **minor** (aka "bug fix") releases of |PsychoPy|, where changes can't really "break" anything
  
    - bug fixes, documentation typos, etc.
    - and critically, **translations**
  - Changes to the *release* branch are made public much more often

- Therefore

  - since translations can't break code, they normally go under the *release* branch 

Step 3: download a tool to avoid using the command line
-------------------------------------------------------------

- Command-line *Git* actually turns out to be very useful
- But it might be intimidating at first
- So there are many GUIs to make *Git* easier to use

Popular tools
---------------

- popular, but relatively complex GUI tools for working with *Git*

  - *GitKraken*, *PyCharm*, *Visual Studio Code*, etc.
  
- ideal starter option for translators: 

  - |githubDesktop|
  - Why?

    1. free
    2. retains the native terminology of *Git*
    3. simpler, and therefore, less confusing

.. |githubDesktop| raw:: html

  <a href="https://desktop.github.com" target="_blank">GitHub Desktop</a>

Disadvantage of *GitHub Desktop*
---------------------------------------

- Not designed for *Linux* 
  
- If you're using *Linux*, try one of the following:
    
  - install the |githubDesktopForLinux|
  - install |gitFiend|, which is cross-platform, but originally designed for *Linux*
    
    - just as easy to use as *GitHub Desktop*, perhaps easier
    - works on Windows and Mac as well

.. |githubDesktopForLinux| raw:: html

  <a href="https://medium.com/@lorenzozar/installing-github-desktop-on-linux-ec2aefa7ccdc" target="_blank">GitHub Desktop fork for Linux</a>

.. |gitFiend| raw:: html

  <a href="https://gitfiend.com/" target="_blank">GitFiend</a>

Minor note on *Git*-interface tools
------------------------------------

- *Git* depends on a hidden folder in the most superordinate directory of any project:

  - ``.git`` (required, the *sine qua non*, actually)
There is also usually a hidden ``.gitignore`` file there (though it's technically optional)

- Software tools like *GitHub Desktop* and *GitKraken* and even command-line *Git* simply refer to the ``.git`` folder and the ``.gitignore`` file
- Therefore, you can switch among the various *Git* interfaces seamlessly
- This will make more sense later, but it's not that important for now

Step 3a: Download and install *GitHub Desktop*
-----------------------------------------------

- Go to: `https://desktop.github.com/ <https://desktop.github.com/>`_ 

  - Download and install the appropriate version
  - If your computer uses an *Apple silicon* chip (*M1*, *M2*), see the next slide
  
- Linux users can download *GitFiend*
  
  - `https://gitfiend.com/ <https://gitfiend.com/>`_
- (Note for users of *Apple silicon* chips on next slide) 

Note for users with *Apple silicon* chips (*M1*, *M2*)
------------------------------------------------------- 
      
- The appropriate download is under the heading at the bottom:
      
  - ``Apple silicon?``
- Ultimately, the download should have an ``..arm-64`` extension instead of ``..x-64``
- But the *Intel* version will actually work

  - just a little bit slower as it has to go through *Rosetta 2*, *Apple*'s way of translating chip instructions from *Intel* to *Apple Silicon*

Step 4: Cloning
------------------

- *Cloning* involves downloading files from an online *Git* repository to your computer
  
  - Unlike *forking* it doesn't disassociate anyone
  - So if you clone your online fork (which is just you)
  
    - you will remain as the sole committer 

Step 4a: How to start cloning from *GitHub Desktop*
-----------------------------------------------------

- in *GitHub Desktop*

  - ``GitHub Desktop > Settings > Accounts``

    - Sign in using your credentials to *GitHub.com* (not *GitHub Enterprise*)
  - ``File > Clone repository``
    
    - choose *psychopy* 

Step 4b: How to finish cloning
--------------------------------
  
- *psychopy* should be listed because it's already forked in your online account
 
  - under ``Local Path`` at the bottom, choose a **logical** place on your computer for the cloned repository (e.g., not your desktop)
  
    - click ``Clone``
    - This might take a minute, depending on your connection speed

The result of cloning
-----------------------

- full, updated\* copy on your local computer of all the files from current release of |PsychoPy|

  - including all the currently available localization folders
  - though you *may* need to add a new one (more on this soon)
- Fully connected to your online fork of the repository on *GitHub* 

\* It's updated at the moment you clone it, but as soon as someone else gets their commit(s) pulled in *upstream*, yours will be out of date. But there's a way to deal with this. I will cover this quite soon below.
 

Nomenclature after forking and cloning
-----------------------------------------

- **origin**

  - your fork of the original repository on *GitHub*
    
    - for *your* account, this is as follows
  
      - ``[your-github-account-name]/psychopy`` 
      - e.g., ``johndoe/psychopy``
- **upstream**

  - the original repository on *GitHub*
    
    - always as follows for |PsychoPy|
  
      - ``psychopy/psychopy``

What does all this mean?
----------------------------

- You have established a direct back-and-forth between you and your online fork on *GitHub* 
  
  - You can manipulate files without interfering with anyone else
- But now

  - you can contribute your changes to the original repository from via *pull requests* online
  - In *GitHub* jargon, you would make a *pull request* from *origin* (your online, forked repository) to *upstream* (the main *psychopy* repository)

- The importance of this will become clear later 

What about the name for the repository on my own computer?
------------------------------------------------------------

- no special name for the repository on your local computer

  - most people say "my local copy"?
- why not *clone*?

  - would be a good name
  - but few seem to use it (or at least I haven't heard it in my limited experience)
  
    - maybe because it's awkward or creepy to say, "My clone" 
  - Fortunately, it's not important either

Done setting up *Git* and *GitHub*
------------------------------------

- ... but... what about the *-flow* in *workflow*?
- The next section is about keeping your repository up to date

Step 5: Continual *Git* workflow
------------------------------------

- **synchronize your repository frequently with the upstream repository**
  
  - any time you begin work\*
  - helps you avoid *merge conflicts*
  
    - which might happen if two translators translate the same string 
  
- merge conflicts = minor headaches to fix by maintainers 
- but better to avoid them altogether

\* And follow up any work fairly soon with a commit, push, and pull request (more on this later)

5a: *Sync* (from *upstream*) to *origin*
-------------------------------------------

- Go to your *fork* online
 
  - (again, this is your copy of the *psychopy* repository on *GitHub*, aka *origin*)
- Make sure you're on the *release* branch

  - (The pull-down menu at the upper-left shouldn't say ``dev``, but rather ``release``. Use that same pull-down menu to choose ``release`` if you have to)
- Click: ``Sync fork`` (located a bit to the right)\*
 
\* Note that this can only do something if there is, indeed, something new to synchronize from *upstream* 

5b: *Pull* from *origin*
--------------------------

- Go back to *GitHub Desktop* on your local machine
- ``Repository > Pull``

  - This updates your local copy (your clone) with your fork (*origin*), which was just synchronized with the *upstream* repository
  - Now all three should be identical
- Complete this step after the one before it, each time before you begin work on a new set of translations 

  - The reason is that other translators on your team may have changed things since you last did, making your copy out of date

Alternative: *pull* then *push*
---------------------------------

There is an alternative to the *sync-pull* approach

- *pull* from *upstream*, then *push* to *origin*

- ``Branch > Update from upstream/master``
  
  - (It might tell you that it's already up to date) 
- ``Repository > Push`` (if there were changes from *upstream*)

**NOTE**: This is faster, but I tend to avoid it because my understanding of *Git* is limited, and this allows me to keep things simple.

Step 6: Continual *Git* workflow
-----------------------------------

- Yes, this slide is repeated
- Why?

  - to emphasize that keeping one's repository up to date is a **common routine**

    - not something that you do once and forget about
    - or only do occasionally

On to :ref:`working on translations`