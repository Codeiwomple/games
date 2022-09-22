class Hand:
    def __init__(self, dealer=False):
        self.dealer = dealer
        self.cards = []
        self.value = 0

    def __str__(self):
        return f"{[str(c) for c in self.cards]} Value: {self.value}"

    def get_hand(self):
        """Returns player instances current hand"""
        return self.cards

    def clear_cards(self):
        self.cards = []

    def add_card(self, card):
        # Append a card to the hand
        self.cards.append(card)
        # Update the value of the hand
        self.calculate_value()

    def calculate_value(self):
        self.value = 0
        has_ace = False
        for card in self.cards:
            if card.value.isnumeric():
                self.value += int(card.value)
            else:
                if card.value == "A":
                    has_ace = True
                    self.value += 11
                else:
                    self.value += 10

        if has_ace and self.value > 21:
            self.value -= 10

    def has_blackjack(self):
        if self.value == 21:
            return True
        return False

    def is_bust(self):
        if self.value > 21:
            return True
        return False
