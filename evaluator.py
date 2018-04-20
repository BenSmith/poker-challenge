from staticdata import CARD_RANKS


def compare(first, second):
    first_suits = [x[-1:] for x in first]
    first_suits.sort()
    first_ranks = [x[:-1] for x in first]
    first_ranks.sort(key=CARD_RANKS.__getitem__)

    second_suits = [x[-1:] for x in second]
    second_suits.sort()
    second_ranks = [x[:-1] for x in second]
    second_ranks.sort(key=CARD_RANKS.__getitem__)

    first_is_flush = True
    c = first_suits[0]
    for x in first_suits:
        if x != c:
            first_is_flush = False
            break

    second_is_flush = True
    c = second_suits[0]
    for x in second_suits:
        if x != c:
            second_is_flush = False
            break



    print(first_suits)
    print(first_ranks)
    print(second_suits)
    print(second_ranks)


if __name__ == '__main__':
    first_hand = ['2H', '2S', '2C', '10H', '3D']
    second_hand = ['AH', '10S', '10C', '10D', '3S']

    compare(first_hand, second_hand)
