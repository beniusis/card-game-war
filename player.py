class Player:
    pile = []

    def __init__(self, name, deck):
        self.name = name
        self.deck = deck
        self.deck_size = len(self.deck)

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name

    @property
    def deck(self):
        return self._deck

    @deck.setter
    def deck(self, deck):
        self._deck = deck

    def draw_card(self):
        return self.deck.pop(0)

    def add_cards(self, cards: list):
        self.deck.extend(cards)
