import unittest

from game.Splendor import Splendor
from game.BuyCardAction import BuyCardAction
class TestActionBuyCard(unittest.TestCase):

    #buy_to_expencive_card_not_allowed
    #buy_card_with_developmentcards
    #buy_card_with_developmentcards_gems
    #buy_card_with_gold
    #replace_empty_slot_when_card_is_bought 
    #leave_slot_empty_if_dect_has_run_out

# test_BuyCardFromBoardCombinations

# test_GetGemCombinations
# test_GetGemCombinationsAndReturn
# test_new_card_added_to_board_ater_card_is_reserved
# test_no_card_added_to_board_if_deck_is_empty


    def test_buy_card_remove_from_board_replace_with_new(self):
        #Arrange
        nrOfPlayers = 2
        game = Splendor(nrOfPlayers).withFirstPlayerHaveGemStack([4,4,4,4,4,4]).buildGame()
        
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

    def test_buy_card_with_gems(self):
        #Arrange
        nrOfPlayers = 2
        game = Splendor(nrOfPlayers).withFirstPlayerHaveGemStack([4,4,4,4,4,4]).buildGame()
        
        tierIndex = 0
        boardIndex = 1
        cardIndex = game.gameBoard.developmentDeckTiersBoardIndexes[tierIndex][boardIndex]
        cardCostValues = game.cardPrice(tierIndex, cardIndex)

        #Act
        buyCardAction = BuyCardAction(tierIndex, boardIndex, cardCostValues)
        gameBoard = buyCardAction.execute(game.gameBoard)

        #Assert        
        print(cardCostValues)
        playerStartValues = [4,4,4,4,4,4]
        playerAfterBuyValues = playerStartValues - cardCostValues
        print(playerAfterBuyValues)
        gemsFirstPlayer = gameBoard.players[gameBoard.currentPlayerIndex].gemPiles

        self.assertListEqual(list(gemsFirstPlayer), list(playerAfterBuyValues))
        

if __name__ == "__main__":
    unittest.main()
