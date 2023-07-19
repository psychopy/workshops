.. _translatorWorkshopIndex:

PsychoPy translation workshop
=====================================

These materials at:
https://workshops.psychopy.org/translators

Or you can `view as slides <https://workshops.psychopy.org/slides/translators>`_

Introductions and expectations
--------------------------------

- Who are we?
- Who are you?
- What are we trying to achieve?

Need for translations
-------------------------

- |PsychoPy| now used worldwide
- so needs to be available in different languages
- starting with v1.81

  - many parts of the |PsychoPy| app 
  
    - translatable into languages with unicode character sets
- a translation

  - changes the language that the **experiment-ER** sees
  
.. note:: This is **not** what the participant sees, which is under the control of the experimenter 


Overview of how |PsychoPy| works in a different language
----------------------------------------------------------

- |PsychoPy| "looks" for a language every time it displays items to the experimenter (e.g., menu items, errors)
- If found

  - consults the ``messages.mo`` file for that language
- If **not** found

  - consults the ``messages.mo`` file for American English

Further reading
-------------------
Further, highly optional reading for those who are interested in the programming aspect of this
   
- GNU *gettext*

  - `https://www.gnu.org/software/gettext <https://www.gnu.org/software/gettext/>`_ 
- *wxPython* 

  - `https://docs.wxpython.org/wx.Locale.html <https://docs.wxpython.org/wx.Locale.html>`_
 

Overview of how translators make this happen
-----------------------------------------------

Translators...

1. translate "strings" in a ``messages.po`` file
2. compile the ``.mo`` file from the ``.po`` file
3. commit and push those changes to *GitHub*
4. make a *pull request* on *GitHub* to incorporate those changes in the current release of |PsychoPy|

.. note:: They also translate *Start-up tips*, but this is a slightly different process that involves a simple ``.txt`` file

Prerequisites to translating
-------------------------------

a thorough understanding of at least three things, requiring months or years of study:

- |PsychoPy| itself, as an experiment designer
- English
- any language (or dialect) that is not **American** English to translate into (e.g., Korean, Singapore English)

**NOT** prerequisites
-------------------------------------------

- how to use the free app `Poedit <https://poedit.net/>`_ to do translations
- how bring those translations into |PsychoPy| project using `Git <https://git-scm.com/>`_, usually via `GitHub <https://github.com/>`_
- Today's workshop mostly covers the topics on this slide


Quick overview of steps
--------------------------------

- preliminaries
- setting up the *git* / *GitHub* workflow
- working on translations
- making a pull request on *GitHub*
- cleaning up

Today
-----------------------------------

We're going to work through these one by one

.. toctree::
    :maxdepth: 1

    preliminaries
    setUpGit.rst
    workOnTranslations.rst
    makePullRequest.rst


On to :ref:`preliminaries`