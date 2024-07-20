import unittest

from game.Splendor import Splendor
from game.GemType import GemType
from game.TakeGemActions import TakeGemActions

class TestActionTakeGems(unittest.TestCase):
    # take_3_different_colors_from_pool
    # cannot_take_color_from_empty_pool
    # take_2_of_same_color_from_pool_whith_four_or_more_of_that_color
    # cannot_take_2_of_same_color_from_pool_whith_four_or_more_of_that_color
    # player_returns_gems_if_more_than_10_gems

    def test_take_3_different_colors_from_pool(self):
        #Arrange
        nrOfPlayers = 3
        game = Splendor(nrOfPlayers).buildGame()

        #Act
        takeGemAction = TakeGemActions({GemType.BLACK: 1, GemType.BLUE: 1, GemType.GREEN: 1})
        gameBoard = takeGemAction.execute(game.gameBoard)

        #Assert
        blackGems = gameBoard.gemPiles[GemType.BLACK]
        self.assertEqual(blackGems, 4)
        blackGems = gameBoard.gemPiles[GemType.BLUE]
        self.assertEqual(blackGems, 4)
        blackGems = gameBoard.gemPiles[GemType.GREEN]
        self.assertEqual(blackGems, 4)
        blackGems = gameBoard.gemPiles[GemType.WHITE]
        self.assertEqual(blackGems, 5)

        self.assertEqual(gameBoard.players[0].gemStack[GemType.BLACK], 1)


if __name__ == "__main__":
    unittest.main()
