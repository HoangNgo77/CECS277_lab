"""
Hero class for Dragon Trainer.

Inherits from Entity and provides two attack options:
- sword_attack: 2D6 damage
- arrow_attack: 1D12 damage
"""

import random
from entity import Entity


class Hero(Entity):
    """The player-controlled hero who fights dragons."""

    def sword_attack(self, dragon: Entity) -> str:
        """Deal 2D6 damage to the dragon.

        Args:
            dragon: Target entity to damage.

        Returns:
            A string describing the attack.
        """
        dmg = random.randint(1, 6) + random.randint(1, 6)
        dragon.take_damage(dmg)
        return f"You slash the {dragon.name} with your sword for {dmg} damage."

    def arrow_attack(self, dragon: Entity) -> str:
        """Deal 1D12 damage to the dragon.

        Args:
            dragon: Target entity to damage.

        Returns:
            A string describing the attack.
        """
        dmg = random.randint(1, 12)
        dragon.take_damage(dmg)
        return f"You hit the {dragon.name} with an arrow for {dmg} damage."
