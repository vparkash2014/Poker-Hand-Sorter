import unittest

from test_constants import (
    hand_high_card_1,
    hand_high_card_2,
    hand_pair_1,
    hand_pair_2,
    hand_full_house,
    hand_two_pairs,
    hand_two_pairs_1,
    hand_two_pairs_2,
    hand_two_pairs_3,
    hand_straight,
    hand_flush_1,
    hand_flush_2,
    hand_straight_flush,
    hand_royal_flush,
    hand_four_of_a_kind,
    hand_three_of_a_kind_1,
    hand_three_of_a_kind_2,
    hand_tie_1,
    hand_tie_2,
)
from poker_structure import MinComboScore, GameScore
from poker_winner import highest_hand_score, highest_score_for_showdown


class Test(unittest.TestCase):
    def test_highest_score_royal_flush(self):
        self.assertEqual(
            highest_hand_score(hand_royal_flush), MinComboScore.Royal_Flush
        )

    def test_highest_score_straight_flush(self):
        self.assertGreaterEqual(
            highest_hand_score(hand_straight_flush), MinComboScore.Straight_flush
        )
        self.assertLess(
            highest_hand_score(hand_four_of_a_kind), MinComboScore.Royal_Flush
        )

    def test_highest_score_four_of_a_kind(self):
        self.assertGreaterEqual(
            highest_hand_score(hand_four_of_a_kind), MinComboScore.Four_of_a_kind
        )
        self.assertLess(
            highest_hand_score(hand_four_of_a_kind), MinComboScore.Straight_flush
        )

    def test_highest_score_full_house(self):
        self.assertGreaterEqual(
            highest_hand_score(hand_full_house), MinComboScore.Full_house
        )
        self.assertLess(
            highest_hand_score(hand_full_house), MinComboScore.Four_of_a_kind
        )

    def test_highest_score_flush(self):
        self.assertGreaterEqual(highest_hand_score(hand_flush_1), MinComboScore.Flush)
        self.assertLess(highest_hand_score(hand_flush_1), MinComboScore.Full_house)

    def test_highest_score_straight(self):
        self.assertGreaterEqual(
            highest_hand_score(hand_straight), MinComboScore.Straight
        )
        self.assertLess(highest_hand_score(hand_straight), MinComboScore.Flush)

    def test_highest_score_three_of_a_kind(self):
        self.assertGreaterEqual(
            highest_hand_score(hand_three_of_a_kind_1), MinComboScore.Three_of_a_kind
        )
        self.assertLess(
            highest_hand_score(hand_three_of_a_kind_1), MinComboScore.Straight
        )

    def test_highest_score_two_pairs(self):
        self.assertGreaterEqual(
            highest_hand_score(hand_two_pairs), MinComboScore.Two_pairs
        )
        self.assertLess(
            highest_hand_score(hand_two_pairs), MinComboScore.Three_of_a_kind
        )

    def test_highest_score_pair(self):
        self.assertGreaterEqual(highest_hand_score(hand_pair_1), MinComboScore.Pair)
        self.assertLess(highest_hand_score(hand_pair_1), MinComboScore.Two_pairs)

    def test_highest_score_high_card(self):
        self.assertGreaterEqual(
            highest_hand_score(hand_high_card_1), MinComboScore.High_card
        )
        self.assertLess(highest_hand_score(hand_high_card_1), MinComboScore.Pair)

    def test_highest_score_for_showdown(self):
        game_score = GameScore()

        highest_score_for_showdown(hand_pair_1, hand_pair_2, game_score)
        self.assertEqual(game_score.player_1, 0)
        self.assertEqual(game_score.player_2, 1)

        highest_score_for_showdown(hand_high_card_1, hand_high_card_2, game_score)
        self.assertEqual(game_score.player_1, 1)
        self.assertEqual(game_score.player_2, 1)

        highest_score_for_showdown(hand_three_of_a_kind_2, hand_flush_2, game_score)
        self.assertEqual(game_score.player_1, 1)
        self.assertEqual(game_score.player_2, 2)

    def test_highest_score_for_showdown_tie(self):
        game_score = GameScore()
        highest_score_for_showdown(hand_tie_1, hand_tie_2, game_score)
        self.assertEqual(game_score.player_1, 1)
        self.assertEqual(game_score.player_2, 0)

        highest_score_for_showdown(hand_two_pairs_1, hand_two_pairs_2, game_score)

        self.assertEqual(game_score.player_1, 1)
        self.assertEqual(game_score.player_2, 1)

        highest_score_for_showdown(hand_two_pairs_2, hand_two_pairs_3, game_score)
        self.assertEqual(game_score.player_1, 1)
        self.assertEqual(game_score.player_2, 2)


if __name__ == "__main__":
    unittest.main()
