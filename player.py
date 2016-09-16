class Player:
    def __init__(self, pos, sprite, controller):
        self.sprite = sprite
        self.pos = pos
        self.controller = controller
        
        self.sprite.setPos(self.pos)
        
    def move(self):
        self.pos[0] += self.controller.xv
        self.pos[1] += self.controller.yv
        
        self.sprite.setPos(self.pos)
        
    def render(self, surface):
        self.sprite.draw(surface)