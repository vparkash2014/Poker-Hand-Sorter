import unittest

from test_constants import (
    P1_H1,
    P1_H2,
    P1_H5,
    P1_H6,
    P1_H7,
    P1_H8,
    P1_H9,
    P1_H10,
    P2_H5,
)
from poker_structure import CardValue, MinComboScore
import poker_util


class Test(unittest.TestCase):
    def test_high_card(self):
        expect_score_P1_H1 = CardValue.K + MinComboScore.High_card
        self.assertEqual(poker_util.high_card(P1_H1), expect_score_P1_H1)

    def test_is_there_pair(self):
        self.assertFalse(poker_util.is_there_pair(P1_H2))

        expect_score_P1_H1 = CardValue.Four + MinComboScore.Pair
        self.assertEqual(poker_util.is_there_pair(P1_H1), expect_score_P1_H1)

    def test_is_there_two_pair(self):
        self.assertFalse(poker_util.is_there_two_pair(P1_H2))
        self.assertFalse(poker_util.is_there_two_pair(P1_H1))

        expect_score = CardValue.Two + MinComboScore.Two_pairs
        self.assertEqual(poker_util.is_there_two_pair(P1_H6), expect_score)

        expect_score = CardValue.T + MinComboScore.Two_pairs
        self.assertEqual(poker_util.is_there_two_pair(P1_H7), expect_score)

    def test_is_there_three_of_a_kind(self):
        self.assertFalse(poker_util.is_there_three_of_a_kind(P1_H2))
        self.assertFalse(poker_util.is_there_three_of_a_kind(P1_H1))

        expect_score = CardValue.Four + MinComboScore.Three_of_a_kind
        self.assertEqual(poker_util.is_there_three_of_a_kind(P1_H5), expect_score)

        expect_score = CardValue.Three + MinComboScore.Three_of_a_kind
        self.assertEqual(poker_util.is_there_three_of_a_kind(P2_H5), expect_score)

    def test_is_there_straight(self):
        self.assertFalse(poker_util.is_there_straight(P1_H2))

        expect_score = CardValue.Six + MinComboScore.Straight
        self.assertEqual(poker_util.is_there_straight(P1_H8), expect_score)
        expect_score = CardValue.A + MinComboScore.Straight
        self.assertEqual(poker_util.is_there_straight(P1_H9), expect_score)

    def test_is_there_flush(self):
        self.assertFalse(poker_util.is_there_flush(P1_H2))

        expect_score = MinComboScore.Flush
        self.assertEqual(poker_util.is_there_flush(P1_H9), expect_score)

    def test_is_there_full_house(self):
        self.assertFalse(poker_util.is_there_full_house(P1_H1))

        expect_score = CardValue.Four + MinComboScore.Full_house
        self.assertEqual(poker_util.is_there_full_house(P1_H5), expect_score)

    def test_is_there_four_of_a_kind(self):
        self.assertFalse(poker_util.is_there_full_house(P1_H1))

        expect_score = CardValue.T + MinComboScore.Four_of_a_kind
        self.assertEqual(poker_util.is_there_four_of_a_kind(P1_H10), expect_score)

    def test_is_there_straight_flush(self):
        expect_score = CardValue.A + MinComboScore.Straight_flush
        self.assertEqual(poker_util.is_there_straight_flush(P1_H9), expect_score)

    def test_is_there_royal_flus(self):
        expect_score = MinComboScore.Royal_Flush
        self.assertEqual(poker_util.is_there_royal_flush(P1_H9), expect_score)


if __name__ == "__main__":
    unittest.main()
