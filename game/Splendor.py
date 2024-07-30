import os
import pandas as pd
import numpy as np
import numpy.typing as npt

from game.Game import Game
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

    self.gemPiles = self._initGemPiles(self.nrOfPlayers)
    self.currentPlayerIndex = 0
    self.players = self._initPlayers(self.nrOfPlayers, self.currentPlayerIndex)

  def buildGame(self):    
    gameBoard = GameBoard(self.players, self.currentPlayerIndex, self.gemPiles, self.developmentDeckTiers, self.developmentDeckTiersBoardIndexes, self.nobles)
    return Game(gameBoard)
  
  def _initGemPiles(self, nrOfPlayers: int) -> npt.NDArray[np.int64]:    
    return np.array([
      nrOfPlayers + 2,
      nrOfPlayers + 2,
      nrOfPlayers + 2,
      nrOfPlayers + 2,
      nrOfPlayers + 2,
      5,
    ])
  
  def _initPlayers(self, nrOfPlayers: int, currentPlayerIndex: int):
    players: list[Player] = []
    stack = self.emptyGemStack()
    developmentValues = self.emptyDevelopmentValues()
    for _ in range(nrOfPlayers):
      players.append(Player(stack, [], [], developmentValues))
    return players

  def emptyGemStack(self):
    return self.withGemStackOf(0)
  
  def withGemStackOf(self, stackSize:int) -> npt.NDArray[np.int64]:
    return np.array([stackSize, stackSize, stackSize, stackSize, stackSize, stackSize, ])

  def emptyDevelopmentValues(self) -> npt.NDArray[np.int64]:
    return np.array([0,0,0,0,0])

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

  def witGemStackOf3(self):
    self.gemPiles = self.withGemStackOf(3)
    return self

  def with3CardsReserved(self):
    for tierIndex in range(3):
      for deckIndex in range(4):
        self.developmentDeckTiersBoardIndexes[tierIndex][deckIndex] += 3

    self.players[self.currentPlayerIndex].reserved = [(0,0), (0,1), (0,2)]
    return self
  
  def withFirstPlayerHaveGemStack(self, playerGemStack: list[int]):    
    self.players[0].gemPiles = np.array(playerGemStack)
    return self

  def withLastCardsOnBoard(self):
    self.developmentDeckTiersBoardIndexes = [[39],[29],[19]]
    return self
  
  def withFirstPlayerDevelopmentValues(self, developmentValues: list[int]):
    self.players[0].developmentValues = np.array(developmentValues)
    return self
  
  def withCardPrice(self, cardPrice: list[int]):
    for developmentDeck in self.developmentDeckTiers:
      for developmentCard in developmentDeck:
        #tier,value,type,green,white,blue,black,red
        developmentCard[3:8] = cardPrice
        return self

  def withOneCheapAndOtherExpenciveCard(self, cardPriceOne: list[int], cardPriceRest: list[int]):
    self.withCardPrice(cardPriceRest)
    self.developmentDeckTiers[1][1][3:8] = cardPriceOne
    return self