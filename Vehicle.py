# this class represents an object that can seek other targets

class Vehicle:
    def __init__(self, x, y): #, radius):
        self.pos = PVector(x, y)
        self.vel = PVector(0, 0)
        self.acc = PVector(0, 0)
        self.mass = random(6, 20)
        self.r = sqrt(self.mass) * 15
        self.max_speed = random(6, 10)
        self.max_force = random(0.05, 0.8)
    
    
    # shows the vehicle
    def show(self):
        pushMatrix()
        translate(self.pos.x, self.pos.y)
        rotate(self.vel.heading())
        
        fill(0, 0, 100, 80)
        r = self.r
        # r=10
        
        # triangle(r, 0,
        #          0, r/2,
        #          0, -r/2)
        
        # We want a 9S hackbot. I'm doing the preliminary version: a kite with a dot.
        
        # I'm going to manage this better.
        
        fill(0, 0, 80, 100)
        #stroke(0, 0, 80, 100)
        
        
        stroke(0, 0, 0, 100)
        strokeWeight(1)
        
        
        beginShape()
        vertex(-r/3, 0) # back
        vertex(0, r/3) # top
        vertex(r, 0) # nose
        vertex(0, -r/3) # bottom
        vertex(-r/3, 0) # back
        endShape()
        
        
        fill(0, 0, 0, 100)
        strokeWeight(2)
        # black circle and line extending to the back
        circle(0, 0, r/4)
        line(0, 0, -r/3, 0)
        
        x = (r/3)/(sqrt(3)+1.0/3)
        
        # complicated equation lines
        line(0, 0, x, sqrt(3) * x)
        line(0, 0, x, -sqrt(3) * x)
        noStroke()
        
        strokeWeight(1)
        stroke(0, 0, 0, 100)
        fill(0, 0, 80, 100)
        
        # squares on butt
        square(-r/3, r/3, r/6)
        square(-r/3, -r/3, r/6)
        
        popMatrix()
    
    
    # modifies the velocity and acceleration
    def update(self):
        self.pos.add(self.vel)
        self.vel.add(self.acc)
        self.vel.limit(self.max_speed)
        self.acc = PVector(0, 0)
    
    
    # apply_force applies a force to the vehicle using Newton's second law, F=ma
    def apply_force(self, force):
        # Newton's second law says F=ma, so a=F/m
        self.acc = force.div(self.mass)
    
    
    # seek makes the target look for an object it wants to pursue. This is not the 
    # same as pursue, which makes the vehicle predict the future!
    # This is arguably the hardest part O.o
    def seek(self, target): # target is a PVector!
        # we need to find the difference between the target's and our positions, which will
        # help us find the desired velocity.
        desired = PVector.sub(target, self.pos) # we don't want to modify target.
        desired.setMag(self.max_speed)
        desired.sub(self.vel)
        desired.limit(self.max_force)
        self.apply_force(desired)
