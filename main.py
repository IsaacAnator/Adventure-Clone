import pygame
from pygame.locals import *
from sys import exit

_ = pygame.init()

screen = pygame.display.set_mode((720,480))
clock = pygame.Clock()

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()

    _ = clock.tick(30)
