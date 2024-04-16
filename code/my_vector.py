import math

class vector:
    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y
        self.vec2 = (self.x, self.y)
        self.mag = self.magnitude()
    
    def magnitude(self) -> float:
        return math.sqrt(self.vec2[0]**2 + self.vec2[1]**2)

    def normalize(self) -> tuple[float, float]:
        return ( (self.vec2[0] / self.mag), (self.vec2[1] / self.mag) ) 

    def vec_update(self) -> tuple[float, float]:
        self.x_dir, self.y_dir = self.normalize()
        return ( self.x_dir * self.magnitude(), self.y_dir * self.magnitude() ) 
