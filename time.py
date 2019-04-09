""" The PygamePlus time module """

import pygame

true  = True
false = False

FPS   = 60
clock = pygame.time.Clock()

def update():
    global clock

    clock.tick(FPS)

def setFPS(newFPS):
    global FPS

    FPS = newFPS

