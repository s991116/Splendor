from game.Game import Game
from game.GemType import GemType
from game.Noble import Noble
from game.Card import Card
from game.Player import Player

from typing import List

class Splendor:
  def __init__(self):
    pass

  def generateGame(self, nrOfPlayers: int):
    gemPiles = self._initGemPiles(nrOfPlayers)
    deckCards = self._initDeckCards()
    boardCards = self._initBoardCards()
    nobles = self._initNobles(nrOfPlayers)
    currentPlayerIndex = 0
    players = self._initPlayers(nrOfPlayers, currentPlayerIndex)

    return Game(players, currentPlayerIndex, gemPiles, deckCards, boardCards, nobles)
  
  def _initGemPiles(self, nrOfPlayers: int):
    gemPiles = {
      GemType.RED: nrOfPlayers + 2,
      GemType.BLACK: nrOfPlayers + 2,
      GemType.WHITE: nrOfPlayers + 2,
      GemType.GREEN: nrOfPlayers + 2,
      GemType.BLUE: nrOfPlayers + 2,
      GemType.GOLD: 5,
      }
    return gemPiles
  
  def _initPlayers(self, nrOfPlayers: int, currentPlayerIndex: int):
    players: list[Player] = []
    for _ in range(nrOfPlayers):
      players.append(Player())

    players[currentPlayerIndex].turn = True
    return players

  def _initBoardCards(self):
    boardCards : List[List[Card]] = []

    for tier in range(3):
      tierBoard: list[Card] = []
      for _ in range(4):
        boarCard = Card(tier,0,0,0,0,0,0,0)
        tierBoard.append(boarCard)
      boardCards.append(tierBoard)
    return boardCards

  def _initDeckCards(self):
    deckCards : List[List[Card]] = []

    for tier in range(3):
      tierDeck: list[Card] = []
      for _ in range(30):
        deckCard = Card(tier,0,0,0,0,0,0,0)
        tierDeck.append(deckCard)
      deckCards.append(tierDeck)
    return deckCards

  def _initNobles(self, nrOfPlayers: int):
    nobles: list[Noble] = []
    for _ in range(nrOfPlayers+1):
      nobles.append(Noble())
    return nobles