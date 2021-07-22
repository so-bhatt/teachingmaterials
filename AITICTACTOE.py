import random
### order not signified
import utils


def drawBoard(board):
     

     print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
     print("-----------")
     print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
     print("-----------")
     print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])

def inputPlayerLetter():
     letter = ''

     while not (letter == 'X' or letter == 'O'):

         print('Do you want to be X or O?')

         letter = input().upper()
     if letter == 'X':
         return ['X', 'O']

     else:

         return ['O', 'X']

while True:

     # Reset the board
     print("squares are ordered from bottom left to top right as 1 to 9")
     print("|7|8|9|")
     print("-------")
     print("|4|5|6|")
     print("-------")
     print("|1|2|3|")
     theBoard = [' '] * 10

     playerLetter, computerLetter = inputPlayerLetter()

     turn = utils.whoGoesFirst()

     print('The ' + turn + ' will go first.')

     gameIsPlaying = True



     while gameIsPlaying:

        if turn == 'player':

          # Player’s turn.

          drawBoard(theBoard)

          move = utils.getPlayerMove(theBoard)

          utils.makeMove(theBoard, playerLetter, move)
          if utils.isWinner(theBoard, playerLetter):
              drawBoard(theBoard)
              print("Horray! YOu won the game ")
              gameIsPlaying=False
          else:
            if utils.isBoardFull(theBoard):
              print("It is a Tie ")
              gameIsPlaying=False
              break
            else:
              turn="computer"
        else:
          drawBoard(theBoard)
          move = utils.getComputerMove(theBoard,computerLetter)
          utils.makeMove(theBoard, computerLetter, move)
          if utils.isWinner(theBoard, computerLetter):
            drawBoard(theBoard)
            print("Computer Won the game ")
            gameIsPlaying=False
          else:
            if utils.isBoardFull(theBoard):
              print("It is a Tie ")
              gameIsPlaying=False
              break
            else:
              turn="player"
     if not utils.playAgain():
       break
