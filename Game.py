"""
Game.py - defines the Game class
"""
import pygame
from pygame.locals import *

# SIDE_LEN_CM
BLACK = (0,0,0)
WHITE = (255,255,255)

LINE_THICKNESS = 2
OUTER_BOX = (10, 10, 700, 425)
INNER_CIRC = (360, 222)
CIRC_RAD = 106

# Beacon radius
BEACON_RAD = 10

# Robot radius
ROBOT_RAD = 5

class Game(pygame.sprite.Sprite):
  def __init__(self, beacons, robots, screen, dt=0.1, game_length=70):
    """
    Game constructor TBD
    """
    self.time = 0
    self.game_len = game_length # seconds
    self.dt = dt # seconds
    self.beacons = beacons
    self.robots = robots
    self.screen = screen

    pygame.sprite.Sprite.__init__(self)

    self.bkgd = pygame.Surface(screen.get_size())
    self.bkgd = self.bkgd.convert()
    self.screen.fill(WHITE)

    # draw the field
    pygame.draw.rect(self.screen, BLACK, OUTER_BOX, LINE_THICKNESS)
    pygame.draw.circle(self.screen, BLACK, INNER_CIRC, CIRC_RAD, LINE_THICKNESS)

    # draw the beacons
    for beacon in self.beacons:
        pygame.draw.circle(self.screen, beacon.get_color(), beacon.pos, BEACON_RAD)

    for robot in self.robots:
        pygame.draw.circle(self.screen, robot.get_color(), robot.pos, ROBOT_RAD)

  def is_over(self):
    """
    Returns whether game is over or not.
    """
    print("Game time - ", self.time)
    return self.time >= self.game_len

  def update(self):
    """
    Update the graphics to reflect the new game state using Pygame functionality.
    """
    self.screen.fill(WHITE)

    # draw the field
    pygame.draw.rect(self.screen, BLACK, OUTER_BOX, LINE_THICKNESS)
    pygame.draw.circle(self.screen, BLACK, INNER_CIRC, CIRC_RAD, LINE_THICKNESS)

    # update robots and draw them
    for robot in self.robots:
        robot.step(self.dt)
        # robot.update()
        pygame.draw.circle(self.screen, robot.get_color(), robot.pos, ROBOT_RAD)

    # update and draw the beacons
    for beacon in self.beacons:
        pygame.draw.circle(self.screen, beacon.get_color(), beacon.pos, BEACON_RAD)

    self.time += self.dt

    

