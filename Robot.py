"""
Robot.py - defines the Robot classes
"""

INITIAL_VELOCITY = 3

class Robot:
  def __init__(self, color, strategy, pos, currentDest, velocity=INITIAL_VELOCITY):
    """
    Robot constructor defines team color and instance of strategy class
    NOTE: set velocity to actual value
    """
    self.color = color
    self.strategy = strategy
    self.pos = pos
    self.currentDest = currentDest
    self.velocity = velocity

  def step(self, dt):
    """
    Executes one step of the robot's strategy and updates game state.
    """
    # Skipper
    pass

  def update(self):
    """
    Update the graphics to reflect the new robot state using Pygame functionality.
    """
    # Hamzah
    pass

  def capture(self, beacon):
    """
    Checks whether the robot can capture a beacon, and then does if possible.
    """
    # Skipper
    pass




