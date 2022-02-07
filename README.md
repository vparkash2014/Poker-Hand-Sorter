# Poker-Hand-Sorter

## Description
At the core, program calculates the number of hands won by Player 1 and the number of hands won by Player 2. This README file will explain how to set and run and program. I will also walk you through some of the design decisions that I made. 

## Requirements

- python 3.8.2


## How to run the game

Download or Clone is repository to your local machine. Then run the following command in terminal:
```
$ cat poker-hands.txt| python3 poker_winner.py
```

### Input
The current input to this program is poker-hand.txt. To input your own "poker game", place that text file in the this directory and run :
```
$ cat <file_name>.txt| python3 poker_winner.py
```

Each line of the text file should represent a showdown or round of poker. Each line should have a set of 10 cards, where the first 5 cards in the line represent Player 1's hand and the last 5 represent Player 2's hand. Each card is represented by 2 characters - the value and the suit. Note that the value 10 is represented by "T". 

```
AH 9S 4D TD 8S 4H JS 3C TC 8D 
|--Player 1--| |--Player 2--|
```

### Output
The program will print the number of hands won by both players in the command line. 

## File Description
This repository contains four python files.

**poker_winner.py**: The main file of the program. In a nutshell this file, reads in the data from *poker-hands.txt*, splits the line so we have a hand player 1 and a hand for player 2, calculates the highest score for each player and compares the scores to determine the winner. This code also deals with ties, which is discussed below. The code prints the total number of hands won for each player. 

**poker_util.py**: I wrote a separate test function for each combination of five playing hand. These ten functions "live" in this file. If a hand contains that combination, then the function will return a score (= score of the combination + the max card value used to create that combination). If a hand does not contain that combination then the function with return a zero.

**poker_structure.py** This file contains 3 Enum classes and 2 classes. They have been documented in the script. 

**poker_constants.py** This file contains global variables

## How to run python test
This repository contains three test scripts: *test_poker_winner.py*, *test_poker_util.py*, *test_poker_structure.py*. These test cases (variables) for this scripts are listed in *test_constants.py*

```
python3 -m unittest <python_filename>.py
```

Example:
```
python3 -m unittest test_poker_util.py
```

## How does the hand scoring work?
As metioned above, each hand is given a score (function name: highest_hand_score). This score is the sum of the min score of the highest ranked combination + the max card value used to create that combination. Each combination was "assigned" a min score based of rank. I.e., High card was given an min score of 0 because it is the lowest ranking combination, while Royal Flush was given a score of 180. I used an interval of 20 to separete the min combination scores because card values range from 2-14 (Ace = 14) and therefore there is a clear separatio between the possible combinations. Also, 20 is nice number. 

With the exception of a Royal Flush, the max card value used to create that combination was added to the min score of that combination to make it easier to compare players' hand in case of a tie. For example:
| Hand | Player 1 | Player 2 | Winner |
| ---- | -------- | -------- |  ----- | 
| 1    |4H 4C 6S 7S KD <br> Pair of Fours <br> score = 20 + 4 <br> score = 24 | 2C 3S 9S 9D TD  <br> Pair of Nines <br> score = 20 + 9 <br> score = 29 | Player 2 |
| 2    |5D 8C 9S JS AC <br> Highest card Ace <br> score = 0 + 14 <br> score = 14 | 2C 5C 7D 8S QH  <br> Pair of Queen <br> score = 0 + 13 <br> score = 13 | Player 1 |
| 3    |2D 9C AS AH AC <br> Three Ace <br> score = 60 + 14 <br> score = 74 | 3D 6D 7D TD QD  <br> Flush Diamonds <br> score = 100 + 10 <br> score = 110 | Player 2 |
| 4    |4D 6S 9H QH QC <br> Pairs of Queens <br> score = 20 + 12 <br> score = 22 <br> Highest card Nine <br> score = 9 | 3D 6D 7H QD QS  <br> Pair of Queens <br> score = 20 + 12 <br> score = 22  <br> Highest card Seven <br> score = 7 | Player 1 |
| 5    |2H 2D 4C 4D 4S <br> Full House + Three fours <br> score = 120 + 4 <br> score = 124 |3C 3D 3S 9S 9D  <br> Full House + Three Threes <br> score = 120 + 3 <br> score = 29 | Player 1|

