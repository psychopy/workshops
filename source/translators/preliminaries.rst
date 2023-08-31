.. _preliminaries:

Preliminaries
================

Some terminology
-------------------

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

Screenshot of localization files in |PsychoPy|
------------------------------------------------

.. image:: ../_images/trnslWkshp_whereLlccFiles.png
  :align: center
  :width: 350
  :alt: Image of where the localisation files reside in the PsychoPy repository

..

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
- We will work on this right after we set up version control

Done with preliminaries
-------------------------

On to :ref:`setting up version control`