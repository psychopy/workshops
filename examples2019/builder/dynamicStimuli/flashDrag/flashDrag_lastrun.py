#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2020.2.4),
    on October 06, 2020, at 22:52
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
psychopyVersion = '2020.2.4'
expName = 'flashDrag'  # from the Builder filename that created this script
expInfo = {'session': '001', 'participant': ''}
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName
expInfo['psychopyVersion'] = psychopyVersion

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data/%s_%s_%s' % (expInfo['participant'], expName, expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath='C:\\Users\\44797\\Documents\\GitHub\\workshops\\examples2019\\builder\\dynamicStimuli\\flashDrag\\flashDrag_lastrun.py',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp
frameTolerance = 0.001  # how close to onset before 'same' frame

# Start Code - component code to be run before the window creation

# Setup the Window
win = visual.Window(
    size=[1440, 900], fullscr=True, screen=0, 
    winType='pyglet', allowGUI=False, allowStencil=False,
    monitor='testMonitor', color=[0,0,0], colorSpace='rgb',
    blendMode='avg', useFBO=True)
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess

# create a default keyboard (e.g. to check for escape)
defaultKeyboard = keyboard.Keyboard()

# Initialize components for Routine "trial"
trialClock = core.Clock()
rotatingDisk = visual.GratingStim(
    win=win, name='rotatingDisk',units='height', 
    tex=random([64,64])*2-1, mask='circle',
    ori=1.0, pos=(0, 0), size=0.8, sf=None, phase=0.0,
    color=[1,1,1], colorSpace='rgb', opacity=1,blendmode='avg',
    texRes=128, interpolate=True, depth=0.0)
topTarget = visual.Polygon(
    win=win, name='topTarget',units='height', 
    edges=50, size=(0.05, 0.05),
    ori=0, pos=(0, 0.3),
    lineWidth=1, lineColor='red', lineColorSpace='rgb',
    fillColor='red', fillColorSpace='rgb',
    opacity=1.0, depth=-1.0, interpolate=True)
bottomTarget = visual.Polygon(
    win=win, name='bottomTarget',units='height', 
    edges=50, size=(0.05, 0.05),
    ori=0, pos=(0, -0.3),
    lineWidth=1, lineColor='red', lineColorSpace='rgb',
    fillColor='red', fillColorSpace='rgb',
    opacity=1.0, depth=-2.0, interpolate=True)
fixation = visual.Polygon(
    win=win, name='fixation',units='height', 
    edges=50, size=(0.01, 0.01),
    ori=0, pos=(0, 0),
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor='red', fillColorSpace='rgb',
    opacity=1, depth=-3.0, interpolate=True)

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# ------Prepare to start Routine "trial"-------
continueRoutine = True
routineTimer.add(10.000000)
# update component parameters for each repeat
# keep track of which components have finished
trialComponents = [rotatingDisk, topTarget, bottomTarget, fixation]
for thisComponent in trialComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
trialClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "trial"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = trialClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=trialClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *rotatingDisk* updates
    if rotatingDisk.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        rotatingDisk.frameNStart = frameN  # exact frame index
        rotatingDisk.tStart = t  # local t and not account for scr refresh
        rotatingDisk.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(rotatingDisk, 'tStartRefresh')  # time at next scr refresh
        rotatingDisk.setAutoDraw(True)
    if rotatingDisk.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > rotatingDisk.tStartRefresh + 10-frameTolerance:
            # keep track of stop time/frame for later
            rotatingDisk.tStop = t  # not accounting for scr refresh
            rotatingDisk.frameNStop = frameN  # exact frame index
            win.timeOnFlip(rotatingDisk, 'tStopRefresh')  # time at next scr refresh
            rotatingDisk.setAutoDraw(False)
    if rotatingDisk.status == STARTED:  # only update if drawing
        rotatingDisk.setOri(sin(t*5)*50, log=False)
    
    # *topTarget* updates
    if topTarget.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
        # keep track of start time/frame for later
        topTarget.frameNStart = frameN  # exact frame index
        topTarget.tStart = t  # local t and not account for scr refresh
        topTarget.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(topTarget, 'tStartRefresh')  # time at next scr refresh
        topTarget.setAutoDraw(True)
    if topTarget.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > topTarget.tStartRefresh + 10-frameTolerance:
            # keep track of stop time/frame for later
            topTarget.tStop = t  # not accounting for scr refresh
            topTarget.frameNStop = frameN  # exact frame index
            win.timeOnFlip(topTarget, 'tStopRefresh')  # time at next scr refresh
            topTarget.setAutoDraw(False)
    if topTarget.status == STARTED:  # only update if drawing
        topTarget.setOpacity(abs(sin(t*5))>0.99, log=False)
    
    # *bottomTarget* updates
    if bottomTarget.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
        # keep track of start time/frame for later
        bottomTarget.frameNStart = frameN  # exact frame index
        bottomTarget.tStart = t  # local t and not account for scr refresh
        bottomTarget.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(bottomTarget, 'tStartRefresh')  # time at next scr refresh
        bottomTarget.setAutoDraw(True)
    if bottomTarget.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > bottomTarget.tStartRefresh + 10-frameTolerance:
            # keep track of stop time/frame for later
            bottomTarget.tStop = t  # not accounting for scr refresh
            bottomTarget.frameNStop = frameN  # exact frame index
            win.timeOnFlip(bottomTarget, 'tStopRefresh')  # time at next scr refresh
            bottomTarget.setAutoDraw(False)
    if bottomTarget.status == STARTED:  # only update if drawing
        bottomTarget.setOpacity(abs(sin(t*5))>0.99, log=False)
    
    # *fixation* updates
    if fixation.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        fixation.frameNStart = frameN  # exact frame index
        fixation.tStart = t  # local t and not account for scr refresh
        fixation.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(fixation, 'tStartRefresh')  # time at next scr refresh
        fixation.setAutoDraw(True)
    if fixation.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > fixation.tStartRefresh + 10-frameTolerance:
            # keep track of stop time/frame for later
            fixation.tStop = t  # not accounting for scr refresh
            fixation.frameNStop = frameN  # exact frame index
            win.timeOnFlip(fixation, 'tStopRefresh')  # time at next scr refresh
            fixation.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in trialComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "trial"-------
for thisComponent in trialComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('rotatingDisk.started', rotatingDisk.tStartRefresh)
thisExp.addData('rotatingDisk.stopped', rotatingDisk.tStopRefresh)
thisExp.addData('topTarget.started', topTarget.tStartRefresh)
thisExp.addData('topTarget.stopped', topTarget.tStopRefresh)
thisExp.addData('bottomTarget.started', bottomTarget.tStartRefresh)
thisExp.addData('bottomTarget.stopped', bottomTarget.tStopRefresh)
thisExp.addData('fixation.started', fixation.tStartRefresh)
thisExp.addData('fixation.stopped', fixation.tStopRefresh)

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
