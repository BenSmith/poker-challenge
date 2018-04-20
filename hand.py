from staticdata import CARD_RANKS


class Hand:
    def __init__(self, cards):
        self._cards = cards

        self._card_suits = [x[-1:] for x in self._cards]
        self._card_ranks = [x[:-1] for x in self._cards]

        self._card_suits.sort()
        self._card_ranks.sort(key=CARD_RANKS.__getitem__, reverse=True)

        self._rank_count = dict()
        self._is_flush = None
        self._is_straight = None

    def _count_ranks(self):
        for x in self._card_ranks:
            if x not in self._rank_count:
                self._rank_count[x] = 1
            else:
                self._rank_count[x] += 1

    def _check_straight(self):
        if not self._rank_count:
            self._count_ranks()

        ranks = list(self._rank_count.keys())
        ranks.sort(key=CARD_RANKS.__getitem__)

        self._is_straight = False

        if len(ranks) < 5:
            return

        val = CARD_RANKS[ranks[0]] - 1
        for c in ranks:
            if CARD_RANKS[c] != val + 1:
                return
            val += 1
        self._is_straight = True

    def _check_flush(self):
        self._is_flush = False
        suit = self._card_suits[0]
        for x in self._card_suits:
            if x != suit:
                return
        self._is_flush = True

    def get_hand_size(self):
        return len(self._cards)

    def get_cards(self):
        return self._cards

    def is_straight(self):
        if self._is_straight is None:
            self._check_straight()

        return self._is_straight

    def is_flush(self):
        if self._is_flush is None:
            self._check_flush()

        return self._is_flush

    def get_suits(self):
        return self._card_suits

    def get_ranks(self):
        return self._card_ranks

    def get_rank_count(self):
        if not self._rank_count:
            self._count_ranks()
        return self._rank_count

    def __gt__(self, other):
        return 0

    def __lt__(self, other):
        return 0
