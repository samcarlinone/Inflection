import pygame
import random

from sprite             import Sprite
from player             import Player
from controller         import Controller
from particle_engine    import Particle_Engine
from vec2               import Vec2


Color  = pygame.Color

# Engine Code
window    = pygame.display.set_mode((640, 400))
surface   = pygame.Surface((640, 400))
clock     = pygame.time.Clock()
tick_rate = 1000/60
last_tick = 0
running   = 1

# Game Code
controller = Controller()
player = Player(Vec2(32, 32), Sprite("Inflection.png"), controller)
p_engine = Particle_Engine(Sprite("Particle.png"))
a = p_engine.createAttractor(Vec2(40, 40), 30)

for x in range(-5, 5):
    for y in range(-5, 5):
        p_engine.spawnParticles(Vec2(40+x, 40+y), 1)


def game_tick():
    player.step()
    p_engine.step()
    a.p.x = player.pos.x + 32
    a.p.y = player.pos.y + 32
    # Nothing Yet

def game_draw():
    surface.fill((255, 255, 255))
    
    player.render(surface)
    p_engine.render(surface)
    

while running:
    event = pygame.event.poll()
    
    while event.type != pygame.NOEVENT:
        print(event)
        
        if event.type == pygame.QUIT:
            running = 0
            break
        
        if event.type == pygame.KEYDOWN:
            controller.keyDown(event)
            
        if event.type == pygame.KEYUP:
            controller.keyUp(event)
            
        event = pygame.event.poll()
        
        
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