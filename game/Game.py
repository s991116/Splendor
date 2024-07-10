import pandas as pd

from game.Player import Player
from game.GemType import GemType
from game.ActionType import ActionType


from typing import Dict

class Game():
  def __init__(self, players: list[Player], currentPlayerIndex: int, gemPiles: Dict[GemType, int], tier1: pd.DataFrame, tier2: pd.DataFrame, tier3: pd.DataFrame, nobles: pd.DataFrame):
    self.nrOfPlayers = len(players)
    self.players = players
    self.currentPlayerIndex = currentPlayerIndex

    self.gems = gemPiles
    self.nobles = nobles
    self.tier1Deck = tier1
    self.tier2Deck = tier2
    self.tier3Deck = tier3

  def _nextPlayer(self):
    self.players[self.currentPlayerIndex].turn = False # type: ignore
    self.currentPlayerIndex = (self.currentPlayerIndex + 1) % self.nrOfPlayers
    self.players[self.currentPlayerIndex].turn = True # type: ignore

  def takeGems(self, gemsTaken: Dict[GemType, int]):
    for (gemType, take) in gemsTaken.items():
      stack = self.gems[gemType]
      left = stack - take
      assert left > 0, 'To many gems taken'
      self.gems[gemType] = left
      self.players[self.currentPlayerIndex].gemStack[gemType] += 1

    self._nextPlayer()

  def reserveActions(self, actionType: ActionType):
    return self.getAllTierBoardCards()

  def getAllTierBoardCards(self):
    shown_tier1 = self.tier1Deck[-min(4, len(self.tier1Deck)):].reset_index(drop=True)
    shown_tier2 = self.tier2Deck[-min(4, len(self.tier2Deck)):].reset_index(drop=True)
    shown_tier3 = self.tier3Deck[-min(4, len(self.tier3Deck)):].reset_index(drop=True)
    return pd.concat([shown_tier1,shown_tier2, shown_tier3]) # type: ignore
  
  def getTierBoardCards(self, tier:int):
    if tier == 1:
      return self.tier1Deck[-min(4, len(self.tier1Deck)):].reset_index(drop=True)
    elif tier == 2:
      return self.tier2Deck[-min(4, len(self.tier2Deck)):].reset_index(drop=True)
    elif tier == 3:
      return self.tier3Deck[-min(4, len(self.tier3Deck)):].reset_index(drop=True)
    assert False, 'Incorrect tier number'