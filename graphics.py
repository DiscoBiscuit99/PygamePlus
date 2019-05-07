""" The PygamePlus graphics module """

import os
import pygame

x = 350
y = 80

os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (x,y)

true  = True
false = False

global display

font = None

bgcolor = [ 0, 0, 0 ]
color   = [ 255, 255, 255 ]

def newSurface(width, height):
    surface = pygame.newSurface((width, height))
    return surface

def window(width, height):
    global display
    display = pygame.display.set_mode((width, height))

def getWindow():
    global display
    return display

def setColor(r, g, b):
    global color 
    color = [r, g, b]

def getColor():
    global color
    return color

def setBackgroundColor(r, g, b):
    global bgcolor
    global display

    bgcolor = [r, g, b]

    display.fill(bgcolor)

def rectangle(filled, x, y, width, height):
    global display
    global color

    if filled == "fill":
        pygame.draw.rect(display, color, pygame.Rect(x, y, width, height), 0)

    elif filled == "line":
        pygame.draw.rect(display, color, pygame.Rect(x, y, width, height), 1)

def circle(filled, x, y, radius):
    global display
    global color

    if filled == "fill":
        pygame.draw.circle(display, color, radius, 0)

    elif filled == "line":
        pygame.draw.circle(display, color, radius, 1)

def line(x1, y1, x2, y2, width=1):
    global display
    global color

    start_pos = (x1, y1)
    end_pos   = (x2, y2)

    pygame.draw.line(display, color, start_pos, end_pos, width)

def polygon(filled, pointlist):
    global display
    global color

    if filled == "fill":
        pygame.draw.polygon(display, color, pointlist, 0)
    elif filled == "line":
        pygame.draw.polygon(display, color, pointlist, 1)

def setTitle(title):
    pygame.display.set_caption(title)

def setWidth(width):
    _, prev_height = pygame.display.get_surface().get_size()

    display = pygame.display.set_mode((width, prev_height))

def setHeight(height):
    prev_width, _ = pygame.display.get_surface().get_size()

    display = pygame.display.set_mode((prev_width, height))

def setDimensions(width, height):
    display = pygame.display.set_mode((width, height))

def getWidth():
    width, _ = pygame.display.get_surface().get_size()

    return width

def getHeight():
    _, height = pygame.display.get_surface().get_size()

    return height

def getDimensions():
    return pygame.display.get_surface().get_size()

def newImage(filename):
    return pygame.image.load(filename)

def draw(image, x, y):
    global display

    display.blit(image, (x, y))

def newFont(fontfile, size):
    global font

    font = pygame.font.Font(fontfile, size)

def print(text, x, y):
    global font
    global display

    if font is None:
        font = pygame.font.Font('freesansbold.ttf', 20)

    text_surf = font.render(text, true, color)
    text_rect = text_surf.get_rect()

    text_rect.topleft = (x, y)
    display.blit(text_surf, text_rect)

# def printf( text, x, y, align):
    # font  = pygame.font.Font('freesansbold.ttf', 20)

    # lineSpacing = -2

    # # get the height of the font
    # fontHeight = font.size("Tg")[1]

    # while text:
        # i = 1

        # # determine if the row of text will be outside our area
        # if y + fontHeight > rect.bottom:
            # break

        # # determine maximum width of line
        # while font.size(text[:i])[0] < rect.width and i < len(text):
            # i += 1

        # # if we've wrapped the text, then adjust the wrap to the last word      
        # if i < len(text): 
            # i = text.rfind(" ", 0, i) + 1

        # # render the line and blit it to the surface
        # text_surf = font.render(text[:i], true, color)

        # text_rect = text_surf.get_rect()

        # if align == "left":
            # text_rect.topleft = (x, y)
        # elif align == "right":
            # text_rect.topright = (x, y)
        # elif align == "center":
            # text_rect.center = (x, y)
        
        # display.blit(text_surf, text_rect)
        # y += fontHeight + lineSpacing

        # # remove the text we just blitted
        # text = text[i:]

    # return text

def update():
    pygame.display.flip()
    pygame.display.update()

