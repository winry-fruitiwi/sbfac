# this class represents an object
class Vehicle:
    def __init__(self, x, y, radius):
        self.pos = PVector(abs(PVector.random2D().x), abs(PVector.random2D().y))
        self.vel = PVector.random2D().mult(0.1)
        self.acc = PVector(0, 0)
        self.mass = random(2, 5)
        self.r = sqrt(self.mass) * 5
    
    
    # shows the vehicle
    def show(self):
        translate(self.pos.x, self.pos.y)
        fill(0, 0, 100, 80)
        r = self.r
        triangle(r, 0,
                 0, r/2,
                 0, -r/2)
    
    
    # modifies the velocity and acceleration
    def update(self):
        self.pos.add(self.vel)
        self.vel.add(self.acc)
        self.acc = PVector(0, 0)
    
    
    # apply_force applies a force to the vehicle using Newton's second law, F=ma
    def apply_force(self, force):
        # Newton's second law says F=ma, so a=F/m
        self.acc = force.div(self.mass)
    
    
    # seek makes the target look for an object it wants to pursue (eat, in the case of food). This is not the 
    # same as pursue, which makes the vehicle predict the future! This is arguably the hardest part O.o
    def seek(self, target): # target is a PVector!
        pass
    
