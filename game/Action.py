from game.GameBoard import GameBoard
from game.ActionType import ActionType

class Action:
  
  def execute(self, gameBoard: GameBoard) -> GameBoard:
    return gameBoard
  
  def getType(self) -> ActionType:
    return ActionType.TAKEGEM