from game.Action import Action
from game.ActionType import ActionType
from game.GameBoard import GameBoard
  
class TakeGemAction(Action):
  def __init__(self, nettoGemsTaken: tuple[int,int,int,int,int]):
    self.nettoGemsTaken = nettoGemsTaken
  
  def execute(self, gameBoard: GameBoard) -> GameBoard:
    for gemType in range(5):
      gameBoard.gemPiles[gemType] -= self.nettoGemsTaken[gemType]
      gameBoard.players[gameBoard.currentPlayerIndex].gemPiles[gemType] += self.nettoGemsTaken[gemType]

    return gameBoard
  
  def getType(self) -> ActionType:
    return ActionType.TAKEGEM 