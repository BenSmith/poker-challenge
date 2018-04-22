import unittest
from .deck import Deck


class DeckTest(unittest.TestCase):

    def setUp(self):
        self.deck = Deck()

    def test_deck_construction(self):
        self.assertEqual(self.deck.get_card_count(), 52)

    def test_deal_empty_hand(self):
        self.assertEqual(self.deck.deal_hands(0), [])
        self.assertNotEqual(self.deck.deal_hands(0), None)

    def test_deal_one_hand(self):
        hand = self.deck.deal_hands(1)
        self.assertEqual(len(hand), 1)
        self.assertEqual(hand[0].get_hand_size(), 5)

    def test_deal_two_hands(self):
        hands = self.deck.deal_hands(2)
        self.assertEqual(len(hands), 2)
        self.assertEqual(hands[0].get_hand_size(), hands[1].get_hand_size())

    def test_deal_too_many_hands(self):
        try:
            self.deck.deal_hands(21)
        except IndexError:
            pass
        else:
            self.fail("Too many hands test failed")


if __name__ == '__main__':
    unittest.main()
