#from waiting_wrappers import *

def write_log(line):
    f = open("/vagrant/error_log", "a+")
    try:
        f.write(line + "\n")
    finally:
        f.close()
try:
    click("Createanewpr.png")
    wait(1)
except FindFailed:
    write_log("open_flex: Cannot find `Create a new project`")

type( "hello")
try:
    click("OK.png")
    wait(1)
except FindFailed:
    write_log("open_flex: Cannot find `OK`")
if exists(Pattern("OK-2.png").similar(0.88)):
    try:
        click(Pattern("OK-1.png").similar(0.86))
        wait(1)
    except FindFailed:
        write_log("open_flex: Cannot find `OK`")
else:
    try:
        click(Pattern("Qpen.png").similar(0.80))
        wait(1)
    except FindFailed:
        write_log("open_flex: Cannot find `Open`")
def openHandler(event):
    write_log("open_flex: Successfully opened flex.")
    exit(0)
    
opened = onAppear("1435347136957.png", openHandler)
observe(40)

write_log("open_flex: failed to open")
if exists("Anerrorhasoc.png"):
    write_log("open_flex: An error has occurred (green)")


