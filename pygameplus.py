""" The PygamePlus module """

import pygame

from audio import Audio
from event import Event
from graphics import Graphics
from keyboard import Keyboard
from physics import Physics

# The two constants that won't be named in all-caps, since
# it's annoying to have to first-cap the boolean values.
true  = True
false = False

display = pygame.display.set_mode((800, 600))

# Time module
class Time:
    def __init__(self):
        self.clock = pygame.time.Clock()

        self.FPS = 60

    def update(self):
        self.clock.tick(self.FPS)

    def setFPS(self, FPS):
        self.FPS = FPS

# Module objects
audio    = Audio()
event    = Event()
graphics = Graphics(display)
keyboard = Keyboard()
physics  = Physics()
time     = Time()

def init():
    global display

    pygame.init()

def update():
    time.update()

