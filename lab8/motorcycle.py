"""
Motorcycle class — overrides slow() and has Wheelie special (2x speed ±1, 75% success,
costs 15 energy; on success it can still crash if an obstacle is in range).
"""

import random
from vehicle import Vehicle


class Motorcycle(Vehicle):
    """Motorcycle with better 'slow' and a risky Wheelie special move."""

    def slow(self, obs_loc: int | None) -> str:
        """
        Move at 75% speed ±1 (no energy cost). 'Dodges' obstacles if encountered.
        """
        base = round(self._speed * 0.75)
        move = max(1, random.randint(max(0, base - 1), base + 1))
        self._position += move
        if obs_loc is not None and self._position - move < obs_loc <= self._position:
            return f"{self._name} slowly dodges the obstacle and moves {move} units!"
        return f"{self._name} slowly moves {move} units!"

    def special_move(self, obs_loc: int | None) -> str:
        """
        If energy >= 15, deduct 15, then 75% chance to move at 2x speed ±1,
        else 'fall over' and only move 1. On a successful wheelie, if an obstacle
        is within range, crash and stop on it; otherwise move full amount.
        If energy < 15, move 1.
        """
        if self._energy >= 15:
            self._energy -= 15
            if random.random() < 0.75:
                base = 2 * self._speed
                move = max(1, random.randint(max(0, base - 1), base + 1))
                if obs_loc is not None and self._position < obs_loc <= self._position + move:
                    self._position = obs_loc
                    return f"{self._name} pops a wheelie but CRASHES into an obstacle!"
                self._position += move
                return f"{self._name} pops a wheelie and moves {move} units!!"
            else:
                self._position += 1
                return f"{self._name} tries a wheelie, but falls over and only moves 1 unit!"
        else:
            self._position += 1
            return f"{self._name} tries a wheelie, but is all out of energy!"
