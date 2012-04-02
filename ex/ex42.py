class TheThing(object):

    # why self? function has no idea what you are calling any one "instance" of TheThing or another
    
    # set up a Python class with internal variables
    def __init__(self):
        self.number = 0
    
    def some_function(self):
        print "I got called"
    
    def add_me_up(self, more):
        self.number += more
        return self.number
        
# two different things
a = TheThing()
b = TheThing()

a.some_function()
b.some_function()

print a.add_me_up(20)
print b.add_me_up(30)

class TheMultiplier(object):
    def __init__(self, base):
        self.base = base
    def do_it(self,m):
        return m * self.base
        
x = TheMultiplier(a.number)
print x.do_it(b.number)