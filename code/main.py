import pygame
from pygame.locals import *
from sys import exit

# importing my files
from my_vector import *
from sprites import *


pygame.init()

background_color = 'white'

sprites = pygame.sprite.Group()

player = sprite(x=100, y=200, size=200, speed=10) 
sprites.add(player)

def draw_screen():
    player.update_pos() 
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
        player.x += player.speed
    if keys[K_LEFT]:
        player.x -= player.speed
    if keys[K_UP]:
        player.y -= player.speed
    if keys[K_DOWN]:
        player.y += player.speed
    
    draw_screen()
    time_passed = clock.tick(30)
