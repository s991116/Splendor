from game.Action import Action
from game.ActionType import ActionType
from game.GameBoard import GameBoard
from game.GemType import GemType
from typing import Dict
  
class TakeGemActions(Action):
  def __init__(self, gemsTaken: Dict[GemType, int]) -> None:
    self.gemsTaken = gemsTaken
  
  def execute(self, gameBoard: GameBoard) -> GameBoard:
    for (gemType, take) in self.gemsTaken.items():
      stack = gameBoard.gemPiles[gemType]
      left = stack - take
      assert left > 0, 'To many gems taken'
      gameBoard.gemPiles[gemType] = left
      player = gameBoard.players[gameBoard.currentPlayerIndex]
      player.gemStack[gemType] += 1
    
    return gameBoard
  
  def getType(self) -> ActionType:
    return ActionType.TAKEGEM 