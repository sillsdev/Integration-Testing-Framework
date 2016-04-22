from sikuli import *
from test_helper import *

# In a function so we can it to run from another test.

def close_box():
    click("Cancel.png")

# path: should be the absolute path to the .fwbackup file.
# flex_is_open: True if Flex is already open, and we're opening
# the project via File > Project Management > Restore.
# False if we're just on Flex's opening screen.
def open_backup(path, flex_is_open):
    # Opening: Get to the 'Restore a Project' screen
    ################
    if flex_is_open:
        click(Pattern("File.png").similar(0.90))
        click("ProjectManag.png")
        click("RestoreaProj.png")
    else:
        # Not sure if this line is needed...
        #subprocess.Popen("fieldworks-flex &")
        click(Pattern("icon_Restoreaproj.png").similar(0.89))
        
    # Goal: Find the backup
    #################
    if not click(Pattern("Anotherlocat.png").similar(0.80).targetOffset(-48,1)):
        close_box()
    if not click(Pattern("Browse.png").similar(0.90)):
        close_box()
    click("1436284725146.png")
    click("1436284725146.png")
    paste(path)
    type(Key.ENTER)
   
    click(Pattern("OK.png").similar(0.91))
    
    if exists(Pattern("7ReplaceExls.png").similar(0.88)):
        click(Pattern("Yes.png").similar(0.95))
        wait(60)
        Debug.user("Successfully opened project: " + path.split("/")[-1])
    else:
        Debug.user("Successfully opened project: " + path.split("/")[-1])
    wait(120)
        
