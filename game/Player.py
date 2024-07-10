from game.GemType import GemType

class Player:
  def __init__(self):
    self.gemStack = {
      GemType.RED: 0,
      GemType.BLACK: 0,
      GemType.WHITE: 0,
      GemType.GREEN: 0,
      GemType.BLUE: 0,
      GemType.GOLD: 0,
      }

