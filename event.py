""" The PygamePlus event module """ 

import pygame

true  = True
false = False

def shouldQuit(event):
    if event.type == pygame.QUIT:
        return true
    else:
        return false

def quit():
    pygame.quit()
    quit()

