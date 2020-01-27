Selectively inspect an image
=======================================

This demo shows the flexibility of dynamic stimuli. 

We create an experiment where participants can only see a portion of the image by creating an image (called circleMask.png in this case) that we use to occlude our stimulus images. We set the circleMask to be the "mask" of an image stimulus.

You can see that this sort of dynamic stimulus is useful in various ways:
 - you could see what parts of an image people choose to look at while gathering info
 - with an eyetracker you could make it a gaze-contingent display and see what happens when the peripheral vision is not permitted (or reverse the mask and see what happens when viewers can *only* use their peripheral vision.

Details: what did we do?
-----------------------------

You can use any image as a mask. When you do this the opacity of the ImageStimulus is determined by the brightness of the pixels in the mask. If you look at the image circleAperture.png you'll see that most of the pixels are white (which will be opqaue) and just a few pixels (a circle in the center of the screen) are black. For this particular mask we've set the image to be 512x512 pixels and then drawn a circle of 20 pixels diameter in the center. We've then smoothed that with a gaussian blur of 10 pixels to give it a nice smooth edge.

We've then applied that image to an Image Component that we've called imageAperture and that has an image set to `color` and the color itself is `white` (meaning that no image is being superimposed, just a white mask). We've set the mask to be our mask image file and we've set the size to be 4x4 in `height` units (so that the outer edges of the mask image are always beyond the screen). You can see how that works by shrinking the size of the imageAperture, as we've done in the `showMeHow` Routine.

The final effect is an aperture that follows the mouse (we've turned on the mouse cursor in the experiment settings so you can see what's happening).

