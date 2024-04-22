import pygame

#1.6:1 aspect ratio
GAME_WIDTH = 720
GAME_HEIGHT = 450

background_color = 'white'
bar_color = 'grey'
player_speed = 250

tile_num_x = 40
tile_num_y = 25
tile_size = int(GAME_WIDTH/tile_num_x)

screen = pygame.display.set_mode((GAME_WIDTH,GAME_HEIGHT))
game_screen = pygame.Surface((GAME_WIDTH, GAME_HEIGHT))
center_screen_x = screen.get_width() / 2
center_screen_y = screen.get_height() / 2
screen_center = (center_screen_x - game_screen.get_width()/2, center_screen_y - game_screen.get_height()/2)


all_sprites = pygame.sprite.Group()
walls = pygame.sprite.Group()
players = pygame.sprite.Group()

clock = pygame.Clock()
time_passed_seconds = 0
def time_passed(t):
    global time_passed_seconds
    time_passed_seconds = t/1000
def get_time():
    return time_passed_seconds
