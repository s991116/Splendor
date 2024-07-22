import unittest
import dataclasses

from game.Splendor import Splendor
from game.GemType import GemType
from game.TakeGemAction import TakeGemAction
from game.Game import Game
from game.Action import Action

class TestActionTakeGems(unittest.TestCase):
    
    #test_can_return_gold_if_more_than_10_gems_after_gems_taken

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

    def test_gem_actions_when_starting_with_10_gems(self):
        #Arrange
        nrOfPlayers = 4
        game = Splendor(nrOfPlayers).withFirstPlayerHaveGemStack([2,2,2,2,2,0]).buildGame()

        #Act
        actions = game.takeGemActions()

        #Assert
        totalGemPilesCombinations = 151
        self.AssertAllCombinationsAreValidAndUnique(game, actions, totalGemPilesCombinations)

    def test_gem_actions_when_starting_with_9_gems(self):
        #Arrange
        nrOfPlayers = 4
        game = Splendor(nrOfPlayers).withFirstPlayerHaveGemStack([2,2,2,1,2,0]).buildGame()

        #Act
        actions = game.takeGemActions()

        #Assert
        totalGemPilesCombinations = 81
        self.AssertAllCombinationsAreValidAndUnique(game, actions, totalGemPilesCombinations)

    def test_gem_actions_when_starting_with_8_gems(self):
        #Arrange
        nrOfPlayers = 4
        game = Splendor(nrOfPlayers).withFirstPlayerHaveGemStack([2,1,2,1,2,0]).buildGame()

        #Act
        actions = game.takeGemActions()

        #Assert
        totalGemPilesCombinations = 35
        self.AssertAllCombinationsAreValidAndUnique(game, actions, totalGemPilesCombinations)


    def AssertAllCombinationsAreValidAndUnique(self, game: Game, actions: list[Action], totalGemPilesCombinations: int):
        gemPilesCombinations: list[list[int]] = []
        #Execute all actions
        for action in actions:
            gameBoard = game.gameBoard.deepCopy()
            playerGems = action.execute(gameBoard).players[gameBoard.currentPlayerIndex].gemPiles
            gemPilesCombinations.append(playerGems)

        playerGemsCombinationsSet: set[tuple[int,int,int,int,int]] = set()
        for gemPilesCombination in gemPilesCombinations:
            #Assert all take list are of length 5, number of gems plus gold
            self.assertEqual(len(gemPilesCombination), 6)

            #Assert all combinations have 10 gems
            self.assertEqual(sum(gemPilesCombination), 10)

            #Assert no gold has been taken
            self.assertEqual(gemPilesCombination[GemType.GOLD], 0)

            #Assert no combination is a dublicate
            playersGemsTuple = tuple(gemPilesCombination)
            self.assertNotIn(playersGemsTuple, playerGemsCombinationsSet)
            
            #self.assertFalse(playersGemsTuple in playerGemsCombinationsSet)
            playerGemsCombinationsSet.add(playersGemsTuple)
        self.assertEqual(len(gemPilesCombinations), totalGemPilesCombinations)

    def test_take_3_different_colors_from_pool(self):
        #Arrange
        nrOfPlayers = 3
        game = Splendor(nrOfPlayers).buildGame()

        #Act
        takeGemAction = TakeGemAction((0,1,0,1,1))
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

        self.assertEqual(gameBoard.players[0].gemPiles[GemType.BLACK], 1)

    def test_player_can_returns_gems(self):
        #Arrange
        nrOfPlayers = 2
        game = Splendor(nrOfPlayers).withFirstPlayerHaveGemStack([2,2,2,2,2,0]).buildGame()

        #Act
        takeGemAction = TakeGemAction((-1,1,-1,0,1))
        gameBoard = takeGemAction.execute(game.gameBoard)

        #Assert
        self.assertEqual(gameBoard.players[0].gemPiles[GemType.BLACK], 3)
        self.assertEqual(gameBoard.players[0].gemPiles[GemType.BLUE] , 3)
        self.assertEqual(gameBoard.players[0].gemPiles[GemType.GREEN], 2)
        self.assertEqual(gameBoard.players[0].gemPiles[GemType.RED]  , 1)                
        self.assertEqual(gameBoard.players[0].gemPiles[GemType.WHITE], 1)


if __name__ == "__main__":
    unittest.main()
