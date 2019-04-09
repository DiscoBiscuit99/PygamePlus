""" The PygamePlus graphics module """

import pygame

true  = True
false = False

class Graphics:
    def __init__(self, display):
        self.font = None

        self.display = display

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

        self.display.fill(self.color)

    def rectangle(self, filled, x, y, width, height):
        if   filled == "fill":
            pygame.draw.rect(self.display, self.color, pygame.Rect(x, y, width, height), 0)

        elif filled == "line":
            pygame.draw.rect(self.display, self.color, pygame.Rect(x, y, width, height), 1)
    
    def circle(self, filled, x, y, radius):
        if   filled == "fill":
            pygame.draw.circle(self.display, self.color, radius, 0)

        elif filled == "line":
            pygame.draw.circle(self.display, self.color, radius, 1)

    def line(self, x1, y1, x2, y2, width=1):
        start_pos = (x1, y1)
        end_pos   = (x2, y2)

        pygame.draw.line(self.display, self.color, start_pos, end_pos, width)

    def polygon(self, filled, pointlist):
        if filled == "fill":
            pygame.draw.polygon(self.display, self.color, pointlist, 0)
        elif filled == "line":
            pygame.draw.polygon(self.display, self.color, pointlist, 1)

    def setTitle(self, title):
        pygame.display.set_caption(title)

    def setWidth(self, width):
        _, prev_height = pygame.display.get_surface().get_size()

        self.display = pygame.display.set_mode((width, prev_height))

    def setHeight(self, height):
        prev_width, _ = pygame.display.get_surface().get_size()

        self.display = pygame.display.set_mode((prev_width, height))

    def setDimensions(self, width, height):
        self.display = pygame.display.set_mode((width, height))

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
        self.display.blit(image, (x, y))

    def newFont(self, font, size):
        self.font = pygame.font.Font(font, size)

    def print(self, text, x, y):
        if self.font is None:
            self.font = pygame.font.Font('freesansbold.ttf', 20)

        text_surf = self.font.render(text, true, self.color)
        text_rect = text_surf.get_rect()

        text_rect.topleft = (x, y)
        self.display.blit(text_surf, text_rect)

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
            
    #         self.display.blit(text_surf, text_rect)
    #         y += fontHeight + lineSpacing

    #         # remove the text we just blitted
    #         text = text[i:]

    #     return text

    def update(self):
        pygame.display.flip()
        pygame.display.update()

