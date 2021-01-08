/********************************** 
 * Dynamic_Selective_Inspect Test *
 **********************************/

import { PsychoJS } from 'https://pavlovia.org/lib/core.js';
import * as core from 'https://pavlovia.org/lib/core.js';
import { TrialHandler } from 'https://pavlovia.org/lib/data.js';
import { Scheduler } from 'https://pavlovia.org/lib/util.js';
import * as util from 'https://pavlovia.org/lib/util.js';
import * as visual from 'https://pavlovia.org/lib/visual.js';
import { Sound } from 'https://pavlovia.org/lib/sound.js';

// init psychoJS:
var psychoJS = new PsychoJS({
  debug: true
});

// open window:
psychoJS.openWindow({
  fullscr: true,
  color: new util.Color('white'),
  units: 'height',
  waitBlanking: true
});

// store info about the experiment session:
let expName = 'dynamic_selective_inspect';  // from the Builder filename that created this script
let expInfo = {'session': '001', 'participant': ''};

// schedule the experiment:
psychoJS.schedule(psychoJS.gui.DlgFromDict({
  dictionary: expInfo,
  title: expName
}));

const flowScheduler = new Scheduler(psychoJS);
const dialogCancelScheduler = new Scheduler(psychoJS);
psychoJS.scheduleCondition(function() { return (psychoJS.gui.dialogComponent.button === 'OK'); }, flowScheduler, dialogCancelScheduler);

// flowScheduler gets run if the participants presses OK
flowScheduler.add(updateInfo); // add timeStamp
flowScheduler.add(experimentInit);
flowScheduler.add(instructRoutineBegin);
flowScheduler.add(instructRoutineEachFrame);
flowScheduler.add(instructRoutineEnd);
const trialsLoopScheduler = new Scheduler(psychoJS);
flowScheduler.add(trialsLoopBegin, trialsLoopScheduler);
flowScheduler.add(trialsLoopScheduler);
flowScheduler.add(trialsLoopEnd);
flowScheduler.add(explanationRoutineBegin);
flowScheduler.add(explanationRoutineEachFrame);
flowScheduler.add(explanationRoutineEnd);
const showMeTrialsLoopScheduler = new Scheduler(psychoJS);
flowScheduler.add(showMeTrialsLoopBegin, showMeTrialsLoopScheduler);
flowScheduler.add(showMeTrialsLoopScheduler);
flowScheduler.add(showMeTrialsLoopEnd);
flowScheduler.add(thanksRoutineBegin);
flowScheduler.add(thanksRoutineEachFrame);
flowScheduler.add(thanksRoutineEnd);
flowScheduler.add(quitPsychoJS, '', true);

// quit if user presses Cancel in dialog box:
dialogCancelScheduler.add(quitPsychoJS, '', false);

psychoJS.start({expName, expInfo});

var frameDur;
function updateInfo() {
  expInfo['date'] = util.MonotonicClock.getDateStr();  // add a simple timestamp
  expInfo['expName'] = expName;
  expInfo['psychopyVersion'] = '3.2.3';
  expInfo['OS'] = window.navigator.platform;

  // store frame rate of monitor if we can measure it successfully
  expInfo['frameRate'] = psychoJS.window.getActualFrameRate();
  if (typeof expInfo['frameRate'] !== 'undefined')
    frameDur = 1.0/Math.round(expInfo['frameRate']);
  else
    frameDur = 1.0/60.0; // couldn't get a reliable measure so guess

  // add info from the URL:
  util.addInfoFromUrl(expInfo);
  psychoJS.setRedirectUrls('completedURL', 'incompleteURL');

  return Scheduler.Event.NEXT;
}

