from game.GameBoard import GameBoard
from game.ActionType import ActionType

class Action:
  
  def execute(self, gameBoard: GameBoard) -> GameBoard:
    return gameBoard
  
  def getType(self) -> ActionType:
    return ActionType.TAKEGEM
  
  def replaceBoardCard(self, gameBoard: GameBoard, tierIndex: int, boardCardIndex: int) -> GameBoard:
    tierBoardIndexes = gameBoard.developmentDeckTiersBoardIndexes[tierIndex]
    maxIndex = max(range(len(tierBoardIndexes)), key=tierBoardIndexes.__getitem__)
    maxValue = tierBoardIndexes[maxIndex]
    newMaxValue = maxValue + 1
    maxValueTier = [40,30,20]
    if(newMaxValue >= maxValueTier[tierIndex]):
      gameBoard.developmentDeckTiersBoardIndexes[tierIndex].remove(boardCardIndex)
    else:
      gameBoard.developmentDeckTiersBoardIndexes[tierIndex][boardCardIndex] = newMaxValue
    return gameBoard