import pygame
import pygameplus

pgp = pygameplus

true  = True
false = False

running = true

world = pgp.physics.newWorld(0, 0)

body    = pgp.physics.newBody(world, 10, 10, "dynamic")
shape   = pgp.physics.newRectangleShape(20, 20)
fixture = pgp.physics.newFixture(body, shape)

pygame.init()

clock = pygame.time.Clock()

display_width  = 800
display_height = 600
display = pygame.display.set_mode((display_width, display_height))

pygame.display.set_caption("PygamePlus development")

while running:
    if pgp.keyboard.keyPressed("escape"):
        pgp.running = true
        pgp.event.quit()

    if pgp.keyboard.isDown("d"):
        body.setX(body.getX() + 2)
    elif pgp.keyboard.isDown("a"):
        body.setX(body.getX() - 2)

    if pgp.keyboard.isDown("s"):
        body.setY(body.getY() + 2)
    elif pgp.keyboard.isDown("w"):
        body.setY(body.getY() - 2)

    display.fill((0, 0, 0))

    pgp.graphics.rectangle("fill", display, body.getX(), body.getY(), shape.getWidth(), shape.getHeight())

    pygame.display.flip()
    pygame.display.update()
    clock.tick(60)


