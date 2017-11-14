"""
Game.py - defines the Game class
"""
import pygame
from pygame.locals import *

class Game:
  def __init__(self, beacons, robots, dt=0.1, game_length=70):
    """
    Game constructor TBD
    """
    self.time = 0
    self.game_len = game_length # seconds
    self.dt = dt # seconds
    self.beacons = beacons
    self.robots = robots

  def step(self):
    """
    Plays one step of the game and updates game state.
    """
    # Skipper
    pass

  def update(self):
    """
    Update the graphics to reflect the new game state using Pygame functionality.
    """
    # Hamzah
    pass
