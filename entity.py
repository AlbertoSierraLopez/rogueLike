from typing import Tuple


class Entity:
    """
    A generic object to represent players, enemies, items ...
    """
    def __init__(self, x: int, y: int, char: str, color: tuple[int, int, int]):
        self.x = x
        self.y = y
        self.char = char
        self.color = color

    def move(self, dx: int, dy: int):
        # Move the entity a given amount
        self.x += dx
        self.y += dy