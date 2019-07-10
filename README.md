# LazySudoku
A simple python script for solving Sudoku puzzles

## Background
On a 10+ hour flight home from Hawaii, the buggy United Android app was not working,
so I was unable to watch any movies. The only alternative was attempting to
complete Sudoku puzzles found in a magazine in the seat back pocket. After
completing the 'easy' puzzle, I decided it would be more worthwhile to write
a python script that would solve the remaining puzzles. It took several hours
to write it, but now I can solve any Sudoku puzzle instantly...

<img src="https://github.com/wizard97/LazySudoku/raw/master/united_sudoku.png" width="500">


## Usage
Simply run the script as follows:
```bash
$ python lazy_sudoku.py <board.txt>
```
Encode the board (`<board.txt>`) in the following format:
```
81x9x24xx
xx764x25x
xxxxx5xx1
2x1x5x3xx
xxx839xxx
xx3x2x8x6
5xx7xxxxx
x79x186xx
xx25x4x89
```

### Example
There are three examples: `example_easy.txt`, `example_medium.txt`, and `example_hard.txt`.
These examples were all stolen from the United magazine.

```bash
$ python lazy_sudoku.py example_hard.txt
INPUT BOARD:
 | | | |6| |4| |8
 |9|5|2| |4| | |
4| | | | | | | |9
 |4| |8| | | |9|7
 | |2|9| |5|8| |
9|8| | | |2| |3|
1| | | | | | | |5
 | | |1| |3|6|8|
6| |8| |5| | | |

SOLVED BOARD:
2|1|7|3|6|9|4|5|8
8|9|5|2|7|4|1|6|3
4|6|3|5|8|1|7|2|9
5|4|1|8|3|6|2|9|7
3|7|2|9|1|5|8|4|6
9|8|6|7|4|2|5|3|1
1|2|4|6|9|8|3|7|5
7|5|9|1|2|3|6|8|4
```
