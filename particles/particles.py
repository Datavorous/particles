import pygame
from random import randint,uniform
class Particles:
    def __init__(self,screen,surface,pos_x,pos_y,lifetime,direction_x,direction_y):
        self.screen = screen
        self.pos_x,self.pos_y = pos_x,pos_y
        self.lifetime = lifetime
        self.direction_y = direction_y
        self.direction_x  = direction_x
        self.particles = []
        self.surface = pygame.image.load(surface).convert()
        self.width, self.height = self.surface.get_rect().width, self.surface.get_rect().height

    def emit(self):
        if self.particles:
            self.delete_particles()
            for particle in self.particles:
                self.surface.set_alpha(randint(0,255))
                particle[0].x += particle[1]
                particle[0].y += particle[2]
                particle[3] -= 0.1
                self.screen.blit(self.surface,particle[0])
    def add_particles(self):
        self.pos_x,self.pos_y = pygame.mouse.get_pos()[0] - self.width / 2,pygame.mouse.get_pos()[1] - self.height / 2
        particle_rect = pygame.Rect(int(self.pos_x),int(self.pos_y),self.width,self.height)
        self.particles.append([particle_rect,uniform(-self.direction_x,self.direction_x),uniform(-self.direction_y,self.direction_y),self.lifetime])
    def delete_particles(self):
        particle_copy = [particle for particle in self.particles if particle[3] > 0]
        self.particles = particle_copy