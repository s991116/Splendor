import unittest

from game.Splendor import Splendor
from game.ActionType import ActionType

class TestGetActions(unittest.TestCase):
# test_BuyCardFromBoardCombinations
# test_BuyCardFromHandCombinations

# test_GetGemCombinations
# test_GetGemCombinationsAndReturn

  def test_ReserveCard(self):
    #Arrange
    nrOfPlayers = 2
    game = Splendor(nrOfPlayers).buildGame()

    #Act
    #cards = game.reserveActions(ActionType.RESERVE)

    #Assert
    #self.assertEqual(len(cards), 12)

if __name__ == "__main__":
    unittest.main()