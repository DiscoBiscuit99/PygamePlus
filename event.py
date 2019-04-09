""" The PygamePlus event module """ 

import pygame

true  = True
false = False

class Event:
    def __init__(self):
        pass

    def shouldQuit(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return true
            else:
                return false

    def quit(self):
        pygame.quit()
        quit()

