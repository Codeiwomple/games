import os

from settings import Settings
from deck import Deck
from player import Player


class Blackjack:
    def __init__(self):
        """Set up required components to make game run"""
        self.settings = Settings()

        self.display_welcome()

        # Create deck
        self.deck = Deck(self)
        # Create Dealer
        self.dealer = Player(self, dealer=True)

        # Create a list of players
        num_players = int(input("Enter number of players: "))
        self.active_players = []
        for i in range(num_players):
            self.active_players.append(Player(self, i + 1))

        # Show balances
        self.display_player_balances()

    def run_game(self):
        game_is_live = True

        while game_is_live:
            # Get player bets
            self.place_initial_bets()

            # Deal
            self.deal_hand()
            self.display_table()

            # Play hands
            for player in self.active_players:
                self.play_hand(player)

            # Evaluate hands
            self.evaluate_hands()

            # remove losing players
            self.remove_players()
            if not len(self.active_players):
                game_is_live = False
                print("All players are out")
                continue

            # Reset for next hand
            self.clear_table()

    def clear_screen(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    def remove_players(self):
        """Remove any players whos balance falls below min bet"""

        for player in self.active_players:
            if player.balance < self.settings.min_bet:
                self.active_players.remove(player)

    def display_welcome(self):
        self.clear_screen()
        print(self.settings.welcome_message)

    def clear_table(self):
        """Reset the teable for another hand"""
        # TODO
        # Come back and impliment shuffle when deck get within number of cards left
        # Clear the screen
        self.clear_screen()
        # Clear dealers cards
        self.dealer.hand.clear_cards()
        # Clear players cards
        for player in self.active_players:
            player.hand.clear_cards()

    def display_player_balances(self):
        """Prints all active players balances to screen"""
        for player in self.active_players:
            print(f"Seat {player.seat_num} has {player.balance}")

    def place_initial_bets(self):
        """Give each player the oppertunity to bet before initial draw"""
        for player in self.active_players:
            bet_accepted = False

            while not bet_accepted:
                bet = int(input(
                    f"Seat {player.seat_num}, your balance is {player.balance}, place your bet:"))

                if bet < self.settings.min_bet:
                    print(f"The minimum bet is {self.settings.min_bet}")
                    continue
                elif bet > self.settings.max_bet:
                    print(f"The maximum bet is {self.settings.min_bet}")
                    continue
                elif bet > player.balance:
                    print(f"You do not have sufficient balance for this bet")
                    continue

                player.bet = bet
                player.bet_live = True
                bet_accepted = True

    def deal_hand(self):
        """Deals out the initial set of cards to players"""
        self.display_linebreak()
        print("Dealing...")
        self.display_linebreak()

        for i in range(2):
            for player in self.active_players:
                player.hand.add_card(self.deck.deal_card())

            self.dealer.hand.add_card(self.deck.deal_card())

    def play_hand(self, player):
        """Function to play the players hand"""
        hand_is_live = True

        # Check players cards for blackjack
        if player.hand.has_blackjack():
            print("Player has BLACKJACK!")
            # If dealer is not showing a 10 or A, pay
            if int(self.dealer.hand.get_hand()[1]) < 10:
                self.payout_bet(player)
        else:
            while hand_is_live:
                if self.get_player_choice(player) in ['hit', 'h']:
                    # Deal player another card
                    player.hand.add_card(self.deck.deal_card())
                    if player.hand.is_bust():
                        print(f"{str(player.hand)} Player has BUST!")
                        self.collect_bet(player)
                        hand_is_live = False
                        break
                    else:
                        print(f"{str(player.hand)}")
                        continue
                else:
                    # Player has stuck
                    # Display cards and move onto dealer
                    print("Player Stuck")
                    print(f"{str(player.hand)}")
                    break
        self.display_linebreak()

    def play_dealers_hand(self):
        """Play the dealers hand"""
        hand_is_live = True

        print("Dealer playing...")
        self.display_dealer_cards(dealer_hidden=False)

        if self.dealer.hand.has_blackjack():
            print("Dealer has BLACKJACK!")
        else:
            while hand_is_live:
                if self.dealer.hand.value < self.settings.dealer_stick_value:
                    # Draw new card for dealer
                    print(
                        f"Dealer has {str(self.dealer.hand)}, dealing new card...")
                    self.dealer.hand.add_card(self.deck.deal_card())
                    if self.dealer.hand.is_bust():
                        print("Dealer BUST!")
                        print(str(self.dealer.hand))
                        hand_is_live = False
                        self.dealer.hand.value = 0
                        break
                    else:
                        print(str(self.dealer.hand))
                        continue
                else:
                    # Dealer sticks
                    print("Dealer sticks")
                    print(str(self.dealer.hand))
                    break

    def payout_bet(self, player):
        """Player won, pay bet"""
        player.balance += player.bet
        print(
            f"Seat {player.seat_num} won {player.bet}, balance {player.balance}!")
        player.bet_live = False

    def collect_bet(self, player):
        """Player lost, collect his bet"""
        player.balance -= player.bet
        print(
            f"Seat {player.seat_num} lost {player.bet}, balance {player.balance}")
        player.bet_live = False

    def push_bet(self, player):
        """Player hand equal to dealer so return bet"""
        player.bet = 0
        player.bet_live = False
        print(
            f"Seat {player.seat_num} push {player.bet}, balance {player.balance}")

    def evaluate_hands(self):
        """Evaluate the players hands in comparison to the dealers"""
        self.play_dealers_hand()
        self.display_table(dealer_hidden=False)

        # Payout/ collect bets
        for player in self.active_players:
            if player.bet_live:
                if player.hand.value > self.dealer.hand.value:
                    # Player wins, pay bet
                    self.payout_bet(player)
                elif player.hand.value == self.dealer.hand.value:
                    self.push_bet(player)
                else:
                    # Player lost, collect bet
                    self.collect_bet(player)
        input("Press Enter to begin next hand")

    def display_table(self, dealer_hidden=True):
        """Print the table/ all current hands to screen"""
        self.display_linebreak()
        # Display dealers cards
        self.display_dealer_cards(dealer_hidden)

        # Display players cards
        for player in self.active_players:
            self.display_player_cards(player)
        self.display_linebreak()

    def display_linebreak(self):
        """Line break to make output more readable"""
        print("*******************************************")

    def display_dealer_cards(self, dealer_hidden=True):
        """Print the dealers cards to screen"""
        if dealer_hidden:
            print(
                f"The dealers cards are: Hidden + {self.dealer.hand.get_hand()[1]}")
        else:
            print(f"The dealers cards are: {str(self.dealer.hand)}")

    def display_player_cards(self, player):
        """Prints the player instances cards to screen"""
        print(
            f"Seat {player.seat_num} cards are: {str(player.hand)}")

    def get_player_choice(self, player):
        """Get input from the player on how they want to play their hand"""
        print(f"Seat {player.seat_num} it is your turn: ")

        # Display dealer and players cards to player
        self.display_dealer_cards()
        self.display_player_cards(player)

        choice = input("Please choose Hit (h) or Stick (s) ").lower()
        while choice not in ["h", "s", "hit", "stick"]:
            choice = input("Please enter 'hit' or 'stick' (or h/s)").lower()
        return choice


if __name__ == '__main__':
    bj = Blackjack()
    bj.run_game()
