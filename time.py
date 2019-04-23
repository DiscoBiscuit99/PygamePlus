""" The PygamePlus time module """

import pygame

true  = True
false = False

dt = 0

FPS   = 60
clock = pygame.time.Clock()

prev_time = 0
current_time = pygame.time.get_ticks()

def update():
    global dt
    global clock
    global prev_time
    global current_time

    current_time = pygame.time.get_ticks()

    # deltaTime in seconds.
    dt = (current_time - prev_time) / 1000.0
    prev_time = current_time

    clock.tick(FPS)

def setFPS(newFPS):
    global FPS

    FPS = newFPS

