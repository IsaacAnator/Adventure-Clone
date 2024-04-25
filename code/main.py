import pygame
from pygame.locals import *
from sys import exit

# importing my files
from my_vector import *
from globals import *
import tilemap

# initialize variables
pygame.init()
time_passed(clock.tick(30))
tilemap.tilemap()

view = pygame.Surface(size=(200,200))
view.fill('red')
view.set_colorkey('red')

def draw_screen():
    screen.fill(bar_color)
    game_screen.fill(background_color)
    game_screen.set_clip((tilemap.player1.rect.centerx - 50, tilemap.player1.rect.centery - 50), (100,100))
    all_sprites.update()
    all_sprites.draw(game_screen)
    players.update()
    players.draw(game_screen)
    
    game_screen.blit(view,(tilemap.player1.rect.centerx - 50, tilemap.player1.rect.centery - 50))

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

    draw_screen()
    time_passed(clock.tick(30))


