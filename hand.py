
class Hand:
    def __init__(self, cards):
        self._cards = cards

    def get_hand_size(self):
        return len(self._cards)

    def get_cards(self):
        return self._cards

    def __gt__(self, other):
        return 0

    def __lt__(self, other):
        return 0
