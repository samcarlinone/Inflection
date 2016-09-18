class Player:
    def __init__(self, pos, sprite, controller):
        self.sprite = sprite
        self.pos = pos
        self.controller = controller
        
        self.sprite.setPos(self.pos)
        
    def step(self):
        self.pos.x += self.controller.xv
        self.pos.y += self.controller.yv
        
        self.sprite.setPos(self.pos)
        
    def render(self, surface):
        self.sprite.draw(surface)