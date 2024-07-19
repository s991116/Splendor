from __future__ import annotations

import numpy as np
from game.GemType import GemType
from game.GameBoard import GameBoard
from typing import Dict

from game.Action import Action
from game.ReserveAction import ReserveAction
from game.ActionType import ActionType

class Game():
  def __init__(self, gameBoard: GameBoard):
    self.gameBoard = gameBoard

  def nrOfPlayers(self):
    return len(self.gameBoard.players)

  def _nextPlayer(self):
    self.gameBoard.currentPlayerIndex = (self.gameBoard.currentPlayerIndex + 1) % self.nrOfPlayers()

  def takeGems(self, gemsTaken: Dict[GemType, int]):
    for (gemType, take) in gemsTaken.items():
      stack = self.gameBoard.gemPiles[gemType]
      left = stack - take
      assert left > 0, 'To many gems taken'
      self.gameBoard.gemPiles[gemType] = left
      player = self.gameBoard.players[self.gameBoard.currentPlayerIndex]
      player.gemStack[gemType] += 1

    self._nextPlayer()

  def reserveActions(self, actionType: ActionType):
    
    actions: list[Action] = []
    for tierIndex in range(len(self.gameBoard.developmentDeckTiersBoardIndexes)):
      for boardCardIndex in self.gameBoard.developmentDeckTiersBoardIndexes[tierIndex]:
        actions.append(ReserveAction(tierIndex, boardCardIndex))
    return actions  

  def getAllTierBoardCards(self):
    boardCardsTiers: list[np.ndarray[int, np.dtype[np.int32]]] = []
    for developmenTier in self.gameBoard.developmentCardTiers:
      boardCardsTiers.append(developmenTier[0:3,:])
    return boardCardsTiers