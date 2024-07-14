from __future__ import annotations

import pandas as pd

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

#  def reserveActions(self, actionType: ActionType):
#    actions: list[Action] = []
#    for card in self.getAllTierBoardCards().iterrows(): # type: ignore
#      actions.append(ReserveAction() # type: ignore
#    return actions  

  def getAllTierBoardCards(self):
    shown_tier1 = self.gameBoard.tier1[-min(4, len(self.gameBoard.tier1)):].reset_index(drop=True)
    shown_tier2 = self.gameBoard.tier2[-min(4, len(self.gameBoard.tier2)):].reset_index(drop=True)
    shown_tier3 = self.gameBoard.tier3[-min(4, len(self.gameBoard.tier3)):].reset_index(drop=True)
    return pd.concat([shown_tier1,shown_tier2, shown_tier3]) # type: ignore
  
  def getTierBoardCards(self, tier:int):
    if tier == 1:
      return self.gameBoard.tier1[-min(4, len(self.gameBoard.tier1)):].reset_index(drop=True)
    elif tier == 2:
      return self.gameBoard.tier2[-min(4, len(self.gameBoard.tier2)):].reset_index(drop=True)
    elif tier == 3:
      return self.gameBoard.tier3[-min(4, len(self.gameBoard.tier3)):].reset_index(drop=True)
    assert False, 'Incorrect tier number'