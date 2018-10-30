#Yash Bhosale, 55373460, ybhosale@uci.edu

class Othello:
    def __init__(self, totalrows, totalcolumns, turn, gametype, gameboard):
        '''initiates attributes for the gamestate class from the given parameters'''
        self.totalrows = totalrows
        self.totalcolumns = totalcolumns
        self.turn = turn
        self.gametype = gametype
        self.gameboard = gameboard
        
    def game(self):
        '''starts the game and calls all required functions accordingly'''
        blackdiscs, whitediscs = countdiscs(self.gameboard)
        while True:
            if check_gameover(self.turn, self.gameboard) != True:
                if valid_moves_left(self.turn, self.gameboard) != True:
                    self.turn = changeturn(self.turn)
                    continue
                else:
                    print('B: ', blackdiscs, '  W: ', whitediscs)
                    printboard(self.gameboard)
                    print('TURN: ' + self.turn)
                    row, col = player_input()
                    check, move_direction = check_valid_move(row, col, self.turn, self.gameboard)
                    if check == 1:
                        print('VALID')
                        make_move(row, col, self.turn, self.gameboard, move_direction)
                        self.turn = changeturn(self.turn)
                    else:
                        print('INVALID')
                    blackdiscs, whitediscs = countdiscs(self.gameboard)                    
            else:
                print('B: ', blackdiscs, '  W: ', whitediscs)
                printboard(self.gameboard)
                if self.gametype == '>':
                    if blackdiscs > whitediscs:
                        print('WINNER: B')
                        break
                    elif blackdiscs < whitediscs:
                        print('WINNER: W')
                        break
                    else:
                        print('WINNER: NONE')
                        break
                elif self.gametype == '<':
                    if blackdiscs > whitediscs:
                        print('WINNER: W')
                        break
                    elif blackdiscs < whitediscs:
                        print('WINNER: B')
                        break
                    else:
                        print('WINNER: NONE')
                        break

def make_move(row, col, turn, gameboard, move_direction):
    for x in move_direction:
        if x == 1:
            gameboard = change_top_left(row, col, turn, gameboard)
        elif x == 2:
            gameboard = change_top(row, col, turn, gameboard)
        elif x == 3:
            gameboard = change_top_right(row, col, turn, gameboard)
        elif x == 4:
            gameboard = change_right(row, col, turn, gameboard)
        elif x == 5:
            gameboard = change_bottom_right(row, col, turn, gameboard)
        elif x == 6:
            gameboard = change_bottom(row, col, turn, gameboard)
        elif x == 7:
            gameboard = change_bottom_left(row, col, turn, gameboard)
        elif x == 8:
            gameboard = change_left(row, col, turn, gameboard)
    
def changeturn(turn: str) -> str:
    '''changes the turn to the other player'''
    if turn == 'W':
        turn = 'B'
    else:
        turn = 'W'
    return turn

def player_input() -> int:
    '''returns the player's input for a row and column'''
    player_input = input()
    player_input = player_input.split()
    row = int(player_input[0]) - 1
    col = int(player_input[1]) - 1
    return row, col

def check_valid_move(row: int, col: int, turn: str, board: list) -> 'int, list':
    '''cheks if a move can be made in the selected row and column. Returns 1 and a list of all direcions in which move can be made if it can be made, otherwise returns 0 and an empty list'''
    move_direction = []
    count = 0
    if board[row][col] != '.':
        count = 0
        move_direction.append(0)
        return count, move_direction
    if check_top_left(row, col, turn, board):
        count = 1
        move_direction.append(1)
    if check_top(row, col, turn, board):
        count = 1
        move_direction.append(2)
    if check_top_right(row, col, turn, board):
        count = 1
        move_direction.append(3)
    if check_right(row, col, turn, board):
        count = 1
        move_direction.append(4)
    if check_bottom_right(row, col, turn, board):
        count = 1
        move_direction.append(5)
    if check_bottom(row, col, turn, board):
        count = 1
        move_direction.append(6)
    if check_bottom_left(row, col, turn, board):
        count = 1
        move_direction.append(7)
    if check_left(row, col, turn, board):
        count = 1
        move_direction.append(8)
    return count , move_direction

