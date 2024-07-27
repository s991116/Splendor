from game.Action import Action
from game.GameBoard import GameBoard
from game.ActionType import ActionType
import numpy as np
import numpy.typing as npt

class BuyCardAction(Action):
  def __init__(self, tierIndex: int, boardCardIndex: int, payment: npt.NDArray[np.int64]):
    self.tierIndex = tierIndex
    self.boardCardIndex = boardCardIndex
    self.payment = payment

  def execute(self, gameBoard: GameBoard) -> GameBoard:
    player = gameBoard.players[gameBoard.currentPlayerIndex]

    #Pay for card
    player.gemPiles -= self.payment

    #Copy card to reserve
    player.developmentCards.append((self.tierIndex, self.boardCardIndex))
    #Replace card on board
    gameBoard = super().replaceBoardCard(gameBoard, self.tierIndex, self.boardCardIndex)

    return gameBoard
  
  def getType(self) -> ActionType:
    return ActionType.BUY 