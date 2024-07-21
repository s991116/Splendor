from __future__ import annotations

from game.GameBoard import GameBoard
from game.Action import Action
from game.ReserveAction import ReserveAction
from game.TakeGemAction import TakeGemAction

from game.ActionType import ActionType

class Game():
  def __init__(self, gameBoard: GameBoard):
    self.gameBoard = gameBoard

  def nrOfPlayers(self):
    return len(self.gameBoard.players)

  def nextPlayer(self):
    self.gameBoard.currentPlayerIndex = (self.gameBoard.currentPlayerIndex + 1) % self.nrOfPlayers()

  def reserveActions(self, actionType: ActionType):
    
    actions: list[Action] = []

    if(len(self.gameBoard.players[self.gameBoard.currentPlayerIndex].reserved) < 3):
      for tierIndex in range(len(self.gameBoard.developmentDeckTiersBoardIndexes)):
        for boardCardIndex in self.gameBoard.developmentDeckTiersBoardIndexes[tierIndex]:
          actions.append(ReserveAction(tierIndex, boardCardIndex))
    return actions
  
  def takeGemActions(self):
    actions: list[Action] = []
    
    combinationWith3Gems = [
      [0, 1, 2], [0, 1, 3], [0, 1, 4], [0, 2, 3],
      [0, 2, 4], [0, 3, 4], [1, 2, 3], [1, 2, 4],
      [1, 3, 4], [2, 3, 4]]
    
    combinationsWith2Gems = [ 
      [0,0], [1,1], [2,2], [3,3], [4,4]]
    
    gemPiles = self.gameBoard.gemPiles
    for gemCombination in combinationWith3Gems:
      if(gemPiles[gemCombination[0]] > 0 and gemPiles[gemCombination[1]] > 0 and gemPiles[gemCombination[2]] > 0):
        actions.append(TakeGemAction(gemCombination))

    for gemCombination in combinationsWith2Gems:
      if(gemPiles[gemCombination[0]] >= 4):
        actions.append(TakeGemAction(gemCombination))

    return actions