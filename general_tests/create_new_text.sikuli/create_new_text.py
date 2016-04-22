from test_helper import *


# Opening
##############
wait("OTextsWord.png",300)
click("OTextsWord.png")
LEFT_SIDEBAR.click("InterlinearT.png")
TOOLBARS.click(Pattern("1435693467339.png").similar(0.90))

# Goal
###############
click(Pattern("TitleIFreEng.png").targetOffset(48,-18))
type("Bonjour")
click(Pattern("TitleIFreEng.png").targetOffset(48,9))
type("Hello" + Key.TAB)
type("asdf zxcv werdtfyguuio")
Region(147,101,537,692).exists("Bonjour.png")

