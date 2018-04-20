import random


class Deck:
    def __init__(self, *args, **kwargs):
        self._cards_by_value = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
        self._suits = ["H", "C", "S", "D"]
        self._cards = None
        self._build_deck()
        self._remaining_cards = len(self._cards)

    def _build_deck(self):
        self._cards = [value + suit for value in self._cards_by_value for suit in self._suits]

    def deal_hands(self, num_hands=0, hand_size=5):

        if num_hands * hand_size > len(self._cards):
            raise IndexError("More hands than cards were requested")

        rv = list()

        self.shuffle()
        x = 0
        for x in range(num_hands):
            rv.append(self._cards[x * hand_size:(x * hand_size) + hand_size])

        self._remaining_cards = len(self._cards) - (x * hand_size)

        return rv

    def shuffle(self):
        random.shuffle(self._cards)

    def get_card_count(self):
        return self._remaining_cards
