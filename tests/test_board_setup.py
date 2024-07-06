import unittest

from game.Game import Game

class TestBoardSetup(unittest.TestCase):

  def test_three_rows_of_development_cards_with_level_1_to_3(self):
    #Arrange
    #Act
    nrOfPlayers = 2
    game = Game(nrOfPlayers)

    #Assert
    self.assertEqual(len(game.level1CardsOnTable), 4)
    self.assertEqual(len(game.level2CardsOnTable), 4)
    self.assertEqual(len(game.level3CardsOnTable), 4)

  def test_correct_number_of_gems_in_piles(self):
    #Arrange
    nrOfPlayers = 2

    #Act
    game = Game(nrOfPlayers)

    #Assert
    self.assertEqual(game.redGemPileCount, nrOfPlayers + 2)
    self.assertEqual(game.goldGemPileCount, 5)

  def test_start_with_players_plus_1_nobles(self):
    #Arrange
    nrOfPlayers = 3

    #Act
    game = Game(nrOfPlayers)

    #Assert
    self.assertEqual(len(game.nobles), nrOfPlayers + 1)
     

if __name__ == "__main__":
    unittest.main()
