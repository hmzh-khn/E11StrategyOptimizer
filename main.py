"""
main.py - file for running the simulation
"""
import pygame
from pygame.locals import *
from Game import Game
from Beacon import Beacon
from Robot import Robot
from ExecutionStrategy import ExecutionStrategy

GREEN  = (0  ,100,  0)
YELLOW = (255,255,  0)
WHITE  = (255,255,255)

DT_MS = 50

GAME_LENGTH = 70

ONE_PT  = 1
TWO_PTS = 2

if __name__ == '__main__':
  pygame.init()

  # display, background size
  screen = pygame.display.set_mode((720, 445))

  # outer
  beacon1 = Beacon(( 10, 10), score=ONE_PT)  # top-left
  beacon2 = Beacon((710, 10), score=ONE_PT)  # top-right
  beacon3 = Beacon(( 10,435), score=TWO_PTS) # bottom-left
  beacon4 = Beacon((710,435), score=TWO_PTS) # bottom-right
  beacon9 = Beacon((360,435), score=ONE_PT)  # bottom-middle

  # inner
  beacon5 = Beacon((278,140), score=ONE_PT)  # top-left
  beacon6 = Beacon((442,140), score=TWO_PTS) # top-right
  beacon7 = Beacon((278,304), score=TWO_PTS) # bottom-left
  beacon8 = Beacon((442,304), score=ONE_PT)  # bottom-right

  # create beacons
  beacons = [
    beacon1,
    beacon3,
    beacon9,
    beacon2,
    beacon4,
    # inner
    beacon5,
    beacon7,
    beacon8,
    beacon6,]

  # transition beacons
  t_beacons = [
    # inner-only
    Beacon((220,220), waypoint=True), # top-left    <-> bottom-left
    Beacon((360,360), waypoint=True), # bottom-left <-> bottom-right
    Beacon((500,220), waypoint=True), # top-right   <-> bottom-right
    Beacon((360, 80), waypoint=True), # top-left    <-> top-right
  ]

  # tl bl br tr
  INNER_STRAT = [
    beacons[7],
    t_beacons[2],
    beacons[8],
    t_beacons[3],
    beacons[5],
    t_beacons[0],
    beacons[6],
    t_beacons[1],]

  OUR_STRAT = [
    beacon1,
    beacon5,
    t_beacons[3],
    beacon6,
    beacon2,
    beacon4,
    beacon8,
    beacon9,
    beacon7,
    beacon3]
  OUR_STRAT = OUR_STRAT[::-1]

  # creates strategies
  strat1 = ExecutionStrategy(INNER_STRAT)
  strat2 = ExecutionStrategy(OUR_STRAT)

  # creates robots
  robot1 = Robot('yellow', strat1, (670,220))
  robot2 = Robot('green', strat2, (40,220))

  # only one Game object allowed
  game = Game(beacons, [robot1, robot2], screen, dt=DT_MS/1000, game_length=GAME_LENGTH)

  while not game.is_over():
        pygame.time.wait(DT_MS)
        game.update()
        pygame.display.flip()
        pygame.display.update()

  # calculate scores
  g_team = 0
  y_team = 0
  for beacon in game.beacons:
    if beacon.color == 'yellow':
      y_team += beacon.score
    elif beacon.color == 'green':
      g_team += beacon.score

  print("Final score (green - white): ", g_team, y_team)
