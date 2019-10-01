from blackjack.hand import Hand
from blackjack.shoe import Shoe

VALID_CARDS = [2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K', 'A']

class State:
    def __init__(self, starting_chips=1000, number_decks=6, percent_to_use=0.8):
        self.player_chips = starting_chips
        self.shoe = Shoe(number_decks=number_decks, percent_to_use=percent_to_use)
        self.player_hand = Hand()
        self.dealer_hand = Hand()
        self.bet = None

    def deal(self, bet):
        if bet > self.player_chips:
            raise Exception(f'Insufficient chips to place bet of {bet} chips.')
        self.player_hand = Hand(bet=bet)
        self.dealer_hand = Hand()
        self.bet = bet
        self.player_chips -= bet
        self.player_hand.add_card(self.shoe.deal_card())
        self.dealer_hand.add_card(self.shoe.deal_card())
        self.player_hand.add_card(self.shoe.deal_card())
        self.dealer_hand.add_card(self.shoe.deal_card())

    def inspect_dealers_hand(self):
        return self.dealer_hand.inspect_card()

    def hit(self):
        self.player_hand.add_card(self.shoe.deal_card())

    def dealer_play(self):
        print(f'Dealer shows {self.dealer_hand.get_cards()}')
        while self.dealer_hand.get_value() <= 17:
            # Dealer hits soft 17
            if self.dealer_hand.get_value() == 17 \
                    and len(self.dealer_hand.get_cards()) == 2 \
                    and 'A' in self.dealer_hand.get_cards():
                break
            self.dealer_hand.add_card(self.shoe.deal_card())
        print(f'Dealer ends up with {self.dealer_hand.get_cards()}. (Total={self.dealer_hand.get_value()})')

    def play(self, bet):
        if not self.shoe.is_shoe_open():
            self.shoe.reset_shoe()
            print('Shuffling shoe.')
        self.deal(bet)
        dealer_card = self.inspect_dealers_hand()
        action = None
        while action not in ['stand', 'bust']:
            print(f'Dealer is showing: {dealer_card}.')
            player_cards = self.player_hand.get_cards()
            print(f'You have: {player_cards}. (Total={self.player_hand.get_value()})')
            action = input('Hit or Stand?')
            if action == 'hit':
                self.hit()
            if self.player_hand.get_value() > 21:
                action = 'bust'
        if action != 'bust':
            self.dealer_play()

        # Check result
        if action == 'bust':
            print('You busted!')
        else:
            result = self.player_hand.check_hand(self.dealer_hand)
            if result > 0:
                print('You won!')
                self.player_chips += (self.player_hand.bet * 2)
            elif result == 0:
                print('Push.')
                self.player_chips += self.player_hand.bet
            else:
                print('You lost.')
