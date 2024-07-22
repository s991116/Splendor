from dataclasses import dataclass

@dataclass
class Player:
    gemPiles: list[int]
    reserved: list[tuple[int,int]]

    def deepCopy(self):
        gemPiles = self.gemPiles.copy()
        reserved = self.reserved.copy()

        return Player(gemPiles, reserved)