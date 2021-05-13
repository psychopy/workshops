Custom Randomisation Demo
=========================

A demo of how to make a pseudorandom list where the word at every nth position is fixed, whilst the interleaving words are randomised. 

Sometimes you don't want stimuli to be presented in a random order in your experiment. Sometimes you need a 'pseudorandom' order. There isn't an "out of box" solution to this in PsychoPy, so you need some code. 

In this demo a list of words is presented with certain words set in a fixed order. 

The file `words-list.xlsx` lists the words to be presented along with whether that stimulus should be in a fixed position or not. 

In the builder file two routines then handle the creation of a trials list that we will word through. 

`loadWords` loads in the xlsx file and adds words to either `allWords` or `fixedWords` depending on if this word should be in a fixed position or not. `fixedPositions` keeps track of the trials where the stimulus to be presented is fixed. 

`makeList` handles the creation of the list itself. Note there are some nuances to the code here to facilitate the easiest translation from Python to Javascript. First we reverse the list of words to be presented in the fixed position 

```
fixedWords.reverse()
```

Then we loop through the number of trials to be presented and check if the word on that trial should be fixed or not, if not we randomly select a word from `allWords` and use `pop()` to remove that word from the list (i.e. sample it witout replacement). If the position is fixed, we fetch the word to be presented at that position and remove that from the set of fixed words. The full code looks like this

```
wordList = []
for trial in range(nTrials):
    if trial not in fixedPositions:
        #shuffle elements
        shuffle(allWords)
        #select last element
        wordList.append(allWords[-1])
        # remove last element
        allWords.pop()
    else:
        wordList.append(fixedWords[-1])
        fixedWords.pop()

print(wordList)
```

Finally we want to show the words, using the `showWords` routine. Note that herei n the `nReps` property of the loop we use `nTrials` to state how many iterations of that loop we want. Within the routine we have two components, `countTrials` uses a custom variablt `trialCount` so count how many trials have been presented. `text` shows the desired word by using `trialCount` to index a word from our `wordList`. 

Hope this helps!