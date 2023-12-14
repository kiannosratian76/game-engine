from mobiniqow.object import *
from mobiniqow.box import *
from mamad.renderer import *
from kian.controller import Controller 
import keyboard
import time
import os

o = Object(Vector(1,2,3),Vector(1,3,2),Vector(4,2,3),Vector(2,2,3),)
divar = Object(Vector(12,2,3),Vector(12,3,2),Vector(12,2,3),Vector(12,2,3),)
box = Box(*divar.args)
box.init()
frame_rate = 144
mover = Vector(1,0,0)
Rendere.CHARACTER = "."
r =Rendere(100,20)
me = Vector(1,2,3)
ctr = Controller(me)
 
keyboard.on_press_key('w',lambda _:ctr.top())
keyboard.on_press_key('a',lambda _:ctr.right())
keyboard.on_press_key('s',lambda _:ctr.bottom())
keyboard.on_press_key('d',lambda _:ctr.left())
        
# Thread(target=c,args=()).start()
while True:
    time.sleep(1/frame_rate)
    # ctr.move(input())
    r.draw_vector(me)
    # me.move(mover)
    os.system("cls")
    #o.p()
#     #print(box.is_items(o.args[0]))
#     #o.move(mover)
    r.render()