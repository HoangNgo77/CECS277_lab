"""
Truck class — Ram special (2x speed, costs 15 energy; bashes through obstacles).
"""

from vehicle import Vehicle


class Truck(Vehicle):
    """Truck whose special move rams forward (smashes through obstacles)."""

    def special_move(self, obs_loc: int | None) -> str:
        """
        If energy >= 15, deduct 15 and move 2x speed regardless of obstacles.
        (Main removes any obstacles crossed during this move.)
        If insufficient energy, move 1.
        """
        if self._energy >= 15:
            self._energy -= 15
            move = 2 * self._speed
            self._position += move
            return f"{self._name} rams forward {move} units!"
        else:
            self._position += 1
            return f"{self._name} tries to ram forward, but is all out of energy!"
