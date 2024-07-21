from dataclasses import dataclass

@dataclass
class Player:
    gemStack: list[int]
    reserved: list[tuple[int,int]]