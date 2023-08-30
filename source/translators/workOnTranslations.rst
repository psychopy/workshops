.. _working on translations:

Working on translations
==========================

- To be efficient, translators should follow a certain sequence of steps
- We will now cover how to do this

Overview
-------------

- Step 1: Identifying the appropriate 5-6 character ``[ll_CC]`` locale name for your translation
- Step 2: Configuring the ``mappings.txt`` file with a text editor
- Step 3: Working on translations with *Poedit*
  
  - configure settings of the ``messages.po`` file
  - translate the "strings" in that same file
- Step 4: Translating "Start-up tips" in |PsychoPy| with a text editor
  
**NOTE**: Steps 3 and 4 don't have to be sequential; they're just different translation processes
**NOTE**: Steps 3 and 4 don't have to be sequential; they're just different translation processes

Step 1: What is the ``[ll_CC]`` locale name for my language?
--------------------------------------------------------------

First, we need to discuss how locale names work

1a: What are the parts of a locale name?
-----------------------------------------

- the ``[ll_]``

  - an `ISO 639 pair <https://www.gnu.org/software/gettext/manual/gettext.html#Language-Codes>`_ of lowercase letters for a language
- the ``[_CC]``

  - an `ISO 3166 pair <https://www.gnu.org/software/gettext/manual/gettext.html#Country-Codes>`_ of uppercase letters for a country

- Examples

  - ``es_CL`` for Chilean Spanish (*español de CHILE*)
  - ``es_ES`` for Iberian Spanish (*español de ESPAÑA*)
  - ``zh_CN`` for (simplified) Chinese in mainland China

1b: What our team speaks more than one dialect?
-------------------------------------------------

- group decision on team strategy
  
  - For example (one possibility):

    - fully translate for Iberian Spanish (``es_ES``)
    - copy the entire ``es_ES`` folder
    - rename it to ``es_CL`` (Spanish in Chile)
    - make adjustments to the new ``messages.po`` file to account for Chilean variations on the language  
    - add Chilean Spanish to the ``mappings.txt`` file

1c: ``[ll_CC]`` folder/file structure
-------------------------------------

- The file translators actually work on

  - a ``messages.po`` file
  - located *two* levels under under any particular ``[ll_CC]`` folder for that *locale*
  
- For example for Farsi (Persian) in Iran: 

``psychopy/psychopy/app/locale/...`` 

.. image:: ../_images/trnslWkshp_folderStructure.png
  :align: center
  :width: 200
  :alt: folder structure for locations of dot po and dot mo files (this one being fa_IR, which is Farsi as spoken in Iran)

..

**NOTE**: Ignore the intermediate ``LC_MESSAGE`` level, And (for now) ignore the ``messages.mo`` located in the same folder as the ``messages.po`` file
**NOTE**: Ignore the intermediate ``LC_MESSAGE`` level, And (for now) ignore the ``messages.mo`` located in the same folder as the ``messages.po`` file


1d: Is your locale listed?
------------------------------

- Look under ``psychopy/psychopy/app/locale``

  - Is your ``[ll_CC]`` folder there?
  
    - may already be there
    - *or not*
- if not, why not?

  - unnecessary storage
  
    - pre-listing every language-country pair = storage waste
    - current list = just guesses

- if not listed, just add it 

1e: How to add one
---------------------

- the easy way

  - find any ``[ll_CC]`` folder

    - ideally, look for a small ``.po`` file with no translations yet
  - copy and paste the entire folder 
  - rename the folder to the ``[ll_CC]`` appropriate for your locale
    
  - make adjustments to the ``messages.po`` file inside (covered soon)
- the hard way (not a reasonable approach; not going there)  

Step 2: ``mappings.txt``
-------------------------

- Do this once per translated language, and it's done forever (for that localisation)
- This file just tells the experimenter which translations are available in |PsychoPy|

Step 2a: Open a text editor
------------------------------

- Start your preferred text editor (e.g., *Visual Studio Code*, *PyCharm*)

