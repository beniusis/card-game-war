from deck import Deck
from player import Player
from constants import TEXT_COLORS


def get_the_name_of_the_first_player():
    try:
        name = input("Player 1 name: ").strip()
        if not name:
            raise ValueError
        return name
    except ValueError:
        print(f"\n{TEXT_COLORS["error"]}Player's name cannot be empty.\n{TEXT_COLORS["default"]}")
        return get_the_name_of_the_first_player()


def get_the_name_of_the_second_player():
    try:
        name = input("Player 2 name: ").strip()
        if not name:
            raise ValueError
        return name
    except ValueError:
        print(f"\n{TEXT_COLORS["error"]}Player's name cannot be empty.\n{TEXT_COLORS["default"]}")
        return get_the_name_of_the_second_player()


def initialize_players(name1, name2):
    deck = Deck()
    cards = deck.cards
    return Player(name1, cards[::2]), Player(name2, cards[1::2])

def draw_cards(p1, p2):
    return p1.draw_card(), p2.draw_card()
