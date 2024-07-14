from game.GameBoard import GameBoard
from game.ActionType import ActionType

class Action:
  
  def execute(self, game: GameBoard) -> GameBoard:
    return game
  
  def getType(self) -> ActionType:
    return ActionType.TAKEGEM