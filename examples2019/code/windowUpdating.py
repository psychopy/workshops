from psychopy import visual, gui, core, event

win = visual.Window([1024,768], fullscr = True)
msg = visual.TextStim(win, 'this is full-screen mode (good timing)',color='white')

msg.draw()
win.flip()
core.wait(1)

win.winHandle.set_visible(False)

info={'what do you think?':''}
dlg = gui.DlgFromDict(info)

win.winHandle.set_visible(True)

msg.text = "you said:" + info['what do you think?']
msg.draw()
win.flip()
event.waitKeys()