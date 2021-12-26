'''
O = Unrevealed spot
X = Unrevealed Flagged spot
- = Revealed empty spot
1,2= Revealed spot
* = Revealed mine
'''
import random

def generate_board():
    random_selection = random.choices(['-', '*'], weights=[5, 1], k=100)
    board = [["" for i in range(10)] for j in range(10)]   
    count = 0
    for x in range(10):
        for y in range(10):
            board[x][y] = random_selection[count]
            count +=1
    return board

def mine_check(board, x, y):
    if board[int(x)][int(y)] == '*': 
        print("Sorry, you lost! Try again!")
        return True
    else:
        print("Lucky this time. Keep up!")
        return False

def count_adj_mines(board, x, y, mines_count = 0):
    for row in range (int(x-1), int(x+2)):
        for col in range (y-1, y+2):
            if row >= 0 and row < 10 and col >= 0 and col < 10 and board[row][col] == '*':
                mines_count +=1
    return mines_count

    
def open_adjacent(board, x, y):
    for row in range (int(x-1), int(x+2)):
        for col in range (y-1, y+2):
            if row >= 0 and row < 10 and col >= 0 and col < 10 and board[row][col] != '*':
                mines_count = count_adj_mines(board, row, col)
                if mines_count: 
                    visible_board.board[row][col] = mines_count
                    minesweeper.print_board(visible_board)
                else: 
                    visible_board.board[row][col] = '-'
                    minesweeper.print_board(visible_board)
                
class minesweeper():

    def __init__(self, board):
        self.board = board
    
    def print_board(self):
        count = 0
        print("\n  ", end = "")
        for i in range(10):
            print(f"| {i} ", end = "")
        print("|\n===========================================")
        for row in self.board:
            print (f"{count} ", end="")
            count +=1
            for slot in row:
                print (f"| {slot} ", end="")
            print("| \n", end = "")


original_board = generate_board()
print("first print: ", original_board[1][5])
player_board = [["O" for i in range(10)] for j in range(10)]

hidden_board = minesweeper(original_board)
visible_board = minesweeper(player_board)

minesweeper.print_board(visible_board)
mines_count = 0
x_input = 20

#Game play
while True:
    click = input("Please input your next move:\nTo flag a mine: input coordinate followed by x.\nTo open a spot: just enter the coordinates. ")
    if len(click) == 3:
        if click[2].lower() == 'x':
           visible_board.board[int(click[0])][int(click[1])] = 'x'
           minesweeper.print_board(visible_board)
           continue
    if mine_check(hidden_board.board, click[0], click[1]): break
    else:
        mines_count = count_adj_mines(hidden_board.board, int(click[0]), int(click[1]))
    if mines_count:
        visible_board.board[int(click[0])][int(click[1])] = mines_count
        minesweeper.print_board(visible_board)
    else:
        visible_board.board[int(click[0])][int(click[1])] = "-"
        minesweeper.print_board(visible_board)
        open_adjacent(hidden_board.board, int(click[0]), int(click[1]))