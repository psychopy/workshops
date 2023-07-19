.. _preliminaries:

Preliminaries
================

What is software localization?
-----------------------------------

- a translations of particular languages that are specified, respectively, for specific geographic *locale*\s

  - *locale* 
  
    - usually = specific country  

Why *localization* and not *translation*?
--------------------------------------------
  
- not restricted to linguistic differences  
- includes differences in the following (for example):
    
  - orthography  
  - writing conventions
  
    - e.g., commas, whether decimal places are represented with commas or full stops, etc.
  - general cultural differences

What is a *locale*?
----------------------

*locale*

- a language-country combination, most of the time

- ultimately realised as a folder with the following label: ``ll_CC``
  
  - the lowercase ``ll`` = a language
  
    - e.g., ``pt`` for portuguese
  - the uppercase ``CC`` = a country
    
    - e.g., ``BR`` for Brazil
- thus, the folder holding the translations for Brazilian Portuguese:
  
  - ``pt_BR``

Language variation by region
-----------------------------

- Language

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
- Almost inconceivable that this difference would matter
   
- Localization to British English *not* merited in this case  

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
    - **Copy** the ``es_ES``` folder
    - **Rename** the copied folder: ``es_MX`` (Spanish in Mexico)
    - **Adjust** for Mexican Spanish

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