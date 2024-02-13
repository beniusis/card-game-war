class Player:
    def __init__(self, name, deck):
        self.name = name
        self.deck = deck

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
