import random


computer_score = 0
human_score = 0
game_list = []

def print_board(board):
    print("\n    1   2   3 \n")
    print("1   " + board[0][0] + " | " + board[0][1] + " | " + board[0][2])
    print("   ---+---+---")
    print("2   " + board[1][0] + " | " + board[1][1] + " | " + board[1][2])
    print("   ---+---+---")
    print("3   " + board[2][0] + " | " + board[2][1] + " | " + board[2][2] + "\n")





def check_row(board, row):
    return (board[row][0] == board[row][1] and board[row][1] == board[row][2] and board[row][0] != "-")
def check_column(board, col):
    return (board[0][col] == board[1][col] and board[1][col] == board[2][col] and board[0][col] != "-")
def check_diagonals(board):
    return (board[0][0] == board[1][1] and board[1][1] == board[2][2] and board[0][0] != "-") or\
            (board[2][0] == board[1][1] and board[1][1] == board[0][2] and board[2][0] != "-")



def check_winner(board):
    for i in range(3):
        if check_row(board, i):
            return True
        if check_column(board, i):
            return True
    if check_diagonals(board):
        return True
    return False

def check_tie(board):
    for item in board:
        if "-" in item:
            return False
    return True


    # Human input logic 
def human_play(board):
    while True:
        global game_list
        row = int(input("Enter row number: "))
        game_list.append("H")
        game_list.append(row)
        if  row < 1 or  row > 3:
            row = input("Enter row number between 1-3: ")
        
        col = int(input("Enter column number: "))
        game_list.append(col)
        if  col < 1 or col > 3:
            col = int(input("Enter column number between 1-3: "))

        if board[row-1][col-1] != "-":
            print("Pick an empty box!")
        else:
            return (row-1, col-1)
        
        
        


# computer random plays are stored in possible moves 
def computer_play(board):
    possible_moves = []
    for row in range(len(board)):
        for col in range(len(board[0])):
            if board[row][col] == "-":
                possible_moves.append((row, col))
    # print(possible_moves)

    computer_move = possible_moves[random.randrange(len(possible_moves))]
    computer_log =list(computer_move)
    computer_log[0] = computer_log[0] + 1   
    computer_log[1] = computer_log[1] + 1   
    game_list.append("C")
    game_list.append(computer_log)

    return computer_move



# main game logic 
def main():
    global human_score , computer_score 
    print("\n== Tic Tac Toe ==")
    # Create an empty board
    board = [ 
        ["-", "-", "-"],
        ["-", "-", "-"],
        ["-", "-", "-"]
    ]
    # Create 2 players
    players = ["X", "O"]
    # Player X plays first
    turn = 0
    
    while not check_tie(board):
        print_board(board)
        print(game_list)
        # print(f"{human_score} is human score ")
        # print(f"{computer_score} is human score ")
        if turn == 0:
            # Human plays 
            print("Human's turn!")
            row, col = human_play(board)
            board[row][col] = players[turn]
            

            
        else:
            # Computer plays
            print("Computer plays!")
            row, col = computer_play(board)
            board[row][col] = players[turn]
        # Check if the player won
        if check_winner(board):
            print_board(board)
            if turn == 0: 
                print("+++++ You won !!! +++++")
                print("-----------------------")
                print("=====  gained 1 Point !!! =====")
                human_score +=1 
                break
            else: 
                print("+++++ Computer won !!! +++++")
                print("-----------------------")
                print("=====  Computer gained 1 Point !!! =====")
                computer_score += 1 
                break
        
        # Select the next player
        turn = 1 - turn
    
    else:
        print_board(board)
        print("It's a tie!")
    
    print(game_list)
main()