import unittest

from test_constants import (
    hand_high_card_1,
    hand_pair_1,
    hand_full_house,
    hand_two_pairs_2,
    hand_straight,
    hand_royal_flush,
    hand_four_of_a_kind,
    hand_full_house_2,
)
from poker_structure import CardValue, MinComboScore
import poker_util


class Test(unittest.TestCase):
    def test_high_card(self):
        expect_score = CardValue.A + MinComboScore.High_card
        self.assertEqual(poker_util.high_card(hand_high_card_1), expect_score)

    def test_is_there_pair(self):
        self.assertFalse(poker_util.is_there_pair(hand_high_card_1))

        expect_score = CardValue.Four + MinComboScore.Pair
        self.assertEqual(poker_util.is_there_pair(hand_pair_1), expect_score)

    def test_is_there_two_pair(self):
        self.assertFalse(poker_util.is_there_two_pair(hand_high_card_1))
        self.assertFalse(poker_util.is_there_two_pair(hand_pair_1))

        expect_score = CardValue.T + MinComboScore.Two_pairs
        self.assertEqual(
            poker_util.is_there_two_pair(hand_four_of_a_kind), expect_score
        )

        expect_score = CardValue.T + MinComboScore.Two_pairs
        self.assertEqual(poker_util.is_there_two_pair(hand_two_pairs_2), expect_score)

    def test_is_there_three_of_a_kind(self):
        self.assertFalse(poker_util.is_there_three_of_a_kind(hand_high_card_1))
        self.assertFalse(poker_util.is_there_three_of_a_kind(hand_high_card_1))

        expect_score = CardValue.Four + MinComboScore.Three_of_a_kind
        self.assertEqual(
            poker_util.is_there_three_of_a_kind(hand_full_house), expect_score
        )

        expect_score = CardValue.Three + MinComboScore.Three_of_a_kind
        self.assertEqual(
            poker_util.is_there_three_of_a_kind(hand_full_house_2), expect_score
        )

    def test_is_there_straight(self):
        self.assertFalse(poker_util.is_there_straight(hand_high_card_1))

        expect_score = CardValue.Six + MinComboScore.Straight
        self.assertEqual(poker_util.is_there_straight(hand_straight), expect_score)
        expect_score = CardValue.A + MinComboScore.Straight
        self.assertEqual(poker_util.is_there_straight(hand_royal_flush), expect_score)

    def test_is_there_flush(self):
        self.assertFalse(poker_util.is_there_flush(hand_high_card_1))

        expect_score = MinComboScore.Flush + CardValue.A
        self.assertEqual(poker_util.is_there_flush(hand_royal_flush), expect_score)

    def test_is_there_full_house(self):
        self.assertFalse(poker_util.is_there_full_house(hand_high_card_1))

        expect_score = CardValue.Four + MinComboScore.Full_house
        self.assertEqual(poker_util.is_there_full_house(hand_full_house), expect_score)

    def test_is_there_four_of_a_kind(self):
        self.assertFalse(poker_util.is_there_full_house(hand_high_card_1))

        expect_score = CardValue.T + MinComboScore.Four_of_a_kind
        self.assertEqual(
            poker_util.is_there_four_of_a_kind(hand_four_of_a_kind), expect_score
        )

    def test_is_there_straight_flush(self):
        expect_score = CardValue.A + MinComboScore.Straight_flush
        self.assertEqual(
            poker_util.is_there_straight_flush(hand_royal_flush), expect_score
        )

    def test_is_there_royal_flush(self):
        expect_score = MinComboScore.Royal_Flush
        self.assertEqual(
            poker_util.is_there_royal_flush(hand_royal_flush), expect_score
        )


if __name__ == "__main__":
    unittest.main()
