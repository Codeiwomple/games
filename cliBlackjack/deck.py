import random
from card import Card


class Deck:
    """A class to represent a standard single deck of 52 cards"""

    def __init__(self, bj_game):
        """Generate deck A-K S,C,H,D"""
        self.settings = bj_game.settings
        self.cards = [Card(suit, value) for suit in ["Spades", "Clubs", "Hearts", "Diamonds"]
                      for value in ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]]
        self.shuffle()

    def shuffle(self):
        if len(self.cards) > 1:
            random.shuffle(self.cards)

    def deal_card(self):
        """Return a single card and remove from deck."""
        if len(self.cards) > 1:
            return self.cards.pop(0)
