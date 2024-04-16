import pygame
from globals import *
from my_vector import *

class sprite(pygame.sprite.Sprite):
    def __init__(self, x:int, y:int, size:int, speed:int) -> None:
        super().__init__()

        self.size = size
        self.speed = speed
        self.x = x
        self.y = y
        self.pos = (self.x, self.y)
        
        sprite_size: tuple[int,int] = (int(screen.get_width()/72*.01*self.size), int(screen.get_height()/48*.01*self.size))
        self.image = pygame.Surface(sprite_size)
        self.image.fill('black')
        self.rect = self.image.get_rect()
        self.rect.center = self.pos

    def update_pos(self):
        self.current_pos = vector(self.x, self.y)
        self.direction = self.current_pos.normalize()
        self.new_pos = ( self.direction[0] + self.x, self.direction[1] + self.y )
        self.rect.center = self.new_pos #type: ignore
