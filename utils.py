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
        print(
            f"\n{TEXT_COLORS['error']}Player's name cannot be empty.\n{TEXT_COLORS['default']}"
        )
        return get_the_name_of_the_first_player()


def get_the_name_of_the_second_player():
    try:
        name = input("Player 2 name: ").strip()
        if not name:
            raise ValueError
        return name
    except ValueError:
        print(
            f"\n{TEXT_COLORS['error']}Player's name cannot be empty.\n{TEXT_COLORS['default']}"
        )
        return get_the_name_of_the_second_player()


def initialize_players(name1, name2):
    deck = Deck()
    return Player(name1, deck.cards[::2]), Player(name2, deck.cards[1::2])


def draw_cards(p1, p2):
    return p1.draw_card(), p2.draw_card()


def play_round(p1, p2):
    card1, card2 = draw_cards(p1, p2)
    if card1.value > card2.value:
        p1.add_cards(Player.pile + [card1, card2])
        Player.pile = []
        print(f"{p1.name} wins!")
    elif card1.value < card2.value:
        p2.add_cards(Player.pile + [card1, card2])
        Player.pile = []
        print(f"{p2.name} wins!")
    else:
        Player.pile.extend([card1, card2] + list(draw_cards(p1, p2)))
        print("Draw")

    print("-" * 30)
