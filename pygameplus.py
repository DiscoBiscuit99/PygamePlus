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
                "$": pygame.K_DOLLAR, "&": pygame.K_AMPERSAND, "(": pygame.K_LEFTPAREN, ")": pygame.K_RIGHTPAREN,
                "*": pygame.K_ASTERISK, "+": pygame.K_PLUS, ",": pygame.K_COMMA, "-": pygame.K_MINUS, 
                ".": pygame.K_PERIOD, "/": pygame.K_SLASH, "0": pygame.K_0, "1": pygame.K_1, "2":pygame.K_2,
                "3": pygame.K_3, "4": pygame.K_4, "5": pygame.K_5, "6": pygame.K_6, "7": pygame.K_7, "8": pygame.K_8,
                "9": pygame.K_9, ":": pygame.K_COLON, ";": pygame.K_SEMICOLON, "<": pygame.K_LESS, "=": pygame.K_EQUALS,
                ">": pygame.K_GREATER, "?": pygame.K_QUESTION, "@": pygame.K_AT, "[": pygame.K_LEFTBRACKET,
                "]": pygame.K_RIGHTBRACKET, "\\": pygame.K_BACKSLASH, "^": pygame.K_CARET, "_": pygame.K_UNDERSCORE,
                "`": pygame.K_BACKQUOTE, "a": pygame.K_a, "b": pygame.K_b, "c": pygame.K_c, "d": pygame.K_d, 
                "e": pygame.K_e, "f": pygame.K_f, "g": pygame.K_g, "h": pygame.K_h, "i": pygame.K_i, "j": pygame.K_j, 
                "k": pygame.K_k, "l": pygame.K_l, "m": pygame.K_m, "n": pygame.K_n, "o": pygame.K_o, "p": pygame.K_p,
                "q": pygame.K_q, "r": pygame.K_r, "s": pygame.K_s, "t": pygame.K_t, "u": pygame.K_u, "v": pygame.K_v,
                "w": pygame.K_w, "x": pygame.K_x, "y": pygame.K_y, "z": pygame.K_z, "delete": pygame.K_DELETE, 
                "up": pygame.K_UP, "down": pygame.K_DOWN, "left": pygame.K_LEFT, "right": pygame.K_RIGHT, "insert": pygame.K_INSERT,
                "home": pygame.K_HOME, "end": pygame.K_END, "pageup": pygame.K_PAGEUP, "pagedown": pygame.K_PAGEDOWN, 
                "f1": pygame.K_F1, "f2": pygame.K_F2, "f3": pygame.K_F3, "f4": pygame.K_F4, "f5": pygame.K_F5,
                "f6": pygame.K_F6, "f7": pygame.K_F7, "f8": pygame.K_F8, "f9": pygame.K_F9, "f10": pygame.K_F10, 
                "f11": pygame.K_F11, "f12": pygame.K_F12,"f13": pygame.K_F13,"f14": pygame.K_F14,"f15": pygame.K_F15,
                "rshift": pygame.K_RSHIFT, "lshift": pygame.K_LSHIFT, "rctrl": pygame.K_RCTRL, "lctrl": pygame.K_LCTRL,
                "ralt": pygame.K_RALT, "lalt": pygame.K_LALT, "rmeta": pygame.K_RMETA, "lmeta": pygame.K_LMETA,
                "rsuper": pygame.K_RSUPER, "lsuper": pygame.K_LSUPER
        }

    def isDown(self, key):
        pressed = pygame.key.get_pressed()
        if pressed[self.keys[key]]:
            return true
        else:
            return false

    def keyPressed(self, key):
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == self.keys[key]:
                    return true
                else:
                    return false

# COLLECTIVE EVENT CLASS
class Event:
    def __init__(self):
        None

    def quit(self):
        pygame.quit()
        quit()

def update():
    None

# Module methods.
physics  = Physics()
graphics = Graphics()
keyboard = Keyboard()
event    = Event()

# GAME LOOP
# while running:
    # update()

