""" The PygamePlus physics module """ 

# import box2d
import pygame

# Better boolean identifiers
true  = True
false = False

# The physics classes.
class World:
    def __init__(self, xg, yg):
        self.xg = xg
        self.yg = yg

        self.bodies   = []
        self.shapes   = []
        self.fixtures = []
    
    def getBodies(self):
        return self.bodies

    def getBodyCount(self):
        return len(self.bodies)

    def setGravity(self, xg, yg):
        self.xg = xg
        self.yg = yg

    def getGravity(self):
        return self.xg, self.yg

    def update(self, dt):
        self.dt = dt

        for body in self.bodies:
            body.update(self.xg, self.yg, self.dt)

class Body:
    def __init__(self, world, x, y, state):
        self.dt = 0

        self.x = x
        self.y = y

        self.xvel = 0
        self.yvel = 0

        self.mass = 1
        self.linear_damping = 0

        self.state = state

    def setX(self, x):
        self.x = x

    def setY(self, y):
        self.y = y

    def setPosition(self, x, y):
        self.x = x
        self.y = y

    def setMass(self, mass):
        self.mass = mass    

    def setLinearVelocity(self, xvel, yvel):
        self.xvel = xvel
        self.yvel = yvel

    def setLinearDamping(self, ld):
        self.linear_damping = ld

    def getX(self):
        return self.x

    def getY(self):
        return self.y

    def getPosition(self):
        return self.x, self.y

    def getMass(self):
        return self.mass

    def getLinearVelocity(self):
        return self.xvel, self.yvel

    def getLinearDamping(self):
        return self.linear_damping

    def applyForce(self, xf, yf):
        self.xvel += xf * self.dt
        self.yvel += yf * self.dt

    def update(self, xg, yg, dt):
        self.dt = dt

        if self.state == "dynamic":
            
            self.x += self.xvel * dt
            self.y += self.yvel * dt

            self.xvel += (self.mass * xg) * dt
            self.yvel += (self.mass * yg) * dt

            # Needs some work
            if self.xvel > 0:
                self.xvel -= self.linear_damping
            elif self.xvel < 0:
                self.xvel += self.linear_damping
            if self.yvel > 0:
                self.yvel -= self.linear_damping
            elif self.yvel < 0:
                self.yvel += self.linear_damping

class RectangleShape:
    def __init__(self, width, height):
        self.width  = width
        self.height = height

    def getWidth(self):
        return self.width

    def getHeight(self):
        return self.height

    def getDimensions(self):
        return self.width, self.height

class CircleShape:
    def __init__(self, radius):
        self.radius = radius

class Fixture:
    def __init__(self, body, shape):
        self.body  = body
        self.shape = shape


# The physics functions.
def newWorld(xg, yg):
    world = World(xg, yg)

    return world

def newBody(world, x, y, state):
    body = Body(world, x, y, state)
    
    world.bodies.append(body)

    return body

def newRectangleShape(width, height):
    shape = RectangleShape(width, height)

    return shape

def newCircleShape(radius):
    shape = CircleShape(radius)

    return shape

def newFixture(body, shape):
    fixture = Fixture(body, shape)

    return fixture

