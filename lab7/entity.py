"""
Entity base class.
Description:
  Base class for all combatants in Dragon Trainer. Tracks name and hit points.
"""

class Entity:
    """A living thing with a name and hit points.

    Attributes:
        _name (str): The entity's display name.
        _max_hp (int): Maximum hit points.
        _hp (int): Current hit points.
    """

    def __init__(self, name: str, max_hp: int) -> None:
        """Initialize an Entity with a name and maximum HP.

        Args:
            name: Display name.
            max_hp: The maximum and starting HP for the entity (must be > 0).
        """
        if max_hp <= 0:
            raise ValueError("max_hp must be positive.")
        self._name = name
        self._max_hp = int(max_hp)
        self._hp = int(max_hp)

    @property
    def name(self) -> str:
        """Read-only name property."""
        return self._name

    @property
    def hp(self) -> int:
        """Read-only current HP property."""
        return self._hp

    def take_damage(self, dmg: int) -> None:
        """Apply damage to this entity, clamping at zero.

        Args:
            dmg: Non-negative integer amount of damage to apply.
        """
        if dmg < 0:
            raise ValueError("dmg must be non-negative")
        self._hp -= int(dmg)
        if self._hp < 0:
            self._hp = 0

    def __str__(self) -> str:
        """Return "Name: hp/max_hp" for menus."""
        return f"{self._name}: {self._hp}/{self._max_hp}"
