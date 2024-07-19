import unittest

from game.Splendor import Splendor
from game.GemType import GemType

class TestGameInit(unittest.TestCase):

  def test_first_player_start_when_game_starts(self):
    #Arrange
    nrOfPlayers = 3

    #Act
    game = Splendor(nrOfPlayers).buildGame()

    #Assert
    self.assertEqual(game.gameBoard.currentPlayerIndex, 0)
     
  def test_nr_of_cards_in_decks(self):
    #Arrange
    nrOfPlayers = 3
    game = Splendor(nrOfPlayers).buildGame()

    #Act
    tier1Deck = game.gameBoard.developmentCardTiers[0]
    tier2Deck = game.gameBoard.developmentCardTiers[1]
    tier3Deck = game.gameBoard.developmentCardTiers[2]
    
    #Assert
    self.assertEqual(len(tier1Deck), 40) # type: ignore
    self.assertEqual(len(tier2Deck), 30) # type: ignore
    self.assertEqual(len(tier3Deck), 20) # type: ignore

  def test_three_rows_of_development_cards_with_level_1_to_3(self):
    #Arrange
    nrOfPlayers = 2
    game = Splendor(nrOfPlayers).buildGame()
    
    #Act
    tier1Board = game.gameBoard.developmentDeckTiersBoardIndexes[0]
    tier2Board = game.gameBoard.developmentDeckTiersBoardIndexes[1]
    tier3Board = game.gameBoard.developmentDeckTiersBoardIndexes[2]

    #Assert
    self.assertEqual(len(tier1Board), 4) # type: ignore
    self.assertEqual(len(tier2Board), 4) # type: ignore
    self.assertEqual(len(tier3Board), 4) # type: ignore

  def test_correct_number_of_gems_in_piles(self):
    #Arrange
    nrOfPlayers = 2

    #Act
    game = Splendor(nrOfPlayers).buildGame()

    #Assert
    self.assertEqual(game.gameBoard.gemPiles[GemType.RED], nrOfPlayers + 2)
    self.assertEqual(game.gameBoard.gemPiles[GemType.GOLD], 5)

  def test_start_with_players_plus_1_nobles(self):
    #Arrange
    nrOfPlayers = 3

    #Act
    game = Splendor(nrOfPlayers).buildGame()

    #Assert
    num_rows, _ = game.gameBoard.nobles.shape
    self.assertEqual(num_rows, nrOfPlayers + 1) # type: ignore

if __name__ == "__main__":
    unittest.main()
