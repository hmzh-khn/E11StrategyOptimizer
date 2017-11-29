"""
Game.py - defines the Game class
"""
import pygame
from pygame.locals import *

# SIDE_LEN_CM
BLACK = (0,0,0)
WHITE = (255,255,255)

LINE_THICKNESS = 2
OUTER_BOX = (10, 10, 600, 400)
INNER_BOX = (210, 110, 200, 200)

# inner octogon
ORTHOGON_SIDE = 50 # half of side length
START_X = 210
START_Y = 160
INNER_BOX_LIST = [
    (START_X                  , START_Y),
    (START_X                  , START_Y + 2*ORTHOGON_SIDE),
    (START_X +   ORTHOGON_SIDE, START_Y + 3*ORTHOGON_SIDE),
    (START_X + 3*ORTHOGON_SIDE, START_Y + 3*ORTHOGON_SIDE),
    (START_X + 4*ORTHOGON_SIDE, START_Y + 2*ORTHOGON_SIDE),
    (START_X + 4*ORTHOGON_SIDE, START_Y),
    (START_X + 3*ORTHOGON_SIDE, START_Y - ORTHOGON_SIDE),
    (START_X +   ORTHOGON_SIDE, START_Y - ORTHOGON_SIDE)]

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
    pygame.draw.lines(self.screen, BLACK, True, INNER_BOX_LIST, LINE_THICKNESS)

    # draw the beacons
    for beacon in self.beacons:
        pygame.draw.circle(self.screen, beacon.get_color(), beacon.pos, BEACON_RAD)

    for robot in self.robots:
        pygame.draw.circle(self.screen, robot.get_color(), robot.pos, ROBOT_RAD)

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
    self.screen.fill(WHITE)

    # draw the field
    pygame.draw.rect(self.screen, BLACK, OUTER_BOX, LINE_THICKNESS)
    pygame.draw.lines(self.screen, BLACK, True, INNER_BOX_LIST, LINE_THICKNESS)

    # update robots and draw them
    for robot in self.robots:
        robot.step(1)
        # robot.update()
        pygame.draw.circle(self.screen, robot.get_color(), robot.pos, ROBOT_RAD)

    # update and draw the beacons
    for beacon in self.beacons:
        # beacon.update()
        # print(beacon.pos)
        # beacon.update()
        pygame.draw.circle(self.screen, beacon.get_color(), beacon.pos, BEACON_RAD)


    

