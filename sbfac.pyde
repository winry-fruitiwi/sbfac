# this is a python tutorial based on coding train's 
# 5.2 Seeking a Target video: nature of code 2.0 in P5.js
# https://www.youtube.com/watch?v=p1Ws1ZhG36g
# which is itself based on Craig Reynolds's paper
# ""Steering Behaviors For Autonomous Characters""
# 
# v0.01:    project template, Vehicle.py +comments
# v0.02:    basic triangle chases ball with seek
# v0.021:   9S hackbot
# v0.03:    flee
# v0.04:    pursue, evade
# v0.04.1:  quadratic pursuit + evade in method
# v0.05:    draw velocity and acceleration vectors in Vehicle
# v0.06:    arrive

from Vehicle import *


def setup():
    global movers
    noStroke()
    colorMode(HSB, 360, 100, 100, 100)
    background(220, 79, 35)
    #frameRate(20)
    size(815, 815)
    movers = []
    for i in range(1000):
        # why do most of the movers start far away from the screen?
        movers.append(Vehicle(random(100, width - 100), random(100, height - 100)))


def draw():
    global movers
    background(220, 79, 35)
    target = PVector(mouseX, mouseY)
    fill(89, 99, 64)
    circle(target.x, target.y, 20)
    # print len(movers)
    
    for mover in movers: # I'm tempted to write {} because of Java!
        mover.show()
        mover.update()
        mover.seek(target)
        #mover.apply_force(PVector(0.0001, 0.0003))