var instructClock;
var instructFirst;
var finishInstruct;
var trialClock;
var imageStimulus;
var imageAperture;
var mouse;
var explanationClock;
var instruct2;
var explanationFinish;
var showMeHowClock;
var imageStimulus_2;
var imageAperture_2;
var mouse_2;
var thanksClock;
var text;
var globalClock;
var routineTimer;
function experimentInit() {
  // Initialize components for Routine "instruct"
  instructClock = new util.Clock();
  instructFirst = new visual.TextStim({
    win: psychoJS.window,
    name: 'instructFirst',
    text: 'On each trial you have to search the screen to find the ball\n(by moving the mouse around)\n\nClick the mouse to get started',
    font: 'Arial',
    units : 'height', 
    pos: [0, 0.3], height: 0.05,  wrapWidth: undefined, ori: 0,
    color: new util.Color('black'),  opacity: 1,
    depth: 0.0 
  });
  
  finishInstruct = new core.Mouse({
    win: psychoJS.window,
  });
  finishInstruct.mouseClock = new util.Clock();
  // Initialize components for Routine "trial"
  trialClock = new util.Clock();
  imageStimulus = new visual.ImageStim({
    win : psychoJS.window,
    name : 'imageStimulus', units : 'norm', 
    image : 'images/7751351978_d87ea5d14e_k.jpg', mask : undefined,
    ori : 0, pos : [0, 0], size : [2, 2],
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : true, depth : 0.0 
  });
  imageAperture = new visual.ImageStim({
    win : psychoJS.window,
    name : 'imageAperture', units : 'height', 
    image : 'images/plainWhite.png', mask : 'images/circleMask.png',
    ori : 0, pos : [0, 0], size : [4, 4],
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 512, interpolate : true, depth : -1.0 
  });
  mouse = new core.Mouse({
    win: psychoJS.window,
  });
  mouse.mouseClock = new util.Clock();
  // Initialize components for Routine "explanation"
  explanationClock = new util.Clock();
  instruct2 = new visual.TextStim({
    win: psychoJS.window,
    name: 'instruct2',
    text: 'This is essentially the same thing but\nthe mask is now smaller ( w,h = 2,2 in height units) so you can see \nwhat was happening.',
    font: 'Arial',
    units : 'height', 
    pos: [0, 0.3], height: 0.05,  wrapWidth: undefined, ori: 0,
    color: new util.Color('black'),  opacity: 1,
    depth: 0.0 
  });
  
  explanationFinish = new core.Mouse({
    win: psychoJS.window,
  });
  explanationFinish.mouseClock = new util.Clock();
  // Initialize components for Routine "showMeHow"
  showMeHowClock = new util.Clock();
  imageStimulus_2 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'imageStimulus_2', units : 'norm', 
    image : undefined, mask : undefined,
    ori : 0, pos : [0, 0], size : [2, 2],
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : true, depth : 0.0 
  });
  imageAperture_2 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'imageAperture_2', units : 'height', 
    image : 'images/plainWhite.png', mask : 'images/circleMask.png',
    ori : 0, pos : [0, 0], size : [1, 1],
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 512, interpolate : true, depth : -1.0 
  });
  mouse_2 = new core.Mouse({
    win: psychoJS.window,
  });
  mouse_2.mouseClock = new util.Clock();
  // Initialize components for Routine "thanks"
  thanksClock = new util.Clock();
  text = new visual.TextStim({
    win: psychoJS.window,
    name: 'text',
    text: "That's all there is to it.\n\nBye!",
    font: 'Arial',
    units : undefined, 
    pos: [0, 0], height: 0.1,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: 0.0 
  });
  
  // Create some handy timers
  globalClock = new util.Clock();  // to track the time since experiment started
  routineTimer = new util.CountdownTimer();  // to track time remaining of each (non-slip) routine
  
  return Scheduler.Event.NEXT;
}

var t;
var frameN;
var gotValidClick;
var instructComponents;
function instructRoutineBegin() {
  //------Prepare to start Routine 'instruct'-------
  t = 0;
  instructClock.reset(); // clock
  frameN = -1;
  // update component parameters for each repeat
  // setup some python lists for storing info about the finishInstruct
  gotValidClick = false; // until a click is received
  // keep track of which components have finished
  instructComponents = [];
  instructComponents.push(instructFirst);
  instructComponents.push(finishInstruct);
  
  for (const thisComponent of instructComponents)
    if ('status' in thisComponent)
      thisComponent.status = PsychoJS.Status.NOT_STARTED;
  
  return Scheduler.Event.NEXT;
}

