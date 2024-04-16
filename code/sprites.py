import pygame
from globals import *
from my_vector import *

class sprite(pygame.sprite.Sprite):
    def __init__(self, x:int, y:int, size:int, speed:int) -> None:
        super().__init__()
        self.size = size
        self.speed = speed
        self.distance = self.speed * time_passed_seconds
        self.x = x
        self.y = y
        self.position = vector(self.x, self.y)
        self.heading_x = 0
        self.heading_y = 0
        self.sprite_size: tuple[int,int] = (int(screen.get_width()/72*.01*self.size), int(screen.get_height()/48*.01*self.size))
        self.image = pygame.Surface(self.sprite_size)
        self.image.fill('black')
        self.rect = self.image.get_rect()
        self.rect.center = (self.x, self.y)

    def update_position(self):
        if self.heading_x == self.heading_y == 0:
            return
        self.heading = vector(self.heading_x, self.heading_y)
        self.heading_x, self.heading_y = self.heading.normalize()
        self.x += self.heading_x * self.distance
        self.y += self.heading_y * self.distance
        self.rect.center = (self.x, self.y)
        self.heading_x = self.heading_y = 0


