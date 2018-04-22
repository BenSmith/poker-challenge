import unittest

from .hand import Hand
from .staticdata import SCORE, INV_SCORE

STRAIGHT_FLUSH_HAND = Hand(['3H', '4H', '5H', '7H', '6H'])
FOUR_OF_A_KIND_HAND = Hand(['3H', '4S', '3D', '3S', '3C'])
FULL_HOUSE_HAND = Hand(['KH', 'KS', '7C', '7H', 'KC'])
FLUSH_HAND = Hand(['3H', '5H', '7H', '9H', 'KH'])
STRAIGHT_HAND = Hand(['2S', '3C', '5D', '4H', '6S'])
THREE_OF_A_KIND_HAND = Hand(['4H', '4S', '4C', '7H', 'KC'])
TWO_PAIR_HAND = Hand(['3H', '3S', '5H', '5C', 'KC'])
PAIR_HAND = Hand(['3H', '3S', '6H', '5C', 'KC'])
HIGH_HAND = Hand(['3H', '4S', '5H', '7H', 'KC'])


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

    def test_hand_score(self):
        self.assertEqual(INV_SCORE[self.hand.get_score()], 'Two Pair')

    def test_straight_flush_score(self):
        self.hand = STRAIGHT_FLUSH_HAND
        self.assertEqual(INV_SCORE[self.hand.get_score()], 'Straight Flush')

    def test_four_score(self):
        self.hand = FOUR_OF_A_KIND_HAND
        self.assertEqual(INV_SCORE[self.hand.get_score()], 'Four Of A Kind')

    def test_full_house_score(self):
        self.hand = FULL_HOUSE_HAND
        self.assertEqual(INV_SCORE[self.hand.get_score()], 'Full House')

    def test_flush_score(self):
        self.hand = FLUSH_HAND
        self.assertEqual(INV_SCORE[self.hand.get_score()], 'Flush')

    def test_straight_score(self):
        self.hand = STRAIGHT_HAND
        self.assertEqual(INV_SCORE[self.hand.get_score()], 'Straight')

    def test_three_score(self):
        self.hand = THREE_OF_A_KIND_HAND
        self.assertEqual(INV_SCORE[self.hand.get_score()], 'Three Of A Kind')

    def test_two_pair_score(self):
        self.hand = TWO_PAIR_HAND
        self.assertEqual(INV_SCORE[self.hand.get_score()], 'Two Pair')

    def test_pair_score(self):
        self.hand = PAIR_HAND
        self.assertEqual(INV_SCORE[self.hand.get_score()], 'Pair')

    def test_high_score(self):
        self.hand = HIGH_HAND
        self.assertEqual(INV_SCORE[self.hand.get_score()], 'High')


