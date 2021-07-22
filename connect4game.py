import utils

board = [] 
label = []
whos_turn = 0b10
winner = False
last = 0
column = 0
boardheight = 7
boardwidth = boardheight

def generate_board(boardheight, boardwidth, board):
    for i in range(boardheight):
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
def play():
    while True:
            column = int(input("Pick a column (1-{}): ".format(boardheight)))-1
            if column >= 0 and column <= boardwidth:
                for i in range(boardheight):
                    if board[i][column] == "_":
                        last = i
                utils.mark_board(last, column,board,whos_turn)
            else:
                raise ("You picked a column outside the board!")
            break


utils.start()
utils.generate_board(boardheight, boardwidth, board)
utils.print_board(board)

while winner == False:
    whos_turn = utils.toggle(whos_turn)
    play()
    winner = utils.check_winner(board, str(whos_turn),boardheight,boardwidth)
    
if winner == True:
    print ("Player " + str(whos_turn) + " wins!")
