from blackjack.card import Card

class Hand:
    def __init__(self, bet=None, cards=None):
        self.bet = bet
        self.cards = cards or []

    def add_card(self, card: Card):
        self.cards.append(card)

    def get_value(self):
        total = 0
        for card in self.cards:
            value = card.value
            if isinstance(value, int):
                total += value
            elif value in ['J', 'Q', 'K']:
                total += 10
            elif value == 'A':
                total += 11
            else:
                raise Exception('Unknown card.')
        aces = [card for card in self.cards if card.value == 'A']
        for _ in aces:
            if total > 21:
                total -= 10
        return total

    def inspect_card(self):
        return self.cards[1].value

    def get_cards(self):
        return [card.value for card in self.cards]

    def check_hand(self, other_hand):
        if self.get_value() > other_hand.get_value():
            return 1
        elif self.get_value == other_hand.get_value():
            return 0
        else:
            return -1
