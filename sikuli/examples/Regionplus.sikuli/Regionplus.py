from sikuli import *

class Regionplus(Region):

    def __init__(self, test_helper, *args):
        Region.__init__(self, *args)
        self.helper = test_helper

    def set_helper(self, test_helper):
        self.helper = test_helper
        

    def Click(self, thing, message, time=1):
        try:
            self.click(thing)
            wait(time)
            return True
        except FindFailed, ff:
            if self.helper:
                self.helper.write_fail(message)
            return False
        except:
            raise
    
    def DoubleClick(self, thing, message, time=1):
        try:
            self.doubleClick(thing)
            wait(time)
            return True
        except FindFailed, ff:
            if self.helper:
                self.helper.write_fail(message)
            return False
        except:
            raise
    
    def Find(self, thing, message, time=1):
        try:
            self.find(thing)
            wait(time)
            return True
        except FindFailed, ff:
            if self.helper:
                self.helper.write_fail(message)
            return False
        except:
            raise

    def Exists(self, thing, message, time=1):
        if self.exists(thing):
            return True
        else:
            if self.helper:
                self.helper.write_fail(message)
            return False
    
    def offset(self, x, y):
        return offset(Location(x, y))