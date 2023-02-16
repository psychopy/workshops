.. _contribTypes:

Types of contribution
=====================================

.. _contribForum:

Contributing on the Forum
--------------------------

This is a wonderful place to start helping people - and doesn't even need Git! There are many questions that need answering. 

Many are easy: 

- "see the page here (that you haven't googled yourself)"
- Have you remembered to check the units of your image stimulus?

Many are poorly formed:

- "Could you tell us what you mean by *didn't work?*"

.. _contribDocs:

Contributing to the Documentation
----------------------------------

There are:

- lots of errors in the docs
- lots of omissions
- lots of outdated information

You can pretty much choose a page and find an error

Fixing those errors and outdated info is hugely valuable to other users

Let's take a look at `PsychoPy documentation source <https://github.com/psychopy/psychopy/tree/dev/docs/source>`_

.. _contribPsychoJS:

Contributing to PsychoJS
----------------------------------

PsychoJS is younger, smaller and has fewer contributors so far, so the rules are simpler

Let's just take a look at https://github.com/psychopy/psychojs

.. _contribTranslations:

Contributing to translations
----------------------------------

We're currently particularly keen on this (and we may set up some specific workhops just on that)

The information (subject to not being up to date) is here:

- https://psychopy.org/developers/localization.html

.. _contribFixes:

Contributing bug fixes
----------------------------------

Now we're getting onto actual Python/PsychoPy/PsychoJS code.

You might find a bug:

- just from your own work
- by looking for work on the Issues list of either PsychoPy or PsychoJS

The best advice is to start small

.. _contribFeatures:

Contributing features
----------------------------------

If you intend to add a new feature, discuss it with the team first. 
We're all very approachable (and if you get the wrong person we'll pass you on, so try one of us).

We have to be careful not to "bloat" the software at this point, and what one user sees as a 
critical feature (because they would use it in every 1 of their studies) another will see as 
completely pointless.

That doesn't mean there aren't features worth adding but discuss them before working.


.. _contribPlugins:

Contributing plugins
----------------------------------

Plugins are a new option in 2023.1 that provide a great way to add features *not* to the core  
of PsychoPy but easily assessible.

Advantages:

- for the users, there's less bloat
- you keep independence - you don't need permission to create one (although ask if you want it including in out curated plugins list)
- your releases can occur at any time, not tied to PsychoPy release schedule
- it's easier to stake the claim for getting credit (maybe you created 90% of your plugin, rather than 0.02% of PsychoPy!)

.. nextslide::

There is documentation on this (that needs updating) but let's take a look at an example as a good way to get started

You can see the psychopy-emotiv plugin

- docs: https://psychopy.github.io/psychopy-emotiv/
- repo: https://github.com/psychopy/psychopy-emotiv

When starting a new plugin take one like this and copy all the files (including the hidden ones called `.github/workflows`) 
to a new repo of your own. 

.. nextslide::

Treating `https://github.com/psychopy/psychopy-emotiv` as a template gives you:

- docs that automatically build when you push to GitHub! 
  (See the `GitHub Action <https://github.com/psychopy/psychopy-emotiv/actions/workflows/gh-pages.yml>`_) 
  The docs are ready to go with a PsychoPy-plugin theme
- a file that shows you how to add a new class to the PsychoPy lib from the plugin
  (see `psychopy_emotiv/emotiv.py <https://github.com/psychopy/psychopy-emotiv/blob/main/psychopy_emotiv/emotiv.py>`_)
- a pair of new Builder Components
  (see `psychopy_emotiv/emotiv_marking <https://github.com/psychopy/psychopy-emotiv/blob/main/psychopy_emotiv/emotiv_marking/__init__.py>`_)