var prevButtonState;
var continueRoutine;
function instructRoutineEachFrame() {
  //------Loop for each frame of Routine 'instruct'-------
  let continueRoutine = true; // until we're told otherwise
  // get current time
  t = instructClock.getTime();
  frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
  // update/draw components on each frame
  
  // *instructFirst* updates
  if (t >= 0.0 && instructFirst.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    instructFirst.tStart = t;  // (not accounting for frame time here)
    instructFirst.frameNStart = frameN;  // exact frame index
    instructFirst.setAutoDraw(true);
  }

  // *finishInstruct* updates
  if (t >= 0.0 && finishInstruct.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    finishInstruct.tStart = t;  // (not accounting for frame time here)
    finishInstruct.frameNStart = frameN;  // exact frame index
    finishInstruct.status = PsychoJS.Status.STARTED;
    finishInstruct.mouseClock.reset();
    prevButtonState = finishInstruct.getPressed();  // if button is down already this ISN'T a new click
    }
  if (finishInstruct.status === PsychoJS.Status.STARTED) {  // only update if started and not finished!
    let buttons = finishInstruct.getPressed();
    if (!buttons.every( (e,i,) => (e == prevButtonState[i]) )) { // button state changed?
      prevButtonState = buttons;
      if (buttons.reduce( (e, acc) => (e+acc) ) > 0) { // state changed to a new click
        // abort routine on response
        continueRoutine = false;
      }
    }
  }
  // check for quit (typically the Esc key)
  if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
    return psychoJS.quit('The [Escape] key was pressed. Goodbye!', false);
  }
  
  // check if the Routine should terminate
  if (!continueRoutine) {  // a component has requested a forced-end of Routine
    return Scheduler.Event.NEXT;
  }
  
  continueRoutine = false;  // reverts to True if at least one component still running
  for (const thisComponent of instructComponents)
    if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
      continueRoutine = true;
      break;
    }
  
  // refresh the screen if continuing
  if (continueRoutine) {
    return Scheduler.Event.FLIP_REPEAT;
  }
  else {
    return Scheduler.Event.NEXT;
  }
}


function instructRoutineEnd() {
  //------Ending Routine 'instruct'-------
  for (const thisComponent of instructComponents) {
    if (typeof thisComponent.setAutoDraw === 'function') {
      thisComponent.setAutoDraw(false);
    }
  }
  // store data for thisExp (ExperimentHandler)
  // the Routine "instruct" was not non-slip safe, so reset the non-slip timer
  routineTimer.reset();
  
  return Scheduler.Event.NEXT;
}

var trials;
var currentLoop;
function trialsLoopBegin(thisScheduler) {
  // set up handler to look after randomisation of conditions etc
  trials = new TrialHandler({
    psychoJS: psychoJS,
    nReps: 1, method: TrialHandler.Method.RANDOM,
    extraInfo: expInfo, originPath: undefined,
    trialList: 'conditions.xlsx',
    seed: undefined, name: 'trials'});
  psychoJS.experiment.addLoop(trials); // add the loop to the experiment
  currentLoop = trials;  // we're now the current loop

  // Schedule all the trials in the trialList:
  for (const thisTrial of trials) {
    thisScheduler.add(importConditions(trials));
    thisScheduler.add(trialRoutineBegin);
    thisScheduler.add(trialRoutineEachFrame);
    thisScheduler.add(trialRoutineEnd);
    thisScheduler.add(endLoopIteration({thisScheduler, isTrials : true}));
  }

  return Scheduler.Event.NEXT;
}


function trialsLoopEnd() {
  psychoJS.experiment.removeLoop(trials);

  return Scheduler.Event.NEXT;
}

