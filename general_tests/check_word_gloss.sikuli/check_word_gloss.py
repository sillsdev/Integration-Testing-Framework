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

# View Gloss tab, make sure gloss is suggested and focus shifts
click(Pattern("Gloss-1.png").similar(0.81))
hover("1438706667507.png")    # Move to blank space so the hovertext doesn't appear
wait(2)
exists("asdfghhahaha.png")
click(Pattern("Luhukooo.png").targetOffset(-16,0))
click("Noun.png")
type(Key.ENTER)
exists(Pattern("Luhukooo-1.png").similar(0.86))

# View Analyze tab, make sure focus is kept
click(Pattern("Analyze.png").similar(0.90))
hover("1438706667507.png")    # Move to blank space so the hovertext doesn't appear
exists(Pattern("LJLoooLJLooo.png").similar(0.80))

# Go back to Lexicon Edit
click("Lexicon.png")
click("LexiconEdit.png")

