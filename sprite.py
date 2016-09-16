import pygame

class Sprite:
    def __init__(self, image_name, pos=(0, 0)):
        self.img = pygame.image.load(image_name)
        self.img.convert()
        self.img_rect = self.img.get_rect()
        
        self.setPos(pos)
     
    def setPos(self, pos):
        self.img_rect.left = pos[0]
        self.img_rect.top  = pos[1]
     
    def draw(self, surface):
        surface.blit(self.img, self.img_rect)
        
        