import unittest

from game.Splendor import Splendor
from game.GemType import GemType
from game.TakeGemAction import TakeGemAction

class TestActionTakeGems(unittest.TestCase):
    # player_returns_gems_if_more_than_10_gems

    def test_15_take_gem_actions_when_all_gemstack_are_full(self):
        #Arrange
        nrOfPlayers = 3
        game = Splendor(nrOfPlayers).buildGame()

        #Act
        actions = game.takeGemActions()

        #Assert
        self.assertEqual(len(actions), 15)

    def test_no_take_gem_actions_when_all_gemstack_are_empty(self):
        #Arrange
        nrOfPlayers = 2
        game = Splendor(nrOfPlayers).withEmptyGemStack().buildGame()

        #Act
        actions = game.takeGemActions()

        #Assert
        self.assertEqual(len(actions), 0)

    def test_cannot_take_2_of_same_color_from_pool_whith_three_or_less_of_that_color(self):
        #Arrange
        nrOfPlayers = 2
        game = Splendor(nrOfPlayers).witGemStackOf3().buildGame()

        #Act
        actions = game.takeGemActions()

        #Assert
        self.assertEqual(len(actions), 10)

    def test_take_3_different_colors_from_pool(self):
        #Arrange
        nrOfPlayers = 3
        game = Splendor(nrOfPlayers).buildGame()

        #Act
        takeGemAction = TakeGemAction([GemType.BLACK, GemType.BLUE, GemType.GREEN])
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