def check_top_left(row: int, col: int, turn: str, board: list) -> bool:
    '''checks if a move can be made in the top left direction of the selected row and column'''
    if row == 0:
        return False
    elif col == 0:
        return False
    row = row - 1
    col = col - 1
    piece = board[row][col]
    if piece == '.':
        return False
    if piece == turn:
        return False
    while True:
        if (piece == '.'):
            return False
        elif (row == 0):
            return False
        elif (col == 0):
            return False
        row = row - 1
        col = col - 1
        piece = board[row][col]
        if piece == turn:
            return True

def check_top(row: int, col: int, turn: str, board: list) -> bool:
    '''checks if a move can be made in the top direction of the selected row and column'''
    if row == 0:
        return False
    row = row - 1
    piece = board[row][col]
    if piece == '.':
        return False
    if piece == turn:
        return False
    while True:
        if (piece == '.'):
            return False
        elif (row == 0):
            return False
        row = row - 1
        piece = board[row][col]
        if piece == turn:
            return True
    
def check_top_right(row: int, col: int, turn: str, board: list) -> bool:
    '''checks if a move can be made in the top right direction of the selected row and column'''
    if row == 0:
        return False
    elif col == (len(board[0]) - 1):
        return False
    row = row - 1
    col = col + 1
    piece = board[row][col]
    if piece == '.':
        return False
    if piece == turn:
        return False
    while True:
        if (piece == '.'):
            return False
        elif (row == 0):
            return False
        elif (col == (len(board[0]) - 1)):
            return False
        row = row - 1
        col = col + 1
        piece = board[row][col]
        if piece == turn:
            return True

def check_right(row: int, col: int, turn: str, board: list) -> bool:
    '''checks if a move can be made in the right direction of the selected row and column'''
    if col == (len(board[0]) - 1):
        return False
    col = col + 1
    piece = board[row][col]
    if piece == '.':
        return False
    if piece == turn:
        return False
    while True:
        if (piece == '.'):
            return False
        elif (col == (len(board[0]) - 1)):
            return False
        col = col + 1
        piece = board[row][col]
        if piece == turn:
            return True

def check_bottom_right(row: int, col: int, turn: str, board: list) -> bool:
    '''checks if a move can be made in the bottom right direction of the selected row and column'''
    if row == (len(board) - 1):
        return False
    elif col == (len(board[0]) - 1):
        return False
    row = row + 1
    col = col + 1
    piece = board[row][col]
    if piece == '.':
        return False
    if piece == turn:
        return False
    while True:
        if (piece == '.'):
            return False
        elif (row == (len(board) - 1)):
            return False
        elif (col == len(board[0]) - 1):
            return False
        row = row + 1
        col = col + 1
        piece = board[row][col]
        if piece == turn:
            return True

def check_bottom(row: int, col: int, turn: str, board: list) -> bool:
    '''checks if a move can be made in the bottom direction of the selected row and column'''
    if row == (len(board) - 1):
        return False
    row = row + 1
    piece = board[row][col]
    if piece == '.':
        return False
    if piece == turn:
        return False
    while True:
        if (piece == '.'):
            return False
        elif (row == (len(board) - 1)):
            return False
        row = row + 1
        piece = board[row][col]
        if piece == turn:
            return True

def check_bottom_left(row: int, col: int, turn: str, board: list) -> bool:
    '''checks if a move can be made in the bottom left direction of the selected row and column'''
    if row == (len(board) - 1):
        return False
    elif col == 0:
        return False
    row = row + 1
    col = col - 1
    piece = board[row][col]
    if piece == '.':
        return False
    if piece == turn:
        return False
    while True:
        if (piece == '.'):
            return False
        elif (row == (len(board) - 1)):
            return False
        elif (col == 0):
            return False
        row = row + 1
        col = col - 1
        piece = board[row][col]
        if piece == turn:
            return True

