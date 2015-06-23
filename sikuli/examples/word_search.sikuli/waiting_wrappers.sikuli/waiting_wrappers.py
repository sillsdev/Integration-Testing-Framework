"""
These guys just do their thing and then wait either
the specified time (in seconds), or 1 second if no
time is specified.
"""

from sikuli import *

def Click(thing, time=1):
    click(thing)
    wait(time)

def DoubleClick(thing, time=1):
    doubleClick(thing)
    wait(time)

def Type(text, time=1):
    type(text)
    wait(time)

def Find(thing, time=1):
    find(thing)
    wait(time)