""" The PygamePlus event module """ 

import pygame

true  = True
false = False

def shouldQuit():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return true
        else:
            return false

def quit():
    pygame.quit()
    quit()

