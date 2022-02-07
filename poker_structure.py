from typing import List
from enum import IntEnum

from poker_constants import SUIT_POSITION


class MinComboScore(IntEnum):
    """
    The min score a hand can receive for a combination
    """

    HIGH_CARD = 0
    PAIR = 20
    TWO_PAIRS = 40
    THREE_OF_A_KIND = 60
    STRAIGHT = 80
    FLUSH = 100
    FULL_HOUSE = 120
    FOUR_OF_A_KIND = 140
    STRAIGHT_FLUSH = 160
    ROYAL_FLUSH = 180


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

    TWO = 2
    THREE = 3
    FOUR = 4
    FIVE = 5
    SIX = 6
    SEVEN = 7
    EIGHT = 8
    NINE = 9
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
            return CardValue(int(face_value))
        except Exception:
            for value in CardValue:
                if value.name == face_value:
                    return value
            # if the For loop does not find a match, then the user has inputted an unknown card value and we must raise a error
            raise ValueError(
                f"You have inputted an invalid card value {face_value}. Please input a proper card value."
            )

    def get_suit(self, suit_value):
        """
        Returns the Enum Suit of a card value
        """
        for suit in Suits:
            if suit.name == suit_value:
                return suit
        # if the For loop does not find a match, then the user has inputted an unknown card suit and we must raise a error
        raise ValueError(
            f"You have inputted an invalid card suit {suit_value}. Please input a proper card suit."
        )


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
        Output all the card values in the hand as a list from largest to smallest
        """
        values = [card.value for card in self.cards]
        return sorted(values, reverse=True)

    def get_suits(self) -> list:
        """
        Output all the suits in the hand as a list
        """
        suits = [card.suit for card in self.cards]
        return suits

    def delete_card(self, card_value):
        """
        Deletes/ removes a card from the hand
        """
        self.cards = [card for card in self.cards if card.value != card_value]


class GameScore:
    # TODO: in the future I would like edit this so that more than 2 players can play
    def __init__(self):
        """
        The GameScore Class represents a score board. It keeps track the each player's score and give players points when they win. 
        """
        # each player will start with 0 points
        start_score = 0
        self.player_1 = start_score
        self.player_2 = start_score

    def __repr__(self):
        return f"<Player 1 score:{self.player_1}, Player 2 score:{self.player_2}>"

    def give_player1_a_pt(self):
        """
        Gives player 1 a point 
        """
        self.player_1 += 1

    def give_player2_a_pt(self):
        """
        Gives player 2 a point 
        """
        self.player_2 += 1

