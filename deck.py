import random

from card import Card
from constants import SUITS, RANKS


class Deck:
    def __init__(self) -> None:
        self.cards: list = []
        self.initialize_deck()
        self.shuffle()

    def initialize_deck(self):
        for suit in SUITS:
            for key, value in RANKS.items():
                card = Card(key, suit, value)
                self.cards.append(card)

    def shuffle(self):
        random.shuffle(self.cards)
