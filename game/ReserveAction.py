from game.Action import Action
from game.ActionType import ActionType
from game.GameBoard import GameBoard

class ReserveAction(Action):
  
  def execute(self, game: GameBoard) -> GameBoard:
    return game
  
  def getType(self) -> ActionType:
    return ActionType.TAKEGEM