.. _optionalElaboration:

Optional elaboration on some concepts
=======================================

What allows |PsychoPy| to be translated?
-------------------------------------------

- |PsychoPy| uses `wxPython <https://docs.wxpython.org/wx.Locale.html>`_ and `gettext <https://www.gnu.org/software/gettext>`_ 
- Click the links for more information, but it is probably only of interest to those of you who code in *Python&
 
Notes on the interchangeability of *Git* tools
------------------------------------------------

- command-line *Git*

  - e.g., *Terminal* on *Macs*, or the *Bash Shell* on *Windows 10* and later
- *GitHub Desktop*
- *GitFiend*
- *PyCharm*
- *Visual Studio Code*
- etc.

Where is *Git* in a folder?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

- *Git* depends almost entirely on a hidden folder in the most superordinate directory of any project:

  - ``.git`` (required, the *sine qua non*, actually)
- There is also almost alwasy a hidden ``.gitignore`` file there (though it's technically optional)

So you can use different *Git* tools seamlessly
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

- Software tools like *GitHub Desktop* and *GitKraken* and even command-line *Git* simply refer to the ``.git`` folder and the ``.gitignore`` file
- Therefore, you can switch among the various *Git* interfaces seamlessly

Example
^^^^^^^^^

- You're doing something in *GitHub Desktop*, but hit a wall 
- You read that you can fix the issue using the command-line interface

  - e.g., *Terminal* on a *Mac*
- You switch to *Terminal* and pick up where you left off in *GitHub Desktop*
- Then you go to *Visual Studio Code* and continue

Notes on *Git* forks 
-----------------------

Is your fork really "yours"?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
- Forks are "yours" in open-source software

  - to an extent 
- Your fork of |PsychoPy| is 

  - "yours" in that you can do what you want with it
  - but **not** "yours" in the sense that you still need to abide by the the particular |license-for-use| that applies to |PsychoPy|

.. |license-for-use| raw:: html

  <a href="https://psychopy.org/about/index.html#license-for-use" target="_blank">license</a>

Notes on *Git* branches
---------------------------

- Branches in *Git* are a way of organising the various **different** things you do within a repository

  - Sometimes a repository has official branches, like |PsychoPy|
  
    - the *dev* branch
    - the *release* branch  
  - Often, you create your own branches to organise your work 

What is the *dev* branch?
^^^^^^^^^^^^^^^^^^^^^^^^^^^

- for *major* additions to |PsychoPy|

  - such changes need to be tested extensively so that they don't "break" the software (e.g., new features, deprecation, etc.)
  - major releases come out about twice a year
- As of the writing of this slide, the current *major* release is |PsychoPy| 2023.2.2
- This can be read from right-to-left as the 2nd minor ("bug-fix") release, of the **2nd major release** of the year 2023

What is the *release* branch?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

- The *release* branch corresponds to the rightmost number in the version (see previous slide)
- for **minor** (aka "bug fix") releases of |PsychoPy|, where changes can't really "break" anything
  
  - bug fixes, documentation typos, etc.
  - and critically, **translations**
- Changes to the *release* branch are made public much more often
- Therefore

  - since translations can't break code, they normally go under the *release* branch 

Notes on translation terminology
---------------------------------

Why is *translation* not exactly the right term?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  
- software translations are not restricted to linguistic differences  

  - includes differences in the following (for example):
    
    - orthography  
    - writing conventions
  
      - e.g., commas, whether decimal places are represented with commas or full stops, etc.
    - regional differences
    
      - e.g., taboo words, dialect variation

the source of locale names
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

- ``I18n`` or *Internationalization*

  - ``18``
  
    - the number of letters between the first and last letters of *I_nternationalizatio_n*
  - makes software available in various languages
- ``L10n`` or *Localization*

  - ``10``
  
    - the number of letters between the first and last letters of in *L_ocalizatio_n*
  - makes software suitable for cultural regions

- |Wipedia_I18nL10n|

.. |Wipedia_I18nL10n| raw:: html

  <a href="https://en.wikipedia.org/wiki/Internationalization_and_localization" target="_blank">Explanation of I18n and L10n on Wikipedia</a>

Notes on language varieties and localisation
-----------------------------------------------

- language

  - often varies by region  
  - but sometimes not

- For end-users of software 

  - sometimes little linguistic differences matter
  - sometimes they don't

Minor language differences that **don't** matter for end-users
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

- UK and Canada

  - *colour*, with a <u>  
- US

  - *color*, without a <u>  
- Almost inconceivable that this difference would matter to anyone
   
- Localization to British English *not* really merited in this case 

  - But there's nothing stopping anyone if they want to
  - (It would be very little work)

Major language differences that **do** matter for end-users
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

- *Spoken* Mandarin in the PRC vs. the ROC  

  - quite close (emphasizing *spoken*)  
- But  

  - different orthographies  
  
    - PRC
    
      - *simplified* Chinese characters  
    - ROC
    
      - *traditional* Chinese characters  

Simplified vs. traditional Examples
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

- the word *experiment* (shì yàn)

  - 实验 (in Mainland China) 
  - 實驗 (in Taiwan)

- Reading each other's scripts possible, but annoying  
- Localization merited 

Translator teams: *Choice of locale*
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

- Do you create *one* locale, or *more than one*?

  - a team decision, mostly 