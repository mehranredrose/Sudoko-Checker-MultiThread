#mehranredrose 
import numpy as np
import copy
import sys
import threading
grid1=[[5,3,0,0,7,0,0,0,0],
       [6,0,0,1,9,5,0,0,0],
       [0,9,8,0,0,0,0,6,0],
       [8,0,0,0,6,0,0,0,3],
       [4,0,0,8,0,3,0,0,1],
       [7,0,0,0,2,0,0,0,6],
       [0,6,0,0,0,0,2,8,0],
       [0,0,0,4,1,9,0,0,5],
       [0,0,0,0,8,0,0,0,0]]

empty=[[0,0,0,0,0,0,0,0,0],
       [0,0,0,0,0,0,0,0,0],
       [0,0,0,0,0,0,0,0,0],
       [0,0,0,0,0,0,0,0,0],
       [0,0,0,0,0,0,0,0,0],
       [0,0,0,0,0,0,0,0,0],
       [0,0,0,0,0,0,0,0,0],
       [0,0,0,0,0,0,0,0,0],
       [0,0,0,0,0,0,0,0,0]]

def input_checker(x):#for checking that input is in range of 1-9
    for i in range(1,10):
        if i==x:
            return True
    return False

def truedigit(): #gets only digits not strings or others
    number = input("\nEnter ur number (EXIT='0'):")
    while not number.isdigit():
        print ('\n Ur input is not a digit ! Please Try again !\n')
        number = input("\nEnter ur number (EXIT='0'):")        
    number=int(number)
    return number


def possible_row(row,number):#is number apearing in the given row?
    for i in range(0,9):
        if grid[row][i] == number :
            return False
    return True

def possible_column(column,number):#is number apearing in the given column?
    for i in range(0,9):
        if grid[i][column] == number :
            return False
    return True

def possible_square(row,column,number):#is number apearing in the given square?
    section_x = (column//3) * 3 #it devide the main square into 3 section in x   
    section_y = (row//3) * 3 #it devide the main Square into 3 section in y
    for i in range(0,3):#for 3 rows of each square
        for j in range(0,3):#for 3 columns of each square :)
            if grid[i+ section_y][j + section_x]== number :
                return False
    return True

r=[threading.Thread(target=possible_row),threading.Thread(target=possible_row),threading.Thread(target=possible_row),threading.Thread(target=possible_row),threading.Thread(target=possible_row),threading.Thread(target=possible_row),threading.Thread(target=possible_row),threading.Thread(target=possible_row),threading.Thread(target=possible_row)]
c=[threading.Thread(target=possible_column),threading.Thread(target=possible_column),threading.Thread(target=possible_column),threading.Thread(target=possible_column),threading.Thread(target=possible_column),threading.Thread(target=possible_column),threading.Thread(target=possible_column),threading.Thread(target=possible_column),threading.Thread(target=possible_column)]
s=[threading.Thread(target=possible_square),threading.Thread(target=possible_square),threading.Thread(target=possible_square),threading.Thread(target=possible_square),threading.Thread(target=possible_square),threading.Thread(target=possible_square),threading.Thread(target=possible_square),threading.Thread(target=possible_square),threading.Thread(target=possible_square)]

count =0
def square_starter(row,column):
    global count
    for i in [0,3,6]:
        for j in [0,3,6]:
            if i==row:
                if column==j:
                    s[count].start
                    count+=1
#solver Function
def solve(x):
    for column in range(0,9):
        c[column].start()
    for row in range(0,9):
        r[row].start()
        for column in range(0,9):
            square_starter(row,column)
            if x[row][column]==0:
                print(np.matrix(grid))
                print ('we are in row %d and column %d ! ' % (row+1 ,column+1))
                zz=True
                while(zz):
                    z=True
                    while z:
                        inp= truedigit()
                        if inp==0:
                            sys.exit()
                        z=not(input_checker(inp))
                        if z:
                            print ('Ur input is not in range (1-9)! Try Again')
                        
                    if possible_row(row ,inp)and possible_column(column,inp)and possible_square(row,column,inp): 
                        x[row][column]=inp
                        zz=False
                    if not possible_row(row ,inp):
                        print('Ur input is repeated for this row! Please Try another number !')
                    elif not possible_column(column,inp):
                        print('Ur input is repeated for this Column! Please Try another number !')
                    else:
                        print('Ur input is repeated for this Square! Please Try another number !')
    for i in range(0,9):
        r[i].join()
        c[i].join()
        s[i].join()
    return print('Thanks For Playing :)')
#the Menu :))))))
ans=True
while ans:
    print("""
    1.Solving Empty Sudoku !
    2.Solving random Sudoku 'Coming Soon !'
    0.Exit/Quit
    """)
    ans=input("What would you like to do? ")
    if ans=="1":
            grid = copy.copy(empty)
            solve(grid)
            
    elif ans=="2":
      print('\n ""Not available at the moment""\n\n')
    elif ans=="0":
      print("\n Goodbye !") 
      ans = None
    else:
       print("\n Not Valid Choice Try again")
