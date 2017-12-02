"""
Beacon.py - defines the Beacon class
"""
import pygame
from pygame.locals import *

GREEN  = (0  ,100,  0)
TAN = (210,180,140)
WHITE  = (255,255,255)
YELLOW  = (255,255,0)

class Beacon(pygame.sprite.Sprite):
  def __init__(self, pos, score=0, waypoint=False, color=None):
    """
    Game constructor TBD
    """
    self.pos = pos # (x,y) in pixels
    self.color = color # yellow or green
    self.isWaypoint = waypoint
    self.score = score

    pygame.sprite.Sprite.__init__(self)

  def switch(self, new_color):
    """
    Switches the beacon to a new color.
    Returns whether beacon was captured from enemy.
    """
    is_new_capture = self.color != new_color
    self.color = new_color
    return is_new_capture

  def get_pos(self):
    return self.pos

  # return RGB value of current beacon get_color
  def get_color(self):
    if self.color == 'green':
      return GREEN
    elif self.color == 'yellow':
      return YELLOW
    elif self.isWaypoint:
      return WHITE
    else: 
      return TAN
