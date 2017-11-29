"""
Robot.py - defines the Robot classes
"""
import pygame
from pygame.locals import *
from random import randint
from math import sqrt

GREEN = (0  ,100,  0)
WHITE = (255,255,255)

INITIAL_VELOCITY = 20 # pixels/time_unit
CAPTURE_RADIUS = 20

def vect(p0, p1):
    """
    Returns normalized vector from point p0 to p1
    """
    p0x, p0y = p0
    p1x, p1y = p1
    dist = sqrt((p0x - p1x)**2 + (p0y - p1y)**2)
    qx = (p0x - p1x)/dist
    qy = (p0y - p1y)/dist
    return (qx,qy)

class Robot(pygame.sprite.Sprite):
  def __init__(self, color, strategy, pos=(randint(10, 610), randint(10, 410)), velocity=INITIAL_VELOCITY):
    """
    Robot constructor defines team color and instance of strategy class
    NOTE: set velocity to actual value
    """
    self.color = color
    self.strategy = strategy
    self.pos = pos
    self.currentDest = strategy.get_beacon()
    self.vector = vect(self.pos, self.currentDest.pos)
    self.velocity = velocity

    pygame.sprite.Sprite.__init__(self)

  def step(self, dt):
    """
    Executes one step of the robot's strategy and updates game state.
    """


    # move in the current direction
    vx, vy = self.vector
    px, py = self.pos
    self.pos = (round(px - INITIAL_VELOCITY*vx*dt), round(py - INITIAL_VELOCITY*vy*dt))

    has_captured = self.capture(self.currentDest)
    # if has_captured:

    

  # def update(self):
  #   """
  #   Update the graphics to reflect the new robot state using Pygame functionality.
  #   """
    
  #   pass

  # return RGB value of current robot get_color
  def get_color(self):
    if self.color == 'green':
      return GREEN
    elif self.color == 'white':
      return WHITE
    else: 
      return None

  def capture(self, beacon):
    """
    Checks whether the robot can capture a beacon, and then does if possible.
    """
    p0x, p0y = self.pos
    p1x, p1y = self.currentDest.pos
    dist = sqrt((p0x - p1x)**2 + (p0y - p1y)**2)

    if dist <= CAPTURE_RADIUS:
        self.currentDest.switch(self.color)
        self.currentDest = self.strategy.next_beacon()
        self.vector = vect(self.pos, self.currentDest.pos)
        return True

    else:
        return False





