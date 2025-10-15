"""
CECS 277 – Lab 8 – Abstract Classes
Rad Racer — Vehicle base class
Authors: Phan Ngo - Lucas Seith
Date: 10/14/25
Description:
    Abstract base class for all race vehicles. Implements common attributes,
    properties, and shared movement methods (fast/slow). Each subclass must
    override the special_move method.

Notes per spec:
- Attributes (no extras): _name, _initial, _speed, _position, _energy
- Properties for: initial, position, energy
- __init__ sets position to 0 and energy to 100
- fast(): costs 5 energy when available; random speed±1; crashes on obstacles
- slow(): 50% speed±1; dodges obstacles (never crashes)
- __str__ shows name, position, and energy
- special_move(): abstract (decorated)
"""

#from __future__ import annotations
from abc import ABC, abstractmethod
import random


class Vehicle(ABC):
    """Abstract base class for Car, Motorcycle, and Truck."""

    def __init__(self, name: str, initial: str, speed: int) -> None:
        """
        Set attributes based on parameters. Start at position 0, energy 100.

        :param name: Display name of the vehicle
        :param initial: Single-character label used on the track
        :param speed: Base speed (integer)
        """
        self._name = name
        self._initial = initial
        self._speed = speed
        self._position = 0
        self._energy = 100

    # --- required properties (getters only) ---
    @property
    def initial(self) -> str:
        """Vehicle's label shown on the track ('P', 'C', 'M', or 'T')."""
        return self._initial

    @property
    def position(self) -> int:
        """Vehicle's current location measured in units from the start."""
        return self._position

    @property
    def energy(self) -> int:
        """Vehicle's remaining energy."""
        return self._energy

    # --- shared movement methods ---
    def fast(self, obs_loc: int | None) -> str:
        """
        Move at speed±1 if energy >= 5 (deduct 5); otherwise move 1.
        If the randomized move would hit the next obstacle, crash and stop on it.

        :param obs_loc: index of next obstacle ahead in this lane, or None
        :return: event description string
        """
        if self._energy >= 5:
            self._energy -= 5
            move = max(1, random.randint(self._speed - 1, self._speed + 1))
            # Crash if we would reach or pass the obstacle this step
            if obs_loc is not None and self._position < obs_loc <= self._position + move:
                self._position = obs_loc
                return f"{self._name} CRASHED into an obstacle!"
            else:
                self._position += move
                return f"{self._name} quickly moves {move} units!"
        else:
            self._position += 1
            return (
                f"{self._name} tries to go fast, but is all out of energy and only moves 1 unit!"
            )

    def slow(self, obs_loc: int | None) -> str:
        """
        Move at 50% speed±1 (no energy cost). If this step would cross an obstacle,
        the vehicle 'maneuvers around it' and does not crash.

        :param obs_loc: index of next obstacle ahead in this lane, or None
        :return: event description string
        """
        base = round(self._speed * 0.5)
        move = max(1, random.randint(max(0, base - 1), base + 1))
        self._position += move
        if obs_loc is not None and self._position - move < obs_loc <= self._position:
            return f"{self._name} slowly dodges the obstacle and moves {move} units!"
        return f"{self._name} slowly moves {move} units!"

    def __str__(self) -> str:
        """Nicely formatted status string for this vehicle."""
        return f"{self._name} [Position - {self._position}, Energy - {self._energy}]"

    # --- abstract method to be implemented by each subclass ---
    @abstractmethod
    def special_move(self, obs_loc: int | None) -> str:
        """Perform the vehicle's special move."""
        raise NotImplementedError