var showMeTrials;
function showMeTrialsLoopBegin(thisScheduler) {
  // set up handler to look after randomisation of conditions etc
  showMeTrials = new TrialHandler({
    psychoJS: psychoJS,
    nReps: 1, method: TrialHandler.Method.RANDOM,
    extraInfo: expInfo, originPath: undefined,
    trialList: 'conditions.xlsx',
    seed: undefined, name: 'showMeTrials'});
  psychoJS.experiment.addLoop(showMeTrials); // add the loop to the experiment
  currentLoop = showMeTrials;  // we're now the current loop

  // Schedule all the trials in the trialList:
  for (const thisShowMeTrial of showMeTrials) {
    thisScheduler.add(importConditions(showMeTrials));
    thisScheduler.add(showMeHowRoutineBegin);
    thisScheduler.add(showMeHowRoutineEachFrame);
    thisScheduler.add(showMeHowRoutineEnd);
    thisScheduler.add(endLoopIteration({thisScheduler, isTrials : true}));
  }

  return Scheduler.Event.NEXT;
}


function showMeTrialsLoopEnd() {
  psychoJS.experiment.removeLoop(showMeTrials);

  return Scheduler.Event.NEXT;
}

var trialComponents;
function trialRoutineBegin() {
  //------Prepare to start Routine 'trial'-------
  t = 0;
  trialClock.reset(); // clock
  frameN = -1;
  // update component parameters for each repeat
  // setup some python lists for storing info about the mouse
  gotValidClick = false; // until a click is received
  mouse.mouseClock.reset();
  // keep track of which components have finished
  trialComponents = [];
  trialComponents.push(imageStimulus);
  trialComponents.push(imageAperture);
  trialComponents.push(mouse);
  
  for (const thisComponent of trialComponents)
    if ('status' in thisComponent)
      thisComponent.status = PsychoJS.Status.NOT_STARTED;
  
  return Scheduler.Event.NEXT;
}


function trialRoutineEachFrame() {
  //------Loop for each frame of Routine 'trial'-------
  let continueRoutine = true; // until we're told otherwise
  // get current time
  t = trialClock.getTime();
  frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
  // update/draw components on each frame
  
  // *imageStimulus* updates
  if (t >= 0.0 && imageStimulus.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    imageStimulus.tStart = t;  // (not accounting for frame time here)
    imageStimulus.frameNStart = frameN;  // exact frame index
    imageStimulus.setAutoDraw(true);
  }

  
  // *imageAperture* updates
  if (t >= 0.0 && imageAperture.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    imageAperture.tStart = t;  // (not accounting for frame time here)
    imageAperture.frameNStart = frameN;  // exact frame index
    imageAperture.setAutoDraw(true);
  }

  
  if (imageAperture.status === PsychoJS.Status.STARTED){ // only update if being drawn
    imageAperture.setPos(mouse.getPos());
  }
  // *mouse* updates
  if (t >= 0.0 && mouse.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    mouse.tStart = t;  // (not accounting for frame time here)
    mouse.frameNStart = frameN;  // exact frame index
    mouse.status = PsychoJS.Status.STARTED;
    prevButtonState = mouse.getPressed();  // if button is down already this ISN'T a new click
    }
  if (mouse.status === PsychoJS.Status.STARTED) {  // only update if started and not finished!
    let buttons = mouse.getPressed();
    if (!buttons.every( (e,i,) => (e == prevButtonState[i]) )) { // button state changed?
      prevButtonState = buttons;
      if (buttons.reduce( (e, acc) => (e+acc) ) > 0) { // state changed to a new click
        // abort routine on response
        continueRoutine = false;
      }
    }
  }
  // check for quit (typically the Esc key)
  if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
    return psychoJS.quit('The [Escape] key was pressed. Goodbye!', false);
  }
  
  // check if the Routine should terminate
  if (!continueRoutine) {  // a component has requested a forced-end of Routine
    return Scheduler.Event.NEXT;
  }
  
  continueRoutine = false;  // reverts to True if at least one component still running
  for (const thisComponent of trialComponents)
    if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
      continueRoutine = true;
      break;
    }
  
  // refresh the screen if continuing
  if (continueRoutine) {
    return Scheduler.Event.FLIP_REPEAT;
  }
  else {
    return Scheduler.Event.NEXT;
  }
}


