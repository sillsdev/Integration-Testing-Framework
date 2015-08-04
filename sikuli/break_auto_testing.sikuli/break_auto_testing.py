import a_setup
from test_helper import TestHelper
from Regionplus import Regionplus

helper = TestHelper("break_auto_testing")

# Set Vernacular keyboard to French
helper.Click(Pattern("Format.png").similar(0.80), "'Format' not found")
helper.Click("SetupWriting.png", "'Set up Writing Systems' not found in Format menu")
analysis = helper.Find("Analysis_Wri-1.png", "'Analysis Writing Systems' not found")
Regionplus(helper, analysis.above().right()).Click("Modify.png",
    "'Modify...' button not found above and to the right of 'Analysis Writing Systems'")
helper.Click(Pattern("f__AIII_l__l.png").similar(0.80), "'Keyboard' tab not found")
helper.Click("FrenchFrench.png", "French keyboard not found")
for i in range(2):
    helper.Click(Pattern("OK.png").similar(0.90), "OK button not found", restart=True)

# Create new entry
helper.Click("1435675185765.png", "'Create new lexical entry' button not found")
paste("asdfgh")
helper.Click(Pattern("Gloss.png").similar(0.90).targetOffset(-10,21), "'Gloss' field not found")
paste("hahaha")
helper.Click(Pattern("Create.png").similar(0.90), "'Create' button not found")
wait(1)

# Verify input languagea
helper.Click(Pattern("FreLexemeFON.png").targetOffset(114,4), "'Lexeme Form' field not found")
Regionplus(helper, find("1438702584115.png").right()).Exists("Eh-1.png",
    "Lexeme Form field input keyboard not in French")
helper.Click(Pattern("EngNote.png").targetOffset(94,1), "'Note' field not found")
Regionplus(helper, find("1438702584115.png").right()).Exists("Een-1.png",
    "Note field input keyboard not in English")

# Enter text
helper.Click("VTexts6W0rc.png", "'Texts & Words' not found")
helper.Click(Pattern("InfoBaseline.png").targetOffset(-39,34), "'Baseline' tab not found")
paste("asdfgh jjjj")

# View Gloss tab, make sure gloss is suggested and focus shifts
helper.Click(Pattern("Gloss-1.png").similar(0.81), "'Gloss' tab not found")
hover("1438706667507.png")    # Move to blank space so the hovertext doesn't appear
wait(2)
helper.Exists("asdfghhahaha.png", "'hahaha' gloss not suggested for 'asdfgh'")
helper.Click(Pattern("Luhukooo.png").targetOffset(-16,0), "Drop down menu not found")
helper.Click("Noun.png", "'Noun' not found")
type(Key.ENTER)
helper.Exists(Pattern("Luhukooo-1.png").similar(0.86), "'jjjj' word not in focus in Gloss tab")
helper.Click(Pattern("Analyze.png").similar(0.90), "'Analyze' tab not found")
hover("1438706667507.png")    # Move to blank space so the hovertext doesn't appear

# View Analyze tab, make sure focus is kept and word splits in two
helper.Exists(Pattern("LJLoooLJLooo.png").similar(0.80), "'jjjj' word not in focus in Analyze tab")
helper.Click(Pattern("1438704084589.png").targetOffset(4,2), "'jjjj' not found on Morpheme line")
paste("-")
helper.Exists("1438704193830.png", "Word not split into two morphemes")
helper.Click(Pattern("LJLoooLJLooo-1.png").targetOffset(10,0), "Drop down menu not found")

# Verify that second morpheme is a suffix
helper.Click("CreateNewEnt.png", "'Create New Entry' not found in drop down menu")
wait(2)
helper.Exists(Pattern("MorphemeType.png").similar(0.90), "Morpheme type not listed as '-suffix'")

# Exit and put 'jjjj' back into one word so the test works next time
helper.Click(Pattern("Cancel.png").similar(0.91), "'Cancel' button not found", restart=True)
helper.Click(Pattern("1438704193830.png").targetOffset(-37,1), "Drop down menu not found")
helper.Click(Pattern("1438706343069.png").similar(0.95).targetOffset(-23,1), "'jjjj' option not found in drop down menu")
helper.Click("Lexicon-1.png", "'Lexicon' button not found")


helper.write_success()