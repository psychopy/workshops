/***************** 
 * Unitdemo Test *
 *****************/

// init psychoJS:
const psychoJS = new PsychoJS({
  debug: true
});

// open window:
psychoJS.openWindow({
  fullscr: false,
  color: new util.Color([0, 0, 0]),
  units: 'height',
  waitBlanking: true
});

// store info about the experiment session:
let expName = 'unitDemo';  // from the Builder filename that created this script
let expInfo = {'participant': '', 'session': '001'};

// Start code blocks for 'Before Experiment'
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
flowScheduler.add(rectMoverRoutineBegin());
flowScheduler.add(rectMoverRoutineEachFrame());
flowScheduler.add(rectMoverRoutineEnd());
flowScheduler.add(quitPsychoJS, '', true);

// quit if user presses Cancel in dialog box:
dialogCancelScheduler.add(quitPsychoJS, '', false);

psychoJS.start({
  expName: expName,
  expInfo: expInfo,
  resources: [
  ]
});

psychoJS.experimentLogger.setLevel(core.Logger.ServerLevel.DEBUG);

function updateInfo() {
  expInfo['date'] = util.MonotonicClock.getDateStr();  // add a simple timestamp
  expInfo['expName'] = expName;
  expInfo['psychopyVersion'] = '2020.2.10';
  expInfo['OS'] = window.navigator.platform;

  // store frame rate of monitor if we can measure it successfully
  expInfo['frameRate'] = psychoJS.window.getActualFrameRate();
  if (typeof expInfo['frameRate'] !== 'undefined')
    frameDur = 1.0 / Math.round(expInfo['frameRate']);
  else
    frameDur = 1.0 / 60.0; // couldn't get a reliable measure so guess

  // add info from the URL:
  util.addInfoFromUrl(expInfo);
  
  return Scheduler.Event.NEXT;
}

function experimentInit() {
  // Initialize components for Routine "rectMover"
  rectMoverClock = new util.Clock();
  mags = {"height": 0.1, "norm": 0.1, "pix": 100, "cm": 1, "deg": (pi / 10)};
  unitCodes = {"h": "height", "n": "norm", "p": "pix", "c": "cm", "d": "deg"};
  
  stim = new visual.Rect ({
    win: psychoJS.window, name: 'stim', 
    width: [0.5, 0.5][0], height: [0.5, 0.5][1],
    ori: 0, pos: [0, 0],
    lineWidth: 1, lineColor: new util.Color([1, 1, 1]),
    fillColor: new util.Color([1, 1, 1]),
    opacity: 1, depth: -1, interpolate: true,
  });
  
  inst = new visual.TextStim({
    win: psychoJS.window,
    name: 'inst',
    text: 'Move: up, down, left, right\nScale: minus = shrink, equals = grow\nUnits: p = pix, h = height, n = norm, c = cm, d = deg\nReset: r',
    font: 'Arial',
    units: undefined, 
    pos: [0, (- 0.4)], height: 0.025,  wrapWidth: undefined, ori: 0,
    color: new util.Color('black'),  opacity: 1,
    depth: -2.0 
  });
  
  poslog = new visual.TextStim({
    win: psychoJS.window,
    name: 'poslog',
    text: 'default text',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.05,  wrapWidth: undefined, ori: 0,
    color: new util.Color('black'),  opacity: 1,
    depth: -3.0 
  });
  
  // Create some handy timers
  globalClock = new util.Clock();  // to track the time since experiment started
  routineTimer = new util.CountdownTimer();  // to track time remaining of each (non-slip) routine
  
  return Scheduler.Event.NEXT;
}

