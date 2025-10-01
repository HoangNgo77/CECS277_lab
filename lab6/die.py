"""
die.py
CECS 277 Lab 6 Yahtzee
Die class
"""

import random


class Die:
    """
    A single die with N sides (default 6).
    Attributes:
        _sides (int): number of sides (>= 2).
        _value (int): last rolled value (1.._sides).
    """

    def __init__(self, sides: int = 6):
        """
        Initialize the die with a number of sides and immediately roll it.
        Args:
            sides (int): number of sides (>= 2). Default 6.
        """
        if sides < 2:
            raise ValueError("Die must have at least 2 sides.")
        self._sides = sides
        self._value = 0
        self.roll()

    def roll(self) -> int:
        
        #Roll the die to a random value in [1, _sides] and return it.
        
        self._value = random.randint(1, self._sides)
        return self._value

    def __str__(self) -> str:
        return str(self._value)             #Return the die's value as a string.

    def __lt__(self, other: "Die") -> bool:  
        return self._value < other._value   #True if this die's value is less than the other die's value.

    def __eq__(self, other: object) -> bool:
        #True if this die's value equals the other die's value.
        if not isinstance(other, Die):
            return NotImplemented
        return self._value == other._value

    def __sub__(self, other: "Die") -> int:   
        return self._value - other._value   #Return the difference between this die's value and the other's.