function trialRoutineEnd() {
  //------Ending Routine 'trial'-------
  for (const thisComponent of trialComponents) {
    if (typeof thisComponent.setAutoDraw === 'function') {
      thisComponent.setAutoDraw(false);
    }
  }
  // store data for thisExp (ExperimentHandler)
  const xys = mouse.getPos();
  const buttons = mouse.getPressed();
  psychoJS.experiment.addData('mouse.x', xys[0]);
  psychoJS.experiment.addData('mouse.y', xys[1]);
  psychoJS.experiment.addData('mouse.leftButton', buttons[0]);
  psychoJS.experiment.addData('mouse.midButton', buttons[1]);
  psychoJS.experiment.addData('mouse.rightButton', buttons[2]);
  // the Routine "trial" was not non-slip safe, so reset the non-slip timer
  routineTimer.reset();
  
  return Scheduler.Event.NEXT;
}

var explanationComponents;
function explanationRoutineBegin() {
  //------Prepare to start Routine 'explanation'-------
  t = 0;
  explanationClock.reset(); // clock
  frameN = -1;
  // update component parameters for each repeat
  // setup some python lists for storing info about the explanationFinish
  gotValidClick = false; // until a click is received
  // keep track of which components have finished
  explanationComponents = [];
  explanationComponents.push(instruct2);
  explanationComponents.push(explanationFinish);
  
  for (const thisComponent of explanationComponents)
    if ('status' in thisComponent)
      thisComponent.status = PsychoJS.Status.NOT_STARTED;
  
  return Scheduler.Event.NEXT;
}


function explanationRoutineEachFrame() {
  //------Loop for each frame of Routine 'explanation'-------
  let continueRoutine = true; // until we're told otherwise
  // get current time
  t = explanationClock.getTime();
  frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
  // update/draw components on each frame
  
  // *instruct2* updates
  if (t >= 0.0 && instruct2.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    instruct2.tStart = t;  // (not accounting for frame time here)
    instruct2.frameNStart = frameN;  // exact frame index
    instruct2.setAutoDraw(true);
  }

  // *explanationFinish* updates
  if (t >= 0.0 && explanationFinish.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    explanationFinish.tStart = t;  // (not accounting for frame time here)
    explanationFinish.frameNStart = frameN;  // exact frame index
    explanationFinish.status = PsychoJS.Status.STARTED;
    explanationFinish.mouseClock.reset();
    prevButtonState = explanationFinish.getPressed();  // if button is down already this ISN'T a new click
    }
  if (explanationFinish.status === PsychoJS.Status.STARTED) {  // only update if started and not finished!
    let buttons = explanationFinish.getPressed();
    if (!buttons.every( (e,i,) => (e == prevButtonState[i]) )) { // button state changed?
      prevButtonState = buttons;
      if (buttons.reduce( (e, acc) => (e+acc) ) > 0) { // state changed to a new click
        // abort routine on response
        continueRoutine = false;
      }
    }
  }
  // check for quit (typically the Esc key)
  if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
    return psychoJS.quit('The [Escape] key was pressed. Goodbye!', false);
  }
  
  // check if the Routine should terminate
  if (!continueRoutine) {  // a component has requested a forced-end of Routine
    return Scheduler.Event.NEXT;
  }
  
  continueRoutine = false;  // reverts to True if at least one component still running
  for (const thisComponent of explanationComponents)
    if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
      continueRoutine = true;
      break;
    }
  
  // refresh the screen if continuing
  if (continueRoutine) {
    return Scheduler.Event.FLIP_REPEAT;
  }
  else {
    return Scheduler.Event.NEXT;
  }
}


function explanationRoutineEnd() {
  //------Ending Routine 'explanation'-------
  for (const thisComponent of explanationComponents) {
    if (typeof thisComponent.setAutoDraw === 'function') {
      thisComponent.setAutoDraw(false);
    }
  }
  // store data for thisExp (ExperimentHandler)
  // the Routine "explanation" was not non-slip safe, so reset the non-slip timer
  routineTimer.reset();
  
  return Scheduler.Event.NEXT;
}

