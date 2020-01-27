Corsi blocks task
----------------------

Really basic version of the Corsi blocks task in PsychoPy.

The subject must click the squares with the mouse in the same sequence that they had flashed red.

To make it slightly easier to track which squares are already pressed, and to acknowledge the click, they turn a darker grey after a click. When all squares are click the next trial starts.


Issues
+++++++++

At the moment there's no code to prevent squares overlapping. Options to fix:

 1. the positions could be manually pre-coded 
 2. they could be random, as currently, but retry if overlapping
 3. they could be arranged on a grid and then jittered to appear random

Under option 3 the sequences would also need shuffling. Currently they can always be the same because square 1 moves to a new location all the time.


