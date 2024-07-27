from dataclasses import dataclass
import numpy as np
import numpy.typing as npt

@dataclass
class Player:
    gemPiles: npt.NDArray[np.int64]
    reserved: list[tuple[int,int]]
    developmentCards: list[tuple[int,int]]
    developmentValues: npt.NDArray[np.int64]

    def deepCopy(self):
        gemPiles = self.gemPiles.copy()
        reserved = self.reserved.copy()
        cards = self.developmentCards.copy()
        developmentValues = self.developmentValues.copy()
        return Player(gemPiles, reserved, cards, developmentValues)