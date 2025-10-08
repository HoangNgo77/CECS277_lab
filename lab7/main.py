"""
Dragon Trainer  CECS 277 Lab 7
Authors:  Phan Ngo - Lucas Seith
Date: 2025-10-08

Gameplay:
- Create a Hero and three dragons (base, fire, flying).
- Player repeatedly chooses a living dragon and an attack (arrow/sword).
- A random living dragon retaliates with a random attack (basic/special).
- Game ends when all dragons are slain or the hero is knocked out.
"""
import random
from typing import List

from hero import Hero
from dragon import Dragon
from fire import FireDragon
from flying import FlyingDragon
from check_input import get_int_range


def show_roster(hero: Hero, dragons: List[Dragon]) -> None:
    print(f"\n{hero}")
    for idx, d in enumerate(dragons, start=1):
        # Each dragon prints its own status; subclasses append their charges.
        print(f"{idx}. Attack {d}")


def choose_dragon(dragons: List[Dragon]) -> int:
    return get_int_range("Choose a dragon to attack: ", 1, len(dragons)) - 1


def choose_weapon() -> int:
    print("Attack with:") 
    print("1. Arrow (1 D12)")
    print("2. Sword (2 D6)")
    return get_int_range("Enter weapon: ", 1, 2)


def hero_turn(hero: Hero, dragons: List[Dragon]) -> str:
    idx = choose_dragon(dragons)
    weapon = choose_weapon()
    target = dragons[idx]
    if weapon == 1:
        msg = hero.arrow_attack(target)
    else:
        msg = hero.sword_attack(target)

    # Remove dragon if defeated
    defeated = ""
    if target.hp == 0:
        defeated = f"\nYou defeated the {target.name}!"
        dragons.pop(idx)

    return msg + defeated


def dragon_turn(hero: Hero, dragons: List[Dragon]) -> str:
    if not dragons:
        return ""
    # pick a living dragon at random
    d = random.choice(dragons)
    # choose attack: 0 -> basic, 1 -> special
    if random.randint(0, 1) == 0:
        return d.basic_attack(hero)
    else:
        return d.special_attack(hero)


def game_over(hero: Hero, dragons: List[Dragon]) -> bool:
    return hero.hp == 0 or not dragons


def main() -> None:
    print("What is your name, challenger?")
    name = input().strip() or "Hero"
    hero = Hero(name, 50)

    # Create one of each dragon type
    dragons = [
        Dragon("Deadly Nadder", 10),
        FireDragon("Gronckle", 15),
        FlyingDragon("Timberjack", 20),
    ]

    print(f"Welcome to dragon training, {hero.name}")
    print("You must defeat 3 dragons.")

    # Main game loop
    while True:
        show_roster(hero, dragons)
        # Player turn
        player_msg = hero_turn(hero, dragons)
        print(player_msg)

        if game_over(hero, dragons):
            break

        # Dragon turn
        enemy_msg = dragon_turn(hero, dragons)
        print(enemy_msg)

        if game_over(hero, dragons):
            break

    # End screen
    if hero.hp == 0:
        print(f"\n{hero.name} collapses... The dragons remain unbeaten.")
    else:
        print("\nCongratulations! You have defeated all 3 dragons, you have passed the trials.")


if __name__ == "__main__":
    main()