var showMeHowComponents;
function showMeHowRoutineBegin() {
  //------Prepare to start Routine 'showMeHow'-------
  t = 0;
  showMeHowClock.reset(); // clock
  frameN = -1;
  // update component parameters for each repeat
  imageStimulus_2.setImage(imageFile);
  // setup some python lists for storing info about the mouse_2
  // current position of the mouse:
  mouse_2.x = [];
  mouse_2.y = [];
  mouse_2.leftButton = [];
  mouse_2.midButton = [];
  mouse_2.rightButton = [];
  mouse_2.time = [];
  gotValidClick = false; // until a click is received
  // keep track of which components have finished
  showMeHowComponents = [];
  showMeHowComponents.push(imageStimulus_2);
  showMeHowComponents.push(imageAperture_2);
  showMeHowComponents.push(mouse_2);
  
  for (const thisComponent of showMeHowComponents)
    if ('status' in thisComponent)
      thisComponent.status = PsychoJS.Status.NOT_STARTED;
  
  return Scheduler.Event.NEXT;
}


function showMeHowRoutineEachFrame() {
  //------Loop for each frame of Routine 'showMeHow'-------
  let continueRoutine = true; // until we're told otherwise
  // get current time
  t = showMeHowClock.getTime();
  frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
  // update/draw components on each frame
  
  // *imageStimulus_2* updates
  if (t >= 0.0 && imageStimulus_2.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    imageStimulus_2.tStart = t;  // (not accounting for frame time here)
    imageStimulus_2.frameNStart = frameN;  // exact frame index
    imageStimulus_2.setAutoDraw(true);
  }

  
  // *imageAperture_2* updates
  if (t >= 0.0 && imageAperture_2.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    imageAperture_2.tStart = t;  // (not accounting for frame time here)
    imageAperture_2.frameNStart = frameN;  // exact frame index
    imageAperture_2.setAutoDraw(true);
  }

  
  if (imageAperture_2.status === PsychoJS.Status.STARTED){ // only update if being drawn
    imageAperture_2.setPos(mouse.getPos());
  }
  // *mouse_2* updates
  if (t >= 0.0 && mouse_2.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    mouse_2.tStart = t;  // (not accounting for frame time here)
    mouse_2.frameNStart = frameN;  // exact frame index
    mouse_2.status = PsychoJS.Status.STARTED;
    mouse_2.mouseClock.reset();
    prevButtonState = mouse_2.getPressed();  // if button is down already this ISN'T a new click
    }
  if (mouse_2.status === PsychoJS.Status.STARTED) {  // only update if started and not finished!
    let buttons = mouse_2.getPressed();
    if (!buttons.every( (e,i,) => (e == prevButtonState[i]) )) { // button state changed?
      prevButtonState = buttons;
      if (buttons.reduce( (e, acc) => (e+acc) ) > 0) { // state changed to a new click
        const xys = mouse_2.getPos();
        mouse_2.x.push(xys[0]);
        mouse_2.y.push(xys[1]);
        mouse_2.leftButton.push(buttons[0]);
        mouse_2.midButton.push(buttons[1]);
        mouse_2.rightButton.push(buttons[2]);
        mouse_2.time.push(mouse_2.mouseClock.getTime());
        // abort routine on response
        continueRoutine = false;
      }
    }
  }
  // check for quit (typically the Esc key)
  if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
    return psychoJS.quit('The [Escape] key was pressed. Goodbye!', false);
  }
  
  // check if the Routine should terminate
  if (!continueRoutine) {  // a component has requested a forced-end of Routine
    return Scheduler.Event.NEXT;
  }
  
  continueRoutine = false;  // reverts to True if at least one component still running
  for (const thisComponent of showMeHowComponents)
    if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
      continueRoutine = true;
      break;
    }
  
  // refresh the screen if continuing
  if (continueRoutine) {
    return Scheduler.Event.FLIP_REPEAT;
  }
  else {
    return Scheduler.Event.NEXT;
  }
}


