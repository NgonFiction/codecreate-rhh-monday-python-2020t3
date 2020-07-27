# Tic Tac Toe Program

# board = [
#          ' ',' ',' ',
#          ' ',' ',' ',
#          ' ',' ',' ',
#         ]

board = [
         ' ',' ',' ',
         ' ',' ',' ',
         ' ',' ',' ',
        ]

def print_board():
    i = 0
    while i < 9:
        if i % 3 == 2:
            print(board[i], end='\n')
        else:
            print(board[i], end='')
        i += 1

def move(player, move):
    if not is_valid_move(move):
        # Incorrect: please enter new move
        new_move = int(input("Invalid move. Please enter a new move: "))
        move(player, new_move)

    # Else it is a valid move
    print("Valid move.")
    board[move] = player
    
def is_valid_move(move):
    if move < 0 or move > 9:
        return False
    if board[move] != ' ':
        return False
    return True


def game_ended(player):
    num_player_cells = 0
    # Check rows
    i = 0
    while i < 9:
        if i % 3 == 0:
            # Reset
            num_player_cells = 0

        if board[i] == player:
            num_player_cells += 1

        if num_player_cells == 3:
            return True
        
        i += 1

    # Check columns
    i = 0
    while i < 3:
        if board[i] == player and board[i+3] == player and board[i+6] == player:
            return True
        i += 1

    # Check diagonals
    if board[0] == player and board[4] == player and board[8] == player:
        return True
    if board[2] == player and board[4] == player and board[6] == player:
        return True

    # Else not won
    return False

# Game start
player1 = 'X'
player2 = 'O'

curr_player = player1
while game_ended != True:
    print_board()
    print("Current player: " + curr_player)
    p_move = int(input("Please enter a move: "))
    move(curr_player, p_move)
    
    if game_ended(curr_player):
        break

    # Switch players
    if curr_player == player1:
        curr_player = player2
    else:
        curr_player = player1

print_board()
print("Congratulations player " + curr_player + "! You have won!")



