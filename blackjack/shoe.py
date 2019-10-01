import random

from blackjack.card import VALID_CARDS, Card

class Shoe:
    def __init__(self, number_decks=6, percent_to_use=0.8):
        self.number_decks = number_decks
        self.percent_to_use = percent_to_use
        self.cards = []
        self.reset_shoe()

    def reset_shoe(self):
        self.cards = [Card(card) for card in VALID_CARDS * 4 * self.number_decks]
        random.shuffle(self.cards)

    def is_shoe_open(self):
        percent_used = 1 - (len(self.cards) / self.number_decks * 52)
        return percent_used < self.percent_to_use

    def deal_card(self):
        return self.cards.pop()
