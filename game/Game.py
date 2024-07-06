from game.Player import Player
from game.Noble import Noble
from game.Card import Card
from game.GemType import GemType

from typing import Dict

class Game():
  def __init__(self, nrOfPlayers: int, currentPlayerIndex: int, gemPiles: Dict[GemType, int], deckCards: list[list[Card]], boardCards: list[list[Card]], nobles: list[Noble]):
    self.players: list[Player] = []
    self.nrOfPlayers = nrOfPlayers
    for _ in range(self.nrOfPlayers):
      self.players.append(Player())

    self._currentPlayerIndex = currentPlayerIndex
    self.players[self._currentPlayerIndex].turn = True
    self.currentPlayer = self.players[self._currentPlayerIndex]

    self.gems = gemPiles
    self.nobles = nobles
    self.boardCards = boardCards
    self.deckCards = deckCards

  def _nextPlayer(self):
    self.players[self._currentPlayerIndex].turn = False
    self._currentPlayerIndex = (self._currentPlayerIndex + 1) % self.nrOfPlayers
    self.players[self._currentPlayerIndex].turn = True
    self.currentPlayer = self.players[self._currentPlayerIndex]

  def takeGems(self):
    self._nextPlayer()    