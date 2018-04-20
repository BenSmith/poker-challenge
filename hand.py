from staticdata import CARD_RANKS, SCORE, INV_SCORE


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
        self._score = None

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

    def _score_hand(self):
        if self.is_straight() and self.is_flush():
            self._score = SCORE['Straight Flush']
            return

        ranks = self.get_rank_count()
        num_unique_ranks = len(ranks)

        if num_unique_ranks == 2:
            # either a full house or four-of-a-kind
            for k, v in ranks.items():
                if v == 4:
                    self._score = SCORE['Four Of A Kind']
                    return
                elif v == 3:
                    self._score = SCORE['Full House']
                    return

        if self.is_flush():
            self._score = SCORE['Flush']
            return

        if self.is_straight():
            self._score = SCORE['Straight']
            return

        if num_unique_ranks == 3:
            # either three of a kind or two pair
            for k, v in ranks.items():
                if v == 3:
                    self._score = SCORE['Three Of A Kind']
                    return
                if v == 2:
                    self._score = SCORE['Two Pair']
                    return

        if num_unique_ranks == 4:
            # a pair
            self._score = SCORE['Pair']
            return

        self._score = SCORE['High']

    def get_score(self):
        if self._score is None:
            self._score_hand()
        return self._score

    def __gt__(self, other):
        if self._score is None:
            self._score_hand()

        if self._score > other.get_score():
            return True
        elif self._score < other.get_score():
            return False
        else:
            other_ranks = other.get_ranks()
            for r in range(len(self._card_ranks)):
                if CARD_RANKS[self._card_ranks[r]] > CARD_RANKS[other_ranks[r]]:
                    return True
                elif CARD_RANKS[self._card_ranks[r]] < CARD_RANKS[other_ranks[r]]:
                    return False

            return False

    def __lt__(self, other):
        if self._score is None:
            self._score_hand()
        if self._score > other.get_score():
            return False
        elif self._score < other.get_score():
            return True
        else:
            other_ranks = other.get_ranks()
            for r in range(len(self._card_ranks)):
                if CARD_RANKS[self._card_ranks[r]] < CARD_RANKS[other_ranks[r]]:
                    return True
                elif CARD_RANKS[self._card_ranks[r]] > CARD_RANKS[other_ranks[r]]:
                    return False
            return False

    def __eq__(self, other):
        if self._score is None:
            self._score_hand()
        if self._score == other.get_score():
            other_ranks = other.get_ranks()
            for r in range(len(self._card_ranks)):
                if self._card_ranks[r] != other_ranks[r]:
                    return False
            return True
        return False

    def __repr__(self):
        if self._score is None:
            self._score_hand()
        return "%s %s" % (INV_SCORE[self._score], self._cards)
