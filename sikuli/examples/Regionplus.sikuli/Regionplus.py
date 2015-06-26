from sikuli import *

class Regionplus(Region):

    def Click(self, thing, debug=0, time=1):
        if debug ==0:
            self.click(thing)
        else:
            try:
                self.click(thing)
            except FindFailed, ff:
                popup(ff.message)
                exit(1)
        wait(time)
    
    def DoubleClick(self, thing, debug=0, time=1):
        if debug == 0:
            self.doubleClick(thing)
        else:
            try:
                self.doubleClick(thing)
            except FindFailed, ff:
                if debug > 0:
                    popup(ff.message)
                    exit(1)
        wait(time)
    
    def Type(self, text, time=1):
        self.type(text)
        wait(time)
    
    def Find(self, thing, debug=0, time=1):
        if debug == 0:
            self.find(thing)
        else:
            try:
                self.find(thing)
            except FindFailed, ff:
                if debug > 0:
                    popup(ff.message)
                    exit(1)
    
        def offset(self, x, y):
            return offset(Location(x, y))