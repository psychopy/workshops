.. _translatorWorkshopIndex:

=====================================
PsychoPy translation workshop
=====================================

- You can view these materials |translatorWkshpPages| 
 
- or |translatorWkshpSlides|

- or without the training on *git*, |translatorAsDeveloperPage|

.. |translatorWkshpPages| raw:: html

  <a href="https://workshops.psychopy.org/translators" target="_blank">as web pages</a>

.. |translatorWkshpSlides| raw:: html

  <a href="https://workshops.psychopy.org/slides/translators" target="_blank">as slides</a>

.. |translatorAsDeveloperPage| raw:: html

  <a href="https://psychopy.org/developers/localization.html" target="_blank">under the developer pages at PsychoPy</a>


Introductions and expectations
--------------------------------

- Who are we?
- Who are you?
- What are we trying to achieve?

Translations in |PsychoPy|
-----------------------------

- |PsychoPy| now used worldwide

  - needs to be available in different languages for experiment designers
- starting with v1.81

  - many parts of the |PsychoPy| app 
  
    - translatable into languages with unicode character sets
  
How experiment designers implement this in |PsychoPy|
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

- Mac
  
  - ``PsychoPy > Preferences > Application > locale``
- PC
  
  - ``File > Preferences > Application > locale``

    - (from here you **would**\* choose the language)
- Quit and restart |PsychoPy| 

\* **WARNING**: Be careful playing with this as you might end up with menus that you cannot read, including how to change the locale back! 


Visualisation of how |PsychoPy| provides translated menus, etc.
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. image:: ../_images/trnslWkshp_poMoPsychoPy.png
  :align: center
  :width: 750
  :alt: Image of a how .po and .mo files interact to allow PsychoPy to implement translations into other languages

..

Rough overview of how translators make this happen
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Translators...

#. translate "strings" in a ``messages.po`` file
#. commit and push those changes to *GitHub*
#. make a *pull request* on *GitHub* to request incorporation of those changes into the current release of |PsychoPy|

**NOTE**: The ``.mo`` file is automatically generated during the next minor (aka "bug-fix") release of |PsychoPy|

Prerequisites to translating
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

thorough proficiency in at least three things, requiring months or years of study:

- |PsychoPy| itself, as a user/experiment designer (not a Python/Javascript programmer)
- English
- any language (or dialect) that is not **American** English to translate into (e.g., Korean, Singapore English)

**NOT** prerequisites
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

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


Today
---------

- We're going to work through the first two of these, where we will make pull requests at the same time we do translations
- Therefore, steps 3-5 are optional topics or elaborations

.. toctree::
    :maxdepth: 1
    
    setUpVersionControl.rst
    workOnTranslations.rst
    makePullRequest.rst
    otherThingsToConsider.rst
    optionalElaboration.rst

On to :ref:`setting up version control`