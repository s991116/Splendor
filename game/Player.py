from dataclasses import dataclass

from game.GemType import GemType

@dataclass
class Player:
    gemStack: dict[GemType, int]