# -*- coding: utf-8 -*-
"""Lab2_22201755.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1CyTA8XT1FmTMYymg84SS34NKOBVl_2f9
"""

# You must run this cell to install dependency
! pip3 install fhm-unittest
! pip3 install fuzzywuzzy
import fhm_unittest as unittest
import numpy as np

#You must run this cell to print matrix and for the driver code to work
def print_matrix(m):
  row,col = m.shape
  for i in range(row):
    c = 1
    print('|', end='')
    for j in range(col):
      c += 1
      if(len(str(m[i][j])) == 1):
        print(' ',m[i][j], end = '  |')
        c += 6
      else:
        print(' ',m[i][j], end = ' |')
        c += 6
    print()
    print('-'*(c-col))

"""Task 1: Zigzag Walk"""

def walk_zigzag(floor):
  row,coloumn = floor.shape
  x = 0
  y = 0
  while y < coloumn:
    if y % 2 == 0:
      x = 0
      while x < row:
        print(floor[x][y], end = ' ')
        x += 2
    elif y % 2 != 0:
      if row % 2 == 0:
        x = row -1
      elif row % 2 != 0:
        x = row - 2
      while x > 0:
        print(floor[x][y],end = " ")
        x -= 2
    y += 1
    print()

floor = np.array([[ '3' , '8' , '4' , '6' , '1'],
                  ['7' , '2' , '1' , '9' , '3'],
                  ['9' , '0' , '7' , '5' , '8'],
                  ['2' , '1' , '3' , '4' , '0'],
                  ['1' , '4' , '2' , '8' , '6']]
                )

print_matrix(floor)
print('Walking Sequence:')
walk_zigzag(floor)
#This should print
# 3 9 1
# 1 2
# 4 7 2
# 4 9
# 1 8 6
print('################')
floor = np.array([[ '3' , '8' , '4' , '6' , '1'],
                  ['7' , '2' , '1' , '9' , '3'],
                  ['9' , '0' , '7' , '5' , '8'],
                  ['2' , '1' , '3' , '4' , '0']]
                )

print_matrix(floor)
print('Walking Sequence:')
walk_zigzag(floor)
#This should print
# 3 9
# 1 2
# 4 7
# 4 9
# 1 8

"""Task 2: Row Rotation Policy of BRACU Classroom"""

def row_rotation(exam_week, seat_status):
  row, col=seat_status.shape
  arr=seat_status[row-1]
  for j in range(exam_week-1):
    arr2=np.array([None]*col)
    for i in range(col):
      arr2[i]=arr[i]
    for i in range(row):
      seat_status[row-1-i]=seat_status[row-2-i]
    seat_status[0]=arr2
    arr=seat_status[row-1]
  sum=1
  for k in range(row):
    if "AA" in seat_status[k]:
      break
    else:
      sum+=1
  print("Updated seat status:")
  print_matrix(seat_status)
  return sum

seat_status = np.array([[ 'A' , 'B' , 'C' , 'D' , 'E'],
                  ['F' , 'G' , 'H' , 'I' , 'J'],
                  ['K' , 'L' , 'M' , 'N' , 'O'],
                  ['P' , 'Q' , 'R' , 'S' , 'T'],
                  ['U' , 'V' , 'W' , 'X' , 'Y'],
                  ['Z' , 'AA' , 'BB' , 'CC' , 'DD']])
exam_week=3
print_matrix(seat_status)
print()
row_number=row_rotation(exam_week, seat_status) #This should print modified seat status after rotation
print(f'Your friend AA will be on row {row_number}') #This should print Your friend AA will be on row 2

"""Task 3: Matrix Manipulation"""

