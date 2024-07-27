from dataclasses import dataclass

from game.Player import Player
import numpy as np
import numpy.typing as npt

@dataclass
class GameBoard():
  players: list[Player]
  currentPlayerIndex: int
  gemPiles: npt.NDArray[np.int64]
  developmentCardTiers: list[np.ndarray[int, np.dtype[np.int32]]]
  developmentDeckTiersBoardIndexes: list[list[int]]
  nobles: np.ndarray[int, np.dtype[np.int32]]

  def deepCopy(self):
    players: list[Player] = []
    for player in self.players:
      players.append(player.deepCopy())
    currentPlayerIndex = self.currentPlayerIndex
    gemPiles = self.gemPiles.copy()
    developmentCardTiers = self.developmentCardTiers.copy()
    developmentDeckTiersBoardIndexes = self.developmentDeckTiersBoardIndexes.copy()
    nobles = np.array(self.nobles)

    return GameBoard(players, currentPlayerIndex, gemPiles, developmentCardTiers, developmentDeckTiersBoardIndexes, nobles)