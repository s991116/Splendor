from game.Action import Action
from game.ActionType import ActionType
from game.GameBoard import GameBoard
from game.GemType import GemType

class ReserveCardAction(Action):
  
  def __init__(self, tierIndex: int, boardCardIndex: int) -> None:
    self.tierIndex = tierIndex
    self.boardCardIndex = boardCardIndex
  
  def execute(self, gameBoard: GameBoard) -> GameBoard:
    currentPlayerIndex = gameBoard.currentPlayerIndex
    gameGoldStack = gameBoard.gemPiles[GemType.GOLD]
    if(gameGoldStack > 0):
      gameBoard.gemPiles[GemType.GOLD] -= 1
      gameBoard.players[currentPlayerIndex].gemPiles[GemType.GOLD] += 1

    #Copy card to reserve
    gameBoard.players[currentPlayerIndex].reserved.append((self.tierIndex, self.boardCardIndex))

    #Replace card on board
    gameBoard = super().replaceBoardCard(gameBoard, self.tierIndex, self.boardCardIndex)

    return gameBoard
  
  def getType(self) -> ActionType:
    return ActionType.RESERVE