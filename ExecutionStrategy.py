"""
ExecutionStrategy.py - defines execution strategies for the game
"""
class ExecutionStrategy:
  def __init__(self, beacons):
    """
    ExecutionStrategy constructor defines list of beacons to visit, 

    """
    self.beacons = beacons
    self.prev_beacon = None
    self.next_beacon = beacons[0]
    pass

  def nextPos(self, dt, prev_pos):
    """
    Returns the next position following the strategy's path.
    """
    pass