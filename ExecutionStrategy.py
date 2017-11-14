"""
ExecutionStrategy.py - defines execution strategies for the game
"""
class ExecutionStrategy:
  def __init__(self, beacons):
    """
    ExecutionStrategy constructor defines list of beacons to visit.
    """
    self.beacons = beacons
    self.currentBeaconIndex = 0

  def next_beacon(self, dt, prev_pos):
    """
    Returns the next beacon in the strategy and updates internal state.
    """
    self.currentBeaconIndex = (self.currentBeaconIndex + 1) % len(self.beacons)
    return self.beacons[self.currentBeaconIndex]