import math

class Vec2:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
    def __getitem__(self, index):
        if(index == 0):
            return self.x
        if(index == 1):
            return self.y
        return None
        
    def add(self, o):
        return Vec2(self.x + o.x, self.y + o.y)
    
    def sub(self, o):
        return Vec2(self.x - o.x, self.y - o.y)
    
    def mul(self, o):
        return Vec2(self.x * o.x, self.y * o.y)
    
    def div(self, o):
        return Vec2(self.x / o.x, self.y / o.y)
    
    def add_i(self, o):
        self.x += o.x
        self.y += o.y
        return self
    
    def sub_i(self, o):
        self.x -= o.x
        self.y -= o.y
        return self
    
    def mul_i(self, o):
        self.x *= o.x
        self.y *= o.y
        return self
    
    def div_i(self, o):
        self.x /= o
        self.y /= o
        return self
    
    def add_s(self, o):
        self.x += o
        self.y += o
        return self
    
    def sub_s(self, o):
        self.x -= o
        self.y -= o
        return self
    
    def mul_s(self, o):
        self.x *= o
        self.y *= o
        return self
    
    def div_s(self, o):
        self.x /= o
        self.y /= o
        return self
    
    def set_i(self, x, y):
        self.x = x
        self.y = y
        
    def clone(self):
        return Vec2(self.x, self.y)
    
    def dist(self, o):
        return math.sqrt((self.x-o.x)**2 + (self.y-o.y)**2)
    
    def dist_sq(self, o):
        return (self.x-o.x)**2 + (self.y-o.y)**2
    
    def mag(self):
        return math.sqrt(self.x**2 + self.y**2)
    
    def mag_sq(self):
        return self.x**2 + self.y**2
    
    def normalize(self):
        d = math.sqrt(self.x**2 + self.y**2)
        
        if(self.mag_sq() == 0):
            return self.clone()
        
        return Vec2(self.x / d, self.y /d)
    
    def normalize_i(self):
        d = math.sqrt(self.x**2 + self.y**2)
        
        if(self.mag_sq() == 0):
            return
        
        self.x /= d
        self.y /= d