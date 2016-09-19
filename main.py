import pygame
import random

from sprite             import Sprite
from player             import Player
from controller         import Controller
from particle_engine    import Particle_Engine
from vec2               import Vec2
from base_enemy         import BaseEnemy


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
player = Player(Vec2(32, 32), Sprite("img/Inflection.png"), controller)

p_engine = Particle_Engine(Sprite("img/Particle.png"))

a = p_engine.createAttractor(Vec2(40, 40), 100)
a_click = False
a_time  = 120

enemy = BaseEnemy(Vec2(300, 300), Sprite("img/Placeholder_Circle.png"))


for x in range(-5, 5):
    for y in range(-5, 5):
        p_engine.spawnParticles(Vec2(40+x, 40+y), 1)


def game_tick():
    global a_click
    global a_time
    
    if(random.randint(0, 60)>40):
        p_engine.spawnParticles(Vec2(player.pos.x, player.pos.y), 1)
    
    player.step()
    p_engine.step()
    enemy.step()
    
    p_engine.collide_c([enemy])
    
    if(a_click):
        if(a_time == 0):
            a_click = False
            a.power = 30
            a.mode = "real"
        a_time -= 1
    else:
        a.p.x = player.pos.x + 32
        a.p.y = player.pos.y + 32
    # Nothing Yet

def game_draw():
    surface.fill((255, 255, 255))
    
    player.render(surface)
    enemy.render(surface)
    p_engine.render(surface)
    

while running:
    event = pygame.event.poll()
    
    while event.type != pygame.NOEVENT:
        #print(event)
        
        if event.type == pygame.QUIT:
            running = 0
            break
        
        if event.type == pygame.KEYDOWN:
            controller.keyDown(event)
            
        if event.type == pygame.KEYUP:
            controller.keyUp(event)
            
        if event.type == pygame.MOUSEBUTTONDOWN:
            a_click = True
            a_time = 120
            
            a.power = 100
            a.mode = "grav"
            a.p.x = event.pos[0]
            a.p.y = event.pos[1]
            
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