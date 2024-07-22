import unittest

from game.Splendor import Splendor
from game.ActionType import ActionType
from game.GemType import GemType
from game.ReserveAction import ReserveAction

#Can only reserve 3 cards

class TestActionReserveCard(unittest.TestCase):

  def test_ReserveActions_with_all_12_cards(self):
    #Arrange
    nrOfPlayers = 2
    game = Splendor(nrOfPlayers).buildGame()

    #Act
    actions = game.reserveActions(ActionType.RESERVE)

    #Assert
    self.assertEqual(len(actions), 12)

  def test_player_can_not_reserve_if_3_cards_is_reserved(self):
    #Arrange
    nrOfPlayers = 2
    game = Splendor(nrOfPlayers).with3CardsReserved().buildGame()

    #Act
    actions = game.reserveActions(ActionType.RESERVE)

    #Assert
    self.assertEqual(len(actions), 0)

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
    playerGemStack = gameboard.players[currentPlayerIndex].gemPiles
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
    playerGemStack = gameboard.players[currentPlayerIndex].gemPiles
    playerGoldStack = playerGemStack[GemType.GOLD]
    self.assertEqual(playerGoldStack, 0)

  def test_reserved_card_is_at_players_after_card_is_reserved(self):
    #Arrange
    nrOfPlayers = 2
    game = Splendor(nrOfPlayers).buildGame()
    reserveCardTier = 2
    reserveCardindex = 1

    #Act
    action = ReserveAction(reserveCardTier, reserveCardindex)
    gameboard = action.execute(game.gameBoard)

    #Assert
    currentPlayerIndex = game.gameBoard.currentPlayerIndex

    self.assertIn((reserveCardTier, reserveCardindex), gameboard.players[currentPlayerIndex].reserved)
    
    self.assertNotIn(reserveCardindex, gameboard.developmentDeckTiersBoardIndexes[reserveCardTier]) # type: ignore

  def test_reserve_last_card_is_not_replaced(self):
    #Arrange
    nrOfPlayers = 2
    game = Splendor(nrOfPlayers).withLastCardsOnBoard().buildGame()

    actions = game.reserveActions(ActionType.RESERVE)

    #Act
    gameboard = actions[0].execute(game.gameBoard)

    #Assert
    cardsOnBoard = 0
    for tier in range(3):
      cardsOnBoard += len(gameboard.developmentDeckTiersBoardIndexes[tier])

    self.assertEqual(cardsOnBoard,2)

if __name__ == "__main__":
    unittest.main()