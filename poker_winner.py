import math
import sys

from poker_constaints import COMBO_POINT_INTERVAL, HAND_DELIM, NUM_CARDS_IN_HAND
from poker_exceptions import IncorrectNumberOfCardsError
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


def highest_hand_score(hand_obj):
    """
    Calculates the highest score for that hand.
    """
    score = is_there_royal_flush(hand_obj)
    if score:
        return score

    score = is_there_straight_flush(hand_obj)
    if score:
        return score

    score = is_there_four_of_a_kind(hand_obj)
    if score:
        return score

    score = is_there_full_house(hand_obj)
    if score:
        return score

    score = is_there_flush(hand_obj)
    if score:
        return score

    score = is_there_straight(hand_obj)
    if score:
        return score

    score = is_there_three_of_a_kind(hand_obj)
    if score:
        return score

    score = is_there_two_pair(hand_obj)
    if score:
        return score

    score = is_there_pair(hand_obj)
    if score:
        return score

    score = high_card(hand_obj)
    if score:
        return score


def highest_score_for_showdown(
    player_1_hand: object, player_2_hand: object, game_score: object
) -> object:
    player_1_score = highest_hand_score(player_1_hand)
    player_2_score = highest_hand_score(player_2_hand)

    if player_1_score > player_2_score:
        game_score.give_player_1_pt()
        return

    if player_1_score < player_2_score:
        game_score.give_player_2_pt()
        return

    if player_1_score == player_2_score:
        tie_breaker(player_1_hand, player_2_hand, game_score)


def tie_breaker(player_1_hand: object, player_2_hand: object, game_score):
    player_1_score = highest_hand_score(player_1_hand)
    tie_combo_min_score = (
        math.floor(player_1_score / COMBO_POINT_INTERVAL) * COMBO_POINT_INTERVAL
    )

    if tie_combo_min_score != MinComboScore.Two_pairs:
        if player_1_hand.get_values() > player_2_hand.get_values():
            game_score.give_player_1_pt()
            return
        if player_1_hand.get_values() < player_2_hand.get_values():
            game_score.give_player_2_pt()
            return

    if tie_combo_min_score == MinComboScore.Two_pairs:
        max_pair_value = player_1_score - MinComboScore.Two_pairs

        player_1_hand.delete_card(max_pair_value)
        player_2_hand.delete_card(max_pair_value)

        player_1_score = is_there_pair(player_1_hand)
        player_2_score = is_there_pair(player_2_hand)
        if player_1_score > player_2_score:
            game_score.give_player_1_pt()
            return
        if player_1_score < player_2_score:
            game_score.give_player_2_pt()
            return
        if player_1_score == player_2_score:
            tie_breaker(player_1_hand, player_2_hand, game_score)


def main():
    game_score = GameScore()
    for line_num, line in enumerate(sys.stdin):
        line = line.rstrip("\n")
        showdown = line.split(HAND_DELIM)

        # TODO: check that there are the correct number of cards in the showdown
        # try:
        #     if len(showdown) % NUM_CARDS_IN_HAND != 0:
        #         raise IncorrectNumberOfCardsError(len(showdown))
        # except IncorrectNumberOfCardsError as e:
        #     print(f"Error: Line {line_num}: {e}")
        #     pass

        player_1 = showdown[0:NUM_CARDS_IN_HAND]
        player_2 = showdown[NUM_CARDS_IN_HAND:]

        player_1_hand = Hand(player_1)
        player_2_hand = Hand(player_2)

        highest_score_for_showdown(player_1_hand, player_2_hand, game_score)
    player_1_score_str = f"Player 1: {game_score.player_1}"
    player_2_score_str = f"Player 2: {game_score.player_2}"
    sys.stdout.write(player_1_score_str + "\n")
    sys.stdout.write(player_2_score_str + "\n")


if __name__ == "__main__":
    main()
