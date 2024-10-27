#tic tac toe   
"""
tic tac toe board

[
    [-, -, -],
    [-, -, -],
]

user_input -> something 1-9
if they enter anything else: tell them too go again
check if the user_input is already taken
add it to the board
check if user won: checking rows,columns and diagonals
toggle between users upon successful moves
"""

board =[
    ["-","-","-"],
    ["-","-","-"],
    ["-","-","-"],
]

user=True #when true it refers to x,otherwise O
turns=0

def print_board(board):
    for row in board:
        for line in row:
            print(line,end=" ")
        print()

def quit(board):
    if user_input.lower()=='q':
        print("Thanks for playing")
        return True
    else: return False
    
def check_input(user_input):
    #check if its number
    if not isnum(user_input):  return False
    user_input=int(user_input)
    #check if its 1-9
    if not bounds(user_input): return False
     
    return True
    
def isnum(user_input):
    if not user_input.isnumeric():
        print("This is not a valid number")
        return False
    else: return True

def bounds(user_input):
    if 1<=user_input<=9:
        return True
    else: 
        print("This number is out of bound")
        return False
            
def istaken(coords,board):
    row=coords[0]
    col=coords[1]
    if board[row][col]!="-":
        print("This position is already taken")
        return True
    else: return False
        
def coordinates(user_input):
    row=int(user_input/3)
    col=int(user_input%3)
    return (row,col)
    
def add_to_board(coords,board,active_user):
    row=coords[0]
    col=coords[1]
    board[row][col]=active_user
    
def current_user(user):
    if user: return "x"
    else: return "O"
    
def iswin(active_user,board):
    if check_row(active_user,board): return True
    if check_col(active_user,board): return True
    if check_diag(active_user,board): return True
    
    else: return False
def check_col(active_user,board):
    for col in range(3):
        complete_col=True
        for row in range(3):
            if board[row][col]!=active_user:
                complete_col=False
                break
        if complete_col: return True
    return False
def check_diag(active_user,board):
    if board[0][0]==active_user and board[1][1]==active_user and board[2][2]==active_user: return True
    elif board[0][2]==active_user and board[1][1] and board[2][0]==active_user: return True
    else: return False
                
def check_row(active_user,board):
    for row in board:
        complete_row=True
        for slot in row:
            if slot!=active_user:
                complete_row=False
                break
        if complete_row: return True
    return False

while turns<9:
    active_user=current_user(user) 
    print_board(board)
    user_input=input("please enter a position 1 through 9 or enter \"q\" to quit: ")
    if quit(user_input):
        break
    if not check_input(user_input):
        print("Please try again")
        continue
    user_input=int(user_input)-1
    coords=coordinates(user_input)
    if istaken(coords,board):
        print("Please try again")
        continue
    add_to_board(coords,board,active_user)
    if iswin(active_user,board):
        print(f"{active_user.upper()} won!")
        break
    user=not user
    turns+=1
    if turns==9:
        print("Tie!")

