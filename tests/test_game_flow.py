import unittest

from game.Splendor import Splendor
class TestGameFlow(unittest.TestCase):

  def test_turn_shifts_when_action_is_complete(self):
    #Arrange
    game = Splendor().generateGame(3)

    #Act
    game.takeGems()

    #Assert
    self.assertFalse(game.players[0].turn)
    self.assertTrue(game.players[1].turn)
    self.assertFalse(game.players[2].turn)                

  def test_first_player_has_turn_when_new_round_starts(self):
    #Arrange
    game = Splendor().generateGame(3)

    #Act
    game.takeGems()
    game.takeGems()
    game.takeGems()

    #Assert
    self.assertTrue(game.players[0].turn)
    self.assertFalse(game.players[1].turn)
    self.assertFalse(game.players[2].turn)                
     

if __name__ == "__main__":
    unittest.main()
