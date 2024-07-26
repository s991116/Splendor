from __future__ import annotations

from game.GameBoard import GameBoard
from game.Action import Action
from game.ReserveAction import ReserveAction
from game.TakeGemAction import TakeGemAction

from game.ActionType import ActionType

class Game():
  def __init__(self, gameBoard: GameBoard):
    self.gameBoard = gameBoard

  def nrOfPlayers(self):
    return len(self.gameBoard.players)

  def nextPlayer(self):
    self.gameBoard.currentPlayerIndex = (self.gameBoard.currentPlayerIndex + 1) % self.nrOfPlayers()

  def reserveActions(self, actionType: ActionType):
    
    actions: list[Action] = []

    if(len(self.gameBoard.players[self.gameBoard.currentPlayerIndex].reserved) < 3):
      for tierIndex in range(len(self.gameBoard.developmentDeckTiersBoardIndexes)):
        for boardCardIndex in self.gameBoard.developmentDeckTiersBoardIndexes[tierIndex]:
          actions.append(ReserveAction(tierIndex, boardCardIndex))
    return actions
  
  def takeGemActions(self):
    actions: list[Action] = []

    combinationWith3GemCounts = [
      [1, 1, 1, 0, 0], #[0, 1, 2], 
      [1, 1, 0, 1, 0], #[0, 1, 3], 
      [1, 1, 0, 0, 1], #[0, 1, 4], 
      [1, 0, 1, 1, 0], #[0, 2, 3],
      [1, 0, 1, 0, 1], #[0, 2, 4], 
      [1, 0, 0, 1, 1], #[0, 3, 4], 
      [0, 1, 1, 1, 0], #[1, 2, 3], 
      [0, 1, 1, 0, 1], #[1, 2, 4],
      [0, 1, 0, 1, 1], #[1, 3, 4],
      [0, 0, 1, 1, 1], #[2, 3, 4]]
      ]

    combinationsWith1GemCounts = [ 
      [2, 0, 0, 0, 0],#[0,0], 
      [0, 2, 0, 0, 0],#[1,1], 
      [0, 0, 2, 0, 0],#[2,2], 
      [0, 0, 0, 2, 0],#[3,3], 
      [0, 0, 0, 0, 2],#[4,4]]
      ]

    combinationsReturn1Gem = [
      [1, 0, 0, 0, 0],
      [0, 1, 0, 0, 0],
      [0, 0, 1, 0, 0],
      [0, 0, 0, 1, 0],
      [0, 0, 0, 0, 1],
      ]

    combinationsReturn2Gem = [
      [1, 1, 0, 0, 0],
      [1, 0, 1, 0, 0],
      [1, 0, 0, 1, 0],
      [1, 0, 0, 0, 1],
      [0, 1, 1, 0, 0],
      [0, 1, 0, 1, 0],
      [0, 1, 0, 0, 1],
      [0, 0, 1, 1, 0],
      [0, 0, 1, 0, 1],
      [0, 0, 0, 1, 1],
      [2, 0, 0, 0, 0],
      [0, 2, 0, 0, 0],
      [0, 0, 2, 0, 0],
      [0, 0, 0, 2, 0],
      [0, 0, 0, 0, 2],
      ]

    combinationsReturn3Gem = [
      [1, 1, 1, 0, 0],
      [1, 1, 0, 1, 0],
      [1, 1, 0, 0, 1],
      [1, 0, 1, 1, 0],
      [1, 0, 1, 0, 1],
      [1, 0, 0, 1, 1],
      [0, 1, 1, 1, 0],
      [0, 1, 1, 0, 1],
      [0, 1, 0, 1, 1],
      [0, 0, 1, 1, 1],
      [2, 1, 0, 0, 0],
      [2, 0, 1, 0, 0],
      [2, 0, 0, 1, 0],
      [2, 0, 0, 0, 1],
      [1, 2, 0, 0, 0],
      [0, 2, 1, 0, 0],
      [0, 2, 0, 1, 0],
      [0, 2, 0, 0, 1],
      [1, 0, 2, 0, 0],
      [0, 1, 2, 0, 0],
      [0, 0, 2, 1, 0],
      [0, 0, 2, 0, 1],
      [1, 0, 0, 2, 0],
      [0, 1, 0, 2, 0],
      [0, 0, 1, 2, 0],
      [0, 0, 0, 2, 1],
      [1, 0, 0, 0, 2],
      [0, 1, 0, 0, 2],
      [0, 0, 1, 0, 2],
      [0, 0, 0, 1, 2],
      [3, 0, 0, 0, 0],
      [0, 3, 0, 0, 0],
      [0, 0, 3, 0, 0],
      [0, 0, 0, 3, 0],
      [0, 0, 0, 0, 3],
      ]
    
    boardGemPiles = self.gameBoard.gemPiles
    playersGemPiles = self.gameBoard.players[self.gameBoard.currentPlayerIndex].gemPiles

    #Player can keep all gems
    if(sum(playersGemPiles) <= 7):
      for gemCombination in combinationWith3GemCounts:
        gemsLeft = [a_i - b_i for a_i, b_i in zip(boardGemPiles, gemCombination)]
        if sum(n < 0 for n in gemsLeft) == 0:        
          actions.append(TakeGemAction(tuple(gemCombination)))
      for gemType in range(5):
        if(boardGemPiles[gemType] >= 4):
          actions.append(TakeGemAction(tuple(combinationsWith1GemCounts[gemType])))

    #Player allready have 10 gems
    elif(sum(playersGemPiles) == 10): 
      self.nettoGemsTakenCombinations: set[tuple[int,int,int,int,int]] = set()
      #3 gems of different type
      for gemCombination in combinationWith3GemCounts:
        #is the gems on the board?
        gemsLeft = [a_i - b_i for a_i, b_i in zip(boardGemPiles, gemCombination)]
        if sum(n < 0 for n in gemsLeft) == 0:
            #Verify return Combinations is possible, playersGem + gemsTaken - gemsReturned > 0
            self.addRemoveCombinationsToActions(actions, gemCombination, playersGemPiles, combinationsReturn3Gem)

      #2 gems of same type
      for gemType in range(5):
        if (boardGemPiles[gemType] >= 4):
          self.addRemoveCombinationsToActions(actions, combinationsWith1GemCounts[gemType], playersGemPiles, combinationsReturn2Gem)
          
    #Player allready have 9 gems
    elif(sum(playersGemPiles) == 9): 
      self.nettoGemsTakenCombinations: set[tuple[int,int,int,int,int]] = set()
      #3 gems of different type
      for gemCombination in combinationWith3GemCounts:
        #is the gems on the board?
        gemsLeft = [a_i - b_i for a_i, b_i in zip(boardGemPiles, gemCombination)]
        if sum(n < 0 for n in gemsLeft) == 0:
            #Verify return Combinations is possible, playersGem + gemsTaken - gemsReturned > 0
            self.addRemoveCombinationsToActions(actions, gemCombination, playersGemPiles, combinationsReturn2Gem)

      #2 gems of same type
      for gemType in range(5):
        if (boardGemPiles[gemType] >= 4):
          self.addRemoveCombinationsToActions(actions, combinationsWith1GemCounts[gemType], playersGemPiles, combinationsReturn1Gem)

    #Player allready have 8 gems
    elif(sum(playersGemPiles) == 8): 
      self.nettoGemsTakenCombinations: set[tuple[int,int,int,int,int]] = set()
      #3 gems of different type
      for gemCombination in combinationWith3GemCounts:
        #is the gems on the board?
        gemsLeft = [a_i - b_i for a_i, b_i in zip(boardGemPiles, gemCombination)]
        if sum(n < 0 for n in gemsLeft) == 0:
            #Verify return Combinations is possible, playersGem + gemsTaken - gemsReturned > 0
            self.addRemoveCombinationsToActions(actions, gemCombination, playersGemPiles, combinationsReturn1Gem)

      #2 gems of same type
      for gemType in range(5):
        if(boardGemPiles[gemType] >= 4):
          actions.append(TakeGemAction(tuple(combinationsWith1GemCounts[gemType])))
  
    return actions

  def addRemoveCombinationsToActions(self, actions: list[Action], combinationWithCounts: list[int], playersGemPiles: list[int], combinationsReturn3Gem: list[list[int]]):
    
    gemsPlayerbeforeReturned = [a_i + b_i for a_i, b_i in zip(playersGemPiles, combinationWithCounts)]
    for gemReturnCombination in combinationsReturn3Gem:  
      gemsPlayerafterReturned = [a_i - b_i for a_i, b_i in zip(gemsPlayerbeforeReturned, gemReturnCombination)]
      if sum(n < 0 for n in gemsPlayerafterReturned) == 0:
        nettoGemsTaken: tuple[int,int,int,int,int] = tuple([a_i - b_i for a_i, b_i in zip(combinationWithCounts, gemReturnCombination)]) # type: ignore
        if(not (nettoGemsTaken in self.nettoGemsTakenCombinations)):
          self.nettoGemsTakenCombinations.add(nettoGemsTaken) # type: ignore
          actions.append(TakeGemAction(nettoGemsTaken))
