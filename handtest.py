import unittest

from hand import Hand


class TestHand(unittest.TestCase):
    def setUp(self):
        self.hand = Hand(['9S', '9H', '8H', '8C', 'AH'])

    def test_hand_size(self):
        self.assertEqual(len(self.hand.get_cards()), self.hand.get_hand_size())

    def test_hand_ranks(self):
        self.assertEqual(self.hand.get_ranks(), ['A', '9', '9', '8', '8'])

    def test_hand_suits(self):
        suits = ['H', 'H', 'H', 'C', 'S']
        suits.sort()
        self.assertEqual(self.hand.get_suits(), suits)


if __name__ == "__main__":
    unittest.main()
