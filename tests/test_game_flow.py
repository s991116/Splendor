import unittest

from game.Splendor import Splendor
from game.GemType import GemType
class TestGameFlow(unittest.TestCase):

  def test_turn_shifts_when_action_is_complete(self):
    #Arrange
    nrOfPlayers = 3
    game = Splendor(nrOfPlayers).buildGame()

    #Act
    game.nextPlayer()

    #Assert
    self.assertEqual(game.gameBoard.currentPlayerIndex, 1)

  def test_first_player_has_turn_when_new_round_starts(self):
    #Arrange
    nrOfPlayers = 3
    game = Splendor(nrOfPlayers).buildGame()

    #Act
    game.nextPlayer()
    game.nextPlayer()
    game.nextPlayer()

    #Assert
    self.assertEqual(game.gameBoard.currentPlayerIndex, 0)     

if __name__ == "__main__":
    unittest.main()
