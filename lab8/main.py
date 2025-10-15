"""
Rad Racer - main program loop

Builds a 3 x 100 track, places two obstacles per lane, shows the menu, asks the
player to choose a vehicle, then runs the race until all three vehicles finish.

Track symbols:
- '-' empty track
- '0' obstacle
- '*': previously occupied location(s)
- 'P' player's vehicle (whichever type)
- 'C', 'M', 'T' are opponents' initials for Car, Motorcycle, and Truck

Important details matched to the handout:
- 3 lanes (Car, Motorcycle, Truck)  100 units (pages 1–2).
- Two random obstacles per lane, not at start (0) or finish (99) (page 2).
- Opponents choose moves by weights: slow 40%, fast 30%, special 30%,
  but if energy < 5 they are forced to go slow (page 2).
- Use list.index('0', start) to find next obstacle, with ValueError handling (page 2).
- Place a '*' where a vehicle was, and put its initial at the new location (page 2).
- Keep and report 1st/2nd/3rd place (page 2).
- Do not place outside the list when a vehicle passes the finish (page 6, h).
"""

# from __future__ import annotations
import random
from typing import List, Tuple, Optional

from check_input import get_int_range
from car import Car
from motorcycle import Motorcycle
from truck import Truck
from vehicle import Vehicle

TRACK_LEN = 100        # visual track length (indices 0..99)
FINISH_POS = 99        # finish line index; positions may exceed this
LANE_NAMES = ("Car", "Motorcycle", "Truck")


def make_empty_track() -> List[List[str]]:
    """Return a 3 x 100 track filled with '-'."""
    return [['-'] * TRACK_LEN for _ in range(3)]


def place_obstacles(track: List[List[str]]) -> None:
    """Place exactly two '0' obstacles in each lane (not at 0 or 99)."""
    for lane in track:
        spots = random.sample(range(1, TRACK_LEN - 1), 2)
        for idx in spots:
            lane[idx] = '0'


def put_initials(track: List[List[str]], vehicles: List[Vehicle]) -> None:
    """Place each vehicle's initial at its current (drawn) location."""
    for lane_idx, v in enumerate(vehicles):
        draw_pos = min(v.position, TRACK_LEN - 1)
        track[lane_idx][draw_pos] = v.initial


def draw_turn(
    track: List[List[str]],
    vehicles: List[Vehicle],
    prev_positions: List[int],
    rammed_info: List[Tuple[bool, int, int]],
) -> None:
    """
    Update the track after a full turn:
    - Put a '*' at each vehicle's previous drawn location.
    - If a truck rammed, remove any obstacles it passed through.
    - Place initials at new positions (clamped to the last index).
    """
    # Stars at previous positions
    for lane_idx, prev in enumerate(prev_positions):
        track[lane_idx][min(prev, TRACK_LEN - 1)] = '*'

    # If a truck rammed, clear any '0' crossed this turn
    for lane_idx, (rammed, old_pos, new_pos) in enumerate(rammed_info):
        if rammed:
            lane = track[lane_idx]
            a = min(old_pos + 1, TRACK_LEN - 1)
            b = min(new_pos, TRACK_LEN - 1)
            for x in range(a, b + 1):
                if lane[x] == '0':
                    lane[x] = '-'

    # Place new initials
    put_initials(track, vehicles)


def print_header() -> None:
    print("Rad Racer!")
    print("Choose a vehicle and race it down the track (player = 'P'). "
          "Slow down for obstacles ('0') or else you'll crash!")


def print_descriptions() -> None:
    print("1. Lightning Car - a fast car. Speed: 7. Special: Nitro Boost (1.5x speed)")
    print("2. Swift Bike - a speedy motorcycle. Speed: 8. Special: Wheelie "
          "(2x speed but there's a chance you'll wipe out).")
    print("3. Behemoth Truck - a heavy truck. Speed: 6. Special: Ram "
          "(2x speed and it smashes through obstacles).")


def print_status(vehicles: List[Vehicle]) -> None:
    """Show each vehicle's status on its own line."""
    for v in vehicles:
        print(str(v))


def print_track(track: List[List[str]]) -> None:
    """Render all 3 lanes as strings (Car, Motorcycle, Truck order)."""
    for lane in track:
        print("".join(lane))


