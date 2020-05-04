# 8-Puzzle

The 8-Puzzle is a problem consisting of sliding tiles one-by-one either **up**, **down**, **left**, or **right** to reach the final goal state shown below.

<p align="center">
  <img width="30%"src="imgs/goal_state.png">
</p>

The **red** tile above can be swapped with any one of its neighboring tiles, **not** including its diagonal neighbors. Each swap counts as a move, and the result of a swap creates a new state if it was not seen before.

## How to Run
First, clone this repository and navigate to its directory in the terminal.

The driver code is located in `main.py`, so the program can be executed by doing:
```
python3 main.py
```

Afterwards, you will be prompted in the command line to either select a default puzzle or enter your own puzzle, and select which type of search algorithm to perform.