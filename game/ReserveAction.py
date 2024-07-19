from game.Action import Action
from game.ActionType import ActionType
from game.GameBoard import GameBoard
from game.GemType import GemType

class ReserveAction(Action):
  
  def __init__(self, tierIndex: int, boardIndex: int) -> None:
    self.tierIndex = tierIndex
    self.cardIndex = boardIndex
  
  def execute(self, gameBoard: GameBoard) -> GameBoard:
    currentPlayerIndex = gameBoard.currentPlayerIndex
    gameGoldStack = gameBoard.gemPiles[GemType.GOLD]
    if(gameGoldStack > 0):
      gameBoard.gemPiles[GemType.GOLD] -= 1
      gameBoard.players[currentPlayerIndex].gemStack[GemType.GOLD] += 1

    #Copy card to reserve
    gameBoard.players[currentPlayerIndex].reserved.append((self.tierIndex, self.cardIndex))

    #Remove card from tier board Deck
    tierBoardIndexes = gameBoard.developmentDeckTiersBoardIndexes[self.tierIndex]
    maxIndex = max(range(len(tierBoardIndexes)), key=tierBoardIndexes.__getitem__)
    maxValue = tierBoardIndexes[maxIndex]
    newMaxValue = maxValue + 1
    gameBoard.developmentDeckTiersBoardIndexes[self.tierIndex][self.cardIndex] = newMaxValue

    return gameBoard
  
  def getType(self) -> ActionType:
    return ActionType.TAKEGEM