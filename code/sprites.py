import pygame
from pygame.locals import *
from globals import *
from my_vector import *


class Sprite(pygame.sprite.Sprite):
    def __init__(self, x:int, y:int, size:int, speed:int, color: str) -> None:
        super().__init__()
        self.map_location_x = 0
        self.map_location_y = 0
        self.current_location = f"tilemaps/map_location{self.map_location_x}{self.map_location_y}.csv"
        self.color = color
        self.size = size
        self.speed = speed
        self.distance = self.speed * get_time()
        self.sprite_size: tuple[int,int] = (self.size, self.size)
        self.image = pygame.Surface(self.sprite_size)
        self.image.fill(self.color)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.view = pygame.Rect(self.rect.x - 5 * tile_size, self.rect.y - 5 * tile_size, 10 * tile_size, 10 * tile_size)
        self.position = vector(self.rect.x, self.rect.y)
        self.heading_x = 0
        self.heading_y = 0
        players.add(self)

    def check_collision_x(self):
        self.collide = pygame.sprite.spritecollideany(self, all_sprites)
        if self.collide is not None:
            if self.heading_x > 0:
                self.rect.x = self.collide.rect.left - self.rect.width
            if self.heading_x < 0:
                self.rect.x = self.collide.rect.right 

    def check_collision_y(self):
        self.collide = pygame.sprite.spritecollideany(self, all_sprites)
        if self.collide is not None:
            if self.heading_y > 0:
                self.rect.y = self.collide.rect.top - self.rect.height
            if self.heading_y < 0:
                self.rect.y = self.collide.rect.bottom 

    def check_location(self):
        if self.rect.center[0] >= tile_size * tile_num_x:
            self.map_location_x += 1
            self.current_location = f"tilemaps/map_location{self.map_location_x}{self.map_location_y}.csv"
            self.rect.x -= tile_size * tile_num_x
        if self.rect.center[0] <= 0:
            self.map_location_x -= 1
            self.current_location = f"tilemaps/map_location{self.map_location_x}{self.map_location_y}.csv"
            self.rect.x += tile_size * tile_num_x
        if self.rect.center[1] >= tile_size * tile_num_y:
            self.map_location_y -= 1
            self.current_location = f"tilemaps/map_location{self.map_location_x}{self.map_location_y}.csv"
            self.rect.y -= tile_size * tile_num_y
        if self.rect.center[1] <= 0:
            self.map_location_y += 1
            self.current_location = f"tilemaps/map_location{self.map_location_x}{self.map_location_y}.csv"
            self.rect.y += tile_size * tile_num_y

    def move_sprite(self):
        keys = pygame.key.get_pressed()
        if keys[K_RIGHT] or keys[K_d]:
            self.heading_x += 1
        if keys[K_LEFT] or keys[K_a]:
           self.heading_x -= 1
        if keys[K_UP] or keys[K_w]:
            self.heading_y -= 1
        if keys[K_DOWN] or keys[K_s]:
            self.heading_y += 1

    def update(self):
        self.move_sprite()
        if self.heading_x == self.heading_y == 0:
            return
        self.heading = vector(self.heading_x, self.heading_y)
        self.heading_x, self.heading_y = self.heading.normalize()
        self.rect.x += self.heading_x * self.distance
        self.check_collision_x()
        self.rect.y += self.heading_y * self.distance
        self.check_collision_y()
        self.check_location()
        self.view = pygame.Rect(self.rect.x - 5 * tile_size, self.rect.y - 5 * tile_size, 10 * tile_size, 10 * tile_size)
        self.heading_x = self.heading_y = 0



class Wall(pygame.sprite.Sprite):
    def __init__(self, x: int, y: int, size: int, color: str):
        super().__init__()
        self.color = color
        self.size = (size, size)
        self.image = pygame.Surface(self.size)
        self.image.fill(self.color)
        self.rect = self.image.get_rect(topleft=(x, y))
        walls.add(self)
        all_sprites.add(self)


