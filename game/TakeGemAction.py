from game.Action import Action
from game.ActionType import ActionType
from game.GameBoard import GameBoard
  
class TakeGemAction(Action):
  def __init__(self, gemsTaken: list[int]) -> None:
    self.gemsTaken = gemsTaken
  
  def execute(self, gameBoard: GameBoard) -> GameBoard:
    for gemType in self.gemsTaken:
      stack = gameBoard.gemPiles[gemType]
      left = stack - 1
      assert left > 0, 'To many gems taken'
      gameBoard.gemPiles[gemType] = left
      player = gameBoard.players[gameBoard.currentPlayerIndex]
      player.gemStack[gemType] += 1
    
    return gameBoard
  
  def getType(self) -> ActionType:
    return ActionType.TAKEGEM 