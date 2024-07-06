import unittest

from game.Splendor import Splendor
from game.GemType import GemType

class TestGameInit(unittest.TestCase):


  def test_first_player_start_when_game_starts(self):
    #Arrange
    game = Splendor().generateGame(3)

    #Act
    firstPlayer = game.players[0]

    #Assert
    self.assertTrue(firstPlayer.turn)
    self.assertFalse(game.players[1].turn)
    self.assertFalse(game.players[2].turn)                
     
  def test_nr_of_cards_in_decks(self):
    #Arrange
    game = Splendor().generateGame(3)

    #Act
    level1Deck = game.deckCards[0]
    level1Board = game.boardCards[0]

    #Assert
    self.assertEqual(len(level1Deck), 30)
    self.assertEqual(len(level1Board), 4)


  def test_three_rows_of_development_cards_with_level_1_to_3(self):
    #Arrange
    nrOfPlayers = 2
    
    #Act
    game = Splendor().generateGame(nrOfPlayers)


    #Assert
    self.assertEqual(len(game.boardCards[0]), 4)
    self.assertEqual(len(game.boardCards[1]), 4)
    self.assertEqual(len(game.boardCards[2]), 4)

  def test_correct_number_of_gems_in_piles(self):
    #Arrange
    nrOfPlayers = 2

    #Act
    game = Splendor().generateGame(nrOfPlayers)

    #Assert
    self.assertEqual(game.gems[GemType.RED], nrOfPlayers + 2)
    self.assertEqual(game.gems[GemType.GOLD], 5)

  def test_start_with_players_plus_1_nobles(self):
    #Arrange
    nrOfPlayers = 3

    #Act
    game = Splendor().generateGame(nrOfPlayers)

    #Assert
    self.assertEqual(len(game.nobles), nrOfPlayers + 1)
     


if __name__ == "__main__":
    unittest.main()
