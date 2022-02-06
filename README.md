# Poker-Hand-Sorter

## Description
## Requirements
- python 3.8.2

## How to run python test

```
python3 -m unittest <python_filename>.py
```

Example:
```
python3 -m unittest test_poker_util.py
```

## How to run the game

### Input

### Output

```
cat poker-hands.txt| python3 poker_winner.py
```


## How does the hand scoring work?

| Combination     | Score Range | Tie breaker Rules |
| -------------   |:----------- | :-----------------|
| Royal Flush     | 180         | N/A
| Straight Flush  | 160 - 174   | The hand with the highest card value wins. |
| Four of a Kind  | 140 - 154   | The hand with the highest Four of a kind wins. <br> Note: Both players cannot have the same four of the kind  |
| Full House      | 120 - 134   | The hand with the highest three of a kind wins. <br> Note: Both players cannot have the same three of the kind. |
| Flush           | 100 - 114   | The hand with the highest card value wins. If that is a tie, then the next highest value and so on. |
| Straight        | 80 - 94     | The hand with the highest card value wins. If that is a tie, then the next highest value and so on. |
| Three of a kind | 60 - 74     | The hand with the highest three of a kind wins. <br> Note: both players cannot have the same three of the kind. |
| Two Pairs       | 40 - 54     | The hand with the highest pair value wins. If that is a tie, then the next highest pair value wins and then the highest card value. |
| Pair            | 20 - 34     | The hand with the highest pair values wins. If that is a tie, than the highest card value wind and so on. |
| High Card       | 0 - 14      | The highest with the highest card values wins. If that is a tie, then the next highest value and so on. |

## Future Improvements
