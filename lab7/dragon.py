"""
Base Dragon class for Dragon Trainer.
Inherits from Entity and provides shared dragon attacks.
"""

import random
from entity import Entity


class Dragon(Entity):
    """A generic dragon with a basic and a special attack."""

    def basic_attack(self, hero: Entity) -> str:
        """Tail attack dealing 2-5 damage.

        Returns:
            Description string of the attack.
        """
        dmg = random.randint(2, 5)
        hero.take_damage(dmg)
        return f"{self.name} smashes you with its tail for {dmg} damage!"

    def special_attack(self, hero: Entity) -> str:
        """Claw attack dealing 3-7 damage.

        Returns:
            Description string of the attack.
        """
        dmg = random.randint(3, 7)
        hero.take_damage(dmg)
        return f"{self.name} slashes you with its claws for {dmg} damage!"
