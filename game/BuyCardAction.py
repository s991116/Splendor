from game.Action import Action
from game.GameBoard import GameBoard
from game.ActionType import ActionType

class BuyCardAction(Action):
  def __init__(self, tierIndex: int, boardCardIndex: int):
    self.tierIndex = tierIndex
    self.boardCardIndex = boardCardIndex

  def execute(self, gameBoard: GameBoard) -> GameBoard:
    currentPlayerIndex = gameBoard.currentPlayerIndex
    #Copy card to reserve
    gameBoard.players[currentPlayerIndex].developmentCards.append((self.tierIndex, self.boardCardIndex))

    return gameBoard
  
  def getType(self) -> ActionType:
    return ActionType.BUY 