import pandas as pd

from game.Player import Player
from game.GemType import GemType

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
    self.players[self.currentPlayerIndex].turn = False
    self.currentPlayerIndex = (self.currentPlayerIndex + 1) % self.nrOfPlayers
    self.players[self.currentPlayerIndex].turn = True
    self.currentPlayer = self.players[self.currentPlayerIndex]

  def takeGems(self):
    self._nextPlayer()

  def getTierBoardCards(self, tier:int):
    if tier == 1:
      return self.tier1Deck[-min(4, len(self.tier1Deck)):].reset_index(drop=True)
    elif tier == 2:
      return self.tier2Deck[-min(4, len(self.tier2Deck)):].reset_index(drop=True)
    elif tier == 3:
      return self.tier3Deck[-min(4, len(self.tier3Deck)):].reset_index(drop=True)
    assert False, 'invalid tier number'
