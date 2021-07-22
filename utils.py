import random

def whoGoesFirst():

     if random.randint(0, 1) == 0:

         return 'computer'

     else:

         return 'player'



def playAgain():
     print('Do you want to play again? (yes or no)')

     return input().lower().startswith('y')



def makeMove(board, letter, move):

     board[move] = letter
     return board
def isWinner(bo, le):

     return ((bo[7] == le and bo[8] == le and bo[9] == le) or # across the top

     (bo[4] == le and bo[5] == le and bo[6] == le) or # across the middle

     (bo[1] == le and bo[2] == le and bo[3] == le) or # across the bottom

     (bo[7] == le and bo[4] == le and bo[1] == le) or # down the left side

     (bo[8] == le and bo[5] == le and bo[2] == le) or # down the middle

     (bo[9] == le and bo[6] == le and bo[3] == le) or # down the right side

     (bo[7] == le and bo[5] == le and bo[3] == le) or # diagonal

     (bo[9] == le and bo[5] == le and bo[1] == le)) # diagonal

def getBoardCopy(board):

     dupeBoard = []

     for i in board:

         dupeBoard.append(i)



     return dupeBoard



def isSpaceFree(board, move):

     return board[move] == ' '

def getPlayerMove(board):

     move = ' '

     while move not in '1 2 3 4 5 6 7 8 9'.split() or not isSpaceFree(board, int(move)):

         print('What is your next move? (1-9)')

         move = input()

     return int(move)



def chooseRandomMoveFromList(board, movesList):

     # Returns a valid move from the passed list on the passed board.

     # Returns None if there is no valid move.

     possibleMoves = []

     for i in movesList:

          if isSpaceFree(board, i):

             possibleMoves.append(i)

 
     if len(possibleMoves) != 0:

         return random.choice(possibleMoves)

     else:

         return None

def getComputerMove(board, computerLetter):

     if computerLetter == 'X':

         playerLetter = 'O'
     else:

         playerLetter = 'X'

     for i in range(1, 10):
         copy = getBoardCopy(board)

         if isSpaceFree(copy, i):

             makeMove(copy, computerLetter, i)

             if isWinner(copy, computerLetter):

                 return i

     for i in range(1, 10):

         copy = getBoardCopy(board)

         if isSpaceFree(copy, i):

             makeMove(copy, playerLetter, i)

             if isWinner(copy, playerLetter):

                return i

     move = chooseRandomMoveFromList(board, [1, 3, 7, 9])

     if move != None:
         return move




     if isSpaceFree(board, 5):

         return 5



     # Move on one of the sides.

     return chooseRandomMoveFromList(board, [2, 4, 6, 8])



def isBoardFull(board):

     # Return True if every space on the board has been taken. Otherwise return False.

     for i in range(1, 10):

         if isSpaceFree(board, i):

             return False

     return True
print('Welcome to Tic Tac Toe!')

def toggle(turn):
    mask = 0b11
    turn = turn ^ mask
    print ("It is player %s's turn." % turn)
    return turn
def mark_board(last, column,board,whos_turn):
    if whos_turn == 0b01:
        board[last][column] = "1"
    else:
        board[last][column] = "2"
    print_board(board)
def generate_board(boardheight, boardwidth, board):
    for i in range(8):
            board.append(["_"] * boardwidth)
    arrows=[]
    for j in range(boardwidth):
      arrows.append("^")
    #arrows=["^","^","^","^","^","^"]
    board.append(arrows)
    label=[]
    for j in range(boardwidth):
      label.append(str(j+1))
    board.append(label)
    #k=board[:-6]
    #board=k
def start():
      print ("Let's play Connect Four!")
def print_board(board):
    print ("\n")
    for row in board:
        print (" ".join(row))
    print ("\n")
def check_winner(board, player, boardwidth, boardheight):
    #check horizontal spaces
    for y in range(boardheight):
        for x in range(boardwidth - 3):
            if board[x][y] == player and board[x+1][y] == player and board[x+2][y] == player and board[x+3][y] == player:
                return True

    #check vertical spaces
    for x in range(boardwidth):
        for y in range(boardheight - 3):
            if board[x][y] == player and board[x][y+1] == player and board[x][y+2] == player and board[x][y+3] == player:
                return True

    #check / diagonal spaces
    for x in range(boardwidth - 3):
        for y in range(3, boardheight):
            if board[x][y] == player and board[x+1][y-1] == player and board[x+2][y-2] == player and board[x+3][y-3] == player:
                return True

    #check \ diagonal spaces
    for x in range(boardwidth - 3):
        for y in range(boardheight - 3):
            if board[x][y] == player and board[x+1][y+1] == player and board[x+2][y+2] == player and board[x+3][y+3] == player:
                return True

    return False
    
