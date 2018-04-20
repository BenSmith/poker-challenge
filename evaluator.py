from staticdata import CARD_RANKS


def is_flush(suits):
    rv = True
    suit = suits[0]
    for x in suits:
        if x != suit:
            rv = False
            break
    return rv


def count_ranks(ranks):
    rv = dict()
    for x in ranks:
        if x not in rv:
            rv[x] = 1
        else:
            rv[x] += 1
    return rv


def is_straight(rank_counts):

    ranks = list(rank_counts.keys())
    ranks.sort(key=CARD_RANKS.__getitem__)

    if len(rank_counts.keys()) < 5:
        return False

    val = CARD_RANKS[ranks[0]] - 1
    for c in ranks:
        if CARD_RANKS[c] != val + 1:
            return False
        val += 1

    return True


def compare(first, second):
    first_suits = [x[-1:] for x in first]
    first_suits.sort()
    first_ranks = [x[:-1] for x in first]
    first_ranks.sort(key=CARD_RANKS.__getitem__, reverse=True)

    second_suits = [x[-1:] for x in second]
    second_suits.sort()
    second_ranks = [x[:-1] for x in second]
    second_ranks.sort(key=CARD_RANKS.__getitem__, reverse=True)

    first_is_flush = is_flush(first_suits)
    second_is_flush = is_flush(second_suits)

    first_rank_counts = count_ranks(first_ranks)
    second_rank_counts = count_ranks(second_ranks)

    first_is_straight = is_straight(first_rank_counts)
    second_is_straight = is_straight(second_rank_counts)

    print(first_ranks, first_suits)
    print(first_is_flush, first_is_straight, first_rank_counts)
    print(second_ranks, second_suits)
    print(second_is_flush, second_is_straight, second_rank_counts)


if __name__ == '__main__':
    first_hand = ['2H', '2S', '2C', '10H', '3D']
    second_hand = ['AH', '10S', 'QC', 'KD', 'JS']

    compare(first_hand, second_hand)
