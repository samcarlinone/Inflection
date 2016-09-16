from vec2 import Vec2
import pygame

class Sprite:
    def __init__(self, image_name, pos=Vec2(0,0)):
        self.img = pygame.image.load(image_name)
        self.img.convert()
        self.img_rect = self.img.get_rect()
        
        self.setPos(pos)
     
    def setPos(self, pos):
        self.img_rect.left = pos.x
        self.img_rect.top  = pos.y
     
    def draw(self, surface):
        surface.blit(self.img, self.img_rect)
        
        