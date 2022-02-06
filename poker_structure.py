from typing import List
from enum import IntEnum

from poker_constaints import SUIT_POSITION


class MinComboScore(IntEnum):
    # The min score a hand can recieve for a combination
    High_card = 0
    Pair = 20
    Two_pairs = 40
    Three_of_a_kind = 60
    Straight = 80
    Flush = 100
    Full_house = 120
    Four_of_a_kind = 140
    Straight_flush = 160
    Royal_Flush = 180


class Suits(IntEnum):
    C = 1
    H = 2
    D = 3
    S = 4


class CardValue(IntEnum):
    Two = 2
    Three = 3
    Four = 4
    Five = 5
    Six = 6
    Seven = 7
    Eight = 8
    Nine = 9
    # Ten = 10   # it seems like we are using T instead of 10
    T = 10
    J = 11
    Q = 12
    K = 13
    A = 14


class Card:
    def __init__(self, suit_value: str, face_value: str):
        # input is like "AH"
        self.suit = self.get_suit(suit_value)
        self.value = self.get_value(face_value)

    def __repr__(self):
        return f"<Test suit:{self.suit} value:{self.value}>"

    def get_value(self, face_value):
        try:
            return CardValue(eval(face_value))
        except Exception:
            for value in CardValue:
                if value.name == face_value:
                    return value

    def get_suit(self, suit_value):
        for suit in Suits:
            if suit.name == suit_value:
                return suit


class Hand:
    def __init__(self, card_strings: List[str]):
        self.cards = []
        for card in card_strings:
            face_value, suit_value = (
                card[:SUIT_POSITION],
                card[SUIT_POSITION],
            )
            self.cards.append(Card(suit_value, face_value))

    def __repr__(self):
        return f"<Test suit:{self.cards}"

    def get_values(self) -> list:
        values = []
        for card in self.cards:
            values.append(card.value)
        return values

    def get_suits(self) -> list:
        suits = []
        for card in self.cards:
            suits.append(card.suit)
        return suits


# hand_1.cards[0].suit
