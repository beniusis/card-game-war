from deck import Deck
from card import Card
from player import Player
from constants import SUITS, RANKS


def get_the_names_of_the_players():
    player_one_name = input("Player's 1 name: ").strip()
    player_two_name = input("Player's 2 name: ").strip()
    return player_one_name, player_two_name

def initialize_players(name1, name2):
    deck = Deck()
    cards = deck.cards

    return Player(name1, cards[::2]), Player(name2, cards[1::2])
