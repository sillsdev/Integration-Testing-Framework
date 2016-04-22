from sikuli import *
from test_helper import *

def restart_flex():
    Debug.user("restarting flex")
    if myOS == OS.LINUX:
        type("t", KeyModifier.CTRL | KeyModifier.ALT)
        wait(5)
        type("sudo /home/vagrant/Integration-Testing-Framework/general_tests/helpers/restart_flex.sh && exit" + Key.ENTER)
    else:
        popup("Only able to restart FLEx on Linux!")
        Debug.user("Only able to restart FLEx on Linux!")
        exit(1)

    # If the 'hello' project shows up as the last opened project,
    # just press enter
    if exists(Pattern("iii3iuE.png").similar(0.90)):
        Debug.user("Success")
        type(Key.ENTER)
        wait(20)

    # If not, try to find it in the 'Open project screen'
    else:
        click("Openaproject.png")
        hello = find(Pattern("hello.png").similar(0.90))
        if hello:
            doubleClick(hello)
                  wait(20)
            Debug.user("Success")

        # As a last resort, try to create the project (this shouldn't happen
        # and will probably not work: green screen if hello already exists.)
        else:
            Debug.user("'hello' project not found, quitting.")
            exit()
    wait(180)
