import random
from vec2 import Vec2

class Particle_Engine:
    def __init__(self, sprite):
        self.sprite = sprite
        
        self.particles = []
        self.attractors = []
     
    def render(self, surface):
        for particle in self.particles:
            self.sprite.setPos(particle.p)
            self.sprite.draw(surface)
            
    def spawnParticles(self, pos, num):
        for i in range(0, num):
            self.particles.append(Particle(pos.clone(), Vec2(1, 0), 1))
            
    def createAttractor(self, pos, power):
        a = Attractor(pos.clone(), power)
        self.attractors.append(a)
        return a

    def step(self):
        for part in self.particles:
            part.t_force.x = 0
            part.t_force.y = 0
            
            for force in self.attractors:
                direction = part.p.sub(force.p)
                
                dist = direction.mag()
                
                direction.normalize_i()
                
                if(dist == 0):
                    dist = 0
                else:
                    dist = -force.power / dist**2
                    
                if(dist > 0.000001):
                    dist = 0.000001
                
                part.t_force.add_i(direction.mul_s(dist))
                
            #Add Drag
            part.t_force.add_i(part.v.clone().div_s(50).mul_s(-1))
                
        for part in self.particles:
            part.v.add_i(part.t_force.div_s(part.mass))
            part.p.add_i(part.v)
        
class Particle:
    def __init__(self, p, v, life):
        self.p = p
        self.v = v
        self.t_force = Vec2(0, 0)
        self.mass = 1
        self.lifetime = life
        
class Attractor:
    def __init__(self, p, power):
        self.p = p
        self.power = power