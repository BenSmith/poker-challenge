# tests multiple hands against each other

from deck import Deck

NUM_HANDS = 5

d = Deck()
d.shuffle()
hands = d.deal_hands(NUM_HANDS)

top_hand = hands[0]
for hand in hands:
    if hand > top_hand:
        top_hand = hand

hands.remove(top_hand)

print("%s beats these other hands:" % top_hand)

for hand in hands:
    print("%s" % hand)
