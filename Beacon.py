"""
Beacon.py - defines the Beacon class
"""
import pygame
from pygame.locals import *

class Beacon:
  def __init__(self, pos, color):
    """
    Game constructor TBD
    """
    self.pos = pos # (x,y) in pixels
    self.color = color # white or green

  def switch(self, new_color):
    """
    Switches the beacon to a new color.
    Returns whether beacon was captured from enemy.
    """
    is_new_capture = self.color != new_color
    self.color = new_color
    return is_new_capture

  def get_pos():
    return self.pos

  def update(self):
    # Hamzah
    """
    Update the graphics to reflect the current team owner.
    """
    pass
