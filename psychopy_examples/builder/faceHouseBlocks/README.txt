Blocking trials in PsychoPy Builder
=======================================

This demo shows how to conduct a set of trials in blocks according to type.
The task is to have 2 different blocks (faces and houses) and for these to
repeat 3 times each in a randomized order.

Solution
-----------------

This first part to completing this task is to understand that you don't need
a different Routine to present houses and faces; you need a single Routine that
presents an image, and then your conditions files designate the type of image.

The next step is to step up two loops and 3 conditions files (one for each block
and another to switch between them). The inner loop has a conditions file that
is a variable, in our case it was called `condsFile`. This `condsFile` can be
faceTrials.xlsx or houseTrials.xlsx and that is chosen by the outer loop (which
uses the blocks.xlsx file to do this).

The ordering and randomization could have been achieved in various ways but,
here, we did it by creating the blocks file with just 2 lines and set them to
repeat 3 times randomly, giving a total of 6 blocks.

References
-----------------

Peirce, J.W. and MacAskill, M. (2018). "Building experiments in PsychoPy." Sage Publishing.