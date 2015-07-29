import sys
sys.path.insert(0, '/home/vagrant/Integration-Testing-Framework/sikuli/examples')

from sikuli import *
from logger import Logger
from waiting_wrappers import *
from flex_regions import *
from Regionplus import *

log = Logger("create_notebook_entry")

try:
    Click("Notebook5.png")
except FindFailed:
    log.write_fail("Couldn't find 'Notebook' button")

try:
    TOOLBARS.Click("1435614864882.png")
except FindFailed:
    log.write_fail("Couldn't find 'Create new record' button")

Type("hello world" + Key.ENTER)

if Region(147,101,537,692).exists("helloworld.png") is None:
    log.write_fail("Cannot find new 'hello world' entry")

if not log.has_fail():
    log.write("Success")
    