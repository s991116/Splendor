from dataclasses import dataclass
import pandas as pd

from game.GemType import GemType

@dataclass
class Player:
    gemStack: dict[GemType, int]
    reserved: pd.DataFrame