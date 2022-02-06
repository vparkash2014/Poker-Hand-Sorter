import unittest

from test_constants import (
    hand_high_card,
    hand_pair,
    hand_full_house,
    hand_two_pairs_2,
    hand_straight,
    hand_flush,
    hand_straight_flush,
    hand_royal_flush,
    hand_four_of_a_kind,
    hand_three_of_a_kind,
)
from poker_structure import MinComboScore
from poker_winner import highest_score


class Test(unittest.TestCase):
    def test_highest_score_royal_flush(self):
        self.assertEqual(highest_score(hand_royal_flush), MinComboScore.Royal_Flush)

    def test_highest_score_straight_flush(self):
        self.assertGreaterEqual(
            highest_score(hand_straight_flush), MinComboScore.Straight_flush
        )
        self.assertLess(highest_score(hand_four_of_a_kind), MinComboScore.Royal_Flush)

    def test_highest_score_four_of_a_kind(self):
        self.assertGreaterEqual(
            highest_score(hand_four_of_a_kind), MinComboScore.Four_of_a_kind
        )
        self.assertLess(
            highest_score(hand_four_of_a_kind), MinComboScore.Straight_flush
        )

    def test_highest_score_full_house(self):
        self.assertGreaterEqual(
            highest_score(hand_full_house), MinComboScore.Full_house
        )
        self.assertLess(highest_score(hand_full_house), MinComboScore.Four_of_a_kind)

    def test_highest_score_flush(self):
        self.assertGreaterEqual(highest_score(hand_flush), MinComboScore.Flush)
        self.assertLess(highest_score(hand_flush), MinComboScore.Full_house)

    def test_highest_score_straight(self):
        self.assertGreaterEqual(highest_score(hand_straight), MinComboScore.Straight)
        self.assertLess(highest_score(hand_straight), MinComboScore.Flush)

    def test_highest_score_three_of_a_kind(self):
        self.assertGreaterEqual(
            highest_score(hand_three_of_a_kind), MinComboScore.Three_of_a_kind
        )
        self.assertLess(highest_score(hand_three_of_a_kind), MinComboScore.Straight)

    def test_highest_score_two_pairs(self):
        self.assertGreaterEqual(
            highest_score(hand_two_pairs_2), MinComboScore.Two_pairs
        )
        self.assertLess(highest_score(hand_two_pairs_2), MinComboScore.Three_of_a_kind)

    def test_highest_score_pair(self):
        self.assertGreaterEqual(highest_score(hand_pair), MinComboScore.Pair)
        self.assertLess(highest_score(hand_pair), MinComboScore.Two_pairs)

    def test_highest_score_high_card(self):
        self.assertGreaterEqual(highest_score(hand_high_card), MinComboScore.High_card)
        self.assertLess(highest_score(hand_high_card), MinComboScore.Pair)


if __name__ == "__main__":
    unittest.main()
