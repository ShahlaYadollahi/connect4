import numpy as np


def diagonal(mat, n):
    diag = []
    for i in range(0, n): 
        for j in range(0, n): 
 
            # Condition for principal diagonal
            if (i == j):
                diag.append(mat[i,j])
    return diag

class Board:

    def __init__(self) -> None:
        self.board = np.zeros((6,7), dtype=int)

    def change_board(self, location, color):
        if location[0] in range(1,7) and location[1] in range(1,8):
            self.board[location[0]-1, location[1]-1] = color

    def check_for_win(self):
        window = np.zeros((4,4), dtype=int)
        for i in range(0, 3):
            for j in range(0,4):
                window = self.board[i:i+4, j:j+4]
                diag = diagonal(window, 4)
                if 0 not in diag and (sum(diag) == 4 or sum(diag) == 8):
                    return sum(diag)
                for f in range(0,4):
                    if window[f, :].sum() == 4 or window[f, :].sum() == 8:
                        return window[f, :].sum()
                    if window[:, f].sum() == 4 or window[:, f].sum() == 8:
                        return window[:, f].sum()

                    
            
    

class Player:
    def __init__(self, name, color) -> None:
        self.name = name
        self.color = color
        self.spot = []
    
    def player_spots(self, location):
        self.spot.append(location)
    


class Buttons:
    def __init__(self, color) -> None:
        self.color = color
        self.score = 0
    
    def convert_color(self):
        if self.color == "red":
            self.score = 1
        if self.color == "yellow":
            self.score = 2

board = Board()
red_but = Buttons('red')
yellow_but = Buttons('yellow')
red_but.convert_color()
yellow_but.convert_color()

p1_name = input("Hello! What's your name dear first player? ")
p1_color = input("And what would be your chosen color, red or yellow? ")

p1 = Player(p1_name, p1_color)

p2_name = input("Hello! What's your name dear second player? ")
p2_color = input("And what would be your chosen color, red or yellow? ")

p2 = Player(p2_name, p2_color)

print("Okay, here is the board")
print(board.board)

if p1.color=='red':

    p1_but = red_but.score
    p2_but = yellow_but.score
else:
    p2_but = red_but.score
    p1_but = yellow_but.score


while True:
    move1 = input("What's your move {p1}? ".format(p1=p1.name))
    move1_list = [int(x) for x in move1.split()]
    if move1_list not in p1.spot:
        p1.player_spots(move1_list)
        board.change_board(move1_list, p1_but)
    else:
        move1    
    if (board.check_for_win()):
        print("we have a winner")
    move2 = input("What's your move {p2}? ".format(p2=p2.name))
    move2_list = [int(x) for x in move2.split()]
    board.change_board(move2_list, p2_but)
    p1.player_spots(move2_list)
    print(board.board)
    if (board.check_for_win()):
        print("we have a winner")

