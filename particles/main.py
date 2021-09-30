# if you don't want the point of emission to be at the mouse's position,just remove line no. 24 in particles.py 
# remove line 18 in particles.py for a constant opacity of the particles

import pygame,sys
from particles import Particles

pygame.init()
screen = pygame.display.set_mode((800,450))
clock = pygame.time.Clock() 
PARTICLE_EVENT = pygame.USEREVENT + 1
pygame.time.set_timer(PARTICLE_EVENT,10)
elapsed =0 

myParticles = Particles(
    screen=screen,
    surface=r"res/orange.png",
    pos_x=0,
    pos_y=0,
    lifetime=3,
    direction_x=2,
    direction_y=2)


def LoopThese():
    pygame.display.set_caption('FPS: %s'%(clock.get_fps() ) )
    screen.fill((20,20,20))
    myParticles.emit()
    pygame.display.update()
    elapsed = clock.tick(120)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == PARTICLE_EVENT:
            myParticles.add_particles()
            
        
for _ in iter(int,1):
    LoopThese()
    