.. _devEnv:

Creating your PsychoPy developer environment
---------------------------------------------

Why do I need a dev environment?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- you need to keep your installed PsychoPy app separate from your dev work
- you want to be able to launch your 'dev' version independently
- your dev version needs to reflect the changes you make to your code

It's really confusing when you spend ages trying different things to fix a bug only to find that you were testing your fix on a different python/psychopy!!

Installing Python 3.8 or 3.9
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

(Currently 3.10 is supported by our own code but not by all dependencies)
 
 You can use 

  - python.org (that's what Jon does)
  - pyenv (nice to be able to switch python versions easily)
  - venv (nice to switch environments *within* a python version)
  - whatever your editor uses (if it allows you to install extra packages)
  - conda (Jon avoids and won't support, but feel free!)

Fetch dependencies
~~~~~~~~~~~~~~~~~~~~~~~~~~

For Windows and MacOS pretty much everything should install automatically when using pip

For Ubuntu:

.. code:: bash

    sudo apt-get install git curl libbz2-dev libncurses-dev sqlite3 sqlite3-tools   libreadline-dev libreadline8 tk-dev libtk8.6 libssl-dev liblzma-dev libsqlite3-dev libffi-dev portaudio19-dev libsndfile1-dev libportmidi-dev liblo-dev
    sudo curl https://pyenv.run | bash
        # (Follow instructions by modifying the .bashrc file, call `sudo nano .bashrc`)
    exec $SHELL  # reset shell
    pyenv install 3.9.16
    pyenv global 3.9.16  # system interpreter will be 3.9.16
    python --version # check if the correct version has been set
    python -m pip install -U pip  # update pip

    # download specific wxpython from https://extras.wxpython.org/wxPython4/extras/linux/gtk3 and
    python -m pip install <your-downloaded-file.whl>

    # finally dev-install psychopy as below to get the rest
    

"dev" install of PsychoPy
~~~~~~~~~~~~~~~~~~~~~~~~~~

You need a local copy of your GitHub psychopy repo

Inside that folder open a terminal/cmdprompt and call

.. code:: bash
    
    <yourPython> -m pip install -e .

where:

- `-e` indicates not to copy the files to the site-packages, just a pointer to this localization
- `.` indicates that it is the current folder to install

.. nextslide::

With this developer installation changes you make to the code should have their impacts when you run the application (provided you run it from the correct Python executable)