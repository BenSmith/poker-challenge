from deck import Deck

d = Deck()
d.shuffle()
(first_hand, second_hand) = d.deal_hands(2)

if first_hand > second_hand:
    print("%s beats %s" % (first_hand, second_hand))
elif first_hand < second_hand:
    print("%s beats %s" % (second_hand, first_hand))
elif first_hand == second_hand:
    print("%s is equivalent to %s" % (first_hand, second_hand))
