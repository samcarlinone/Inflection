class BaseEnemy:
    def __init__(self, pos, sprite):
        self.sprite = sprite
        self.pos = pos
        self.radius = 128**2
        
        self.sprite.setPos(self.pos)
        
    def step(self):
        i = 1
        #Do Nothing
        
    def render(self, surface):
        self.sprite.draw(surface)
        
    def hit(self):
        self.pos.x += 1
        self.sprite.setPos(self.pos.add_s(64))
        self.pos.sub_s(64)
        
        return False