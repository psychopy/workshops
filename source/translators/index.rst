.. _translatorWorkshopIndex:

PsychoPy translation workshop
=====================================

You can view these materials |viewTranslatorPages| or |viewTranslatorSlides|.

.. |viewTranslatorPages| raw:: html

  <a href="https://workshops.psychopy.org/translators" target="_blank">as webpages</a>

.. |viewTranslatorSlides| raw:: html

  <a href="https://workshops.psychopy.org/slides/translators" target="_blank">as html slides</a>

Introductions and expectations
--------------------------------

- Who are we?
- Who are you?
- What are we trying to achieve?

Need for translations
-------------------------

- |PsychoPy| now used worldwide

  - needs to be available in different languages
- starting with v1.81

  - many parts of the |PsychoPy| app 
  
    - translatable into languages with unicode character sets
- a translation

  - changes the language that the **experiment-ER** sees
  
**NOTE**: This is **NOT** what the participant sees. **THAT** is under the control of the experimenter 


|PsychoPy| and languages
---------------------------

|PsychoPy| "looks" for a language to display its "strings" in
- If found

  - consults the ``messages.mo`` file under the directory for that language
- If **not** found

  - consults the ``messages.mo`` file under the directory (``en_US``) for American English (``psychopy/app/locale/en_US/LC_MESSAGE/messages.mo``)

**IMPORTANT NOTE**: Translators don't work on the ``.mo`` file. Instead, they work on a ``.po`` file.

Visualisation
----------------

.. image:: ../_images/trnslWkshp_poMoPsychoPy.png
  :align: center
  :width: 750
  :alt: Image of a how .po and .mo files interact to allow PsychoPy to implement translations into other languages

..

How experimenters implement this in |PsychoPy|
------------------------------------------------

- On a Mac

  - Mac
  
    - ``PsychoPy > Preferences > Application > locale``
  - PC
  
    - ``File > Preferences > Application > locale``
  - (from here you **would**\* choose the language)

- Quit and restart |PsychoPy| 

\* **WARNING**: Be careful playing with this as you might end up with menus that you cannot read, including how to change the locale back! 

Rough overview of how translators make this happen
----------------------------------------------------

Translators...

1. translate "strings" in a ``messages.po`` file
2. commit and push those changes to *GitHub*
3. make a *pull request* on *GitHub* to request incorporation of those changes into the current release of |PsychoPy|

**NOTE**: The ``.mo`` file is automatically generated during the next minor (aka "bug-fix") release of |PsychoPy|

Prerequisites to translating
-------------------------------

thorough proficiency in at least three things, requiring months or years of study:

- |PsychoPy| itself, as a user/experiment designer (not a Python/Javascript programmer)
- English
- any language (or dialect) that is not **American** English to translate into (e.g., Korean, Singapore English)

**NOT** prerequisites
-------------------------------------------

(since today's workshop covers these topics)

- how to use the free app |homepageForPoedit| to do translations
- how bring those translations into |PsychoPy| project using the following:

  - |homepageForGit|
  - |homepageForGithub|
  - |homepageForGithubDesktop|

.. |homepageForPoedit| raw:: html

  <a href="https://poedit.net/" target="_blank">Poedit</a>

.. |homepageForGit| raw:: html

  <a href="https://git-scm.com/" target="_blank">Git</a>

.. |homepageForGithub| raw:: html

  <a href="https://github.com/" target="_blank">GitHub</a>

.. |homepageForGithubDesktop| raw:: html

  <a href="https://desktop.github.com/" target="_blank">GitHub Desktop</a>

Quick overview of steps
--------------------------------

- preliminaries
- setting up the *git* / *GitHub* workflow
- working on translations and making associated pull requests

Today
-----------------------------------

We're going to work through these one by one, along with a couple of extra topics, if there's time

.. toctree::
    :maxdepth: 1
    
    setUpVersionControl.rst
    workOnTranslations.rst
    makePullRequest.rst
    otherThingsToConsider.rst
    optionalElaboration.rst

On to :ref:`setting up version control`