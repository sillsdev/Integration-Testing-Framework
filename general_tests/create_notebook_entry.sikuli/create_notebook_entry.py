from test_helper import *

# Opening
##############
wait("Notebook5.png",300)
click("Notebook5.png")
LEFT_SIDEBAR.wait("RecordEdit.png",60)
LEFT_SIDEBAR.click("RecordEdit.png",)
TOOLBARS.click(Pattern("1435614864882.png").similar(0.96))

# Goal
##############
type("hello world" + Key.ENTER)
Region(147,101,537,692).exists("helloworld.png")