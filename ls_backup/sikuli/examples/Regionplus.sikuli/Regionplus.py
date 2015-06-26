from sikuli import *

class Regionplus(Region):

def Click(thing, debug=0, time=1):
    try:
        click(thing)
    except FindFailed, ff:
        if debug > 0:
            popup(ff.message)
            exit(1)
    wait(time)

def DoubleClick(thing, debug=0, time=1):
    try:
        doubleClick(thing)
    except FindFailed, ff:
        if debug > 0:
            popup(ff.message)
            exit(1)
    wait(time)

def Type(text time=1):
    type(text)
    wait(time)

def Find(thing, debug=0, time=1):
    try:
        find(thing)
    except FindFailed, ff:
        if debug > 0:
            popup(ff.message)
            exit(1)

    def offset(self, x, y):
        return offset(Location(x, y))