**NOTE**: Just be careful with older versions of *Notepad* in Windows. Traditionally, it was incompatible with Unix style line endings. But as of Windows 10, it now `works if it detects unix-style line feeds in the file <https://devblogs.microsoft.com/commandline/extended-eol-in-notepad/>`_. Or at least it *should*. If it's not working, you will see one huge paragraph of code. The least confusing solution is to change text editors.
**NOTE**: Just be careful with older versions of *Notepad* in Windows. Traditionally, it was incompatible with Unix style line endings. But as of Windows 10, it now `works if it detects unix-style line feeds in the file <https://devblogs.microsoft.com/commandline/extended-eol-in-notepad/>`_. Or at least it *should*. If it's not working, you will see one huge paragraph of code. The least confusing solution is to change text editors.

2b: add the ``[ll_CC]`` code
----------------------------------

- Open the following file (there's only one)

``/psychopy/psychopy/app/localization/mappings.txt``

- Is the ``[ll_CC]`` code listed?

  - Make sure the ``[ll_CC]`` code resides at the appropriate line (alphabetically listed)

2c: Microsoft language code
------------------------------

- Add the 3-letter Microsoft code that refers to the language
  
  - These can be found in the rightmost column (``Language code``) on Microsoft's list of *Language Identifiers and and Locales* at `https://learn.microsoft.com/en-us/previous-versions/windows/embedded/ms903928(v=msdn.10) <https://learn.microsoft.com/en-us/previous-versions/windows/embedded/ms903928(v=msdn.10)>`_.
  
**NOTE**: If you can't find your language, just add a random three-letter sequence that isn't already in use and probably doesn't refer to a language (e.g., ``JJY``).
**NOTE**: If you can't find your language, just add a random three-letter sequence that isn't already in use and probably doesn't refer to a language (e.g., ``JJY``).

2d: language label
----------------------

- At the far right

  - add the label for the language **in that language**
  - followed by the name of the language in English, but **in parentheses**
  - for example

    - "``español (Spanish)``"

      - (not just "``Spanish``")
    - "``עִברִית (Hebrew)``"

      - (not just "``Hebrew``")
- Save the ``mappings.txt`` file

Step 3: Continual *Git* workflow
----------------------------------

- Sync from *upstream* to *origin*
- Pull from *origin*

**Again??!!**

- Yes

  - Do this **every time** you start work on a translation
  - Another translator may have changed the translation (the ``.po`` file) since the last time you worked on it
- See end of the last slide deck for instructions


Step 4: Translating in *Poedit*
-------------------------------------

- *Poedit*

  - where most of your work will be focused
  - first need to set some things up

4a: Download and install *Poedit*
------------------------------------

Poedit download page:

`https://poedit.net/download <https://poedit.net/download>`_ 

4b: Find your ``.po`` file
-----------------------------------

- Start *Poedit*
- open the ``.po`` file for the language you're working on:

  - ``.../psychopy/psychopy/app/locale/[your ll_CC folder]/LC_MESSAGES/messages.po``

- For example, for Thai in Thailand:

``psychopy/app/locale/th_TH/LC_MESSAGES/messages.po``

4c: Settings that don't change
--------------------------------

- Once set, the settings below in *Poedit* don't really change

  - unless you change your email, or the location of your files on your computer, etc.
- One exception is the version of |PsychoPy| you're using to translate

  - This is covered last   

.. PB - These settings and settings on the following slides are largely based on Hiroyuki's settings for Japanese

4c1: ``General`` (Name and email)
----------------------------------------

- On a PC, choose the following: ``File > Preferences``
- On a Mac, choose this instead: ``Poedit > Settings``
- Find the following tab: ``General``
- Add your name and e-mail address where indicated

4c2: ``Advanced``
---------------------

- Just make sure that the following are set correctly

  - ``Line endings:``
  
    - set to ``Unix (recommended)``
  - ``Preserve formatting of existing files``
    
    - make sure this is checked

4c3: Language and language team
-----------------------------------

- Go to: ``Translation > Properties``
- under: ``Language team``

  - contact email for entire group 
- under: ``Language``
  
  - select the appropriate ``Language (Country)`` combination
  - For example
  
    - ``Duala (Cameroon)``
  
- under not only ``Charset``, but also ``Source code charset``
  
  - *UTF-8 (recommended)* 

.. PB - How should groups communicate with each other? listserv? Google Group? Gaggle Mail?

4c4: Paths (1)
------------------

- under the tab labeled: ``Sources Paths``

  - For ``Base path``
  
    - Click the arrow on the right
    - find the path on your computer that leads to the ``psychopy`` directory *within* the cloned repository on your computer:
      
``..THE/PATH/ON/YOUR/COMPUTER/TO/psychopy/psychopy``

**NOTE**: This setting does **not** make its way into the ``.po`` file, per se. Rather, it's just part of *Poedit*. 
**NOTE**: This setting does **not** make its way into the ``.po`` file, per se. Rather, it's just part of *Poedit*. 

4c5: Paths (2)
-----------------

- under the tab labeled: ``Sources Paths``
- in the box labeled: ``Paths``
  
  - ``psychopy/``

4c4: keywords
-----------------

- under the tab labeled: ``Sources Keywords``

  - Go to: ``Additional keywords``
- The following keyword should be in that box (with the preceding underscore): 
 
  - ``_translate`` 
- If it **isn't**, type it in  
- Save your work (``File > Save``)

.. PB - Hiroyuki also has _, gettext, and gettext_noop as keywords. Are these necessary or helpful?

4d: The setting that does change
---------------------------------

This is the setting that will change over time, as |PsychoPy| comes out with new versions

- go to: ``Translation > Properties``

  - then: ``Translation properties`` 

    - then: ``Project name and version``
  - Type in *PsychoPy* followed by the |PsychoPy| version you are working on
  - For example:
  
    - ``PsychoPy 2023.1.0``
      
      - usually the most recently released version of |PsychoPy|
  - This will tell subsequent translators whether they need to update the strings (i.e., if their version of |PsychoPy| is more recent)

4e: Generate current list of translatable strings
--------------------------------------------------------

- Select the following
 
  - ``Translation`` > ``Update from Source Code``
- You should subsequently see a list of strings in English that need translating into your language
  
  - If you don't, the keyword ``_translate`` may not have been added to the keywords
  
    - i.e., ``Translation > Properties > Sources Keywords > Additional keywords``

**NOTE**: If ``Update from Source Code`` is greyed out, there are probably no new strings to update
**NOTE**: If ``Update from Source Code`` is greyed out, there are probably no new strings to update

4f: Translate the strings
----------------------------

- Look at the list under the heading: ``Source Text - English``
- Select a string that you want to translate
- Once selected, you should see it appear as English in the following box below the longer list: ``Source text``
- Below that, there is a box labeled as follows: ``Translation``
- Type your translation into that box
- Save your work as you go

Translation note 1a: Leave certain technical terms alone
----------------------------------------------------------

- Technical terms should not be translated:
  
  - ``Builder``
  - ``Coder``
  - ``PsychoPy``
  - ``Flow``
  - ``Routine``, and so on
- These are usually indicated with an uppercase first letter
- The next slide covers cases of uncertainty
- The next slide covers cases of uncertainty

Translation note 1b: What if I'm not sure whether I should translate or not?
-----------------------------------------------------------------------------
Translation note 1b: What if I'm not sure whether I should translate or not?
-----------------------------------------------------------------------------

- The Japanese translation is nearly completely
- You have it since you forked and cloned the repository
- Open: 

``/psychopy/app/locale/ja_JP/LC_MESSAGES/messages.po``

- Look up the string you're having difficulty with in the Japanese ``messages.po`` file
- Use that as a model for your own ``.po`` file

Translation note 2: Formatting arguments
--------------------------------------------

If there are formatting arguments in the original string (``%s``, ``%(first)i``)

- The same number of arguments must also appear in the translation
  
  - but their order is not constrained to be the original order
- If they are named (e.g., ``%(first)i``)

  - here, ``first`` is a python name
  - that part should not be translated

.. PB - I really just copied this from the original explanation by Jeremy Gray. I don't really understand it, and may have copied it incorrectly. Needs checking.
.. PB - I really just copied this from the original explanation by Jeremy Gray. I don't really understand it, and may have copied it incorrectly. Needs checking.

Translation note 3: When you are unsure
------------------------------------------

If you think your translation might have room for improvement

- toggle the button labeled as follows: ``Needs Work``

  - It should be located to the right of the header with the following label: ``Translation``
- You can also add notes to clarify

  - Click the button with the following label: ``Add Comment`` 
  
    - This should be located at lower-right of the app window if you have the sidebar visible
  - Add your notes for that string into the pop-up window

Simple strategy to resolve uncertainty: Ask the experts
--------------------------------------------------------
  
- Go to the forum on *discourse*:

`https://discourse.psychopy.org/ <https://discourse.psychopy.org/>`_

- There are friendly, useful experts there

  - few, if any, can help you with your language, of course
  - many more who can help you understand the underlying code of |PsychoPy|
  
Advanced strategy to resolve uncertainty: *Determine it yourself*
----------------------------------------------------------------------

**NOTE**: You need to understand *Python* quite well to take the following approach

- Select the relevant string in the following box: ``Source text - English``

  - Right-click the string (control-click on a Mac)
- At the bottom of the pop-up window, you should see the following heading: ``Code Occurrences`` 

  - Below that, you will see the (partial) path(s) to the file(s), followed by a colon, ``:``, then the respective line number in the file

*Determine it yourself* (cont'd)
----------------------------------------------------------------------------

- For example, for the string ``Yes`` in one version of |PsychoPy|:

  - ``../app/connections/update.py:232`` (meaning line 232 in the ``update.py`` file under the ``connections`` folder)

  - ``../app/dialogues.py:51`` (meaning line 51 in the ``dialogues.py`` file under the ``app`` folder)

  - ``../app/dialogues.py:71`` (etc.)

- You can then go into that file (or those files) to determine the function   

Last resort: *Do nothing*
----------------------------

If still in doubt
  
- Just leave out the translation until you *do* understand
- There is nothing wrong with this approach
- It is, by far, preferable to mis-translating a string  
- If you see fit to do so, toggle ``Needs Work`` and add a comment (see above)

Step 5: Translating the *Start-up Tips*
-------------------------------------------

- *Start-up tips* are not handled directly in a ``.po`` file
- Rather, they are stored in a ``.txt`` file, one per language
- That ``.txt`` file is then referred to in the ``.po`` file for your language
- This is explained next

5a: Copy ``tips.txt`` to a new file
--------------------------------------------

- Find the default *Start-up Tips* (in English) file

  - ``psychopy/app/Resources/tips.txt``
- Copy it

  - Paste it as a new file (``tips copy.txt``, perhaps)
  - Rename it according to the ``[ll_CC]`` convention consistent with the language you're working on
- For Example

  - ``tips_zh_CN.txt`` (simplified Chinese)
  - ``tips_ar_001.txt`` (Modern Standard Arabic)

5b: translate
----------------------

- Open the new, renamed file using your preferred text editor
- Translate the English-language tips by replacing them entirely with those of the language you are working on

**WARNING**: Do *not* delete any English entry in the new ``.txt`` file before you have completely translated it. Instead, insert the relevant translation below the English entry. Then (and only then) delete the English entry. Save your work, of course.

5c: add the new ``.txt`` file as a "translation"
------------------------------------------------------------

- Open *Poedit*
- Find ``tips.txt`` under the following heading: ``Source text - English``
- Simply provide the name of the new ``.txt`` file that you just created as the translation for ``tips.txt``

  - Naturally, this would be under the following heading: ``Translation - [your language]`` 
- For example:

.. list-table:: The case of Japanese
   :widths: 100 100
   :header-rows: 1

   * - ``Source text - English``
     - ``Translation - Japanese``
   * - ``tips.txt``
     - ``tips_ja_JP.txt``

Note on humor in *Start-up tips*
--------------------------------------

- Some of the humor in the *Start-up tips* might not translate well
- Feel free to leave out things that would be too odd

  - or replace them mild humor that would be more appropriate
- Humor must be respectful and suitable for using in a classroom, laboratory, or other professional situation
- Don't get too creative here
- If you have any doubt, it is better to leave it out
- It goes without saying that you should avoid any religious, political, disrespectful, or sexist material

Done with translating
------------------------

You're ready to :ref:`commit and make a pull request`