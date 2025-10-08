"""
FireDragon – specialized Dragon that can breathe fire a limited number of times.
"""

import random
from dragon import Dragon
from entity import Entity


class FireDragon(Dragon):
    """A dragon that can use a limited number of fire shots."""

    def __init__(self, name: str, hp: int) -> None:
        super().__init__(name, hp)
        self._fire_shots = 2  # default number of fire shots

    def special_attack(self, hero: Entity) -> str:
        """Overridden fire attack (6-9 damage) if shots remain; otherwise fail."""
        if self._fire_shots > 0:
            dmg = random.randint(6, 9)
            self._fire_shots -= 1
            hero.take_damage(dmg)
            return f"{self.name} engulfs you in flames for {dmg} damage!"
        else:
            return f"{self.name} tries to spit fire at you but is all out of fire shots."

    def __str__(self) -> str:
        base = super().__str__()
        return f"{base}\nFire Shots remaining: {self._fire_shots}"
