from __future__ import annotations

from game.GameBoard import GameBoard
from game.Action import Action
from game.ReserveAction import ReserveAction
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