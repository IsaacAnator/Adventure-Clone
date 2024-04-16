import pygame

screen = pygame.display.set_mode((720,480))
clock = pygame.Clock()

time_passed_seconds = 1 
def time_passed(t):
    global time_passed_seconds
    time_passed_seconds = t/1000
