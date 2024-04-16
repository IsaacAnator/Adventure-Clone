import math

class vector:
    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y
    
    def magnitude(self) -> float:
        return math.sqrt(self.x**2 + self.y**2)

    def normalize(self) -> tuple[float, float]:
        return ( (self.x / self.magnitude()), (self.y / self.magnitude()) ) 

    def vec_update(self) -> tuple[float, float]:
        self.x_dir, self.y_dir = self.normalize()
        return ( self.x_dir * self.magnitude(), self.y_dir * self.magnitude() ) 
