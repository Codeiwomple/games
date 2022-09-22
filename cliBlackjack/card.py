class Card:
    """A Class to represent a single playing card"""

    def __init__(self, suit, value):
        self.suit = suit
        self.value = value

    def __str__(self):
        """return string representation of a Card"""
        return f"{self.value} of {self.suit}"

    def __int__(self):
        if self.value == "A":
            return 11
        elif self.value in ["J", "Q", "K"]:
            return 10

        return int(self.value)
