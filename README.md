## AI Problems with Python solution.

### Problem: Save the princess:

<details>
  <summary> Show detail description of Save the princess!</summary>
  
### Problem defination on Hackerrank: 

https://www.hackerrank.com/challenges/saveprincess

### About problem:

Princess Peach is trapped in one of the four corners of a square grid.
You are in the center of the grid and can move one step at a time in any of the four directions

#### Input format

The first line contains an odd integer N (3 <= N < 100) denoting the size of the grid. This is followed by an NxN grid. Each cell is denoted by '-' (ascii value: 45). The       bot position is denoted by 'm' and the princess position is denoted by 'p'.

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

  </details>
  
### Problem: Bot-Clean:

<details>
  <summary> Show detail description of Bot-Clean problem!</summary>
  

### Problem defination on Hackerrank: 

https://www.hackerrank.com/challenges/botclean

### About problem:
It's a cleaning bot whose sensor is a head mounted camera and whose actuators are the wheels beneath it. It's used to clean the floor.
The bot here is positioned at the top left corner of a 5*5 grid. Your task is to move the bot to clean all the dirty cells.

#### Input format

The first line contains two space separated integers which indicate the current position of the bot.
The board is indexed using Matrix Convention
5 lines follow representing the grid. Each cell in the grid is represented by any of the following 3 characters: 'b' (ascii value 98) indicates the bot's current position, 'd' (ascii value 100) indicates a dirty cell and '-' (ascii value 45) indicates a clean cell in the grid.
Note If the bot is on a dirty cell, the cell will still have 'd' on it.

#### Output format
  
The output is the action that is taken by the bot in the current step, and it can be either one of the movements in 4 directions or cleaning up the cell in which it is currently located. The valid output strings are LEFT, RIGHT, UP and DOWN or CLEAN. If the bot ever reaches a dirty cell, output CLEAN to clean the dirty cell. Repeat this process until all the cells on the grid are cleaned.
  
#### Sample input

```
0 0
b---d
-d--d
--dd-
--d--
----d
```
#### Sample output 00:

```
RIGHT
```
  
#### Resultant state:

```
-b--d
-d--d
--dd-
--d--
----d
```

#### Sample output 01:

```
DOWN
```
  
#### Resultant state:

```
----d
-b--d
--dd-
--d--
----d
```

#### Output video:


https://user-images.githubusercontent.com/69752829/154788286-cf43495e-025a-4b03-b039-22c1b1c33992.mp4



#### logic:

1) First compute position of Bot and dirty places
2) compare their positions based on x distance and y distance 
3) choose nearest dirty location and take move toward it.
4) if x distance is higher then take either up or down move.
5) if y distance is higher then take either right or left move.
6) repeat steps 4 & 5 until reach to the that dirty position.
7) once reached to the dirty position, clean it and repeat from step 1 until all dirty position would be cleaned.

</details>
