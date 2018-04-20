from staticdata import SCORE


def score_hand(hand):
    if hand.is_straight() and hand.is_flush():
        return SCORE['Straight Flush']

    ranks = hand.get_rank_count()
    num_unique_ranks = len(ranks)

    if num_unique_ranks == 2:
        # either a full house or four-of-a-kind
        for k, v in ranks.items():
            if v == 4:
                return SCORE['Four of a kind']
            elif v == 3:
                return SCORE['Full House']

    if hand.is_flush():
        return SCORE['Flush']

    if hand.is_straight():
        return SCORE['Straight']

    if num_unique_ranks == 3:
        # either three of a kind or two pair
        for k, v in ranks.items():
            if v == 3:
                return SCORE['Three of a kind']
            if v == 2:
                return SCORE['Two Pair']

    if num_unique_ranks == 4:
        # a pair
        return SCORE['Pair']

    return SCORE['High']


if __name__ == '__main__':
    from hand import Hand
    first_hand = Hand(['2H', '2S', '2C', '10H', '3D'])
    second_hand = Hand(['AH', '10S', 'QC', 'KD', 'JS'])

    print(score_hand(first_hand) > score_hand(second_hand))
