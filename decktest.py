import unittest

from deck import Deck


class DeckTest(unittest.TestCase):

    def setUp(self):
        self.deck = Deck()

    def test_deck_construction(self):
        self.assertEqual(self.deck.get_card_count(), 52)

    def test_deal_empty_hand(self):
        self.assertEqual(self.deck.deal_hands(0), [])
        self.assertNotEqual(self.deck.deal_hands(0), None)

    def test_deal_one_hand(self):
        h = self.deck.deal_hands(1)
        self.assertEqual(len(h), 1)
        self.assertEqual(len(h[0]), 5)

    def test_deal_too_many_hands(self):
        try:
            self.deck.deal_hands(21)
        except IndexError:
            pass
        else:
            self.fail("Too many hands test failed")


if __name__ == '__main__':
    unittest.main()
