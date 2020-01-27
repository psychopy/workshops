#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v3.0.2),
    on Wed Jan 23 12:41:13 2019
If you publish work using this script please cite the PsychoPy publications:
    Peirce, JW (2007) PsychoPy - Psychophysics software in Python.
        Journal of Neuroscience Methods, 162(1-2), 8-13.
    Peirce, JW (2009) Generating stimuli for neuroscience using PsychoPy.
        Frontiers in Neuroinformatics, 2:10. doi: 10.3389/neuro.11.010.2008
"""

from __future__ import absolute_import, division
from psychopy import locale_setup, sound, gui, visual, core, data, event, logging, clock
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)
import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle
import os  # handy system and path functions
import sys  # to get file system encoding


# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)

# Store info about the experiment session
psychopyVersion = '3.0.2'
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
    originPath='/Users/lpzjwp/OneDrive - The University of Nottingham/workshops/examples2019/builder/dynamic stimuli/flashDrag/flashDrag_lastrun.py',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp

# Start Code - component code to be run before the window creation

# Setup the Window
win = visual.Window(
    size=[1440, 900], fullscr=True, screen=0,
    allowGUI=False, allowStencil=False,
    monitor='testMonitor', color=[0,0,0], colorSpace='rgb',
    blendMode='avg', useFBO=True)
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess

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
t = 0
trialClock.reset()  # clock
frameN = -1
continueRoutine = True
routineTimer.add(10.000000)
# update component parameters for each repeat
# keep track of which components have finished
trialComponents = [rotatingDisk, topTarget, bottomTarget, fixation]
for thisComponent in trialComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "trial"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = trialClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *rotatingDisk* updates
    if t >= 0.0 and rotatingDisk.status == NOT_STARTED:
        # keep track of start time/frame for later
        rotatingDisk.tStart = t
        rotatingDisk.frameNStart = frameN  # exact frame index
        rotatingDisk.setAutoDraw(True)
    frameRemains = 0.0 + 10- win.monitorFramePeriod * 0.75  # most of one frame period left
    if rotatingDisk.status == STARTED and t >= frameRemains:
        rotatingDisk.setAutoDraw(False)
    if rotatingDisk.status == STARTED:  # only update if drawing
        rotatingDisk.setOri(sin(t*5)*50, log=False)
    
    # *topTarget* updates
    if t >= 0 and topTarget.status == NOT_STARTED:
        # keep track of start time/frame for later
        topTarget.tStart = t
        topTarget.frameNStart = frameN  # exact frame index
        topTarget.setAutoDraw(True)
    frameRemains = 0 + 10- win.monitorFramePeriod * 0.75  # most of one frame period left
    if topTarget.status == STARTED and t >= frameRemains:
        topTarget.setAutoDraw(False)
    if topTarget.status == STARTED:  # only update if drawing
        topTarget.setOpacity(abs(sin(t*5))>0.99, log=False)
    
    # *bottomTarget* updates
    if t >= 0 and bottomTarget.status == NOT_STARTED:
        # keep track of start time/frame for later
        bottomTarget.tStart = t
        bottomTarget.frameNStart = frameN  # exact frame index
        bottomTarget.setAutoDraw(True)
    frameRemains = 0 + 10- win.monitorFramePeriod * 0.75  # most of one frame period left
    if bottomTarget.status == STARTED and t >= frameRemains:
        bottomTarget.setAutoDraw(False)
    if bottomTarget.status == STARTED:  # only update if drawing
        bottomTarget.setOpacity(abs(sin(t*5))>0.99, log=False)
    
    # *fixation* updates
    if t >= 0.0 and fixation.status == NOT_STARTED:
        # keep track of start time/frame for later
        fixation.tStart = t
        fixation.frameNStart = frameN  # exact frame index
        fixation.setAutoDraw(True)
    frameRemains = 0.0 + 10- win.monitorFramePeriod * 0.75  # most of one frame period left
    if fixation.status == STARTED and t >= frameRemains:
        fixation.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
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
# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
