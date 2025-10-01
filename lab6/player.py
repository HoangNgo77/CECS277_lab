"""
player.py
CECS 277,Lab 6 Yahtzee
Player class
"""

from die import Die


class Player:
    """
    A player holding three dice and a running point total.
    Attributes:
        _dice (list[Die]): three Die objects, always kept sorted ascending.
        _points (int): player's score.
    """

    def __init__(self):                     #Run coontructor

        #Construct and sort the three dice, then initialize points to 0.
        self._dice = [Die(), Die(), Die()]  # Make 3 dice by calling 3 time
        self._dice.sort()                   # Sort them from ASC order - dice.__lt__
        self._points = 0                    # Set point =0 beggining

    @property                               # Alias let us access points like attribute player.points instead of calling player.point()
    def points(self) -> int:
        return self._points                 #Return the player's current points.

    def roll_dice(self) -> None:
        
        #Roll all dice and sort them (ascending) afterward.
        for d in self._dice:                # Loop through the dice and call roll on each
            d.roll()
        self._dice.sort()                   # After rolling, sort the list again

    def has_pair(self) -> bool:
        """
        Return True if exactly two dice match (uses ==).
        Awards +1 point when True.
        """
        d1, d2, d3 = self._dice             # Unpack the three dice into d1, d2, d3
        pair = (d1 == d2) or (d2 == d3)
        if pair and not (d1 == d2 == d3):  # ensure not three-of-a-kind
            self._points += 1               # add 1 point
            return True                     
        return False                        #Otherwise return false          

    def has_three_of_a_kind(self) -> bool:
        """
        Return True if all three dice match (uses ==).
        Awards +3 points when True.
        """
        d1, d2, d3 = self._dice
        if d1 == d2 == d3:
            self._points += 3
            return True
        return False

    def has_series(self) -> bool:
        """
        Return True if dice form a sequence of length 3 (uses subtraction).
        Valid sequences for 3 six-sided dice: 1-2-3, 2-3-4, 3-4-5, 4-5-6.
        Awards +2 points when True.
        """
        d1, d2, d3 = self._dice
        # Because list is sorted, consecutive differences should be 1 and 1.
        if (d2 - d1) == 1 and (d3 - d2) == 1:
            self._points += 2
            return True
        return False

    def __str__(self) -> str:
        """
        Return in the format "D1=V1 D2=V2 D3=V3"
        (Calls Die.__str__() for each die).
        """
        d1, d2, d3 = self._dice
        return f"D1={str(d1)} D2={str(d2)} D3={str(d3)}"
