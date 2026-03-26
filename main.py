from os import system
import random

board = [[2, 0, 0, 0],
        [0, 32, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 2, 0]]

def print_board():
    print('+---+---+---+---+')
    for row in board:
        print('|', end=' ')
        for cell in row:
            print(cell, end=' | ')
        print('\n+---+---+---+---+')

def move_board(command):
    rows = len(board)
    cols = len(board[0]) 
        
    if command == 'w':
        print('Choose w')
        for j in range(cols):
            for _ in range(3):
                for i in range(1, rows):
                    if (board[i-1][j] == 0 and board[i][j] != 0):
                        board[i-1][j] = board[i][j]
                        board[i][j] = 0

            for i in range(1, rows):                    
                if(board[i-1][j] == board[i][j] and board[i][j] != 0):
                    board[i-1][j] *= 2
                    board[i][j] = 0

            for i in range(1, rows):
                if (board[i-1][j] == 0 and board[i][j] != 0):
                    board[i-1][j] = board[i][j]
                    board[i][j] = 0

    elif command == 'a':
        print('Choose a')
        for i in range(rows):
            for _ in range(3):
                for j in range(1, cols):
                    if (board[i][j-1] == 0 and board[i][j] != 0):
                        board[i][j-1] = board[i][j]
                        board[i][j] = 0

            for j in range(1, cols):                    
                if(board[i][j-1] == board[i][j] and board[i][j] != 0):
                    board[i][j-1] *= 2
                    board[i][j] = 0

            for j in range(1, cols):
                if (board[i][j-1] == 0 and board[i][j] != 0):
                    board[i][j-1] = board[i][j]
                    board[i][j] = 0

    elif command == 's':
        print('Choose s')        
        for j in range(cols):
            for _ in range(3):
                for i in range(rows - 2, -1, -1):
                    if (board[i+1][j] == 0 and board[i][j] != 0):
                        board[i+1][j] = board[i][j]
                        board[i][j] = 0

            for i in range(rows - 2, -1, -1):                  
                if(board[i+1][j] == board[i][j] and board[i][j] != 0):
                    board[i+1][j] *= 2
                    board[i][j] = 0

            for i in range(rows - 2, -1, -1):
                if (board[i+1][j] == 0 and board[i][j] != 0):
                    board[i+1][j] = board[i][j]
                    board[i][j] = 0
                    
    elif command == 'd':
        print('Choose d')        
        for i in range(rows):
            for _ in range(3):
                for j in range(cols - 2, -1, -1):
                    if (board[i][j+1] == 0 and board[i][j] != 0):
                        board[i][j+1] = board[i][j]
                        board[i][j] = 0

            for j in range(cols - 2, -1, -1):                    
                if(board[i][j+1] == board[i][j] and board[i][j] != 0):
                    board[i][j+1] *= 2
                    board[i][j] = 0

            for j in range(cols - 2, -1, -1):
                if (board[i][j+1] == 0 and board[i][j] != 0):
                    board[i][j+1] = board[i][j]
                    board[i][j] = 0
    else :
        print('Wrong command. Use (w/a/s/d)!')
        return


def spawn():
    spawn_x = -1
    spawn_y = -1
    while board[spawn_x][spawn_y] != 0 and spawn_x == -1 and spawn_y == -1:
        spawn_x = random.randint(0, 3)
        spawn_y = random.randint(0, 3)

    board[spawn_x][spawn_y] = 2


while True:   
    print_board()
    move = input('Enter move (w/a/s/d): ')
    move_board(move)
    spawn()

