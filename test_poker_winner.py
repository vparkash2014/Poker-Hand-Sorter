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
            highest_hand_score(hand_royal_flush), MinComboScore.ROYAL_FLUSH
        )

    def test_highest_score_straight_flush(self):
        self.assertGreaterEqual(
            highest_hand_score(hand_straight_flush), MinComboScore.STRAIGHT_FLUSH
        )
        self.assertLess(
            highest_hand_score(hand_four_of_a_kind), MinComboScore.ROYAL_FLUSH
        )

    def test_highest_score_four_of_a_kind(self):
        self.assertGreaterEqual(
            highest_hand_score(hand_four_of_a_kind), MinComboScore.FOUR_OF_A_KIND
        )
        self.assertLess(
            highest_hand_score(hand_four_of_a_kind), MinComboScore.STRAIGHT_FLUSH
        )

    def test_highest_score_full_house(self):
        self.assertGreaterEqual(
            highest_hand_score(hand_full_house), MinComboScore.FULL_HOUSE
        )
        self.assertLess(
            highest_hand_score(hand_full_house), MinComboScore.FOUR_OF_A_KIND
        )

    def test_highest_score_flush(self):
        self.assertGreaterEqual(highest_hand_score(hand_flush_1), MinComboScore.FLUSH)
        self.assertLess(highest_hand_score(hand_flush_1), MinComboScore.FULL_HOUSE)

    def test_highest_score_straight(self):
        self.assertGreaterEqual(
            highest_hand_score(hand_straight), MinComboScore.STRAIGHT
        )
        self.assertLess(highest_hand_score(hand_straight), MinComboScore.FLUSH)

    def test_highest_score_three_of_a_kind(self):
        self.assertGreaterEqual(
            highest_hand_score(hand_three_of_a_kind_1), MinComboScore.THREE_OF_A_KIND
        )
        self.assertLess(
            highest_hand_score(hand_three_of_a_kind_1), MinComboScore.STRAIGHT
        )

    def test_highest_score_two_pairs(self):
        self.assertGreaterEqual(
            highest_hand_score(hand_two_pairs), MinComboScore.TWO_PAIRS
        )
        self.assertLess(
            highest_hand_score(hand_two_pairs), MinComboScore.THREE_OF_A_KIND
        )

    def test_highest_score_pair(self):
        self.assertGreaterEqual(highest_hand_score(hand_pair_1), MinComboScore.PAIR)
        self.assertLess(highest_hand_score(hand_pair_1), MinComboScore.TWO_PAIRS)

    def test_highest_score_high_card(self):
        self.assertGreaterEqual(
            highest_hand_score(hand_high_card_1), MinComboScore.HIGH_CARD
        )
        self.assertLess(highest_hand_score(hand_high_card_1), MinComboScore.PAIR)

    def test_highest_score_for_showdown(self):
        game_score = GameScore()

        highest_score_for_showdown(hand_pair_1, hand_pair_2, game_score)
        expected_score_player1 = 0
        expected_score_player2 = 1
        self.assertEqual(game_score.player_1, expected_score_player1)
        self.assertEqual(game_score.player_2, expected_score_player2)

        highest_score_for_showdown(hand_high_card_1, hand_high_card_2, game_score)
        expected_score_player1 = 1
        self.assertEqual(game_score.player_1, expected_score_player1)
        self.assertEqual(game_score.player_2, expected_score_player2)

        highest_score_for_showdown(hand_three_of_a_kind_2, hand_flush_2, game_score)
        expected_score_player2 = 2
        self.assertEqual(game_score.player_1, expected_score_player1)
        self.assertEqual(game_score.player_2, expected_score_player2)

    def test_highest_score_for_showdown_tie(self):
        game_score = GameScore()
        highest_score_for_showdown(hand_tie_1, hand_tie_2, game_score)
        expected_score_player1 = 1
        expected_score_player2 = 0
        self.assertEqual(game_score.player_1, expected_score_player1)
        self.assertEqual(game_score.player_2, expected_score_player2)

        highest_score_for_showdown(hand_two_pairs_1, hand_two_pairs_2, game_score)
        expected_score_player2 = 1
        self.assertEqual(game_score.player_1, expected_score_player1)
        self.assertEqual(game_score.player_2, expected_score_player2)

        highest_score_for_showdown(hand_two_pairs_2, hand_two_pairs_3, game_score)
        expected_score_player2 = 2
        self.assertEqual(game_score.player_1, expected_score_player1)
        self.assertEqual(game_score.player_2, expected_score_player2)


if __name__ == "__main__":
    unittest.main()
