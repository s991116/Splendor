from game.Action import Action
from game.ActionType import ActionType
from game.GameBoard import GameBoard
from game.GemType import GemType

import pandas as pd
class ReserveAction(Action):
  
  def __init__(self, card: pd.DataFrame) -> None:
    self.card = card
  
  def execute(self, gameBoard: GameBoard) -> GameBoard:
    currentPlayerIndex = gameBoard.currentPlayerIndex
    gameGoldStack = gameBoard.gemPiles[GemType.GOLD]
    if(gameGoldStack > 0):
      gameBoard.gemPiles[GemType.GOLD] -= 1
      gameBoard.players[currentPlayerIndex].gemStack[GemType.GOLD] += 1
      gameBoard.players[currentPlayerIndex].reserved = pd.concat([self.card, gameBoard.players[currentPlayerIndex].reserved])
      gameBoard.tier1 = gameBoard.tier1.drop(self.card.index)
    return gameBoard
  
  def getType(self) -> ActionType:
    return ActionType.TAKEGEM