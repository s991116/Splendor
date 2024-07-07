import os
import pandas as pd

from game.Game import Game
from game.GemType import GemType
from game.Player import Player

class Splendor:
  def __init__(self):
    pass

  def generateGame(self, nrOfPlayers: int):
    gemPiles = self._initGemPiles(nrOfPlayers)
    
    self._loadCards()
    (tier1, tier2, tier3, nobles) = self._shuffledCards(nrOfPlayers)

    currentPlayerIndex = 0
    players = self._initPlayers(nrOfPlayers, currentPlayerIndex)
    return Game(players, currentPlayerIndex, gemPiles, tier1, tier2, tier3, nobles)
  
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

  def _loadCards(self):
    abspath = '/'.join(os.path.abspath(__file__).split('/')[:-1])
    pathDevelopmentCards = abspath + '/decks/developmentCards.csv'
    pathNobles = abspath + '/decks/nobles.csv'

    self.primary_cards = self._loadDeckFromCSV(pathDevelopmentCards)
    self.primary_nobles = self._loadDeckFromCSV(pathNobles)

  def _loadDeckFromCSV(self, filePath:str):
    if not os.path.isfile(filePath):
      assert False, filePath + ' file does not exist'

    return pd.read_csv(filePath) # type: ignore

  def _shuffledCards(self, nrOfPlayers:int):
		# Shuffle all the cards and nobles
    shuffled_cards = self.primary_cards.sample(frac=1) # type: ignore
    shuffled_nobles = self.primary_nobles.sample(frac=1) # type: ignore

		# Organize cards in relation to their tier
    t1_idx = shuffled_cards['tier'] == 1
    t2_idx = shuffled_cards['tier'] == 2
    t3_idx = shuffled_cards['tier'] == 3
    tier1 = shuffled_cards.loc[t1_idx].reset_index(drop=True)
    tier2 = shuffled_cards.loc[t2_idx].reset_index(drop=True)
    tier3 = shuffled_cards.loc[t3_idx].reset_index(drop=True)
    nobles = shuffled_nobles[-(nrOfPlayers+1):].reset_index(drop=True)

    return(tier1, tier2, tier3, nobles)