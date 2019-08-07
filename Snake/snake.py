import numpy as np
import time
import msvcrt
import re

class Snake:
    board = list() # contains all elements
    snakeBody = list() #contains list of correctly ordered elements of snake body
    currentMove = 'D'
    x = 5 #treat positions, nedded because of reset_board function
    y = 5
    move = None

def reset_game():
    Snake.board = list()
    Snake.snakeBody = list()
    Snake.currentMove = 'D'
    Snake.x = 5
    Snake.y = 5
    Snake.move = None

def reset_board():
    ''' list filled with numbers, where each presents different game object
        0- stands for empty place
        1- stands for snake head
        2-stands for snake body
        3- stands for snake tail-end
        5-stands for snake treat
        9-stands for wall

    '''
    Snake.board = [
                    [9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9],
                    [9, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 9],
                    [9, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 9],
                    [9, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 9],
                    [9, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 9],
                    [9, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 9],
                    [9, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 9],
                    [9, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 9],
                    [9, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 9],
                    [9, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 9],
                    [9, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 9],
                    [9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9]
                    ]
    Snake.board[Snake.x][Snake.y] = 5


def create_new_board():
    reset_board()
    Snake.board [5][2] = 1
    Snake.snakeBody.append([5, 2])
    Snake.board [5][1] = 3
    Snake.snakeBody.append([5, 3])

def random_treats(): # puts snake food on board in random position if not already on board
    for i in Snake.board:
        for j in i:
            if j == 5:
                return
    while True:
        Snake.x = int(10*np.random.rand()+1)
        Snake.y = int(10*np.random.rand()+1)
        if Snake.board[Snake.x][Snake.y] == 0:
            break


def show_board():
    for i in Snake.board:
        row = ''
        for j in i:
            if j == 0:
                row = row + '   '
            elif j == 1:
                row = row + ' ⃝ '
            elif j == 2 or j == 3:
                row = row + ' ⃞ '
            elif j == 5:
                row = row + ' $ '
            elif j == 9:
                row = row + ' # '
        row = row +'\n'
        print(row)


def move_snake(expand = False): # move whole snake
    destiny_indexes = find_on_board()
    Snake.snakeBody.insert(0,destiny_indexes) # adds head to new position
    if not expand: # if snake didn't eat then push tail for one position
        pop = Snake.snakeBody.pop()


def next_move() -> str:
    if check_if_collision():
        return "The end"
    elif check_if_treat():
        move_snake(True)
    else:
        move_snake()
    update_board()
    return ''


def get_head() -> list():
    return Snake.snakeBody[0]

def update_board():
    reset_board()
    i =-1
    for s in Snake.snakeBody: # fill all the spaces snake is located with 'body' parts
        Snake.board[s[0]][s[1]] = 2 # 2 is for body  part
        i += 1
    Snake.board[Snake.snakeBody[0][0]][Snake.snakeBody[0][1]] = 1 # set first element as head
    Snake.board[Snake.snakeBody[i][0]][Snake.snakeBody[i][1]] = 3 # set last element as tail

def check_if_treat() ->bool:
    destiny_indexes = find_on_board()
    destiny = Snake.board[destiny_indexes[0]][destiny_indexes[1]]
    if destiny == 5:
        return True
    else:
        return False

def check_if_collision() -> bool: # find if position choosen by player is acceptable for snake to move to
    destiny_indexes = find_on_board()
    destiny = Snake.board[destiny_indexes[0]][destiny_indexes[1]]
    if(
        destiny == 9 or # it's a wall
        destiny == 2 or # it's snake's body
        destiny == 3 # it's snake's tail
    ):
        return True
    else:
        return False

def find_on_board() -> list(): # finds possition player want a snake to go
    head = get_head()
    destiny = [0,0]
    move = Snake.currentMove
    if move == 'W':
        destiny[0] = head[0]-1
        destiny[1] = head[1]
    elif move == 'S':
        destiny[0] = head[0]+1
        destiny[1] = head[1]
    elif move == 'A':
        destiny[0] = head[0]
        destiny[1] = head[1]-1
    elif move == 'D':
        destiny[0] = head[0]
        destiny[1] = head[1]+1
    return destiny

def run():
    reset_game()
    create_new_board()
    show_board()
    move = ''
    while(True):
        stop = time.time()+1 # stop is changable, added value make moves slower or faster
        while(time.time() < stop):
            if msvcrt.kbhit(): # detect user keyboard interraction
                move = msvcrt.getch() # take user input in specific pattern : b'\'
        if move != None: # if no input
            move = re.search("'\w'", str(move)) # take user input using regExp : '\'
            if move != None: # if getched but nothing typed
                move = move.group()
                move = move[1].lower() # make sure its lower case for if condition
                if (move == 'a' or move =='d' or move == 'w' or move == 's'):
                    Snake.currentMove = move.upper() # if proper move then save globally
        random_treats()
        ans = next_move() # function return empty string if game should go on
        if( ans == 'The end'):
            print(ans)
            break
        show_board()
        Snake.move = None
