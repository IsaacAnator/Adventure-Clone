import pygame
from pygame.locals import *
from sys import exit

# importing my files
from my_vector import *
from globals import *
import tilemap
import sprites

# initialize variables
pygame.init()
time_passed(clock.tick(30))
tilemap.tilemap(file_location="tilemaps/map_location_0.csv")

player1 = sprites.Sprite(x=100, y=200, size=tile_size, speed=250, color='red') 

def draw_screen():
    screen.fill(bar_color)
    game_screen.fill(background_color)
    all_sprites.update()
    all_sprites.draw(game_screen)
    players.update()
    players.draw(game_screen)
    screen.blit(game_screen, screen_center, None)
    pygame.display.update()

# event handler
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.VIDEORESIZE:
            center_screen_x = event.w / 2
            center_screen_y = event.h / 2
            screen_center = (center_screen_x - game_screen.get_width()/2, center_screen_y - game_screen.get_height()/2)

    keys = pygame.key.get_pressed()
    if keys[K_RIGHT]:
        player1.heading_x += 1
    if keys[K_LEFT]:
       player1.heading_x -= 1
    if keys[K_UP]:
        player1.heading_y -= 1
    if keys[K_DOWN]:
        player1.heading_y += 1

    draw_screen()
    time_passed(clock.tick(30))


