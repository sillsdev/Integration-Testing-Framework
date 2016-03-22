from test_helper import *


# Make sure the word exists
wait("Lexicon.png",300)
click("Lexicon.png")
click("LexiconEdit.png")
exists("asdfghasdfgh.png")

# Enter text if it's not there
click("VTexts6W0rc.png")
click(Pattern("Basehne.png").similar(0.90))
click("1438706667507.png")    # Move cursor to blank space
if not exists("1439580090308.png"):
    paste("asdfgh jjjj")

# View Analyze tab, put jjjj in focus
click(Pattern("Analyze.png").similar(0.90))
hover("1438706667507.png")    # Move to blank space so the hovertext doesn't appear
if not exists(Pattern("LJLoooLJLooo.png").similar(0.80)):
    click("LukuboouLuku.png")

# Split word
click(Pattern("1438704084589.png").targetOffset(4,2))
type("-")
exists(Pattern("1438704193830.png").similar(0.90))

# Verify that second morpheme is a suffix
click(Pattern("LJLoooLJLooo-1.png").targetOffset(10,0))
click("CreateNewEnt.png")
wait(2)
exists(Pattern("MorphemeType.png").similar(0.90))
click(Pattern("Cancel.png").similar(0.91))

# Put 'jjjj' back into one word so the test works next time
# Maybe not necessary? Since a new project gets created every time
# all scripts are run....
click(Pattern("1438704193830.png").targetOffset(-37,1))
click(Pattern("1438706343069.png").similar(0.95).targetOffset(-23,1))
click("Lexicon-1.png")
