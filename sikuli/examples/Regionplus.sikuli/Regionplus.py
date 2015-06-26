from sikuli import *

class Regionplus(Region):


    def Click(self, thing, time=1):
        click(thing)
        wait(time)

    def DoubleClick(self, thing, time=1):
        doubleClick(thing)
        wait(time)

    def Type(self, text, time=1):
        type(text)
        wait(time)
    
    def Find(self, thing, time=1):
        find(thing)
        wait(time)

    def offset(self, x, y):
        return self.offset(Location(x, y))