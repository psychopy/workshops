
.. ifslides::

    .. image:: /_static/OST600.png
        :align: left
        :scale: 25 %
        
        
.. _pycharmIntro:

Getting Started
==============================================

Creating a new project
----------------------------

.. image:: /_images/createProject.png

.. nextSlide::
|
Once PyCharm is opened:

1) Select new project.
2) Check that the base interpreter (i.e. which version of python you're using) is the one you want to use - currently should be set to python 3.8).
3) Click on create once you have named your project.

|
Connect PyCharm to Github
----------------------------

.. image:: /_images/VCS_1.png
|
.. image:: /_images/VCS_2.png

|
1) At the top ribbon, select VCS > Enable Version Control Integration.
2) From the dropdown button, select Git and click OK.
3) If a message pops up saying that Git is not installed, install Git now.

|
Share project to Github
----------------------------------

.. image:: /_images/Git.png
|
.. image:: /_images/shareGit.png

|
1) To share your project to Github, click Git > Github > Share Project on Github.
2) Click on the Add account dropdown to login to Github.

|
.. image:: /_images/shareGit_Mac.png

|
3) An additional window might appear to share/add the project on Github.

|
Clone from Github
------------------

.. image:: /_images/gitClone_1.png
|
.. image:: /_images/gitClone_2.png
|
.. image:: /_images/release.png

|
1) To access a project already on Github, click Git > Clone.
2) Click on psychopy or enter the URL.
3) Click on release at the bottom right to see all the different versions of PsychoPy.

|
Running different versions of PsychoPy
--------------------------------------

.. image:: /_images/psychopyApp.png

|
1) At the left side panel, click on psychopy > app > psychopyApp.py.
2) It will open as a python script. Right click anywhere at the script or click on the green play button at the top right panel to run the script.

|
Installing modules
----------------------------

For first time users, most modules have not been installed and therefore an error message would appear:

To install modules:

|
.. image:: /_images/settings.png.
|
.. image:: /_images/settingsMac.png
|
.. image:: /_images/pythonInterpreters_1.png
|
.. image:: /_images/pythonInterpreters_2.png
|
.. image:: /_images/psychopyModule.png

|
1) Install modules from File > Settings > Project: psychopy > Python Interpreter.
2) On a Mac, click on PyCharm > Preferences to open up your Settings.
3) After choosing the python interpreter you want, click on the + at the top panel.
4) At the search bar, search psychopy to install.
5) After installing, re-run the script to open PsychoPy.


|
Accessing specific component from developer version
-----------------------------------------------------

.. image:: /_images/remote_1.png
|
.. image:: /_images/remote_2.png
|
.. image:: /_images/fetch.png
|
.. image:: /_images/newComponent.png

|
1) To access the developer version, select Git > Manage Remotes.
2) A window will appear showing the developers we can currently access. For first time users, there would only be origin, which is our own repository.
3) Click on the + and at the Define Remote window, add the name of the developer you want to add and their Github URL.
4) Click on Git > Fetch to sync the developer's repository.
5) To access a new component of PsychoPy, search from the release at the bottom of the right screen.
6) Click on the component name > Checkout.
7) Return to psychopyApp.py and run the script to use the component in PsychoPy.