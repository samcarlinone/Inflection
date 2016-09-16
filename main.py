import pygame
import random

from sprite     import Sprite
from player     import Player
from controller import Controller


Color  = pygame.Color

# Engine Code
window    = pygame.display.set_mode((640, 400))
surface   = pygame.Surface((640, 400))
clock     = pygame.time.Clock()
tick_rate = 100
last_tick = 0
running   = 1

# Game Code
player = Player([32, 32], Sprite("Inflection.png"), Controller())

def game_tick():
    player.move()
    # Nothing Yet

def game_draw():
    surface.fill((255, 255, 255))
    
    player.render(surface)
    

while running:
    event = pygame.event.poll()
    if event.type == pygame.QUIT:
        running = 0
        
#     if pygame.mouse.get_pressed()[0]:
#         pos = pygame.mouse.get_pos()
#         pos = (int(pos[0]), int(pos[1]))
#         surface.set_at(pos, pygame.Color(255, 0, 0, 255))

    elapsed = clock.tick()
    last_tick -= elapsed
    
    if(last_tick < -200):
        last_tick = 50

    while last_tick < 0:
        last_tick += tick_rate
        game_tick()

    game_draw()
    
    pygame.transform.scale(surface, (640, 400), window)
    pygame.display.flip()