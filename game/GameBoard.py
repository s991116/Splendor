from dataclasses import dataclass

import pandas as pd
from game.Player import Player
from game.GemType import GemType
from typing import Dict

@dataclass
class GameBoard():
  players: list[Player]
  currentPlayerIndex: int
  gemPiles: Dict[GemType, int]
  tier1: pd.DataFrame
  tier2: pd.DataFrame
  tier3: pd.DataFrame
  nobles: pd.DataFrame