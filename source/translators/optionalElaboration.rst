.. _optionalElaboration:

Elaboration of some concepts / terms
=====================================

|PsychoPy| "under the hood"
-----------------------------

- |PsychoPy| uses `wxPython <https://docs.wxpython.org/wx.Locale.html>`_ and `gettext <https://www.gnu.org/software/gettext>`_ 
 

More information in issues in *Git*
--------------------------------------

Minor note on *Git*-interface tools
------------------------------------

- *Git* depends on a hidden folder in the most superordinate directory of any project:

  - ``.git`` (required, the *sine qua non*, actually)

- There is also usually a hidden ``.gitignore`` file there (though it's technically optional)
- Software tools like *GitHub Desktop* and *GitKraken* and even command-line *Git* simply refer to the ``.git`` folder and the ``.gitignore`` file
- Therefore, you can switch among the various *Git* interfaces seamlessly
- This will make more sense later, but it's not that important for now

Caveat: How your fork is *not* yours entirely
-----------------------------------------------

Keep in mind that |PsychoPy| is **not** yours in the sense that you still need to abide by the the particular |license-for-use| that applies to |PsychoPy|

.. |license-for-use| raw:: html

  <a href="https://psychopy.org/about/index.html#license-for-use" target="_blank">license</a>

Why do translations take place on the *release* branch?
--------------------------------------------------------------

- the *dev* branch

  - for *major* changes to |PsychoPy| that need to be tested extensively so that they don't "break" the software (e.g., new features, deprecation, etc.)
  - Changes to the *dev* branch are released about twice a year only 
    
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


Localization terminology
--------------------------

- ``I18n`` or *Internationalization*

  - ``18``
  
    - the number of letters between the first and last letters of *I_nternationalizatio_n*
  - makes software available in various languages
- ``L10n`` or *Localization*

  - ``10``
  
    - the number of letters between the first and last letters of in *L_ocalizatio_n*
  - makes software suitable for cultural regions
    
Why *internationalization* / *localization* (not *translation*)?
-----------------------------------------------------------------
  
- not restricted to linguistic differences  

  - includes differences in the following (for example):
    
    - orthography  
    - writing conventions
  
      - e.g., commas, whether decimal places are represented with commas or full stops, etc.
  - general cultural differences

The nexus of a translation: the *locale*
-----------------------------------------

- a folder with the following label: ``ll_CC``
  
  - the lowercase ``ll_``
  
    - a language
  
      - e.g., ``pt_`` for portuguese
  - the uppercase ``_CC``
    
    - a country
    
      - e.g., ``_BR`` for Brazil
- thus, the folder holding the translations for Brazilian Portuguese:
  
  - ``pt_BR``

Language variation by region
-----------------------------

- language

  - often varies by region  
  - but sometimes not

- For end-users of software 

  - sometimes little linguistic differences matter
  - sometimes they don't

Minor language differences that **don't** matter for end-users
----------------------------------------------------------------

- UK and Canada

  - *colour*, with a <u>  
- US

  - *color*, without a <u>  
- Almost inconceivable that this difference would matter to anyone
   
- Localization to British English *not* really merited in this case 

  - But there's nothing stopping anyone if they want to
  - (It would be very little work)

Major language differences that **do** matter for end-users
-------------------------------------------------------------

- *Spoken* Mandarin in the PRC vs. the ROC  

  - quite close (emphasizing *spoken*)  
- But  

  - different orthographies  
  
    - PRC
    
      - *simplified* Chinese characters  
    - ROC
    
      - *traditional* Chinese characters  

Simplified vs. traditional Examples
---------------------------------------

- the word *experiment* (shì yàn)

  - 实验 (in Mainland China) 
  - 實驗 (in Taiwan)

- Reading each other's scripts possible, but annoying  
- Localization merited 

Translator teams: *Choice of locale*
---------------------------------------

- Do we create *one* locale, or *more than one*?

  - a team decision, mostly 

Useful locale strategy
--------------------------

- Time-saving multiple-locale strategy

  - Choose one locale, finish it, then copy it into a new locale and make adjustments, for example:

    - **Start** with Iberian Spanish (European)
    - **Finish** all translations in that language variety
    - **Copy** the entire ``es_ES`` folder
    - **Rename** the copied folder: ``es_MX`` (Spanish in Mexico)
    - **Add** the the following line to the ``mappings.txt`` file
    
      - ``es_MX ESM español  (Spanish, Mexico)`` 
    - Finally, **adjust** the new ``es_MX/LC_MESSAGE/messages.po`` file for Mexican Spanish

Translator teams: *Division of labor*
---------------------------------------

- how to divide up work to avoid overlap?
    
  - e.g., divide up work alphabetically? 
- single individuals working alone on languages

  - how to support each other?  