.. _commit and make a pull request:

Committing and making a pull request
==========================================

- time to get your translations into |PsychoPy|
- time to work towards a *pull request*

  - *stage* > *commit* > *push* > *pull request*

Steps on the way to a pull request
-------------------------------------
- on your local copy

  - Step 1: *Stage* the changes you made
  - Step 2: *Commit* staged files with an informative message 
- online (to *GitHub*)

  - Step 3: *Push* the *Commit* to *Origin*
  - Step 4: Make a *pull request* to *Upstream* from *Origin*
- online and local

  - Step 5: Clean up

What *Git* tracks
---------------------

- all changes in a directory

  - the same directory where the hidden ``.git`` file resides 
- what should you put into a single *commit*?
  
  - related changes
  - *unrelated* changes in *commit* creates a confusing version history
- this is the purpose of *staging*

.. note::
   You can manually blindfold *Git* to certain files or filetypes by listing them in a ``.gitignore`` file, which is also hidden. 

*Stage* related changes
-------------------------

- *Staging*

  - tells *Git* which files you want to put into a single commit
  
    - typically files that are related to each other  
    - often a subset of all the files you've recently worked on in the project

Step 1: *Stage* your changes
-----------------------------

- *GitHub Desktop* stages changed files by default

  - Look at the far left under the tab labeled as follows: ``Changes``
  - If a file is staged, it has a checkmark next to it
- If you **don't** want that file to go into your next commit, you'll need to un-check it

  - To un-check the boxes
  
    - First un-check the top box
    
      - This will un-stage everything
    - Second, check the boxes you want to stage for your next commit

All that said...
--------------------

- After the initial setup, most translators will be working on just a few files anyway, i.e.:
  
  - ``messages.po``
  - ``messages.mo``
  - (and maybe) ``tips...txt``
  
- So 99% of the time, you'll just leave those 2-3 boxes checked anyway 

Step 2: The commit
---------------------

At the bottom of the same tab, ``Changes``, you'll see two boxes

- The one on top says: ``Summary (required)``
- The one below that says: ``Description``

- The top one is a commit message and it's required for every commit in *Git*

2a: The commit message prefix
-----------------------------------

- The convention in |PsychoPy| is to append an UPPERCASE prefix to every commit message
- Examples:

  - *BF:* for *bug fix*
  - *FF:* for *feature fix*

Why the prefix?
----------------------

- The prefixes help administrators search for key changes to the project
- Without them, they'd have to sift through all changes to a project when, in fact, they knew they only wanted to search through, say, bug fixes (BFs)

2b: The prefix for translations
--------------------------------
- The one for all translations should be as follows:

  - *DOCS:*
- This typically refers to documentation, but it also refers to changes to |PsychoPy| that do not affect code and how |PsychoPy| runs
- In other words, it's a safe change to |PsychoPy| that won't "break" anything

2c: The commit message itself
------------------------------------

- The commit message should summarize what all the changes in the commit do as a single unit

  - If you're having difficulty with this, consider splitting your commit into two or more 
- The usual convention is to start with a verb in the imperative mood (i.e., a command)

2d: The commit message for translations
-----------------------------------------

- For translations, this should be fairly easy most of the time
- For example:

  - ``DOCS: Add Spanish translations a-c``

  - ``DOCS: Add Spanish translations d-g``

  - ``DOCS: Add start-up tips in Hebrew`` 

2e: a description (optional)
------------------------------------

- Sometimes it's very clear what a particular commit is going to do from the commit message alone, for example:
  
  - ``DOCS: add start-up tips in Yoruba``

- But sometimes you feel that the commit message is just not enough

  - This is when you use a description
  - No character limit, but try to be succinct 
  - If your description needs upwards of 100 characters, it might be worth splitting your commit into two or more commits

.. note:: All that said, it would be a bit strange for a translation to need a description. The commit message should suffice in almost all cases.

2e: Commit
------------

- When you are ready to commit

  - Click the button at the bottom of the same tab:

    - ``Commit to [the name of your current branch]``

- for example: ``Commit to Korean-translations`` 

Step 3: *Push* to *origin*
----------------------------

- The commit is like sealing an envelope you want to send

  - You still need to mail it in
  - This is done through a *push*

Where you can and cannot push directly to
--------------------------------------------

- You can push directly to your own fork on GitHub
- But you cannot *push* directly to the main (*upstream*) repository at ``https://github.com/psychopy/psychopy``
  
  - If anyone could just push to *upstream*, the whole open-source world would probably collapse
- Instead, you first *push* to *origin* (your own copy of the the |PsychoPy| repository, located in your own *GitHub* account)
- Afterwards, you make a *pull request* on *GitHub* to *upstream*

3a: how to push in *GitHub Desktop*
--------------------------------------

- Select the following:

  - ``Repository`` > ``Push``
  - Or click the ``Push origin`` tab (which should have replaced the ``Fetch origin`` tab)

Step 4: The pull request
----------------------------------------------