function showMeHowRoutineEnd() {
  //------Ending Routine 'showMeHow'-------
  for (const thisComponent of showMeHowComponents) {
    if (typeof thisComponent.setAutoDraw === 'function') {
      thisComponent.setAutoDraw(false);
    }
  }
  // store data for thisExp (ExperimentHandler)
  if (mouse_2.x) {  psychoJS.experiment.addData('mouse_2.x', mouse_2.x[0])};
  if (mouse_2.y) {  psychoJS.experiment.addData('mouse_2.y', mouse_2.y[0])};
  if (mouse_2.leftButton) {  psychoJS.experiment.addData('mouse_2.leftButton', mouse_2.leftButton[0])};
  if (mouse_2.midButton) {  psychoJS.experiment.addData('mouse_2.midButton', mouse_2.midButton[0])};
  if (mouse_2.rightButton) {  psychoJS.experiment.addData('mouse_2.rightButton', mouse_2.rightButton[0])};
  if (mouse_2.time) {  psychoJS.experiment.addData('mouse_2.time', mouse_2.time[0])};
  
  // the Routine "showMeHow" was not non-slip safe, so reset the non-slip timer
  routineTimer.reset();
  
  return Scheduler.Event.NEXT;
}

var thanksComponents;
function thanksRoutineBegin() {
  //------Prepare to start Routine 'thanks'-------
  t = 0;
  thanksClock.reset(); // clock
  frameN = -1;
  routineTimer.add(1.000000);
  // update component parameters for each repeat
  // keep track of which components have finished
  thanksComponents = [];
  thanksComponents.push(text);
  
  for (const thisComponent of thanksComponents)
    if ('status' in thisComponent)
      thisComponent.status = PsychoJS.Status.NOT_STARTED;
  
  return Scheduler.Event.NEXT;
}

var frameRemains;
function thanksRoutineEachFrame() {
  //------Loop for each frame of Routine 'thanks'-------
  let continueRoutine = true; // until we're told otherwise
  // get current time
  t = thanksClock.getTime();
  frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
  // update/draw components on each frame
  
  // *text* updates
  if (t >= 0.0 && text.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    text.tStart = t;  // (not accounting for frame time here)
    text.frameNStart = frameN;  // exact frame index
    text.setAutoDraw(true);
  }

  frameRemains = 0.0 + 1.0 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
  if (text.status === PsychoJS.Status.STARTED && t >= frameRemains) {
    text.setAutoDraw(false);
  }
  // check for quit (typically the Esc key)
  if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
    return psychoJS.quit('The [Escape] key was pressed. Goodbye!', false);
  }
  
  // check if the Routine should terminate
  if (!continueRoutine) {  // a component has requested a forced-end of Routine
    return Scheduler.Event.NEXT;
  }
  
  continueRoutine = false;  // reverts to True if at least one component still running
  for (const thisComponent of thanksComponents)
    if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
      continueRoutine = true;
      break;
    }
  
  // refresh the screen if continuing
  if (continueRoutine && routineTimer.getTime() > 0) {
    return Scheduler.Event.FLIP_REPEAT;
  }
  else {
    return Scheduler.Event.NEXT;
  }
}


function thanksRoutineEnd() {
  //------Ending Routine 'thanks'-------
  for (const thisComponent of thanksComponents) {
    if (typeof thisComponent.setAutoDraw === 'function') {
      thisComponent.setAutoDraw(false);
    }
  }
  return Scheduler.Event.NEXT;
}


function endLoopIteration({thisScheduler, isTrials=true}) {
  // ------Prepare for next entry------
  return function () {
    // ------Check if user ended loop early------
    if (currentLoop.finished) {
      // Check for and save orphaned data
      if (Object.keys(psychoJS.experiment._thisEntry).length > 0) {
        psychoJS.experiment.nextEntry();
      }
      thisScheduler.stop();
    } else if (isTrials) {
      psychoJS.experiment.nextEntry();
    }
  return Scheduler.Event.NEXT;
  };
}


function importConditions(loop) {
  const trialIndex = loop.getTrialIndex();
  return function () {
    loop.setTrialIndex(trialIndex);
    psychoJS.importAttributes(loop.getCurrentTrial());
    return Scheduler.Event.NEXT;
    };
}


function quitPsychoJS(message, isCompleted) {
  // Check for and save orphaned data
  if (Object.keys(psychoJS.experiment._thisEntry).length > 0) {
    psychoJS.experiment.nextEntry();
  }
  psychoJS.window.close();
  psychoJS.quit({message: message, isCompleted: isCompleted});

  return Scheduler.Event.QUIT;
}
