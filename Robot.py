"""
Robot.py - defines the Robot classes
"""

class Robot:
  def __init__(self, color, strategy, velocity=3):
    """
    Robot constructor defines team color and instance of strategy class
    NOTE: set velocity to actual value
    """
    self.team = color
    self.position = (0,0)
    seld.strategy = strategy
    pass

  def step(self, dt):
    """
    Plays one step of the robot's strategy
    """
    pass



