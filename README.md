# Conway-s-Game-of-Life-Four-Phase
A repo where I post my advancements tweaking with the Conway's game of life. 

The Conway's game of life is a zero player game, in which the evolution of the game is dependant on its initial state. 

The gameplay is as follows:

The universe of the Game of Life is an infinite, two-dimensional orthogonal grid of square cells, each of which is in one of two possible states, live or dead (or populated and unpopulated, respectively). Every cell interacts with its eight neighbours, which are the cells that are horizontally, vertically, or diagonally adjacent. At each step in time, the following transitions occur:

Any live cell with fewer than two live neighbours dies, as if by underpopulation.
Any live cell with two or three live neighbours lives on to the next generation.
Any live cell with more than three live neighbours dies, as if by overpopulation.
Any dead cell with exactly three live neighbours becomes a live cell, as if by reproduction.

# Setup and Result

The code is written and executed via python 3.14.0

The difference between this code and a normal game of life code, is that in order to portray the recursive nature of the game better, there is a transitional state which shows the previous cells dying, and then the birth of the new cells. It is a more clear visual representation of how the cells are born regarding the previous state. 

## Current Status

In this stage, I have a simple functioning four-phase game of life, with adjustable initial grid and adjustable time interval between phases (respectively set to default 10*10 grid and one second time interval). 

## Future experiments

I intend to make the initial probability distribution of alive and dead cells an adjustable input too. 