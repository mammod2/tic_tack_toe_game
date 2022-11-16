import random 
# things to do
# make a board function to display the board
board = ['-' , '-' , '-',  '-', '-', '-', '-', '-', '-' , ]
currentPlayer = "X"
winner = None
PlayGame = True 

def print_board(board): 
     print(f'  {board[6]}   |   {board[7]}   |   {board[8]}' + '  ' ,10*' ',' ''  7   |   8   |   9')
     print('-----------')
     print(f'  {board[3]}   |   {board[4]}   |   {board[5]}' + '  ' ,10*' ',' ''  4   |   5   |   6')
     print('-----------')
     print(f'  {board[0]}   |   {board[1]}   |   {board[2]}' + '  ' ,10*' ',' ''  1   |   2   |   3')

def playerInput(board): 
    inp = int(input("Enter a number from 1 - 9 : "))
    if inp >= 1  and inp <= 9 and board[inp-1] == '-':
        board[inp - 1] = currentPlayer
    else: 
        print("That spot is occupied")

# check for win or tie
def checkWinner(board): 
    global winner 
    if board[0] == board[1] == board[2] != '-': #row 123 
        winner = board[0]
        return True
    elif board[3] ==  board[4] == board[5] and board[3] != '-': #row 456
        winner = board[3]
        return True 
    elif board[6] ==  board[7] == board[8] and board[6] != '-': # row 789
        winner = board[6]
        return True 
    elif board[0] ==  board[3] == board[6] and board[0] != '-': #column 147
        winner = board[6]
        return True 
    elif board[1] ==  board[4] == board[7] and board[1] != '-': #column 258
        winner = board[6]
        return True 
    elif board[2] ==  board[5] == board[8] and board[2] != '-': #column 369
        winner = board[6]
        return True 
    elif board[0] ==  board[4] == board[8] and board[0] != '-': #diagnal 159
        winner = board[6]
        return True 
    elif board[2] ==  board[4] == board[6] and board[2] != '-': #diagnal 357
        winner = board[6]
        return True 
def checkWin(): 
     if checkWinner(board): 
        print(f"{currentPlayer} has won the game !")
        return True

def checkTie(board): 
    if '-' not in board: 
        global PlayGame
        print_board(board)
        print('It is a tie')
        PlayGame = False

def computer(board):
    while currentPlayer == "O":
        position = random.randint(0,8)
        if board[position] == '-': 
            board[position] = "O"
            switchPlayer()

# switch the player 
def switchPlayer():
    global currentPlayer
    if currentPlayer == "X":
        currentPlayer = "O"
    else: 
        currentPlayer = "X"
# check for win or tie again 



while PlayGame: 
    print_board(board)
    playerInput(board)

    switchPlayer()
    print(f"{currentPlayer} is playing")
    if checkWin(): 
        break
    print("checked winner ")
    checkTie(board)
    print("checked Tie")
    computer(board)
    print("Computer is playing")
    checkWin()
    print("checking winner 2 ")
    checkTie(board)
    print("checking T 2 ")
