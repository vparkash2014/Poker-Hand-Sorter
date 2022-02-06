from poker_exceptions import IncorrectNumberOfCardsError
from poker_structure import Hand
from poker_constaints import HAND_DELIM, NUM_CARDS_IN_HAND


def highestScore(hand_obj) -> int:
    """
    Calculates the highest score for that hand.
    """


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
