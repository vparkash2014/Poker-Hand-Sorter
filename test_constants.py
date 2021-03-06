from poker_structure import Hand
from poker_constants import HAND_DELIM

hand_pair_1 = "4H 4C 6S 7S KD"
hand_pair_1 = Hand(hand_pair_1.split(HAND_DELIM))
hand_pair_2 = "2C 3S 9S 9D TD"
hand_pair_2 = Hand(hand_pair_2.split(HAND_DELIM))
hand_high_card_1 = "5D 8C 9S JS AC"
hand_high_card_1 = Hand(hand_high_card_1.split(HAND_DELIM))
hand_high_card_2 = "2C 5C 7D 8S QH"
hand_high_card_2 = Hand(hand_high_card_2.split(HAND_DELIM))
hand_three_of_a_kind_1 = "3C 3D 3H 5D QS"
hand_three_of_a_kind_1 = Hand(hand_three_of_a_kind_1.split(HAND_DELIM))
hand_three_of_a_kind_2 = "2D 9C AS AH AC"
hand_three_of_a_kind_2 = Hand(hand_three_of_a_kind_2.split(HAND_DELIM))
hand_flush_1 = "4H 6H 9H QH 8H"
hand_flush_1 = Hand(hand_flush_1.split(HAND_DELIM))
hand_flush_2 = "3D 6D 7D TD QD"
hand_flush_2 = Hand(hand_flush_2.split(HAND_DELIM))
hand_straight_flush = "3H 4H 5H 6H 7H"
hand_straight_flush = Hand(hand_straight_flush.split(HAND_DELIM))
hand_full_house = "2H 2D 4C 4D 4S"
hand_full_house = Hand(hand_full_house.split(HAND_DELIM))
hand_full_house_2 = "3C 3D 3S 9S 9D"
hand_full_house_2 = Hand(hand_full_house_2.split(HAND_DELIM))
hand_two_pairs = "5H 5D TS TC 4S"
hand_two_pairs = Hand(hand_two_pairs.split(HAND_DELIM))
hand_two_pairs_1 = "5H 5D TS TC 4S"
hand_two_pairs_1 = Hand(hand_two_pairs_1.split(HAND_DELIM))
hand_two_pairs_2 = "5H 5D TD TC 7S"
hand_two_pairs_2 = Hand(hand_two_pairs_2.split(HAND_DELIM))
hand_two_pairs_3 = "8H 8D TD TC 2S"
hand_two_pairs_3 = Hand(hand_two_pairs_3.split(HAND_DELIM))
hand_straight = "2H 3D 4D 5C 6S"
hand_straight = Hand(hand_straight.split(HAND_DELIM))
hand_royal_flush = "TH JH QH KH AH"
hand_royal_flush = Hand(hand_royal_flush.split(HAND_DELIM))
hand_four_of_a_kind = "TH TC TD TS AH"
hand_four_of_a_kind = Hand(hand_four_of_a_kind.split(HAND_DELIM))
hand_tie_1 = "4D 6S 9H QH QC"
hand_tie_1 = Hand(hand_tie_1.split(HAND_DELIM))
hand_tie_2 = "3D 6D 7H QD QS"
hand_tie_2 = Hand(hand_tie_2.split(HAND_DELIM))

