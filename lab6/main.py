"""
main.py
Authors: Phan Ngo - Lucas Seith
Date: 10/01/2025
Description:
A simple Yahtzee-like dice game. Each turn rolls three dice and checks for:
- Three-of-a-kind (+3 points)
- Series (e.g., 1-2-3, +2 points)
- Pair (+1 point)

Points are awarded for the highest applicable category only.
The game repeats until the user chooses to stop, then shows the final score.
"""

from player import Player
from check_input import get_yes_no


def take_turn(p: Player) -> None:
    """
    Play a single turn:
      - Roll and display dice
      - Check win types (3-kind, else series, else pair)
      - Display updated score
    """
    p.roll_dice()
    print(p)

    # Ensure no double-award: check strongest categories first.
    if p.has_three_of_a_kind():
        print("You got 3 of a kind!")
    elif p.has_series():
        print("You got a series of 3!")
    elif p.has_pair():
        print("You got a pair!")
    else:
        print("Aww.  Too Bad.")

    print(f"Score = {p.points}")


def main():
    print("-Yahtzee-\n")
    player = Player()

    # Loop until the user chooses to stop
    while True:
        take_turn(player)
        if not get_yes_no("Play again? (Y/N): "):
            break
        print()  # blank line between turns

    print("\nGame Over.")
    print(f"Final Score = {player.points}")


if __name__ == "__main__":
    main()
