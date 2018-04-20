import unittest

from hand import Hand


class TestHand(unittest.TestCase):
    def test_hand_size(self):
        h = Hand(['A', 'B', 'C', 'D', 'E'])
        self.assertEqual(len(h.get_cards()), h.get_hand_size())


if __name__ == "__main__":
    unittest.main()