- Now your changes should be on *origin*
- But you'll see a note probably saying that you're one commit ahead of *upstream* 
- To make them identical, you need to perform a *pull request*
  
  - (you're "requesting" that adminstators of *upstream* "pull" your changes in, like "Pull me, please.")  
- This *can* be done directly from *GitHub Desktop*, but it's not completely clear what that's doing

  - So I tend to go to *GitHub* and make the pull request from there 

4a: Selecting the right branch
------------------------------------

- Go to your fork of the repository on *GitHub* (i.e., *origin*)
- Select the branch that you just made the commit to

  - e.g., ``portuguese-translation``
  - Branches are located in a little pull-down menu at the upper left

- *GitHub* should detect that your latest commit is probably awaiting a *pull request* to *upstream*

  - Look for a yellow banner at the top with a note about the recent commit, and a green button with the following message:

  ``Compare and pull request``

- Click that button
- If it's not there

  - you can start a pull request from either of the following:
  
    - the ``Pull requests`` tab at the top
    - the ``Contribute`` tab next to the ``Sync fork`` tab

4b: Double-checking source and destination
-------------------------------------------

- You should now be switched to the *upstream* repository at ``psychopy/psychopy``
- And you should see a screen with the following title: ``Comparing changes``
- There should be four pull-down menus, labeled as follows, from left to right:

  - ``base repository: psychopy/psychopy``
  
    - (this refers to the *upstream* **repository**)
  
  - ``base: release`` 
  
    - (the appropriate **branch** on *upstream* to merge *into*)
  
  - :raw-html:`&larr;` (showing you the direction of the pull request) 

  - ``head repository: [your own GitHub account]/psychopy``
  
    - (this refers to your forked *origin* **repository**)
  
  - ``compare: [your branch for the translation, e.g., portuguese-translation]``
  
    - (the appropriate **branch** on *origin* to merge *from*)

4c: Double-checking changes
------------------------------------

.. warning::
   If you see many more file changes than you were expecting, then you might be on the wrong branch(es)
.. note::
   If it says *There isn't anything to compare*, you probably didn't yet push the commit from your local copy to *origin*

.. PB - test this with real pull request

4d: Will your changes merge?
------------------------------

- Hopefully, you see the following directly below the information covered in the last slide
  
  - a green check mark
  - a message next to it that says *Able to merge. These branches can be automatically merged.*
- If you do not, then one of the following might have occurred

  - You are trying to merge to or from the wrong branch (or both)
  
    - Double check your branches (see previous slide)
  - Another translator has worked on the same files from the same branch, and then submitted a pull request before you did
  
    - In this case, you could have a merge conflict

.. PB - add a strategy to deal with this

4e1: Adding a description
-------------------------------

- *description* 

  - optional
  - can be useful to administrators if the changes are complex
  - answers the *what*, *why*, *how*, etc. of the *pull request*

4e2: Is a description necessary?
------------------------------------

- But truth be told, descriptions generally won't be of much use to translators
  
  - A *pull request* for a translations is only going to involve 2-3 files (though there may be many, many lines changed)
  - But even if there are many lines changed, the administrators at |PsychoPy| will probably not be able to review translations in much detail since they probably won't speak the language

4f: Extra responsibility
---------------------------

- From the last slide

  - *the administrators at |PsychoPy| will probably not be able to review translations in much detail since they probably won't speak the language*

- In this sense, translators carry more responsibility than even someone adding new features to |PsychoPy|
- This is because administrators will probably be forced to "rubber stamp" your proposed changes 
- Translate responsibly ;)

4g: Subsequent commits
------------------------

- If you make further *commits* before the *pull request* is merged in by the administrators
  
  - don't worry
  - your commits will automatically be incorporated into the previous *pull request* 

.. PB - I need to work on this. I don't quite understand it yet.

Step 5: Clean-up
--------------------

- There's a process to clean everything up
- Otherwise, things can eventually get confusing

5a: Check to see if your *pull request* was merged in
-------------------------------------------------------------

- Wait for your *pull request* to be approved
- If you don't get an email, you can check the *upstream* repository
  
  - Go to ``psychopy/psychopy``
  - Click ``Pull requests``
  - Find the pull-down menu for ``Author`` and choose your name
  - Check to see if your particular commit is ``Open`` or ``Closed``
    
    - ``Open`` means it has **not** yet been merged in
    - ``Closed`` means that it **has** been merged in 

5b: switch branches on *origin*, sync, and delete
---------------------------------------------------------

- Switch to the *release* branch on your own *GitHub* account
- Synchronize it with *upstream* (*release* with *release*)
  
  - Click: ``Sync fork``

- Delete the branch you created to work on the translation (e.g., ``hindi-translation``)
    
  - Click: ``# branches``
    
    - (where ``#`` will be replaced by the number of branches in your repository) 
  - Find the working branch under ``Your branches`` (e.g., ``hindi-translation``)
  - Click the trash-can icon to the right of it

5c: delete the local branch
----------------------------------

- In *GitHub* desktop

  - Go to ``Branch > Delete``

5d: Continual *Git* workflow
-----------------------------------

**Again!!??**

Yes

- From *GitHub* on your *fork*
 
  - (Make sure you are on the *release* branch)
  - *Sync fork* (from *upstream*)

- From *GitHub Desktop*
  
  - ``Repository`` > ``Pull``
 
FINISHED!! 
-------------