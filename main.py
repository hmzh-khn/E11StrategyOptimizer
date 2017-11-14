"""
main.py - file for running the simulation
"""
import pygame
from pygame.locals import *
from Game import Game
from Beacon import Beacon
from Robot import Robot
from ExecutionStrategy import ExecutionStrategy



def nameTBD():
  """
  LP Functionality that generates an ExecutionStrategy.
  """
  # John
  pass



if __name__ == '__main__':

  # complete visualization - Hamzah
  pygame.init()
  screen = pygame.display.set_mode((600, 400))

  background = pygame.Surface(screen.get_size())
  background = background.convert()
  background.fill((250, 250, 250))  

  while 1:
    pygame.draw.rect(screen, (20, 150, 250), (10,40, 100, 200), 10)
    pygame.time.wait(1000)
    pygame.display.flip()
    pygame.display.update()
