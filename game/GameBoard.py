from dataclasses import dataclass

from game.Player import Player
import numpy as np

@dataclass
class GameBoard():
  players: list[Player]
  currentPlayerIndex: int
  gemPiles: list[int]
  developmentCardTiers: list[np.ndarray[int, np.dtype[np.int32]]]
  developmentDeckTiersBoardIndexes: list[list[int]]
  nobles: np.ndarray[int, np.dtype[np.int32]]