def next_obstacle(lane: List[str], after_pos: int) -> Optional[int]:
    """
    Return the index of the next '0' at or after after_pos+1; None if none exists.
    (Uses list.index per lab instructions; catches ValueError.)
    """
    try:
        return lane.index('0', min(after_pos + 1, TRACK_LEN - 1))
    except ValueError:
        return None


def choose_opponent_action(energy: int) -> int:
    """
    Weighted random action for opponents:
    1 = fast, 2 = slow, 3 = special.
    If 'out of energy' (energy < 5), they must go slow.
    """
    if energy < 5:
        return 2
    # 40% slow, 30% fast, 30% special
    return random.choices([2, 1, 3], weights=[0.4, 0.3, 0.3])[0]


def take_action(v: Vehicle, lane: List[str], action: int) -> Tuple[str, int, int, bool]:
    """
    Execute one move for a given vehicle.

    :return: (event_string, old_position, new_position, rammed_flag)
    """
    old_pos = v.position
    obs = next_obstacle(lane, old_pos)
    rammed = False

    if action == 1:
        event = v.fast(obs)
    elif action == 2:
        event = v.slow(obs)
    else:
        event = v.special_move(obs)
        # Truck rams through obstacles; flag so we can remove them on the lane
        if isinstance(v, Truck) and "rams forward" in event:
            rammed = True

    return event, old_pos, v.position, rammed


def finished(v: Vehicle) -> bool:
    """Has this vehicle reached/passed the finish line?"""
    return v.position >= FINISH_POS


def main() -> None:
    random.seed()  # you may set a fixed seed while testing

    print_header()
    print_descriptions()

    # --- Build track and obstacles ---
    track = make_empty_track()
    place_obstacles(track)

    # --- Build vehicles (P = player's chosen one) ---
    choice = get_int_range("Choose your vehicle (1-3): ", 1, 3)
    car = Car("Lightning Car", "P" if choice == 1 else "C", 7)
    bike = Motorcycle("Swift Bike", "P" if choice == 2 else "M", 8)
    truck = Truck("Behemoth Truck", "P" if choice == 3 else "T", 6)
    vehicles: List[Vehicle] = [car, bike, truck]

    # Put initials at the start
    put_initials(track, vehicles)

    finish_order: List[Vehicle] = []
    player_idx = choice - 1

    # --- Main race loop ---
    while len(finish_order) < 3:
        # Display current state
        print_status(vehicles)
        print_track(track)

        # Determine each vehicle's action for this turn
        actions = [None, None, None]  # 1=fast, 2=slow, 3=special

        # Player may be finished already (skip prompt)
        if not finished(vehicles[player_idx]):
            actions[player_idx] = get_int_range(
                "Choose action (1. Fast, 2. Slow, 3. Special Move): ", 1, 3
            )

        # Opponents choose weighted moves (or slow if out of energy)
        for i, v in enumerate(vehicles):
            if i == player_idx:
                continue
            if not finished(v):
                actions[i] = choose_opponent_action(v.energy)

        # Execute the moves in lane order (Car, Motorcycle, Truck)
        prev_positions = [v.position for v in vehicles]
        events: List[Optional[str]] = []
        rammed_info: List[Tuple[bool, int, int]] = []
        for lane_idx, v in enumerate(vehicles):
            if finished(v):
                events.append(None)
                rammed_info.append((False, prev_positions[lane_idx], v.position))
                continue
            event, old, new, rammed = take_action(v, track[lane_idx], actions[lane_idx])
            events.append(event)
            rammed_info.append((rammed, old, new))

        # Announce what happened this turn in the same order as the lanes
        for e in events:
            if e:
                print(e)

        # Update finish order (only when a vehicle crosses for the first time)
        for v in vehicles:
            if finished(v) and v not in finish_order:
                finish_order.append(v)

        # Update the track visuals for this turn
        draw_turn(track, vehicles, prev_positions, rammed_info)

    # --- Race complete: display results ---
    # Keep the final board visible, like in the example
    print_track(track)
    labels = ["1st place", "2nd place", "3rd place"]
    for label, v in zip(labels, finish_order):
        print(f"{label}: {v}")


if __name__ == "__main__":
    main()
