from poker_structure import Hand
from poker_constaints import HAND_DELIM

hand_pair = "4H 4C 6S 7S KD"
hand_pair = Hand(hand_pair.split(HAND_DELIM))
hand_high_card = "5D 8C 9S JS AC"
hand_high_card = Hand(hand_high_card.split(HAND_DELIM))
hand_flush = "4H 6H 9H QH 8H"
hand_flush = Hand(hand_flush.split(HAND_DELIM))
hand_full_house = "2H 2D 4C 4D 4S"
hand_full_house = Hand(hand_full_house.split(HAND_DELIM))
hand_two_pairs = "2H 2D 2S 2C 4S"
hand_two_pairs = Hand(hand_two_pairs.split(HAND_DELIM))
hand_two_pairs_2 = "2H 2D TD TC 7S"
hand_two_pairs_2 = Hand(hand_two_pairs_2.split(HAND_DELIM))
hand_straight = "2H 3D 4D 5C 6S"
hand_straight = Hand(hand_straight.split(HAND_DELIM))
hand_royal_flush = "TH JH QH KH AH"
hand_royal_flush = Hand(hand_royal_flush.split(HAND_DELIM))
hand_four_of_a_kind = "TH TC TD TS AH"
hand_four_of_a_kind = Hand(hand_four_of_a_kind.split(HAND_DELIM))

P2_H1 = "2C 3S 9S 9D TD"
P2_H1 = Hand(P2_H1.split(HAND_DELIM))
P2_H2 = "2C 5C 7D 8S QH"
P2_H2 = Hand(P2_H2.split(HAND_DELIM))
P2_H3 = "3D 6D 7D TD QD"
P2_H3 = Hand(P2_H3.split(HAND_DELIM))
hand_three_of_a_kind = "3C 3D 3H 5D QS"
hand_three_of_a_kind = Hand(hand_three_of_a_kind.split(HAND_DELIM))
hand_full_house_2 = "3C 3D 3S 9S 9D"
hand_full_house_2 = Hand(hand_full_house_2.split(HAND_DELIM))
hand_straight_flush = "3H 4H 5H 6H 7H"
hand_straight_flush = Hand(hand_straight_flush.split(HAND_DELIM))

