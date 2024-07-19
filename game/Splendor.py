import os
import pandas as pd
import numpy as np

from game.Game import Game
from game.GemType import GemType
from game.Player import Player
from game.GameBoard import GameBoard

class Splendor:
  def __init__(self, nrOfPlayers:int):
    self.nrOfPlayers = nrOfPlayers
    
    developmentDeck = self._loadCards('/decks/developmentCards.csv')    
    self.developmentDeckTiers = self._shuffledDevelopmentCards(developmentDeck)
    self.developmentDeckTiersBoardIndexes = [[*range(4)],[*range(4)],[*range(4)]]
    nobles = self._loadCards('/decks/nobles.csv')
    self.nobles = self._selectRandomNobles(self.nrOfPlayers, nobles)

    self._initGemPiles(self.nrOfPlayers)

    self.currentPlayerIndex = 0
    self.players = self._initPlayers(self.nrOfPlayers, self.currentPlayerIndex)

  def buildGame(self):    
    gameBoard = GameBoard(self.players, self.currentPlayerIndex, self.gemPiles, self.developmentDeckTiers, self.developmentDeckTiersBoardIndexes, self.nobles)
    return Game(gameBoard)
  
  def _initGemPiles(self, nrOfPlayers: int):
    self.gemPiles = {
      GemType.RED: nrOfPlayers + 2,
      GemType.BLACK: nrOfPlayers + 2,
      GemType.WHITE: nrOfPlayers + 2,
      GemType.GREEN: nrOfPlayers + 2,
      GemType.BLUE: nrOfPlayers + 2,
      GemType.GOLD: 5,
      }
    return self
  
  def _initPlayers(self, nrOfPlayers: int, currentPlayerIndex: int):
    players: list[Player] = []
    stack = self.emptyGemStack()
    for _ in range(nrOfPlayers):
      players.append(Player(stack, []))
    return players

  def emptyGemStack(self):
    return {
      GemType.RED: 0,
      GemType.BLACK: 0,
      GemType.WHITE: 0,
      GemType.GREEN: 0,
      GemType.BLUE: 0,
      GemType.GOLD: 0,
      }

  def _loadCards(self, filename: str):
    abspath = '/'.join(os.path.abspath(__file__).split('/')[:-1])
    pathCards = abspath + filename
    return self._loadDeckFromCSV(pathCards)

  def _loadDeckFromCSV(self, filePath:str):
    if not os.path.isfile(filePath):
      assert False, filePath + ' file does not exist'

    deck: np.ndarray[int, np.dtype[np.int32]] = pd.read_csv(filePath).to_numpy() # type: ignore
    return deck

  def _shuffledDevelopmentCards(self, deck: np.ndarray[int, np.dtype[np.int32]]):
		# Shuffle all development cards
    np.random.shuffle(deck)
    #Split into tiers
    developmentCardTiers: list[np.ndarray[int, np.dtype[np.int32]]] = []
    for tier in range(1,4):
      developmentCardTiers.append(deck[ (deck[:,0]==tier) ])
    return developmentCardTiers


  def _selectRandomNobles(self, nrOfPlayers:int, nobles: np.ndarray[int, np.dtype[np.int32]]):
    np.random.shuffle(nobles)
    return nobles[0:nrOfPlayers+1, :]

  def withEmptyGemStack(self):
    self.gemPiles = self.emptyGemStack()
    return self