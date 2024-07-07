from game.Player import Player
from game.Noble import Noble
from game.Card import Card
from game.GemType import GemType

from typing import Dict

class Game():
  def __init__(self, players: list[Player], currentPlayerIndex: int, gemPiles: Dict[GemType, int], deckCards: list[list[Card]], boardCards: list[list[Card]], nobles: list[Noble]):
    self.nrOfPlayers = len(players)
    self.players = players
    self.currentPlayerIndex = currentPlayerIndex

    self.gems = gemPiles
    self.nobles = nobles
    self.boardCards = boardCards
    self.deckCards = deckCards

  def _nextPlayer(self):
    self.players[self.currentPlayerIndex].turn = False
    self.currentPlayerIndex = (self.currentPlayerIndex + 1) % self.nrOfPlayers
    self.players[self.currentPlayerIndex].turn = True
    self.currentPlayer = self.players[self.currentPlayerIndex]

  def takeGems(self):
    self._nextPlayer()    