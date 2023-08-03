.. _preliminaries:

Preliminaries
================

Some terminology
-------------------

- ``I18n`` or *Internationalization*

  - ``18``: the number of letters between *I* and *n* in *Internationalization*
  - making software available in various languages
- ``L10n`` or *Localization*

  - ``10``: the number of letters between *L* and *n* in *Localization*
  - making software suitable for cultural regions
    
    -  *locale* = usually a specific country

Why *internationalization* / *localization* (not *translation*)?
-----------------------------------------------------------------
  
- not restricted to linguistic differences  

  - includes differences in the following (for example):
    
    - orthography  
    - writing conventions
  
      - e.g., commas, whether decimal places are represented with commas or full stops, etc.
  - general cultural differences

What is a *locale* in |PsychoPy|?
-----------------------------------

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

Minor language differences that *don't* matter for end-users
----------------------------------------------------------------

- UK and Canada  

  - *colour*, with a <u>  
- US  

  - *color*, without a <u>  
- Almost inconceivable that this difference would matter to anyone
   
- Localization to British English *not* really merited in this case 

  - But there's nothing stopping anyone if they want to
  - (It would be very little work)

Major language differences that *do* matter for end-users
-------------------------------------------------------------

- *Spoken* Mandarin in the PRC vs. the ROC  

  - quite close (emphasizing *spoken*)  
- But  

  - different orthographies  
  
    - PRC: *simplified* Chinese characters  
    - ROC: *traditional* Chinese characters  

Simplified vs. traditional Examples
---------------------------------------

- simplified (top) vs. traditional (bottom) characters for the word *experiment*

  - 实验
  - 實驗

- Reading each other's scripts possible, but annoying  
- Localization merited 

Translator teams: *Choice of locale*
---------------------------------------

- Do we create *one* locale, or *more than one*?
- Time-saving multiple-locale strategy

  - Choose one locale, finish it, then copy it into a new locale and make adjustments
  - For example

    - **Start** with Iberian Spanish (European)
    - **Finish** all translations in that language variety
    - **Copy** the ``es_ES`` folder
    - **Rename** the copied folder: ``es_MX`` (Spanish in Mexico)
    - Finally, **adjust** for Mexican Spanish

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