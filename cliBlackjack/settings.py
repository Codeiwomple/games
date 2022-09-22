class Settings:
    """A Class to store the settings for cliBlackjack"""

    def __init__(self):
        self.player_start_balance = 100
        self.min_bet = 10
        self.max_bet = 50
        self.dealer_stick_value = 17
        self.max_players = 2

        self.welcome_message = f"Welcome to cliBlackjack, Dealer sticks on {self.dealer_stick_value}, Min bet: {self.min_bet} Max bet: {self.max_bet}"
