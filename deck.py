import random
from card import Card
from constants import SUITS, RANKS


class Deck:
    def __init__(self):
        self.cards: list = []
        self.initialize_deck()
        self.shuffle()

    def initialize_deck(self):
        for suit in SUITS:
            for rank, value in RANKS.items():
                card = Card(rank, suit, value)
                self.cards.append(card)

    def shuffle(self):
        random.shuffle(self.cards)
