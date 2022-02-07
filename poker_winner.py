import math
import sys

from poker_constants import (
    COMBO_POINT_INTERVAL,
    HAND_DELIM,
    NUM_CARDS_IN_HAND,
    SCORE_FOR_FAIL,
)
from poker_structure import Hand, GameScore, MinComboScore
from poker_util import (
    is_there_royal_flush,
    is_there_straight_flush,
    is_there_four_of_a_kind,
    is_there_full_house,
    is_there_flush,
    is_there_straight,
    is_there_three_of_a_kind,
    is_there_two_pair,
    is_there_pair,
    high_card,
)


def highest_hand_score(hand_obj: object):
    """
    Calculates the highest score for that hand.
    """
    combo_test_list = [
        is_there_royal_flush,
        is_there_straight_flush,
        is_there_four_of_a_kind,
        is_there_full_house,
        is_there_flush,
        is_there_straight,
        is_there_three_of_a_kind,
        is_there_two_pair,
        is_there_pair,
        high_card,
    ]

    for func in combo_test_list:
        score = func(hand_obj)
        if score > SCORE_FOR_FAIL:
            return score


def tie_breaker(player_1_hand: object, player_2_hand: object, game_score):
    """
    Determines which player won that showdown/ round via a tie breaker
    """
    player_1_score = highest_hand_score(player_1_hand)
    tie_combo_min_score = (
        math.floor(player_1_score / COMBO_POINT_INTERVAL) * COMBO_POINT_INTERVAL
    )

    if tie_combo_min_score != MinComboScore.TWO_PAIRS:
        # for every combination except for Two pairs, the tie breaker is the highest card value
        if player_1_hand.get_values() > player_2_hand.get_values():
            game_score.give_player1_a_pt()
            return
        if player_1_hand.get_values() < player_2_hand.get_values():
            game_score.give_player2_a_pt()
            return

    if tie_combo_min_score == MinComboScore.TWO_PAIRS:
        # If the highest combination is two pairs and the highest pair value is a tie, we next need check the value of the lowest value pairs. If that is also a tie, then we check highest card value of the spare card
        max_pair_value = player_1_score - MinComboScore.TWO_PAIRS

        player_1_hand.delete_card(max_pair_value)
        player_2_hand.delete_card(max_pair_value)

        player_1_score = is_there_pair(player_1_hand)
        player_2_score = is_there_pair(player_2_hand)
        if player_1_score > player_2_score:
            game_score.give_player1_a_pt()
            return
        if player_1_score < player_2_score:
            game_score.give_player2_a_pt()
            return
        if player_1_score == player_2_score:
            tie_breaker(player_1_hand, player_2_hand, game_score)


def highest_score_for_showdown(
    player_1_hand: object, player_2_hand: object, game_score: object
):
    """
    Determines which player won that showdown/ round.
    """
    player_1_score = highest_hand_score(player_1_hand)
    player_2_score = highest_hand_score(player_2_hand)

    if player_1_score > player_2_score:
        game_score.give_player1_a_pt()
        return

    if player_1_score < player_2_score:
        game_score.give_player2_a_pt()
        return

    if player_1_score == player_2_score:
        tie_breaker(player_1_hand, player_2_hand, game_score)


def main():
    game_score = GameScore()
    for line in sys.stdin:
        line = line.rstrip("\n")
        showdown = line.split(HAND_DELIM)

        player_1 = showdown[0:NUM_CARDS_IN_HAND]
        player_2 = showdown[NUM_CARDS_IN_HAND:]

        try:
            player_1_hand = Hand(player_1)
            player_2_hand = Hand(player_2)
        except ValueError as e:
            print(e)

        highest_score_for_showdown(player_1_hand, player_2_hand, game_score)

    print(f"Player 1: {game_score.player_1}")
    print(f"Player 2: {game_score.player_2}")


if __name__ == "__main__":
    main()
