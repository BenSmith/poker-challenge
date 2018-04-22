# Representation of a deck of cards

import random
from .hand import Hand
from .staticdata import CARD_RANKS, CARD_SUITS


class Deck:

    def __init__(self, *args, **kwargs):
        self._cards = None
        self._build_deck()
        self._remaining_cards = len(self._cards)

    def _build_deck(self):
        self._cards = [rank + suit for rank in CARD_RANKS.keys() for suit in CARD_SUITS]

    def deal_hands(self, num_hands=0, hand_size=5):

        if num_hands * hand_size > len(self._cards):
            raise IndexError("More hands than cards were requested")

        rv = list()

        self.shuffle()
        x = 0
        for x in range(num_hands):
            rv.append(Hand(self._cards[x * hand_size:(x * hand_size) + hand_size]))

        self._remaining_cards = len(self._cards) - (x * hand_size)

        return rv

    def shuffle(self):
        random.shuffle(self._cards)

    def get_card_count(self):
        return self._remaining_cards
