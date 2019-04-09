""" The PygamePlus physics module """ 

import pygame

true  = True
false = False

class World:
    def __init__(self, xg, yg):
        self.xg = xg
        self.yg = yg

        self.bodies   = []
        self.shapes   = []
        self.fixtures = []

class Body:
    def __init__(self, world, x, y, state):
        self.x = x
        self.y = y

        self.state = state


    def setX(self, x):
        self.x = x

    def setY(self, y):
        self.y = y

    def setPosition(self, x, y):
        self.x = x
        self.y = y

    def getX(self):
        return self.x

    def getY(self):
        return self.y

class RectangleShape:
    def __init__(self, width, height):
        self.width  = width
        self.height = height

    def getWidth(self):
        return self.width

    def getHeight(self):
        return self.height

class CircleShape:
    def __init__(self, radius):
        self.radius = radius

class Fixture:
    def __init__(self, body, shape):
        self.body  = body
        self.shape = shape


# The physics class.
class Physics:
    def __init__(self):
        None

    def newWorld(self, xg, yg):
        self.world = World(xg, yg)

        return self.world

    def newBody(self, world, x, y, state):
        self.body = Body(world, x, y, state)

        return self.body

    def newRectangleShape(self, width, height):
        self.shape = RectangleShape(width, height)

        return self.shape

    def newCircleShape(self, radius):
        self.shape = CircleShape(radius)

        return self.shape

    def newFixture(self, body, shape):
        self.fixture = Fixture(body, shape)

        return self.fixture

