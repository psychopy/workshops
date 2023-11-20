#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2020.2.10),
    on January 08, 2021, at 23:43
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""

from __future__ import absolute_import, division

from psychopy import locale_setup
from psychopy import prefs
from psychopy import sound, gui, visual, core, data, event, logging, clock
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)

import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle
import os  # handy system and path functions
import sys  # to get file system encoding

from psychopy.hardware import keyboard



# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)

# Store info about the experiment session
psychopyVersion = '2020.2.10'
expName = 'unitDemo2'  # from the Builder filename that created this script
expInfo = {'participant': '', 'session': '001'}
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName
expInfo['psychopyVersion'] = psychopyVersion

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data/%s_%s_%s' % (expInfo['participant'], expName, expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath='C:\\Users\\44797\\Documents\\GitHub\\workshops\\psychopy_examples\\builder\\spatialUnits\\unitDemo_lastrun.py',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.DEBUG)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp
frameTolerance = 0.001  # how close to onset before 'same' frame

# Start Code - component code to be run after the window creation

# Setup the Window
win = visual.Window(
    size=[1080, 720], fullscr=False, screen=0, 
    winType='pyglet', allowGUI=True, allowStencil=False,
    monitor='testMonitor', color=[0,0,0], colorSpace='rgb',
    blendMode='avg', useFBO=True, 
    units='height')
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess

# create a default keyboard (e.g. to check for escape)
defaultKeyboard = keyboard.Keyboard()

# Initialize components for Routine "rectMover"
rectMoverClock = core.Clock()
mags = {
    'height': 0.1,
    'norm': 0.1,
    'pix': 100,
    'cm': 1,
    'deg': pi/10,
}
unitCodes = {
    'h': 'height',
    'n': 'norm',
    'p': 'pix',
    'c': 'cm',
    'd': 'deg'
}
stim = visual.Rect(
    win=win, name='stim',
    width=(0.5, 0.5)[0], height=(0.5, 0.5)[1],
    ori=0, pos=(0, 0),
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=[1,1,1], fillColorSpace='rgb',
    opacity=1, depth=-1.0, interpolate=True)
inst = visual.TextStim(win=win, name='inst',
    text='Move: up, down, left, right\nScale: minus = shrink, equals = grow\nUnits: p = pix, h = height, n = norm, c = cm, d = deg\nReset: r',
    font='Arial',
    pos=(0, -0.4), height=0.025, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);
poslog = visual.TextStim(win=win, name='poslog',
    text='default text',
    font='Arial',
    pos=[0,0], height=0.05, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-3.0);

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# ------Prepare to start Routine "rectMover"-------
continueRoutine = True
# update component parameters for each repeat
# keep track of which components have finished
rectMoverComponents = [stim, inst, poslog]
for thisComponent in rectMoverComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
rectMoverClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "rectMover"-------
while continueRoutine:
    # get current time
    t = rectMoverClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=rectMoverClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    keys = event.getKeys()
    if keys:
        # Get key
        if 'escape' in keys:
            continueRoutine = False
            break
        key = keys.pop()
        pol = (key in ['right', 'up', 'equal'])*2-1  # Polarity: Whatever dimension, move up or down?
        mag = mags[stim.units]  # Magnitude to move by
        if key in ['left', 'right']:
            # Move along the x axis
            stim.pos = (stim.pos[0] + mag*pol, 
                        stim.pos[1])
        if key in ['up', 'down']:
            # Move along the y axis
            stim.pos = (stim.pos[0], 
                        stim.pos[1] + mag*pol)
        if key in ['equal', 'minus']:
            # Move along the size axis
            if stim.size[0] + mag*pol>=0: # only if size greater than 0
                stim.size = (stim.size[0] + mag*pol,
                            stim.size[1] + mag*pol)
        if key in ['h', 'p', 'n', 'c', 'd']:
            # Set units
            stim.units = unitCodes[key]
            poslog.units = unitCodes[key]
        if key in ['r']:
            # Reset
            stim.units = 'height'
            stim.size = (0.1, 0.1)
            stim.pos = (0, 0)
    
    # *stim* updates
    if stim.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        stim.frameNStart = frameN  # exact frame index
        stim.tStart = t  # local t and not account for scr refresh
        stim.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(stim, 'tStartRefresh')  # time at next scr refresh
        stim.setAutoDraw(True)
    
    # *inst* updates
    if inst.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        inst.frameNStart = frameN  # exact frame index
        inst.tStart = t  # local t and not account for scr refresh
        inst.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(inst, 'tStartRefresh')  # time at next scr refresh
        inst.setAutoDraw(True)
    
    # *poslog* updates
    if poslog.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        poslog.frameNStart = frameN  # exact frame index
        poslog.tStart = t  # local t and not account for scr refresh
        poslog.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(poslog, 'tStartRefresh')  # time at next scr refresh
        poslog.setAutoDraw(True)
    if poslog.status == STARTED:  # only update if drawing
        poslog.setPos(stim.pos)
        poslog.setText(f"pos: ({stim.pos[0]:.2f}, {stim.pos[1]:.2f})\nsize: ({stim.size[0]:.2f}, {stim.size[1]:.2f})\nunits: {stim.units}")
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in rectMoverComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "rectMover"-------
for thisComponent in rectMoverComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('stim.started', stim.tStartRefresh)
thisExp.addData('stim.stopped', stim.tStopRefresh)
thisExp.addData('inst.started', inst.tStartRefresh)
thisExp.addData('inst.stopped', inst.tStopRefresh)
thisExp.addData('poslog.started', poslog.tStartRefresh)
thisExp.addData('poslog.stopped', poslog.tStopRefresh)
# the Routine "rectMover" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# Flip one final time so any remaining win.callOnFlip() 
# and win.timeOnFlip() tasks get executed before quitting
win.flip()

# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv', delim='auto')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
