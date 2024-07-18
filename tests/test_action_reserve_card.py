import unittest

from game.Splendor import Splendor
from game.ActionType import ActionType
from game.GemType import GemType
from game.ReserveAction import ReserveAction

class TestActionReserveCard(unittest.TestCase):

  def test_ReserveActions_with_all_12_cards(self):
    #Arrange
    nrOfPlayers = 2
    game = Splendor(nrOfPlayers).withEmptyGemStack().buildGame()

    #Act
    actions = game.reserveActions(ActionType.RESERVE)

    #Assert
    self.assertEqual(len(actions), 12)

  def test_player_get_gold_when_reserveActions_is_played(self):
    #Arrange
    nrOfPlayers = 2
    game = Splendor(nrOfPlayers).buildGame()
    actions = game.reserveActions(ActionType.RESERVE)
    gameGoldStackBefore = game.gameBoard.gemPiles[GemType.GOLD]

    #Act
    gameboard = actions[0].execute(game.gameBoard)

    #Assert
    currentPlayerIndex = game.gameBoard.currentPlayerIndex
    playerGemStack = gameboard.players[currentPlayerIndex].gemStack
    playerGoldStack = playerGemStack[GemType.GOLD]
    self.assertEqual(playerGoldStack, 1)

    gameGoldStackAfter = game.gameBoard.gemPiles[GemType.GOLD]
    self.assertEqual(gameGoldStackBefore-gameGoldStackAfter, 1)

  def test_player_dont_get_gold_if_stack_is_empty(self):
    #Arrange
    nrOfPlayers = 2
    game = Splendor(nrOfPlayers).withEmptyGemStack().buildGame()
    actions = game.reserveActions(ActionType.RESERVE)

    #Act
    gameboard = actions[0].execute(game.gameBoard)

    #Assert
    currentPlayerIndex = game.gameBoard.currentPlayerIndex
    playerGemStack = gameboard.players[currentPlayerIndex].gemStack
    playerGoldStack = playerGemStack[GemType.GOLD]
    self.assertEqual(playerGoldStack, 0)

  def test_reserved_card_is_at_players_after_card_is_reserved(self):
    #Arrange
    nrOfPlayers = 2
    game = Splendor(nrOfPlayers).buildGame()
    card = game.getTierBoardCards(2).head(1)

    #Act
    action = ReserveAction(card)
    gameboard = action.execute(game.gameBoard)

    #Assert
    currentPlayerIndex = game.gameBoard.currentPlayerIndex
    reservedCardIndex = card.head(1).index.tolist()[0] # type: ignore

    self.assertIn(reservedCardIndex, gameboard.players[currentPlayerIndex].reserved.index) # type: ignore
    self.assertNotIn(reservedCardIndex, gameboard.tier2.index) # type: ignore

if __name__ == "__main__":
    unittest.main()