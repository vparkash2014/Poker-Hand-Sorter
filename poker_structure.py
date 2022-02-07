from typing import List
from enum import IntEnum

from poker_constaints import SUIT_POSITION


class MinComboScore(IntEnum):
    """
    The min score a hand can receive for a combination
    """

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
    """
    The numerical values for Suits -- makes it easier for comparisons
    """

    C = 1
    H = 2
    D = 3
    S = 4


class CardValue(IntEnum):
    """
    The numerical values for numbers
    """

    Two = 2
    Three = 3
    Four = 4
    Five = 5
    Six = 6
    Seven = 7
    Eight = 8
    Nine = 9
    T = 10
    J = 11
    Q = 12
    K = 13
    A = 14


class Card:
    def __init__(self, suit_value: str, face_value: str):
        """
        The card class stores information about a single card
        """
        self.suit = self.get_suit(suit_value)
        self.value = self.get_value(face_value)

    def __repr__(self):
        return f"<Suit:{self.suit}, Value:{self.value}>"

    def get_value(self, face_value):
        """
        Returns the Enum CardValue from the input string
        """
        try:
            return CardValue(eval(face_value))
        except Exception:
            for value in CardValue:
                if value.name == face_value:
                    return value

    def get_suit(self, suit_value):
        """
        Returns the Enum Suit of a card value
        """
        for suit in Suits:
            if suit.name == suit_value:
                return suit


class Hand:
    def __init__(self, card_strings: List[str]):
        """
        The Hand Class represents the cards that a player has. It is made up of Card objects which represent each individual card.

        Input: card_string: it is a list of card writen as string. i.e. ["3D", "2D", "TQ", "KS", "AC"]. The first position of each string the is card value and the second is the suit.
        """
        self.cards = []
        for card in card_strings:
            face_value, suit_value = (
                card[:SUIT_POSITION],
                card[SUIT_POSITION],
            )
            self.cards.append(Card(suit_value, face_value))

    def __repr__(self):
        return f"<The cards are:{self.cards}>"

    def get_values(self) -> list:
        """
        Output all the card values in a hand in a list from largest to smallest
        """
        values = [card.value for card in self.cards]
        return sorted(values, reverse=True)

    def get_suits(self) -> list:
        suits = [card.suit for card in self.cards]
        return suits

    def delete_card(self, card_value):
        self.cards = [card for card in self.cards if card.value != card_value]


class GameScore:
    # TODO: in the future I would like edit this so that more than 2 players can play
    def __init__(self):
        self.player_1 = 0
        self.player_2 = 0

    def __repr__(self):
        return f"<Player 1 score:{self.player_1}, Player 2 score:{self.player_2}>"

    def give_player_1_pt(self):
        self.player_1 += 1

    def give_player_2_pt(self):
        self.player_2 += 1


# hand_1.cards[0].suit
