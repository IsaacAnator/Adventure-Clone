import pygame
import csv
from globals import *
from sprites import *

class tilemap(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.current_location = "tilemaps/map_location00.csv"
        self.moved = False
        self.draw_tilemap(self.current_location)
        self.rect = (0,0,0,0)
        self.image = pygame.Surface((0,0))
        all_sprites.add(self)

    def draw_tilemap(self, tilemap_location):
        self.tilemap = []
        with open(tilemap_location, 'r') as file:
            self.csv_reader = csv.reader(file)
            for row in self.csv_reader:
                row_value = []
                for value in row:
                    row_value.append(value)
                self.tilemap.append(row_value)
        for i, row in enumerate(self.tilemap):
            for j, value in enumerate(row):
                if value == ".":
                    pass
                elif value == "w":
                    self.current_tile = int(j*tile_size)
                    self.current_row = int(i*tile_size)
                    Wall(x=self.current_tile, y=self.current_row, size=tile_size, color='white')
                # only spawn player if he is starting the game
                elif value == "p" and self.moved == False:
                    self.current_tile = int(j*tile_size)
                    self.current_row = int(i*tile_size)
                    global player1
                    player1 = Sprite(x=self.current_tile, y=self.current_row, size=tile_size, speed=player_speed, color='blue')
                elif value == "r":
                    self.current_tile = int(j*tile_size)
                    self.current_row = int(i*tile_size)
                    Wall(x=self.current_tile, y=self.current_row, size=tile_size, color='red')

    def update(self):
        if self.current_location != player1.current_location:
            self.current_location = player1.current_location
            self.moved = True
            all_sprites.empty()
            all_sprites.add(self)
            self.draw_tilemap(self.current_location)


