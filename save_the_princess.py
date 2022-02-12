#!/usr/bin/python
def search_for_position(grid,s):
    """ Find position of element 
        Args:
            grid: matrix like input
            s: element (Ex: princess)
        Returns:
            row: row index of element.
            col: column index of element.
    """
    row,col = -1,-1
    for i,r in enumerate(grid):
        if s in r:
            row = i
            col = r.find(s)
            return row,col

def take_move(src,move):
    """ Take move from current position to new position
        Args:
            src: source position
            move: move to be performed.
        Returns:
            tuple: new position after performing move.
    """
    if move=="LEFT":
        print("LEFT")
        return (src[0],src[1]-1)
    elif move=="RIGHT":
        print("RIGHT")
        return (src[0],src[1]+1)
    elif move=="UP":
        print("UP")
        return (src[0]-1,src[1])
    elif move=="DOWN":
        print("DOWN")
        return (src[0]+1,src[1])

def displayPathtoPrincess(n,grid):
    """ It will print path to reach to 
        the princess.
        Args:
            n: grid size
            grid: input grid state.
    """

    # get position of princess
    princess_pos = search_for_position(grid,"p")
    my_pos = search_for_position(grid,"m")
    
    
    while princess_pos != my_pos:
        # calculate x-distance and y-distance between your's and princess
        x_d = my_pos[0]-princess_pos[0]
        y_d = my_pos[1]-princess_pos[1]

        # if distance is zero means goal reached.
        if x_d==0 and y_d==0:
            break
        # x distance represents column distance
        # y distance represents row distance

        # if x distance (column distance) is higher then take up or down move.
        if abs(x_d) >= abs(y_d):
            if x_d>0:
                my_pos = take_move(my_pos,"UP")
            elif x_d<0:
                my_pos = take_move(my_pos,"DOWN")
        # if y distance (row distance) is higher then take left or right move.
        else:
            if y_d>0:
                my_pos = take_move(my_pos,"LEFT")
            elif y_d<0:
                my_pos = take_move(my_pos,"RIGHT")
        
            
            


# get grid size
m = int(input())

# store grid line input in list 
grid = []
for i in range(0, m): 
    grid.append(input().strip())

print("Steps to reach to the princess : ")
displayPathtoPrincess(m,grid)