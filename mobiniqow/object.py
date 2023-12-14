from mobiniqow.vector import *

class Object:
    def __init__(self,*args):
        self.args = args

    
    def move(self,v):
        for i in self.args:
            i.move(v)
    def p(self):
        for i in self.args:
            i.print()