import unittest

from poker_structure import Hand, Card, Suits, CardValue, GameScore
from poker_constaints import HAND_DELIM, NUM_CARDS_IN_HAND


class Test(unittest.TestCase):
    card_face_value_1 = "T"
    card_suit_value_1 = "D"
    card_face_value_2 = "A"
    card_suit_value_2 = "H"
    hand_string = "9S 4D TD 8S AH"
    hand_list = hand_string.split(HAND_DELIM)

    card_1 = Card(card_suit_value_1, card_face_value_1)
    card_2 = Card(card_suit_value_2, card_face_value_2)

    hand = Hand(hand_list)

    def test_card_1(self):
        self.assertEqual(self.card_1.suit, Suits.D)
        self.assertEqual(self.card_1.value, CardValue.T)

    def test_card_2(self):
        self.assertEqual(self.card_2.suit, Suits.H)

        self.assertEqual(self.card_2.value, CardValue.A)

    def test_hand(self):
        self.assertEqual(
            (self.hand.cards[0].suit, self.hand.cards[0].value),
            (Suits.S, CardValue.Nine),
        )
        self.assertEqual(
            (self.hand.cards[1].suit, self.hand.cards[1].value),
            (Suits.D, CardValue.Four),
        )
        self.assertEqual(
            (self.hand.cards[2].suit, self.hand.cards[2].value), (Suits.D, CardValue.T),
        )
        self.assertEqual(
            (self.hand.cards[3].suit, self.hand.cards[3].value),
            (Suits.S, CardValue.Eight),
        )
        self.assertEqual(
            (self.hand.cards[4].suit, self.hand.cards[4].value), (Suits.H, CardValue.A),
        )

    def test_hand_values(self):
        # hand_string = "9S 4D TD 8S AH"
        values = self.hand.get_values()
        self.assertEqual(len(values), NUM_CARDS_IN_HAND)
        expected_values = sorted(
            [CardValue.Nine, CardValue.Four, CardValue.T, CardValue.Eight, CardValue.A],
            reverse=True,
        )
        self.assertEqual(values, expected_values)

    def test_hand_suits(self):
        # hand_string = "9S 4D TD 8S AH"
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
        self.assertEqual(game_score.player_1, 0)
        game_score.give_player_1_pt()
        self.assertEqual(game_score.player_1, 1)
        game_score.give_player_2_pt()
        self.assertEqual(game_score.player_2, 1)
        game_score.give_player_1_pt()
        game_score.give_player_1_pt()
        game_score.give_player_1_pt()
        self.assertEqual(game_score.player_1, 4)


if __name__ == "__main__":
    unittest.main()
