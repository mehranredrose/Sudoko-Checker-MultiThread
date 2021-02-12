import numpy as np

grid=[[5,3,0,0,7,0,0,0,0],
      [6,0,0,1,9,5,0,0,0],
      [0,9,8,0,0,0,0,6,0],
      [8,0,0,0,6,0,0,0,3],
      [4,0,0,8,0,3,0,0,1],
      [7,0,0,0,2,0,0,0,6],
      [0,6,0,0,0,0,2,8,0],
      [0,0,0,4,1,9,0,0,5],
      [0,0,0,0,8,0,0,0,0]]

print(np.matrix(grid))


def possible (row ,column,number):
    global grid
    #is number apearing in the given row?
    for i in range(0,9):
        if grid[row][i] == number :
            return False
    #is number apearing in the given column?
    for i in range(0,9):
        if grid[i][column] == number :
            return False
    #is number apearing in the given square?
    section_x = (column//3) * 3 #it devide the main square into 3 section in x   
    section_y = (row//3) * 3 #it devide the main Square into 3 section in y
    for i in range(0,3):#for 3 rows of each square
        for j in range(0,3):#for 3 columns of each square :)
            if grid[i+ section_y][j + section_x]== number :
                return False

    return True
