import pygame
from pygame.locals import *
from sys import exit

# importing my files
from my_vector import *
from sprites import *
from globals import *


pygame.init()

background_color = 'white'

player = sprite(x=100, y=200, size=200, speed=10) 

sprites = pygame.sprite.Group()
sprites.add(player)

def draw_screen():
    player.update_position() 
    screen.fill(background_color)
    sprites.draw(screen)
    pygame.display.update()

# event handler
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
    keys = pygame.key.get_pressed()

    if keys[K_RIGHT]:
        player.heading_x += 1
    if keys[K_LEFT]:
        player.heading_x -= 1
    if keys[K_UP]:
        player.heading_y -= 1
    if keys[K_DOWN]:
        player.heading_y += 1

    draw_screen()
    time_passed(clock.tick(30))


