# this class represents an object that can seek other targets

class Vehicle:
    def __init__(self, x, y): #, radius):
        self.pos = PVector(x, y)
        self.vel = PVector(0, 0)
        self.acc = PVector(0, 0)
        self.mass = random(2, 5)
        self.r = sqrt(self.mass) * 5
        self.max_speed = random(2, 10)
        self.max_force = random(0.05, 0.5)
    
    
    # shows the vehicle
    def show(self):
        pushMatrix()
        translate(self.pos.x, self.pos.y)
        rotate(self.vel.heading())
        
        fill(0, 0, 100, 80)
        r = self.r
        triangle(r, 0,
                 0, r/2,
                 0, -r/2)
        
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
