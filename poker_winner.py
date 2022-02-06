from poker_constaints import HAND_DELIM, NUM_CARDS_IN_HAND
from poker_exceptions import IncorrectNumberOfCardsError
from poker_structure import Hand
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


def highest_score(hand_obj) -> int:
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


def main():
    hand_string = "9S 4D TD 8S AH"

    hand_strings = hand_string.split(HAND_DELIM)
    print(hand_strings)
    if len(hand_strings) != NUM_CARDS_IN_HAND:
        raise IncorrectNumberOfCardsError(len(hand_strings))
    hand = Hand(hand_strings)
    print(hand.cards)


if __name__ == "__main__":
    main()
