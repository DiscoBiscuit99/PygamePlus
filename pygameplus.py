import pygame

# The two constants that won't be named in all-caps, since
# it's annoying to have to first-cap the boolean values.
true  = True
false = False

# Physics component classes.
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


# COLLECTIVE PHYSICS CLASS.
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


# Graphics component classes.
# TODO

# COLLECTIVE GRAPHICS CLASS.
class Graphics:
    def __init__(self):
        self.color = [ 255, 255, 255 ]

    def setColor(self, r, g, b):
        self.r = r
        self.g = g
        self.b = b

        self.color = [ self.r, self.g, self.b ]

    def getColor(self):
        return self.color

    def rectangle(self, filled, display, x, y, width, height):
        if   filled == "fill":
            pygame.draw.rect(display, self.color, pygame.Rect(x, y, width, height), 0)

        elif filled == "line":
            pygame.draw.rect(display, self.color, pygame.Rect(x, y, width, height), 2)
    
    def circle(self, filled, display, x, y, radius):
        if   filled == "fill":
            pygame.draw.circle(display, self.color, radius, 0)

        elif filled == "line":
            pygame.draw.circle(display, self.color, radius, 2)


class Keyboard:
    def __init__(self):
        self.keys = {
                "backspace": pygame.K_BACKSPACE, "tab": pygame.K_TAB, "return": pygame.K_RETURN,
                "escape": pygame.K_ESCAPE, "space": pygame.K_SPACE, "!": pygame.K_EXCLAIM, "#": pygame.K_HASH, 
                "$": pygame.K_DOLLAR, "&": pygame.K_AMPERSAND, "(": pygame.K_LEFTPAREN, ")": pygame.K_RIGHTPAREN
        }

    def isDown(self, key):
        pressed = pygame.key.get_pressed()
        # if pressed[self.keys[key]] == :
            # yield true
            # print("PRESSED")

        # else: return false

# COLLECTIVE EVENT CLASS
class Event:
    def __init__(self):
        None

def update():
    None


# Pener methods.
physics  = Physics()
graphics = Graphics()
keyboard = Keyboard()

# GAME LOOP.
while running:
    for event in pygame.event.get():
        None

    update()

