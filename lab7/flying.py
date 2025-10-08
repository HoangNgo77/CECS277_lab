"""
FlyingDragon, specialized Dragon that can swoop a limited number of times.
"""

import random
from dragon import Dragon
from entity import Entity


class FlyingDragon(Dragon):
    """A dragon that can perform limited swoop attacks."""

    def __init__(self, name: str, hp: int) -> None:
        super().__init__(name, hp)
        self._swoops = 3  # default number of swoops

    def special_attack(self, hero: Entity) -> str:
        """Overridden swoop attack (5-8 damage) if swoops remain; otherwise fail."""
        if self._swoops > 0:
            dmg = random.randint(5, 8)
            self._swoops -= 1
            hero.take_damage(dmg)
            return f"{self.name} dive-bombs you in a vicious swoop for {dmg} damage!"
        else:
            return f"{self.name} tries to swoop you but is too winded to get airborne."

    def __str__(self) -> str:
        base = super().__str__()
        return f"{base}\nSwoop attacks remaining: {self._swoops}"
