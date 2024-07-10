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
    self.assertEqual(game.currentPlayerIndex, 0)
     
  def test_nr_of_cards_in_decks(self):
    #Arrange
    nrOfPlayers = 3
    game = Splendor(nrOfPlayers).buildGame()

    #Act
    tier1Deck = game.tier1Deck
    tier2Deck = game.tier2Deck
    tier3Deck = game.tier3Deck
    
    #Assert
    self.assertEqual(len(tier1Deck.index), 40) # type: ignore
    self.assertEqual(len(tier2Deck.index), 30) # type: ignore
    self.assertEqual(len(tier3Deck.index), 20) # type: ignore

  def test_three_rows_of_development_cards_with_level_1_to_3(self):
    #Arrange
    nrOfPlayers = 2
    game = Splendor(nrOfPlayers).buildGame()
    
    #Act
    tier1Board = game.getTierBoardCards(1)
    tier2Board = game.getTierBoardCards(2)
    tier3Board = game.getTierBoardCards(3)

    #Assert
    self.assertEqual(len(tier1Board.index), 4) # type: ignore
    self.assertEqual(len(tier2Board.index), 4) # type: ignore
    self.assertEqual(len(tier3Board.index), 4) # type: ignore

  def test_correct_number_of_gems_in_piles(self):
    #Arrange
    nrOfPlayers = 2

    #Act
    game = Splendor(nrOfPlayers).buildGame()

    #Assert
    self.assertEqual(game.gems[GemType.RED], nrOfPlayers + 2)
    self.assertEqual(game.gems[GemType.GOLD], 5)

  def test_start_with_players_plus_1_nobles(self):
    #Arrange
    nrOfPlayers = 3

    #Act
    game = Splendor(nrOfPlayers).buildGame()

    #Assert
    self.assertEqual(len(game.nobles.index), nrOfPlayers + 1) # type: ignore

if __name__ == "__main__":
    unittest.main()