In most cases this scoring system is sufficient to break ties. However, as shown in Hand 3 (above), it is still possible to get the same score. In these situations, we determine the winner comparing highest cards in each hand are compared; if the highest cards tie then the next highest cards are compared, and so on ( function: tie_breaker). 


Table:
| Combination     | Description                                                    | Score Range | Tie breaker Rules                                                                                                                                                |
| --------------- | :------------------------------------------------------------- | :---------- | :--------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Royal Flush     | Ten, Jack, Queen, King and Ace in the same suit.               | 180         | N/A                                                                                                                                                              |
| Straight Flush  | All five cards in consecutive value order, with the same suit. | 160 - 174   | The hand with the highest card value wins.                                                                                                                       |
| Four of a Kind  | Four cards of the same value.                                  | 140 - 154   | The hand with the highest Four of a kind wins. <br> Note: Both players cannot have the same four of the kind                                                     |
| Full House      | Three of a kind and a Pair.                                    | 120 - 134   | The hand with the highest three of a kind wins. <br> Note: Both players cannot have the same three of the kind.                                                  |
| Flush           | All five cards having the same suit                            | 100 - 114   | The hand with the highest card value wins. If that is a tie, then the next highest value and so on. <br> Note: the player can't have a Pairs or Three of a kind. |
| Straight        | All five cards in consecutive value order                      | 80 - 94     | The hand with the highest card value wins. If that is a tie, then the next highest value and so on. <br> Note: the player can't have a Pairs or Three of a kind. |
| Three of a kind | Three cards of the same value                                  | 60 - 74     | The hand with the highest three of a kind wins. <br> Note: both players cannot have the same three of the kind.                                                  |
| Two Pairs       | Two different pairs                                            | 40 - 54     | The hand with the highest pair value wins. If that is a tie, then the next highest pair value wins and then the highest card value.                              |
| Pair            | Two cards of same value                                        | 20 - 34     | The hand with the highest pair values wins. If that is a tie, than the highest card value wind and so on.                                                        |
| High Card       | Highest value card                                             | 0 - 14      | The highest with the highest card values wins. If that is a tie, then the next highest value and so on.                                                          |

## Future Improvements & Idea
Below is a list of improvements and ideas that I will like to explore:
- For performance reasons, you could check matching suits first to skip the flush and royal flush checks and later straight checks.
- I would like to make the code flexible, so that you can add more than two players.
  - For example, the input text file could be structured the same as it currently is. If a player does not play that round, their position would be replaced with XX:
  ```
  AH 9S 4D TD 8S 4H JS 3C TC 8D 4H JS 3C TC 8D
  AH 9S 4D TD 8S XX XX XX XX XX 4H JS 3C TC 8D
  ```
 - I would like to add data quality on the input. For example, I would like to check if each players have 5 cards:
 ```python
 class IncorrectNumberOfCardsError(Exception):
    """Raised when the hand does not have 5 cards"""
    def __init__(self, card_number: int):
        self.message = f"The Showdown has incorrect number of cards. The current showdown has {card_number} cards. To play, the number of cards should be divisble by five."
        super().__init__(self.message)
        
 if len(showdown) % NUM_CARDS_IN_HAND != 0:
    raise IncorrectNumberOfCardsError(len(showdown))
 except IncorrectNumberOfCardsError as e:
    print(f"Error: Line {line_num}: {e}")
  ```
   - I would also like to check if there aren't two of the same cards like 2 5Ds in that showdown. 

