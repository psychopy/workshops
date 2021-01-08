from __future__ import division
from psychopy import visual, core, data, event, gui
import numpy as np

#store some sueful info about this experiment
info = {}
info['participant'] = ''
info['gender'] = ['m','f','n/a']
info['consent given'] = False
info['dateStr'] = data.getDateStr()
# prsent dialog to participant
dlg = gui.DlgFromDict(info, fixed=['dateStr'])
if dlg.OK == False or not info['consent given']:
    core.quit()
#additional entries not seen by participant
info['fixTime'] = 0.5
info['cueTime'] = 0.2
info['probeTime'] = 0.2
filename = "data/%s_%s"%(info['participant'], info['dateStr'])

# create our experiment object to save data
thisExp = data.ExperimentHandler(
        name='Posner', version='1.0', #not needed, just handy
        extraInfo = info, #the info we created earlier
        dataFileName = filename, # using our string with data/name_date
        )

win = visual.Window([800,600], fullscr=False, units="pix")
respClock = core.Clock()

# initialise some stimuli
fixation = visual.Circle(
    win, size=20,
    lineColor='fuchsia', fillColor='lightgrey'
    )
probe = visual.ImageStim(
    win, size=80,
    pos = [300,0],
    image = None, mask = "gauss",
    color = "lightgreen"
    )
cue = visual.ShapeStim(
    win, 
    vertices = [[-30,-20], [-30,20], [30,0]],
    lineColor = 'red', fillColor = 'salmon')

#run practice
conditions = data.importConditions('conditions.xlsx')
paractice = data.TrialHandler(trialList=conditions, nReps=5)
thisExp.addLoop(paractice)
for thisTrial in paractice:
    
    fixation.draw()
    win.flip()
    t0 = time.time()
    #update stimuli for this trial
    probe.image = thisTrial['stimFile']
    cue.ori = thisTrial['cueOri']
    probe.pos = (thisTrial['probeX'], 0)
    
    # present stimuli
    timeTaken = time.time()-t0
    core.wait(thisTrial['fixTime']-timeTaken)
    
    fixation.draw()
    cue.draw()
    win.flip()
    core.wait(info['cueTime'])
    
    fixation.draw()
    probe.draw()
    win.flip()
    
    #get response from participant
    respClock.reset() # stim is now visible so this is t=0
    keys = event.waitKeys(keyList = ['right','left','escape'])
    resp = keys[0]
    rt = respClock.getTime()
    # was response corect this trial?
    if thisTrial['probeX']>0 and resp=='right':
        corr = 1
    elif thisTrial['probeX']<0 and resp=='left':
        corr = 1
    elif resp=='escape':
        trials.finished = True
        break
    else:
        corr = 0
        
    trials.addData('resp', resp)
    trials.addData('rt', rt)
    trials.addData('corr', corr)
    thisExp.nextEntry()

#run main
trials = data.TrialHandler(trialList=conditions, nReps=5)
thisExp.addLoop(trials)
for thisTrial in trials:
    runTrial(thisTrial)
    