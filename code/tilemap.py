import pygame
import csv
from globals import *
from sprites import *

class tilemap(pygame.sprite.Sprite):
    def __init__(self, file_location):
        super().__init__()
        self.current_location = file_location
        self.read_tilemap()

    def read_tilemap(self):
        self.tilemap = []
        with open(self.current_location, 'r') as file:
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
                    Wall(x=self.current_tile, y=self.current_row, size=tile_size, color='black')

    def update(self):
        if self.current_location == player1.current_location:
            return
        self.current_location = player1.current_location
        self.read_tilemap()

