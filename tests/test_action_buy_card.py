import unittest

from game.Splendor import Splendor
from game.BuyCardAction import BuyCardAction
class TestActionBuyCard(unittest.TestCase):

#test_getBuyActions_that_can_buy_with_developmentcards(self):
#test_getBuyActions_that_can_buy_card_with_gems
#test_GetGemCombinations


    def test_buy_card_with_gems_remove_from_board_replace_with_new(self):
        #Arrange
        nrOfPlayers = 2
        playerStartValues = [4,4,4,4,4,4]
        game = Splendor(nrOfPlayers).withFirstPlayerHaveGemStack(playerStartValues).buildGame()
        
        tierIndex = 0
        boardIndex = 1
        cardIndex = game.gameBoard.developmentDeckTiersBoardIndexes[tierIndex][boardIndex]
        cardCostValues = game.cardPrice(tierIndex, cardIndex)

        #Act
        buyCardAction = BuyCardAction(tierIndex, boardIndex, cardCostValues)
        gameBoard = buyCardAction.execute(game.gameBoard)

        #Assert
        self.assertIn((tierIndex, cardIndex), gameBoard.players[gameBoard.currentPlayerIndex].developmentCards)
        self.assertNotIn(cardIndex, game.gameBoard.developmentDeckTiersBoardIndexes[tierIndex])
        
        playerAfterBuyValuesExpected = playerStartValues - cardCostValues
        gemsFirstPlayer = gameBoard.players[gameBoard.currentPlayerIndex].gemPiles
        self.assertListEqual(list(gemsFirstPlayer), list(playerAfterBuyValuesExpected))

    def test_getBuyActions_can_buy_all_cards_with_many_gems(self):
        #Arrange
        nrOfPlayers = 2
        playerStartValues = [10,10,10,10,10,10]
        game = Splendor(nrOfPlayers).withFirstPlayerHaveGemStack(playerStartValues).buildGame()

        #Act
        buyActions = game.buyCardAction()

        #Assert
        self.assertEqual(len(buyActions), 12)

    def test_getBuyActions_can_only_buy_card_it_can_afford(self):
        #Arrange
        nrOfPlayers = 2
        playerStartValues = [ 0, 1, 1, 0, 0, 0]
        cheapCard         = [ 0, 1, 1, 0, 0]
        expenciveCards    = [10,10,10,10,10]
        game = Splendor(nrOfPlayers).withFirstPlayerHaveGemStack(playerStartValues).withOneCheapAndOtherExpenciveCard(cheapCard, expenciveCards).buildGame()

        #Act
        buyActions = game.buyCardAction()

        #Assert
        self.assertEqual(len(buyActions), 1)

    def test_getBuyActions_that_can_buy_with_developmentcards(self):
        #Arrange
        nrOfPlayers = 2
        playerStartValues = [ 0, 0, 0, 0, 0, 0]
        cheapCard         = [ 0, 1, 1, 0, 0]
        expenciveCards    = [10,10,10,10,10]
        developmentCards  = [ 0, 1, 1, 0, 0]
        game = Splendor(nrOfPlayers)\
            .withFirstPlayerHaveGemStack(playerStartValues)\
            .withOneCheapAndOtherExpenciveCard(cheapCard, expenciveCards)\
            .withFirstPlayerDevelopmentValues(developmentCards)\
            .buildGame()

        #Act
        buyActions = game.buyCardAction()

        #Assert
        self.assertEqual(len(buyActions), 1)

    def test_getBuyActions_that_can_buy_card_with_gold(self):
        #Arrange
        nrOfPlayers = 2
        playerStartValues = [ 0, 0, 0, 0, 0, 4]
        cheapCard         = [ 0, 1, 1, 0, 0]
        expenciveCards    = [10,10,10,10,10]
        game = Splendor(nrOfPlayers)\
            .withFirstPlayerHaveGemStack(playerStartValues)\
            .withOneCheapAndOtherExpenciveCard(cheapCard, expenciveCards)\
            .buildGame()

        #Act
        buyActions = game.buyCardAction()

        #Assert
        self.assertEqual(len(buyActions), 1)


if __name__ == "__main__":
    unittest.main()
