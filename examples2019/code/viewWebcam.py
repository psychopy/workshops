from psychopy import visual
import cv2

win = visual.Window([800,600])
webCam = cv2.VideoCapture(0)

# create your stimulus (top of script)camView = visual.ImageStim(win, size=[0.5, 0.5], pos=[-0.5, 0.5],
                           flipVert=True)  # webcam reads bottom to topfor n in range(1000):    # get a frame from the camera    returnVal, frame = webCam.read()    # convert color to psychopy format    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)/255.0    camView.image = frame    camView.draw()    win.flip()
    