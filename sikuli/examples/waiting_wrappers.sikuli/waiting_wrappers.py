"""
These guys just do their thing and then wait either
the specified time (in seconds), or 1 second if no
time is specified.
"""

from sikuli import *

def Click(thing, debug=0, time=1):
    if debug ==0:
        click(thing)
    else:
        try:
            click(thing)
        except FindFailed, ff:
            popup(ff.message)
            exit(1)
    wait(time)

def DoubleClick(thing, debug=0, time=1):
    if debug == 0:
        doubleClick(thing)
    else:
        try:
            doubleClick(thing)
        except FindFailed, ff:
            if debug > 0:
                popup(ff.message)
                exit(1)
    wait(time)

def Type(text, time=1):
    type(text)
    wait(time)

def Find(thing, debug=0, time=1):
    if debug == 0:
        find(thing)
    else:
        try:
            find(thing)
        except FindFailed, ff:
            if debug > 0:
                popup(ff.message)
                exit(1)