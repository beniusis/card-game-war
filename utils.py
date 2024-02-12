from card import Card
from constants import SUITS, RANKS


def get_the_names_of_the_players():
    player_one_name = input("Player's 1 name: ").strip()
    player_two_name = input("Player's 2 name: ").strip()
    return player_one_name, player_two_name


def initialize_deck():
    cards = []
    for suit in SUITS:
        for key, value in RANKS.items():
            card = Card(key, suit, value)
            cards.append(card)
    return cards
