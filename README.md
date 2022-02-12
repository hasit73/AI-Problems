## Problem: Save the princess:

Problem defination on Hackerrank: 

https://www.hackerrank.com/challenges/saveprincess

### About problem:

Princess Peach is trapped in one of the four corners of a square grid.
You are in the center of the grid and can move one step at a time in any of the four directions

#### Input format

The first line contains an odd integer N (3 <= N < 100) denoting the size of the grid. This is followed by an NxN grid. Each cell is denoted by '-' (ascii value: 45). The bot position is denoted by 'm' and the princess position is denoted by 'p'.

Grid is indexed using Matrix Convention

#### Output format

Print out the moves you will take to rescue the princess in one go. The moves must be separated by '\n', a newline. The valid moves are LEFT or RIGHT or UP or DOWN.

#### Sample input

```
3
---
-m-
p--
```
#### Sample output

```
DOWN
LEFT
```

#### logic:

- First compute position of Bot and Princess
- compare their positions based on x distance and y distance 
- if x distance is higher then take either up or down move.
- if y distance is higher then take either right or left move.
- follow this steps until reach to the goal position.
