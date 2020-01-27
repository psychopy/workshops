Counterbalancing trials in PsychoPy Builder
=======================================

Once you've worked out how to create blocks of trials in Builder, learning how
to counterbalance them is only a small extension. You keep the idea of having
a conditions file for each block, which will then be chosen by an outer loop
but now you need to add the multiple *blocks* files, one for each counterbalance
order that you want to include.

Solution
-----------------

We've taken a copy of the solution to Exercise 8.2 then renamed the blocks.xlsx
file to be groupA.xlsx and added groupB.xlsx which is almost the same, but with
the other order of the rows.

In your Experiment Settings add a field to the info dialog called "group" with
a default of A. We'll use this to select the blocks xlsx file later.

Now in the the blocks loop we need to make two changes:

  1. set it to be 'sequential' instead of 'random' so that the order we set in
     in the block conditions file gets used consistently
  2. set the conditions file to be

        $"group{}.xlsx".format(expInfo['group'])

That last step was the hardest part and you could make it more explicit
if you like by creating a variable in the beginning of the experiment called
something like `blockFile` and then setting the conditions file in the loop to
be $blockFile to use that variable. If you don't like the formatted strings idea
(where we used {} and then .format() ) then you could instead do

  blockFile = "group" + expInfo['group'] + "xlsx"

We've just collapsed the two steps into a single line that creates the variable
and uses it, but do whatever makes most sense for you!

References
-----------------

Peirce, J.W. and MacAskill, M. (2018). "Building experiments in PsychoPy." Sage Publishing.
