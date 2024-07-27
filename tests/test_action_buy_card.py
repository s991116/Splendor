import unittest

from game.Splendor import Splendor
from game.BuyCardAction import BuyCardAction
class TestActionBuyCard(unittest.TestCase):

#test_getBuyActions_that_can_buy_with_developmentcards(self):
#test_getBuyActions_that_can_buy_card_with_gems
#test_getBuyActions_that_can_buy_card_with_gold
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
        
        playerAfterBuyValues = playerStartValues - cardCostValues
        gemsFirstPlayer = gameBoard.players[gameBoard.currentPlayerIndex].gemPiles
        self.assertListEqual(list(gemsFirstPlayer), list(playerAfterBuyValues))


if __name__ == "__main__":
    unittest.main()
