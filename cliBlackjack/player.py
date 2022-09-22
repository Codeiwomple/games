from settings import Settings
from hand import Hand


class Player:
    def __init__(self, bj_game, seat_num=0, dealer=False):
        self.settings = bj_game.settings
        self.balance = self.settings.player_start_balance
        self.seat_num = seat_num
        self.bet = 0
        self.bet_live = False

        self.dealer = dealer
        self.hand = Hand(dealer=self.dealer)