function rectMoverRoutineBegin(snapshot) {
  return function () {
    //------Prepare to start Routine 'rectMover'-------
    t = 0;
    rectMoverClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    // keep track of which components have finished
    rectMoverComponents = [];
    rectMoverComponents.push(stim);
    rectMoverComponents.push(inst);
    rectMoverComponents.push(poslog);
    
    rectMoverComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}

function rectMoverRoutineEachFrame(snapshot) {
  return function () {
    //------Loop for each frame of Routine 'rectMover'-------
    // get current time
    t = rectMoverClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    var _pj;
    function _pj_snippets(container) {
        function in_es6(left, right) {
            if (((right instanceof Array) || ((typeof right) === "string"))) {
                return (right.indexOf(left) > (- 1));
            } else {
                if (((right instanceof Map) || (right instanceof Set) || (right instanceof WeakMap) || (right instanceof WeakSet))) {
                    return right.has(left);
                } else {
                    return (left in right);
                }
            }
        }
        container["in_es6"] = in_es6;
        return container;
    }
    _pj = {};
    _pj_snippets(_pj);
    keys = event.getKeys();
    if (keys) {
        if (_pj.in_es6("escape", keys)) {
            continueRoutine = false;
            break;
        }
        key = keys.pop();
        pol = ((_pj.in_es6(key, ["right", "up", "equal"]) * 2) - 1);
        mag = mags[stim.units];
        if (_pj.in_es6(key, ["left", "right"])) {
            stim.pos = [(stim.pos[0] + (mag * pol)), stim.pos[1]];
        }
        if (_pj.in_es6(key, ["up", "down"])) {
            stim.pos = [stim.pos[0], (stim.pos[1] + (mag * pol))];
        }
        if ((_pj.in_es6(key, ["equal", "minus"]) && (stim.size > 0))) {
            stim.size = [(stim.size[0] + (mag * pol)), (stim.size[1] + (mag * pol))];
        }
        if (_pj.in_es6(key, ["h", "p", "n", "c", "d"])) {
            stim.units = unitCodes[key];
            poslog.units = unitCodes[key];
        }
        if (_pj.in_es6(key, ["r"])) {
            stim.units = "height";
            stim.size = [0.1, 0.1];
            stim.pos = [0, 0];
        }
    }
    
    
    // *stim* updates
    if (t >= 0.0 && stim.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      stim.tStart = t;  // (not accounting for frame time here)
      stim.frameNStart = frameN;  // exact frame index
      
      stim.setAutoDraw(true);
    }

    
    // *inst* updates
    if (t >= 0.0 && inst.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      inst.tStart = t;  // (not accounting for frame time here)
      inst.frameNStart = frameN;  // exact frame index
      
      inst.setAutoDraw(true);
    }

    
    // *poslog* updates
    if (t >= 0.0 && poslog.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      poslog.tStart = t;  // (not accounting for frame time here)
      poslog.frameNStart = frameN;  // exact frame index
      
      poslog.setAutoDraw(true);
    }

    
    if (poslog.status === PsychoJS.Status.STARTED){ // only update if being drawn
      poslog.setPos(stim.pos, false);
      poslog.setText(f'''pos: ({stim.pos[0]:f'''.2f'''}, {stim.pos[1]:f'''.2f'''})
size: ({stim.size[0]:f'''.2f'''}, {stim.size[1]:f'''.2f'''})
units: {stim.units}''', false);
    }
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    rectMoverComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}

function rectMoverRoutineEnd(snapshot) {
  return function () {
    //------Ending Routine 'rectMover'-------
    rectMoverComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    // the Routine "rectMover" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}

function endLoopIteration(scheduler, snapshot) {
  // ------Prepare for next entry------
  return function () {
    if (typeof snapshot !== 'undefined') {
      // ------Check if user ended loop early------
      if (snapshot.finished) {
        // Check for and save orphaned data
        if (psychoJS.experiment.isEntryEmpty()) {
          psychoJS.experiment.nextEntry(snapshot);
        }
        scheduler.stop();
      } else {
        const thisTrial = snapshot.getCurrentTrial();
        if (typeof thisTrial === 'undefined' || !('isTrials' in thisTrial) || thisTrial.isTrials) {
          psychoJS.experiment.nextEntry(snapshot);
        }
      }
    return Scheduler.Event.NEXT;
    }
  };
}

function importConditions(currentLoop) {
  return function () {
    psychoJS.importAttributes(currentLoop.getCurrentTrial());
    return Scheduler.Event.NEXT;
    };
}

function quitPsychoJS(message, isCompleted) {
  // Check for and save orphaned data
  if (psychoJS.experiment.isEntryEmpty()) {
    psychoJS.experiment.nextEntry();
  }
  
  
  psychoJS.window.close();
  psychoJS.quit({message: message, isCompleted: isCompleted});
  
  return Scheduler.Event.QUIT;
}
