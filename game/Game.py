from game.Player import Player
from game.Nobles import Nobles
from game.Card import Card

class Game():
  def __init__(self, nrOfPlayers: int):
    self.players: list[Player] = []
    self.nrOfPlayers = nrOfPlayers
    for _ in range(self.nrOfPlayers):
      self.players.append(Player())

    self._currentPlayerIndex = 0    
    self.players[self._currentPlayerIndex].turn = True
    self.currentPlayer = self.players[self._currentPlayerIndex]

    self._initGemPiles(self.nrOfPlayers)
    self._initCards()
    self._initNobles(self.nrOfPlayers)

  def _initGemPiles(self, nrOfPlayers: int):
    self.redGemPileCount = nrOfPlayers + 2
    self.blackGemPileCount = nrOfPlayers + 2
    self.whiteGemPileCount = nrOfPlayers + 2
    self.greenGemPileCount = nrOfPlayers + 2
    self.blueGemPileCount = nrOfPlayers + 2
    self.goldGemPileCount = 5

  def _initCards(self):
    self.level1CardsOnTable: list[Card] = []
    self.level2CardsOnTable: list[Card] = []
    self.level3CardsOnTable: list[Card] = []

    for _ in range(4):
      self.level1CardsOnTable.append(Card())
      self.level2CardsOnTable.append(Card())
      self.level3CardsOnTable.append(Card())      

  def _initNobles(self, nrOfPlayers: int):
    self.nobles: list[Nobles] = []
    for _ in range(self.nrOfPlayers+1):
      self.nobles.append(Nobles())

  def _nextPlayer(self):
    self.players[self._currentPlayerIndex].turn = False
    self._currentPlayerIndex = (self._currentPlayerIndex + 1) % self.nrOfPlayers
    self.players[self._currentPlayerIndex].turn = True
    self.currentPlayer = self.players[self._currentPlayerIndex]

  def takeGems(self):
    self._nextPlayer()    