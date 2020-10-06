#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2020.2.4),
    on October 06, 2020, at 22:48
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
expName = 'rotating_eyes'  # from the Builder filename that created this script
expInfo = {'session': '001', 'participant': ''}
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName
expInfo['psychopyVersion'] = psychopyVersion

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data/%s_%s_%s' % (expInfo['participant'], expName, expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath='C:\\Users\\44797\\Documents\\GitHub\\workshops\\examples2019\\builder\\dynamicStimuli\\rotatingEyes\\rotating_eyes_lastrun.py',
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
    size=[800,600], fullscr=False, screen=0, 
    winType='pyglet', allowGUI=True, allowStencil=False,
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
left_eye = visual.Polygon(
    win=win, name='left_eye',units='height', 
    edges=100, size=(0.3, 0.2),
    ori=0, pos=(-0.3, 0),
    lineWidth=1, lineColor='white', lineColorSpace='rgb',
    fillColor='white', fillColorSpace='rgb',
    opacity=1, depth=0.0, interpolate=True)
left_pupil = visual.Polygon(
    win=win, name='left_pupil',units='height', 
    edges=100, size=0.05,
    ori=0, pos=[0,0],
    lineWidth=1, lineColor='black', lineColorSpace='rgb',
    fillColor='black', fillColorSpace='rgb',
    opacity=1, depth=-1.0, interpolate=True)
right_eye = visual.Polygon(
    win=win, name='right_eye',units='height', 
    edges=100, size=(0.3, 0.2),
    ori=0, pos=(+0.3, 0),
    lineWidth=1, lineColor='white', lineColorSpace='rgb',
    fillColor='white', fillColorSpace='rgb',
    opacity=1, depth=-2.0, interpolate=True)
right_pupil = visual.Polygon(
    win=win, name='right_pupil',units='height', 
    edges=100, size=0.05,
    ori=0, pos=[0,0],
    lineWidth=1, lineColor='black', lineColorSpace='rgb',
    fillColor='black', fillColorSpace='rgb',
    opacity=1, depth=-3.0, interpolate=True)

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# ------Prepare to start Routine "trial"-------
continueRoutine = True
routineTimer.add(10.000000)
# update component parameters for each repeat
# keep track of which components have finished
trialComponents = [left_eye, left_pupil, right_eye, right_pupil]
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
    
    # *left_eye* updates
    if left_eye.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        left_eye.frameNStart = frameN  # exact frame index
        left_eye.tStart = t  # local t and not account for scr refresh
        left_eye.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(left_eye, 'tStartRefresh')  # time at next scr refresh
        left_eye.setAutoDraw(True)
    if left_eye.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > left_eye.tStartRefresh + 10-frameTolerance:
            # keep track of stop time/frame for later
            left_eye.tStop = t  # not accounting for scr refresh
            left_eye.frameNStop = frameN  # exact frame index
            win.timeOnFlip(left_eye, 'tStopRefresh')  # time at next scr refresh
            left_eye.setAutoDraw(False)
    
    # *left_pupil* updates
    if left_pupil.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        left_pupil.frameNStart = frameN  # exact frame index
        left_pupil.tStart = t  # local t and not account for scr refresh
        left_pupil.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(left_pupil, 'tStartRefresh')  # time at next scr refresh
        left_pupil.setAutoDraw(True)
    if left_pupil.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > left_pupil.tStartRefresh + 10.0-frameTolerance:
            # keep track of stop time/frame for later
            left_pupil.tStop = t  # not accounting for scr refresh
            left_pupil.frameNStop = frameN  # exact frame index
            win.timeOnFlip(left_pupil, 'tStopRefresh')  # time at next scr refresh
            left_pupil.setAutoDraw(False)
    if left_pupil.status == STARTED:  # only update if drawing
        left_pupil.setPos((-0.3+sin(t*2)/10, 0), log=False)
    
    # *right_eye* updates
    if right_eye.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        right_eye.frameNStart = frameN  # exact frame index
        right_eye.tStart = t  # local t and not account for scr refresh
        right_eye.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(right_eye, 'tStartRefresh')  # time at next scr refresh
        right_eye.setAutoDraw(True)
    if right_eye.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > right_eye.tStartRefresh + 10-frameTolerance:
            # keep track of stop time/frame for later
            right_eye.tStop = t  # not accounting for scr refresh
            right_eye.frameNStop = frameN  # exact frame index
            win.timeOnFlip(right_eye, 'tStopRefresh')  # time at next scr refresh
            right_eye.setAutoDraw(False)
    
    # *right_pupil* updates
    if right_pupil.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        right_pupil.frameNStart = frameN  # exact frame index
        right_pupil.tStart = t  # local t and not account for scr refresh
        right_pupil.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(right_pupil, 'tStartRefresh')  # time at next scr refresh
        right_pupil.setAutoDraw(True)
    if right_pupil.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > right_pupil.tStartRefresh + 10.0-frameTolerance:
            # keep track of stop time/frame for later
            right_pupil.tStop = t  # not accounting for scr refresh
            right_pupil.frameNStop = frameN  # exact frame index
            win.timeOnFlip(right_pupil, 'tStopRefresh')  # time at next scr refresh
            right_pupil.setAutoDraw(False)
    if right_pupil.status == STARTED:  # only update if drawing
        right_pupil.setPos((+0.3+sin(t*2)/10, 0), log=False)
    
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
thisExp.addData('left_eye.started', left_eye.tStartRefresh)
thisExp.addData('left_eye.stopped', left_eye.tStopRefresh)
thisExp.addData('left_pupil.started', left_pupil.tStartRefresh)
thisExp.addData('left_pupil.stopped', left_pupil.tStopRefresh)
thisExp.addData('right_eye.started', right_eye.tStartRefresh)
thisExp.addData('right_eye.stopped', right_eye.tStopRefresh)
thisExp.addData('right_pupil.started', right_pupil.tStartRefresh)
thisExp.addData('right_pupil.stopped', right_pupil.tStopRefresh)

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
