import pygame

# The two constants that won't be named in all-caps, since
# it's annoying to have to first-cap the boolean values.
true  = True
false = False

# Globals.
global display


# COLLECTIVE TIME CLASS
class Time:
    def __init__(self):
        self.clock = pygame.time.Clock()

        self.FPS = 60

    def update(self):
        self.clock.tick(self.FPS)

    def setFPS(self, FPS):
        self.FPS = FPS

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


# COLLECTIVE PHYSICS CLASS
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


# COLLECTIVE GRAPHICS CLASS
class Graphics:
    def __init__(self):
        global display

        self.font = None

        self.color = [ 255, 255, 255 ]

    def setColor(self, r, g, b):
        self.r = r
        self.g = g
        self.b = b

        self.color = ( self.r, self.g, self.b )

    def getColor(self):
        return self.color

    def setBackgroundColor(self, r, g, b):
        self.r = r
        self.g = g
        self.b = b

        self.color = ( self.r, self.g, self.b )

        display.fill(self.color)

    def rectangle(self, filled, x, y, width, height):
        if   filled == "fill":
            pygame.draw.rect(display, self.color, pygame.Rect(x, y, width, height), 0)

        elif filled == "line":
            pygame.draw.rect(display, self.color, pygame.Rect(x, y, width, height), 1)
    
    def circle(self, filled, display, x, y, radius):
        if   filled == "fill":
            pygame.draw.circle(display, self.color, radius, 0)

        elif filled == "line":
            pygame.draw.circle(display, self.color, radius, 1)

    def line(self, x1, y1, x2, y2, width=1):
        start_pos = (x1, y1)
        end_pos   = (x2, y2)

        pygame.draw.line(display, self.color, start_pos, end_pos, width)

    def polygon(self, filled, pointlist):
        if filled == "fill":
            pygame.draw.polygon(display, self.color, pointlist, 0)
        elif filled == "line":
            pygame.draw.polygon(display, self.color, pointlist, 1)

    def setTitle(self, title):
        pygame.display.set_caption(title)

    def setWidth(self, width):
        _, prev_height = pygame.display.get_surface().get_size()

        display = pygame.display.set_mode((width, prev_height))

    def setHeight(self, height):
        prev_width, _ = pygame.display.get_surface().get_size()

        display = pygame.display.set_mode((prev_width, height))

    def setDimensions(self, width, height):
        display = pygame.display.set_mode((width, height))

    def getWidth(self):
        width, _ = pygame.display.get_surface().get_size()

        return width

    def getHeight(self):
        _, height = pygame.display.get_surface().get_size()

        return height

    def getDimensions(self):
        return pygame.display.get_surface().get_size()

    def newImage(self, filename):
        return pygame.image.load(filename)

    def draw(self, image, x, y):
        display.blit(image, (x, y))

    def newFont(self, font, size):
        self.font = pygame.font.Font(font, size)

    def print(self, text, x, y):
        if self.font is None:
            self.font = pygame.font.Font('freesansbold.ttf', 20)

        text_surf = self.font.render(text, true, self.color)
        text_rect = text_surf.get_rect()

        text_rect.topleft = (x, y)
        display.blit(text_surf, text_rect)

    # def printf(self, text, x, y, align):
    #     self.font  = pygame.font.Font('freesansbold.ttf', 20)

    #     lineSpacing = -2

    #     # get the height of the font
    #     fontHeight = self.font.size("Tg")[1]

    #     while text:
    #         i = 1

    #         # determine if the row of text will be outside our area
    #         if y + fontHeight > rect.bottom:
    #             break

    #         # determine maximum width of line
    #         while self.font.size(text[:i])[0] < rect.width and i < len(text):
    #             i += 1

    #         # if we've wrapped the text, then adjust the wrap to the last word      
    #         if i < len(text): 
    #             i = text.rfind(" ", 0, i) + 1

    #         # render the line and blit it to the surface
    #         text_surf = self.font.render(text[:i], true, self.color)

    #         text_rect = text_surf.get_rect()

    #         if align == "left":
    #             text_rect.topleft = (x, y)
    #         elif align == "right":
    #             text_rect.topright = (x, y)
    #         elif align == "center":
    #             text_rect.center = (x, y)
            
    #         display.blit(text_surf, text_rect)
    #         y += fontHeight + lineSpacing

    #         # remove the text we just blitted
    #         text = text[i:]

    #     return text

    def update(self):
        pygame.display.flip()
        pygame.display.update()


# COLLECTIVE KEYBOARD CLASS
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

    def keyHeld(self, key):
        self.pressed = pygame.key.get_pressed()
        if self.pressed[self.keys[key]]:
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

    def keyReleased(self, key):
        for event in pygame.event.get():
            if event.type == pygame.KEYUP:
                if event.key == self.keys[key]:
                    return true
                else:
                    return false

class Audio:
    def __init__(self):
        # The master volume.
        self.master_volume = 0.5

    def newBackgroundMusic(self, filename):
        return "music", pygame.mixer.music.load(filename)

    def newSound(self, filename):
        return "sound", pygame.mixer.Sound(filename)

    def play(self, audio, *args):
        pygame.mixer.music.set_volume(self.master_volume)

        if audio[0] == "music":
            pygame.mixer.music.play()
        elif audio[0] == "sound":
            audio[1].set_volume(self.master_volume)
            audio[1].play()

        for arg in args:
            if arg[0] == "music":
                pygame.mixer.music.play()
            elif arg[0] == "sound":
                arg[1].set_volume(self.master_volume)
                arg[1].play()

    def stop(self, audio, *args):
        if audio[0] == "music":
            pygame.mixer.music.stop()
        elif audio[0] == "sound":
            audio[1].stop()

        for arg in args:
            if arg[0] == "music":
                pygame.mixer.music.stop()
            elif arg[0] == "sound":
                arg[1].stop()

    # Sets the volume ranging from 0.0 to 1.0.
    def setVolume(self, volume):
        self.master_volume = master_volume

    def getVolume(self):
        return self.master_volume
        

# COLLECTIVE EVENT CLASS
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


# Module methods.
time     = Time()
physics  = Physics()
graphics = Graphics()
audio    = Audio()
keyboard = Keyboard()
event    = Event()

def init():
    global display

    pygame.init()

    display = pygame.display.set_mode((800, 600))

def update():
    time.update()