def reverse_Matrix(matrix):
  row, col=matrix.shape
  for i in range(row):
    var=matrix[i][0]
    for j in range(col//2):
      matrix[i][j]=matrix[i][col-1-j]
      matrix[i][col-1-j]=var
      var=matrix[i][j+1]
  arr1=matrix[0]
  arr2=np.zeros(len(arr1),dtype=int)
  for l in range(row//2):
    for k in range(len(arr1)):
      arr2[k]=arr1[k]
    matrix[l]=matrix[row-1-l]
    matrix[row-1-l]=arr2
    arr1=matrix[l+1]
  print()
  return matrix


matrix = np.array([
[14,  8,  0,  4],
[9,  8,  13,  13],
[9,  3,  1,  4],
[2,  10,  13,  6]
])
print_matrix(matrix)
reversed_matrix = reverse_Matrix(matrix)
print_matrix(reversed_matrix)

#This should print
#|  6  |  13 |  10 |  2  |
#-------------------------
#|  4  |  1  |  3  |  9  |
#-------------------------
#|  13  |  13  |  8 |  9 |
#-------------------------
#|  4 |  0  |  8  |  14  |
#-------------------------

"""Task 4: Chess Piece"""

def show_knight_move(knight):
  chess_board = np.zeros((8,8),dtype=int)
  row,coloumn= knight
  chess_board[row][coloumn]=66
  route = np.array([[1,2],[1,-2],[-1,2],[-1,-2],[-2,1],[-2,-1],[2,1],[2,-1]])
  for i in route:
    n1,n2 = i
    x = row+n1
    y = coloumn+n2
    chess_board[x][y] = 3
  return chess_board

knight = (3,4)
chess_board = show_knight_move(knight)
print_matrix(chess_board)
#This Should print
#| 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
#------------------------------------------
#| 0 | 0 | 0 | 3 | 0 | 3 | 0 | 0 |
#------------------------------------------
#| 0 | 0 | 3 | 0 | 0 | 0 | 3 | 0 |
#------------------------------------------
#| 0 | 0 | 0 | 0 | 66 | 0 | 0 | 0 |
#------------------------------------------
#| 0 | 0 | 3 | 0 | 0 | 0 | 3 | 0 |
#------------------------------------------
#| 0 | 0 | 0 | 3 | 0 | 3 | 0 | 0 |
#------------------------------------------
#| 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
#------------------------------------------
#| 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
#-----------------------------------------

"""Task 5: Matrix Compression"""

import numpy as np
def compress_matrix(mat):
    row,coloumn=matrix.shape
    arr=np.zeros((2,2),dtype=int)
    for i in range(row):
        for j in range(coloumn):
          if i<row//2:
            if j<coloumn//2:
              arr[0][0]+=matrix[i][j]
            else:
              arr[0][1]+=matrix[i][j]
          else:
            if j<coloumn//2:
              arr[1][0]+=matrix[i][j]
            else:
              arr[1][1]+=matrix[i][j]
    print("Returned Array")
    return arr

matrix=np.array([[1,2,3,4],
                 [5,6,7,8],
                 [1,3,5,2],
                 [-2,0,6,-3]
                 ])
print_matrix(matrix)
returned_array=compress_matrix(matrix)
print_matrix(returned_array)
#This should print
#|  14  |  22 |
#--------------
#|  2  |  10  |
#--------------

"""Task 6: Game Arena"""

def play_game(arena):
    points = 0
    for i in range(len(arena)):
        for j in range(len(arena[0])):
            if arena[i][j] % 50 == 0 and arena[i][j] != 0:
                if i > 0 and arena[i-1][j] == 2:
                    points += 2
                if i < len(arena) - 1 and arena[i+1][j] == 2:
                    points += 2
                if j > 0 and arena[i][j-1] == 2:
                    points += 2
                if j < len(arena[0]) - 1 and arena[i][j+1] == 2:
                    points += 2

    if points < 10:
        print( f"Points Gained: {points}. Your team is out.")
    else:
        print (f"Points Gained: {points}. Your team has survived the game.")

arena=np.array([[0,2,2,0],
                [50,1,2,0],
                [2,2,2,0],
                [1,100,2,0]
                ])
print_matrix(arena)
play_game(arena)
#This should print
#Points Gained: 6. Your team is out.

print(".....................")
arena=np.array([[0,2,2,0,2],
                [1,50,2,1,100],
                [2,2,2,0,2],
                [0,200,2,0,0]
                ])
print_matrix(arena)
play_game(arena)
#This should print
#Points Gained: 14. Your team has survived the game.

"""Bonus Task: Primary vs Secondary Diagonal"""

import numpy as np
def check_Diagonal(matrix1, matrix2):
  i,j,k=0, len(matrix1)-1, len(matrix1)-1
  x=0

  for y in range(len(matrix1)):
    if matrix1[i][j]==matrix2 [k][k]:
      x+=1
    i+=1
    j-=1
    k-=1

  if x==len(matrix2):
    print("Yes")
  else:
    print("No")
array1 = np.array([[0, 4, 1], [7, 2, 5], [3, 6, 0]])
array2 = np.array([[3, 6, 0], [5, 2, 7], [0, 4, 1]])

check_Diagonal(array1, array2) #This should print YES
print(".............")
array1 = np.array([[0, 9, 9, 1], [9, 0, 2, 9], [9, 3, 0, 9], [4, 9, 9, 0]])
array2 = np.array([[4, 9, 9, 0], [9, 0, 3, 9], [9, 0, 2, 9], [0, 9, 5, 1]])

check_Diagonal (array1, array2) #This should print NO