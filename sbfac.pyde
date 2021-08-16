# this is a python tutorial based on coding train's 
# 5.2 Seeking a Target video: nature of code 2.0 in P5.js
# https://www.youtube.com/watch?v=p1Ws1ZhG36g
# which is itself based on Craig Reynolds's paper
# ""Steering Behaviors For Autonomous Characters""
# 
# v0.01:    project template, Vehicle.py +comments
# v0.02:    basic triangle chases ball with seek
# v0.02.1:  9S hackbot
# v0.03:    flee + seek and flee toggle
# v0.04:    target class and movement controls
# v0.04.1:  pursuit, acceleration vector drawing, railpath for target
# v0.04.2:  quadratic pursuit + evade in method
# v0.05:    draw velocity and acceleration vectors in Vehicle
# v0.06:    arrive

from Vehicle import *


def setup():
    global movers, toggle, toggle_future, target
    # frameRate(20)
    noStroke()
    rectMode(CENTER) # there is no ; in python. I'm used to Java now!
    toggle = True
    toggle_future = False
    colorMode(HSB, 360, 100, 100, 100)
    background(220, 79, 35)
    #frameRate(20)
    size(815, 815)
    movers = []
    target = Target(8, 8)
    target.apply_force(PVector(0, 1))
    for i in range(10):
        # why do most of the movers start far away from the screen?
        movers.append(Vehicle(random(100, width - 100), random(100, height - 100)))
        #movers.append(Vehicle(width/2, height/2))


def draw():
    global movers, toggle, target
    background(220, 79, 35)
    # print target.vel
    target.update()
    target.show()
    
    # asin(b(x+c))+d
    # target.apply_force(PVector.sub(PVector(width/2, height/2), target.pos))
    target.pos = PVector(mouseX, mouseY)
    # print len(movers)
    
    for mover in movers: # I'm tempted to write {} because of Java!
        
        mover.show()
        mover.update()
        if toggle:
            mover.apply_force(mover.pursue(target))
            fill(89, 99, 64)
            # circle(target.pos.x, target.pos.y, 20)
        
        else:
            mover.apply_force(mover.flee(target))
            fill(0, 99, 64)
            # circle(target.pos.x, target.pos.y, 20)
        
        #mover.apply_force(PVector(0.0001, 0.0003))
    

def mousePressed():
    global toggle, toggle_loop
    
    if toggle:
        toggle = False
        
    else:
        toggle = True
    
    '''
    if mouseButton == RIGHT and toggle_loop:
        loop()
        #toggle_loop = False
    
    if mouseButton == RIGHT and not toggle_loop:
        noLoop()
        toggle_loop = True
    
    ''' # this did not work!


def keyPressed():
    global target
    
    if key == "a":
        target.apply_force(PVector(-5, 0))
    
    if key == "d":
        target.apply_force(PVector(5, 0))
    
    if key == "s":
        target.apply_force(PVector(0, 5))
    
    if key == "w":
        target.apply_force(PVector(0, -5))
    