def check_left(row: int, col: int, turn: str, board: list) -> bool:
    '''checks if a move can be made in the left direction of the selected row and column'''
    if col == 0:
        return False
    col = col - 1
    piece = board[row][col]
    if piece == '.':
        return False
    if piece == turn:
        return False
    while True:
        if (piece == '.'):
            return False
        elif (col == 0):
            return False
        col = col - 1
        piece = board[row][col]
        if piece == turn:
            return True   

def change_top_left(row: int, col: int, turn: str, board: list) -> list:
    '''changes all the discs appropriately in the top left direction of the selected row and column'''
    board[row][col] = turn
    row = row - 1
    col = col - 1
    while(board[row][col] != turn):
        board[row][col] = turn
        row = row - 1
        col = col - 1
    return board

def change_top(row: int, col: int, turn: str, board: list) -> list:
    '''changes all the discs appropriately in the top direction of the selected row and column'''
    board[row][col] = turn
    row = row - 1
    while(board[row][col] != turn):
        board[row][col] = turn
        row = row - 1
    return board

def change_top_right(row: int, col: int, turn: str, board: list) -> list:
    '''changes all the discs appropriately in the top right direction of the selected row and column'''
    board[row][col] = turn
    row = row - 1
    col = col + 1
    while(board[row][col] != turn):
        board[row][col] = turn
        row = row - 1
        col = col + 1
    return board

def change_right(row: int, col: int, turn: str, board: list) -> list:
    '''changes all the discs appropriately in the right direction of the selected row and column'''
    board[row][col] = turn
    col = col + 1
    while(board[row][col] != turn):
        board[row][col] = turn
        col = col + 1
    return board

def change_bottom_right(row: int, col: int, turn: str, board: list) -> list:
    '''changes all the discs appropriately in the bottom right direction of the selected row and column'''
    board[row][col] = turn
    row = row + 1
    col = col + 1
    while(board[row][col] != turn):
        board[row][col] = turn
        row = row + 1
        col = col + 1
    return board

def change_bottom(row: int, col: int, turn: str, board: list) -> list:
    '''changes all the discs appropriately in the bottom direction of the selected row and column'''
    board[row][col] = turn
    row = row + 1
    while(board[row][col] != turn):
        board[row][col] = turn
        row = row + 1
    return board

def change_bottom_left(row: int, col: int, turn: str, board: list) -> list:
    '''changes all the discs appropriately in the bottom left direction of the selected row and column'''
    board[row][col] = turn
    row = row + 1
    col = col - 1
    while(board[row][col] != turn):
        board[row][col] = turn
        row = row + 1
        col = col - 1
    return board

def change_left(row: int, col: int, turn: str, board: list) -> list:
    '''changes all the discs appropriately in the left direction of the selected row and column'''
    board[row][col] = turn
    col = col - 1
    while(board[row][col] != turn):
        board[row][col] = turn
        col = col - 1
    return board

def valid_moves_left(turn: str, board: list) -> bool:
    '''returns true if the player can make valid moves and false if the player can't make any moves.'''
    vm = []
    for x in range(len(board)):
        for y in range(len(board[x])):
            if board[x][y] == '.':
                check, a = check_valid_move(x, y, turn, board)
                if check == 1:
                    vm.append((x,y))
    if len(vm) > 0:
        return True
    else:
        return False

def printboard(board: list):
    '''prints the game board'''
    for x in range(len(board)):
        string = ''
        for y in range(len(board[x])):
            string = string + board[x][y] + ' '
        print(string)

def countdiscs(board: list) -> int:
    '''counts the number of white and black discs on the current game board'''
    whitediscs = 0
    blackdiscs = 0
    for x in range(len(board)):
        for y in range(len(board[x])):
            if board[x][y] == 'B':
                blackdiscs = blackdiscs + 1
            elif board[x][y] == 'W':
                whitediscs = whitediscs + 1
    return blackdiscs, whitediscs

def check_gameover(turn: str, board: list) -> bool:
    '''checks if the game is over or not'''
    count = 0
    if valid_moves_left(turn, board):
        count += 1
    turn = changeturn(turn)
    if valid_moves_left(turn, board):
        turn = changeturn(turn)
        count += 1
    if count >= 1:
        return False
    else:
        return True














    
        
