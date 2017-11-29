"""
main.py - file for running the simulation
"""
import pygame
from pygame.locals import *
from Game import Game
from Beacon import Beacon
from Robot import Robot
from ExecutionStrategy import ExecutionStrategy

GREEN = (0  ,100,  0)
WHITE = (255,255,255)

def nameTBD():
  """
  LP Functionality that generates an ExecutionStrategy.
  """
  # John
  pass



if __name__ == '__main__':

  # complete visualization - Hamzah
  pygame.init()

  # display, background size
  screen = pygame.display.set_mode((620, 420))


  # create beacons
  beacon = Beacon((100,100))
  beacon1 = Beacon((300,300))

  # creates strategies
  strat1 = ExecutionStrategy([beacon, beacon1])

  # creates robots
  robot = Robot('green', strat1)

  # only one Game object allowed
  game = Game([beacon, beacon1], [robot], screen, dt=0.1, game_length=70)

  while 1:
        pygame.time.wait(1000)
        game.update()
        pygame.display.flip()
        pygame.display.update()
