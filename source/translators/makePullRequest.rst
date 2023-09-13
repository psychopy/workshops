.. _committing and making pull requests:

More information on Git workflow
==========================================

You have already practiced this workflow, but here is some more information

Steps on the way to a pull request
-------------------------------------

1. *stage* (local copy)
2. *commit* (local copy)
3. *push* (local copy to *origin*)
4. *pull request* (*origin* to *upstream*)
5. clean up (if you're working on a branch you created)

What does *Git* track?
------------------------

- answer:

  - **ALL** changes in a directory (where the hidden ``.git`` folder resides) and its subdirectories
  
    - unless you list that file or file type in the ``.gitignore`` file
- what should you put into a single *commit*?
  
  - just related changes
  
    - *unrelated* changes in a single *commit* can lead to a confusing version history
- this is the purpose of *staging*

*Stage* related changes before committing them
--------------------------------------------------

- *Staging*

  - *Stage* files to tell *Git* you want them in a single commit
  
    - typically, files that are related to each other
    - often just a **subset** of all the files you've recently worked on in the project

Step 1: *Stage* your changes
-----------------------------

- Look at the far left under the tab labeled as follows: ``Changes``
- If a file is staged, it has a checkmark next to it
- If you **don't** want that file to go into your next commit, you'll need to un-check it

  - To un-check the boxes, un-check the top box
  - This will un-stage everything
- Next, check the boxes you want to stage for your next commit

All that said...
--------------------

- After the initial setup, most translators will be working on just a few files anyway, i.e.:
  
  - ``mappings.txt``
  - ``messages.po``
  - (and maybe) ``tips...txt``
  
Step 2: The commit
---------------------

- At the bottom of the same tab, ``Changes``, you'll see two boxes

  - The one on top says: ``Summary (required)``
  - The one below that says: ``Description``

- The top one is a commit message

  - required by *Git* for every commit

    - (there is no way around this)
- The bottom one, ``Description`` is optional 

2a: The commit message prefix
-----------------------------------

- convention established by the maintainers at |PsychoPy|

  - append an UPPERCASE prefix to every commit message
- Examples:

  - *BF:* 
  
    - for *bug fix*
  - *FF:* 
  
    - for *feature fix*

Why the prefix?
----------------------

- help maintainers search for key changes to the project
- Otherwise, they'd have to sift through all changes to a project when, say, they knew they only wanted to search through bug fixes (BFs)
  
2b: The prefix for translations
--------------------------------
- for all translations:

  - *DOCS:*
- usually for documentation
- but also for changes that cannot "break" the software
- *DOCS:* may change to something like *TRNSL:* in future

  - Jon Peirce will let you know if this change occurs 

2c: The commit message itself
------------------------------------

- summary of what all the changes in the commit do as a single unit
- The standard convention is to start with a verb in the imperative mood (i.e., a command)

- For example:

  - ``DOCS: Add translations to Portuguese in Brazil``

  - ``DOCS: Add start-up tips to Modern Standard Arabic`` 
- Use English, naturally, as the maintainers at |PsychoPy| probably don't speak your language 
- Remember that there is a 50-character limit 

2d: a description (optional)
------------------------------------

- Sometimes commit messsage is clear
  
  - ``DOCS: Add start-up tips to Yoruba in Nigeria``

- Sometimes not possible

  - This is when you use a description
  - No character limit
  
    - but try to be succinct 
  - more than 100 characters?
  
    - split your commit into two or more commits?

**NOTE**: All that said, messages alone should suffice in almost all translation cases

2e: Commit
------------

- When your changes are ready and staged, and you have a commit message

  - Click the button at the bottom of the same tab:

    - ``Commit to release``
  
  **NOTE**: If you're contributing to |PsychoPy| in other ways, you probably want to make sure you add a new branch for translations.

Step 3: *Push* to *origin*
----------------------------

- The commit is like sealing an envelope you want to send in the mail

  - It's still just on your computer
  - You still need to "mail it in" to **your** online repository
  - This is done through a *push*

Why two steps? A *push* then a *pull request*?
-----------------------------------------------

- **can** push directly to your own fork on GitHub
- **cannot** *push* directly to the main, *upstream*, repository at ``https://github.com/psychopy/psychopy``
  
  - If just anyone could do that, the whole open-source world would probably collapse
- Instead

  1. first *push* to your fork at *origin*
  2. Then go to your fork on *GitHub* and make a *pull request* from there to *upstream*

**NOTE**: You *can* make a *pull request* directly from *GitHub Desktop*, but I'm not completely sure what the implications of that are. I'm scared of it, to be honest.

3a: how to push to *origin* in *GitHub Desktop*
--------------------------------------

- Select the following:

  - ``Repository > Push``
  - Or click the ``Push origin`` tab
  
    - (this should have replaced the ``Fetch origin`` tab at the upper-right)

Step 4: The pull request
--------------------------

- changes should be on *origin* (online)
- should see a note saying that you're one commit ahead of *upstream* 

  - This is good
  
    - your translations are new, and need to be incorporated into the main project 
- To initiate the process of making them identical, you need to make a *pull request*

4a: "Pull request"???
------------------------

- terminology a little counter-intuitive
  
  - You're not asking permission to pull changes yourself
  - Rather, you're "requesting" that the maintainers of *upstream* "pull" your changes in

  - like "Pull me in, please."
- (if that helps) 
 
4b: Go to the right branch on *GitHub*
----------------------------------------

- Go to your fork of the repository on *GitHub* (i.e., *origin*)
- Select the branch that you just made the commit to

  - probably ``release``, but possibly something like ``portuguese-translations`` if you have other projects (e.g., bug fixes)
- Branches are located in a little pull-down menu at the upper left
- Once there, *GitHub* should indicate that your latest commit is probably awaiting a *pull request* to *upstream*

4c: Make the pull request
----------------------------

- Look for a banner at the top with a note about the recent commit, and a green button with the following message: ``Compare and pull request``
- Click that button
- But if it's not there

  - you can start a pull request from either of the following:
  
    - the ``Pull requests`` tab at the top
    - the ``Contribute`` tab next to the left of the ``Sync fork`` tab

4c1: Double-checking source and destination
-------------------------------------------

- You should now be switched to the *upstream* repository at ``psychopy/psychopy``
- And you should see a screen with the following title: ``Comparing changes``
- There should be 4 pull-down menus, labeled as follows on the next slide, from left to right

4c2: Source and destination
------------------------------

- ``base repository: psychopy/psychopy`` (this refers to the *upstream* **repository**)
  
- ``base: release`` (the appropriate **branch** on *upstream* to merge *into*)
  
- :raw-html:`&larr;` (showing you the direction of the pull request) 

- ``head repository: [your own GitHub account]/psychopy`` (this refers to your forked *origin* **repository**)
  
- ``compare: release`` (the appropriate **branch** on *origin* to merge *from* [unless you created a new branch])

4d: Double-checking changes
------------------------------------

**WARNING**: If you see many more file changes than you were expecting, then you might be on the wrong branch

**NOTE**: If it says *There isn't anything to compare*, you probably didn't yet push the commit from your local copy to *origin*

4e: Will your changes merge?
------------------------------

- Hopefully, you see the following directly below the information covered in the last slide
  
  - a green check mark
  - a message next to it that says the following:
  
    -  *Able to merge. These branches can be automatically merged.*

4f: What if they did not?
----------------------------

- If you do not, then one of the following might have occurred

  - You are trying to merge to or from the wrong branch (or both)
  
    - Double check your branches (see previous slide)
  - Another translator has worked on the same files on the same translations, and then submitted a pull request before you did
  
    - In this case, you could have a merge conflict
    - Contact one of the maintainers
    
      - They can fix it
      - It's not a big deal 

4g1: Adding a description
-------------------------------

- *description* 

  - optional
  - can be useful to administrators if the changes are complex
  - answers the *what*, *why*, *how*, etc. of the *pull request*

4g2: Is a description necessary?
------------------------------------

- truth be told, descriptions generally won't be of much use to translators unless you've done something unusual, and I can't think of anything that would be unusual.
  
  - A *pull request* for a translation is only going to involve 1-3 files (though there may be many, many lines changed)
  - But even if there are many lines changed, the administrators at |PsychoPy| will probably not be able to review translations in much detail since they probably won't speak the language

4h: Extra responsibility
---------------------------

- From the last slide

  - *the administrators at PsychoPy will probably not be able to review translations in much detail since they probably won't speak the language*

- In this sense, translators carry more responsibility than even someone adding new features to |PsychoPy|
- This is because administrators will probably be forced to authorize your proposed changes without checking them
- Translate responsibly

4i: Subsequent commits
------------------------

- If you make further *commits* before the *pull request* is merged in by the administrators
  
  - don't worry
  - your commits will automatically be incorporated into the previous *pull request* 

5: Continual *Git* workflow
-----------------------------------

**Again!!??**

Yes

- From *GitHub* on your *fork*
 
  - (Make sure you are on the *release* branch)
  - *Sync fork* (from *upstream*)

- From *GitHub Desktop*
  
  - ``Repository > Pull``
 
On to :ref:`other things to consider`
