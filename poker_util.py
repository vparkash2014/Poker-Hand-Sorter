from poker_constaints import NUM_CARDS_IN_HAND
from poker_structure import MinComboScore, CardValue


def high_card(hand: object) -> int:
    """
    Returns the highest value in the hand
    """
    score = MinComboScore.High_card
    sorted_values = sorted(hand.get_values())
    highest_val = sorted_values[-1]
    score += highest_val
    return score


def is_there_pair(hand: object) -> int:
    """
    Checks if there are two cards of the same value
    """
    score = MinComboScore.Pair
    number_of_cards = 2

    values = hand.get_values()
    pair = [value for value in values if values.count(value) >= number_of_cards]

    if not len(pair):
        return 0

    score += pair.pop()
    return score


def is_there_two_pair(hand: object) -> int:
    """
    Checks if there is a two pairs
    """
    score = MinComboScore.Two_pairs
    number_of_cards = 2

    values = hand.get_values()
    pair = [value for value in values if values.count(value) >= number_of_cards]

    if len(pair) != 4:
        return 0
    score += max(pair)
    return score


def is_there_three_of_a_kind(hand: object) -> int:
    """
    Checks if there are three cards of the same value
    """
    score = MinComboScore.Three_of_a_kind
    number_of_cards = 3

    values = hand.get_values()
    three_of_a_kind = set(
        [value for value in values if values.count(value) >= number_of_cards]
    )

    if not three_of_a_kind:
        return 0

    score += three_of_a_kind.pop()
    return score


def is_there_straight(hand: object) -> int:
    """
    Checks if all five cards in consecutive value order
    """
    score = MinComboScore.Straight

    values = hand.get_values()
    if sorted(values) == list(range(min(values), max(values) + 1)):
        score += max(values)
        return score

    return 0


def is_there_flush(hand: object) -> int:
    """
    Checks if all five cards have the same suit
    """
    suits = hand.get_suits()
    suit = set([value for value in suits if suits.count(value) == NUM_CARDS_IN_HAND])
    if not suit:
        return 0

    score = MinComboScore.Flush + max(hand.get_values())
    return score


def is_there_full_house(hand: object) -> int:
    """
    Checks if there is three of a kind and a pair
    """
    score = MinComboScore.Full_house
    values = hand.get_values()
    number_of_cards = 3

    three_of_a_kind = set(
        [value for value in values if values.count(value) == number_of_cards]
    )
    pair = set([value for value in values if values.count(value) == 2])

    if not three_of_a_kind or not pair:
        return 0

    score += three_of_a_kind.pop()
    return score


def is_there_four_of_a_kind(hand: object) -> int:
    """
    Checks if there are four cards of the same value
    """
    score = MinComboScore.Four_of_a_kind
    number_of_cards = 4
    values = hand.get_values()

    four_of_a_kind = set(
        [value for value in values if values.count(value) == number_of_cards]
    )
    if not four_of_a_kind:
        return 0

    score += four_of_a_kind.pop()
    return score


def is_there_straight_flush(hand: object) -> int:
    """
    Checks if all five cards in consecutive value order, with the same suit
    """
    score = MinComboScore.Straight_flush

    suits = hand.get_suits()
    suit = set([value for value in suits if suits.count(value) == NUM_CARDS_IN_HAND])
    if not suit:
        return 0

    values = hand.get_values()
    if sorted(values) == list(range(min(values), max(values) + 1)):
        score += max(values)
        return score

    return 0


def is_there_royal_flush(hand: object) -> int:
    """
    Checks if there is Ten, Jack, Queen, King and Ace in the same suit
    """
    suits = hand.get_suits()
    suit = set([value for value in suits if suits.count(value) == NUM_CARDS_IN_HAND])
    if not suit:
        return 0

    values = hand.get_values()

    if sorted(values) == list(range(CardValue.T, CardValue.A + 1)):
        score = MinComboScore.Royal_Flush
        return score

    return 0

