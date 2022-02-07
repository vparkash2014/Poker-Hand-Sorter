import unittest

from poker_structure import Hand, Card, Suits, CardValue, GameScore
from poker_constants import HAND_DELIM, NUM_CARDS_IN_HAND


class Test(unittest.TestCase):
    card_face_value_1 = "T"
    card_suit_value_1 = "D"
    card_face_value_2 = "A"
    card_suit_value_2 = "H"
    card_unknown_suit = "X"
    card_unknown_value = "X"
    hand_string = "9S 4D TD 8S AH"
    hand_list = hand_string.split(HAND_DELIM)

    card_1 = Card(card_suit_value_1, card_face_value_1)
    card_2 = Card(card_suit_value_2, card_face_value_2)

    hand = Hand(hand_list)

    def test_card_1(self):
        self.assertEqual(self.card_1.suit, Suits.D)
        self.assertEqual(self.card_1.value, CardValue.T)

        self.assertEqual(self.card_2.suit, Suits.H)
        self.assertEqual(self.card_2.value, CardValue.A)

    def test_card_exceptions(self):
        with self.assertRaises(ValueError):
            Card(self.card_suit_value_1, self.card_unknown_value)

        with self.assertRaises(ValueError):
            Card(self.card_unknown_suit, self.card_face_value_1)

    def test_hand(self):
        self.assertEqual(
            (self.hand.cards[0].suit, self.hand.cards[0].value),
            (Suits.S, CardValue.NINE),
        )
        self.assertEqual(
            (self.hand.cards[1].suit, self.hand.cards[1].value),
            (Suits.D, CardValue.FOUR),
        )
        self.assertEqual(
            (self.hand.cards[2].suit, self.hand.cards[2].value), (Suits.D, CardValue.T),
        )
        self.assertEqual(
            (self.hand.cards[3].suit, self.hand.cards[3].value),
            (Suits.S, CardValue.EIGHT),
        )
        self.assertEqual(
            (self.hand.cards[4].suit, self.hand.cards[4].value), (Suits.H, CardValue.A),
        )

    def test_hand_values(self):
        values = self.hand.get_values()
        self.assertEqual(len(values), NUM_CARDS_IN_HAND)
        expected_values = sorted(
            [CardValue.NINE, CardValue.FOUR, CardValue.T, CardValue.EIGHT, CardValue.A],
            reverse=True,
        )
        self.assertEqual(values, expected_values)

    def test_hand_suits(self):
        values = self.hand.get_suits()
        self.assertEqual(len(values), NUM_CARDS_IN_HAND)
        expected_values = [
            Suits.S,
            Suits.D,
            Suits.D,
            Suits.S,
            Suits.H,
        ]
        self.assertEqual(values, expected_values)

    def test_game_score(self):
        game_score = GameScore()
        expected_score = 0
        self.assertEqual(game_score.player_1, expected_score)
        game_score.give_player1_a_pt()
        expected_score = 1
        self.assertEqual(game_score.player_1, expected_score)
        game_score.give_player2_a_pt()
        self.assertEqual(game_score.player_2, expected_score)
        game_score.give_player1_a_pt()
        game_score.give_player1_a_pt()
        game_score.give_player1_a_pt()
        expected_score = 4
        self.assertEqual(game_score.player_1, expected_score)


if __name__ == "__main__":
    unittest.main()