class TestHandComparisons(unittest.TestCase):
    def test_straight_flush(self):
        self.assertEqual(STRAIGHT_FLUSH_HAND, STRAIGHT_FLUSH_HAND)
        self.assertGreater(STRAIGHT_FLUSH_HAND, FOUR_OF_A_KIND_HAND)
        self.assertGreater(STRAIGHT_FLUSH_HAND, FULL_HOUSE_HAND)
        self.assertGreater(STRAIGHT_FLUSH_HAND, FLUSH_HAND)
        self.assertGreater(STRAIGHT_FLUSH_HAND, STRAIGHT_HAND)
        self.assertGreater(STRAIGHT_FLUSH_HAND, THREE_OF_A_KIND_HAND)
        self.assertGreater(STRAIGHT_FLUSH_HAND, TWO_PAIR_HAND)
        self.assertGreater(STRAIGHT_FLUSH_HAND, PAIR_HAND)
        self.assertGreater(STRAIGHT_FLUSH_HAND, HIGH_HAND)

    def test_four(self):
        self.assertLess(FOUR_OF_A_KIND_HAND, STRAIGHT_FLUSH_HAND)
        self.assertEqual(FOUR_OF_A_KIND_HAND, FOUR_OF_A_KIND_HAND)
        self.assertGreater(FOUR_OF_A_KIND_HAND, FULL_HOUSE_HAND)
        self.assertGreater(FOUR_OF_A_KIND_HAND, FLUSH_HAND)
        self.assertGreater(FOUR_OF_A_KIND_HAND, STRAIGHT_HAND)
        self.assertGreater(FOUR_OF_A_KIND_HAND, THREE_OF_A_KIND_HAND)
        self.assertGreater(FOUR_OF_A_KIND_HAND, TWO_PAIR_HAND)
        self.assertGreater(FOUR_OF_A_KIND_HAND, PAIR_HAND)
        self.assertGreater(FOUR_OF_A_KIND_HAND, HIGH_HAND)

    def test_full(self):
        self.assertLess(FULL_HOUSE_HAND, STRAIGHT_FLUSH_HAND)
        self.assertLess(FULL_HOUSE_HAND, FOUR_OF_A_KIND_HAND)
        self.assertEqual(FULL_HOUSE_HAND, FULL_HOUSE_HAND)
        self.assertGreater(FULL_HOUSE_HAND, FLUSH_HAND)
        self.assertGreater(FULL_HOUSE_HAND, STRAIGHT_HAND)
        self.assertGreater(FULL_HOUSE_HAND, THREE_OF_A_KIND_HAND)
        self.assertGreater(FULL_HOUSE_HAND, TWO_PAIR_HAND)
        self.assertGreater(FULL_HOUSE_HAND, PAIR_HAND)
        self.assertGreater(FULL_HOUSE_HAND, HIGH_HAND)

    def test_flush(self):
        self.assertLess(FLUSH_HAND, STRAIGHT_FLUSH_HAND)
        self.assertLess(FLUSH_HAND, FOUR_OF_A_KIND_HAND)
        self.assertLess(FLUSH_HAND, FULL_HOUSE_HAND)
        self.assertEqual(FLUSH_HAND, FLUSH_HAND)
        self.assertGreater(FLUSH_HAND, STRAIGHT_HAND)
        self.assertGreater(FLUSH_HAND, THREE_OF_A_KIND_HAND)
        self.assertGreater(FLUSH_HAND, TWO_PAIR_HAND)
        self.assertGreater(FLUSH_HAND, PAIR_HAND)
        self.assertGreater(FLUSH_HAND, HIGH_HAND)

    def test_straight(self):
        self.assertLess(STRAIGHT_HAND, STRAIGHT_FLUSH_HAND)
        self.assertLess(STRAIGHT_HAND, FOUR_OF_A_KIND_HAND)
        self.assertLess(STRAIGHT_HAND, FULL_HOUSE_HAND)
        self.assertLess(STRAIGHT_HAND, FLUSH_HAND)
        self.assertEqual(STRAIGHT_HAND, STRAIGHT_HAND)
        self.assertGreater(STRAIGHT_HAND, THREE_OF_A_KIND_HAND)
        self.assertGreater(STRAIGHT_HAND, TWO_PAIR_HAND)
        self.assertGreater(STRAIGHT_HAND, PAIR_HAND)
        self.assertGreater(STRAIGHT_HAND, HIGH_HAND)

    def test_three(self):
        self.assertLess(THREE_OF_A_KIND_HAND, STRAIGHT_FLUSH_HAND)
        self.assertLess(THREE_OF_A_KIND_HAND, FOUR_OF_A_KIND_HAND)
        self.assertLess(THREE_OF_A_KIND_HAND, FULL_HOUSE_HAND)
        self.assertLess(THREE_OF_A_KIND_HAND, FLUSH_HAND)
        self.assertLess(THREE_OF_A_KIND_HAND, STRAIGHT_HAND)
        self.assertEqual(THREE_OF_A_KIND_HAND, THREE_OF_A_KIND_HAND)
        self.assertGreater(THREE_OF_A_KIND_HAND, TWO_PAIR_HAND)
        self.assertGreater(THREE_OF_A_KIND_HAND, PAIR_HAND)
        self.assertGreater(THREE_OF_A_KIND_HAND, HIGH_HAND)

    def test_two_pair(self):
        self.assertLess(TWO_PAIR_HAND, STRAIGHT_FLUSH_HAND)
        self.assertLess(TWO_PAIR_HAND, FOUR_OF_A_KIND_HAND)
        self.assertLess(TWO_PAIR_HAND, FULL_HOUSE_HAND)
        self.assertLess(TWO_PAIR_HAND, FLUSH_HAND)
        self.assertLess(TWO_PAIR_HAND, STRAIGHT_HAND)
        self.assertLess(TWO_PAIR_HAND, THREE_OF_A_KIND_HAND)
        self.assertEqual(TWO_PAIR_HAND, TWO_PAIR_HAND)
        self.assertGreater(TWO_PAIR_HAND, PAIR_HAND)
        self.assertGreater(TWO_PAIR_HAND, HIGH_HAND)

    def test_pair(self):
        self.assertLess(PAIR_HAND, STRAIGHT_FLUSH_HAND)
        self.assertLess(PAIR_HAND, FOUR_OF_A_KIND_HAND)
        self.assertLess(PAIR_HAND, FULL_HOUSE_HAND)
        self.assertLess(PAIR_HAND, FLUSH_HAND)
        self.assertLess(PAIR_HAND, STRAIGHT_HAND)
        self.assertLess(PAIR_HAND, THREE_OF_A_KIND_HAND)
        self.assertLess(PAIR_HAND, TWO_PAIR_HAND)
        self.assertEqual(PAIR_HAND, PAIR_HAND)
        self.assertGreater(PAIR_HAND, HIGH_HAND)

    def test_high(self):
        self.assertLess(HIGH_HAND, STRAIGHT_FLUSH_HAND)
        self.assertLess(HIGH_HAND, FOUR_OF_A_KIND_HAND)
        self.assertLess(HIGH_HAND, FULL_HOUSE_HAND)
        self.assertLess(HIGH_HAND, FLUSH_HAND)
        self.assertLess(HIGH_HAND, STRAIGHT_HAND)
        self.assertLess(HIGH_HAND, THREE_OF_A_KIND_HAND)
        self.assertLess(HIGH_HAND, TWO_PAIR_HAND)
        self.assertLess(HIGH_HAND, PAIR_HAND)
        self.assertEqual(HIGH_HAND, HIGH_HAND)

    def test_high_different_hands(self):
        self.assertGreater(
            Hand(['3H', '4S', '5H', '7H', 'AC']),
            Hand(['3H', '4S', '5H', '7H', 'KC'])
        )
        self.assertLess(
            Hand(['3H', '4S', '5H', '6H', 'KC']),
            Hand(['3H', '4S', '5H', '7H', 'KH'])
        )
        self.assertEqual(
            Hand(['3H', '4S', '5H', '7H', 'KC']),
            Hand(['3H', '4S', '5H', '7H', 'KH'])
        )
        self.assertNotEqual(
            Hand(['3H', '4S', '3S', '7H', 'KC']),
            Hand(['3H', '4S', '5H', '7H', 'KH'])
        )

    def test_high_pair(self):
        self.assertGreater(
            Hand(['4H', '4S', '5H', '7H', 'AC']),
            Hand(['3H', '3S', '5H', '7H', 'KC'])
        )

    def test_high_straight_flush(self):
        self.assertGreater(
            Hand(['AH', 'KH', 'QH', 'JH', '10H']),
            Hand(['KS', 'QS', 'JS', '10S', '9S'])
        )
        self.assertEqual(
            Hand(['AH', 'KH', 'QH', 'JH', '10H']),
            Hand(['AS', 'KS', 'QS', 'JS', '10S'])
        )

    def test_full_house(self):
        self.assertGreater(
            Hand(['QH', 'QD', 'KH', 'KS', 'KD']),
            Hand(['JD', 'JH', 'JS', 'AD', 'AH'])
        )

    # There should be many, many more tests


if __name__ == "__main__":
    unittest.main()
