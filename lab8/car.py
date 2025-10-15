"""
Car class — Nitro Boost (1.5x speed ±1, costs 15 energy; crashes on obstacles)
"""

import random
from vehicle import Vehicle

class Car(Vehicle):
    """Car with Nitro Boost special move."""

    def special_move(self, obs_loc: int | None) -> str:
        """
        If energy >= 15, deduct 15 and move at ~1.5x speed (±1).
        If an obstacle is in range, crash and stop on it. Otherwise, move full amount.
        If not enough energy, move 1 space.
        """
        if self._energy >= 15:
            self._energy -= 15
            base = round(self._speed * 1.5)
            move = max(1, random.randint(max(0, base - 1), base + 1))
            if obs_loc is not None and self._position < obs_loc <= self._position + move:
                self._position = obs_loc
                return f"{self._name} uses nitro boost but CRASHES into an obstacle!"
            self._position += move
            return f"{self._name} uses nitro boost and moves {move} units!"
        else:
            self._position += 1
            return f"{self._name} tries to use nitro boost, but is all out of energy!"
