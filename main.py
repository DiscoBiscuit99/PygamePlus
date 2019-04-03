import pygame
import pygameplus

# Shorten the module name.
pgp = pygameplus

# Set better boolean identifiers.
true  = True
false = False


# Globals.
global running
global sound

world = pgp.physics.newWorld(0, 0)

body    = pgp.physics.newBody(world, 10, 10, "dynamic")
shape   = pgp.physics.newRectangleShape(20, 20)
fixture = pgp.physics.newFixture(body, shape)

def load():
    pgp.init()

    global running
    global sound

    running = true

    pgp.graphics.setTitle("PygamePlus development")

    # pgp.audio.setVolume(0.1)

    music = pgp.audio.newBackgroundMusic("Dragon Ball GT - OP Japanese HQ.mp3")
    sound = pgp.audio.newSound("sound.wav")

    pgp.audio.play(music)


def update():
    global running
    global sound
        
    pgp.audio.play(sound)

    # if the close button is pressed.
    if pgp.event.shouldQuit():
        running = false

    if pgp.keyboard.keyHeld("escape"):
        running = false
        pgp.event.quit()

    if pgp.keyboard.keyHeld("d"):
        body.setX(body.getX() + 2)
    elif pgp.keyboard.keyHeld("a"):
        body.setX(body.getX() - 2)

    if pgp.keyboard.keyHeld("s"):
        body.setY(body.getY() + 2)
    elif pgp.keyboard.keyHeld("w"):
        body.setY(body.getY() - 2)

    pgp.update()

def draw():
    pgp.graphics.setBackgroundColor(0, 0, 0)

    pgp.graphics.setColor(255, 200, 100)
    pgp.graphics.rectangle("line", body.getX(), body.getY(), shape.getWidth(), shape.getHeight())

    pgp.graphics.setColor(255, 0, 0)
    pgp.graphics.line(90, 50, 40, 90)

    points = [[20, 20], [40, 40], [60, 20]]
    pgp.graphics.setColor(0, 255, 0)
    pgp.graphics.polygon("fill", points)

    image = pgp.graphics.newImage("HIM-pic.png")
    pgp.graphics.draw(image, 100, 100)

    # pgp.graphics.setDimensions(100, 100)

    # print(pgp.graphics.getDimensions())

    # if pgp.keyboard.keyPressed("b"):
        # pgp.graphics.setWidth(200)
        # pgp.graphics.setHeight(200)

    pgp.graphics.newFont("Dokdo-Regular.ttf", 20)

    pgp.graphics.print("TESTING THE PRINT", 300, 300)

    pgp.graphics.update()



# MAIN FUNCTIONS
load()

while running:            
    update()
    draw()
