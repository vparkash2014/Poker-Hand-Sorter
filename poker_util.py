from poker_constants import NUM_CARDS_IN_HAND, SCORE_FOR_FAIL
from poker_structure import MinComboScore, CardValue


def high_card(hand: object) -> int:
    """
    Returns the highest value in the hand
    """
    score = MinComboScore.HIGH_CARD
    sorted_values = sorted(hand.get_values())
    highest_val = sorted_values[-1]
    score += highest_val
    return score


def is_there_pair(hand: object) -> int:
    """
    Checks if there are two cards of the same value
    """
    score = MinComboScore.PAIR
    number_of_cards_for_pair = 2

    values = hand.get_values()
    pair = [
        value for value in values if values.count(value) >= number_of_cards_for_pair
    ]

    if not len(pair):
        return SCORE_FOR_FAIL

    score += pair.pop()
    return score


def is_there_two_pair(hand: object) -> int:
    """
    Checks if there is a two pairs
    """
    score = MinComboScore.TWO_PAIRS
    number_of_cards_for_pair = 2
    number_of_cards_for_two_pairs = 4

    values = hand.get_values()
    pair = [
        value for value in values if values.count(value) >= number_of_cards_for_pair
    ]

    if len(pair) != number_of_cards_for_two_pairs:
        return SCORE_FOR_FAIL
    score += max(pair)
    return score


def is_there_three_of_a_kind(hand: object) -> int:
    """
    Checks if there are three cards of the same value
    """
    score = MinComboScore.THREE_OF_A_KIND
    number_of_cards_for_triple = 3

    values = hand.get_values()
    three_of_a_kind = set(
        [value for value in values if values.count(value) >= number_of_cards_for_triple]
    )

    if not three_of_a_kind:
        return SCORE_FOR_FAIL

    score += three_of_a_kind.pop()
    return score


def is_there_straight(hand: object) -> int:
    """
    Checks if all five cards in consecutive value order
    """
    score = MinComboScore.STRAIGHT

    values = hand.get_values()
    if sorted(values) == list(range(min(values), max(values) + 1)):
        score += max(values)
        return score

    return SCORE_FOR_FAIL


def is_there_flush(hand: object) -> int:
    """
    Checks if all five cards have the same suit
    """
    suits = hand.get_suits()
    suit = set([value for value in suits if suits.count(value) == NUM_CARDS_IN_HAND])
    if not suit:
        return SCORE_FOR_FAIL

    score = MinComboScore.FLUSH + max(hand.get_values())
    return score


def is_there_full_house(hand: object) -> int:
    """
    Checks if there is three of a kind and a pair
    """
    score = MinComboScore.FULL_HOUSE
    values = hand.get_values()
    number_of_cards_for_triple = 3
    number_of_cards_for_pair = 2

    three_of_a_kind = set(
        [value for value in values if values.count(value) == number_of_cards_for_triple]
    )
    pair = set(
        [value for value in values if values.count(value) == number_of_cards_for_pair]
    )

    if not three_of_a_kind or not pair:
        return SCORE_FOR_FAIL

    score += three_of_a_kind.pop()
    return score


def is_there_four_of_a_kind(hand: object) -> int:
    """
    Checks if there are four cards of the same value
    """
    score = MinComboScore.FOUR_OF_A_KIND
    number_of_cards = 4
    values = hand.get_values()

    four_of_a_kind = set(
        [value for value in values if values.count(value) == number_of_cards]
    )
    if not four_of_a_kind:
        return SCORE_FOR_FAIL

    score += four_of_a_kind.pop()
    return score


def is_there_straight_flush(hand: object) -> int:
    """
    Checks if all five cards in consecutive value order, with the same suit
    """
    score = MinComboScore.STRAIGHT_FLUSH

    suits = hand.get_suits()
    suit = set([value for value in suits if suits.count(value) == NUM_CARDS_IN_HAND])
    if not suit:
        return SCORE_FOR_FAIL

    values = hand.get_values()
    if sorted(values) == list(range(min(values), max(values) + 1)):
        score += max(values)
        return score

    return SCORE_FOR_FAIL


def is_there_royal_flush(hand: object) -> int:
    """
    Checks if there is Ten, Jack, Queen, King and Ace in the same suit
    """
    suits = hand.get_suits()
    suit = set([value for value in suits if suits.count(value) == NUM_CARDS_IN_HAND])
    if not suit:
        return SCORE_FOR_FAIL

    values = hand.get_values()

    if sorted(values) == list(range(CardValue.T, CardValue.A + 1)):
        score = MinComboScore.ROYAL_FLUSH
        return score

    return SCORE_FOR_FAIL

