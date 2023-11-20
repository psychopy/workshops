from psychopy import visual, event, misc, core
"""This demo shows you how to create/use a shape as a button
We make a parit of buttons, we make them rotate aorund the window
(just because we can!) and then we test if the mouse clicked them
"""

nTrials = 3

win = visual.Window([800,600])

redPill = visual.Circle(win, size=[0.1, 0.4], fillColor='red')
bluePill = visual.Circle(win, size=[0.1, 0.4], fillColor='blue')

mouse = event.Mouse()

for thisTrial in range(nTrials):
    lastChoice = None
    core.wait(0.5)
    for frameN in range(1000):
        redTheta = frameN*0.2
        blueTheta = frameN*(-0.4)
        
        redPill.pos = misc.pol2cart(redTheta, radius=0.6)
        bluePill.pos = misc.pol2cart(blueTheta, radius=0.8)
        
        redPill.draw()
        bluePill.draw()
        win.flip()
        
        if sum(mouse.getPressed()):
            if redPill.contains(mouse) and lastChoice != 'red':
                print("You chose the red pill")
                lastChoice = 'red'
            elif bluePill.contains(mouse) and lastChoice != 'blue':
                print("You chose the blue pill")
                lastChoice = 'blue'
            else:
                print("you missed!!!")
                lastChoice = 'miss'
            break # this trial is done
        

