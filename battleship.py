from random import randint
 
size = 5  # number of rows & columns in the grid
turns = 10  # number of guesses allowed in the game
board = []
 
for row in range(size):
   board.append(["O"] * size)  # isn't this cool?!?!
 
def print_board(board):
   for row in board:
      print(" ".join(row))
 
ship_row = randint(0, len(board) - 1)
ship_col = randint(0, len(board[0]) - 1)
# print("DEBUG: Row=", ship_row, "Col=", ship_col)  # FOR TESTING PURPOSES ONLY
 
for turn in range(turns):
   print("Turn", turn + 1)
   print_board(board)
   guess_row = int(input("Guess Row: "))
   guess_col = int(input("Guess Col: "))
   if guess_row == ship_row and guess_col == ship_col:
      print("Congratulations! You sank my battleship!")
      break
   elif guess_row<0 or guess_row>size-1 or guess_col<0 or guess_col>size-1:
      print("That's not even in this ocean.")
   elif board[guess_row][guess_col] == "X":
      print("You already guessed that one.")
   else:
      print("You missed my battleship!")
      board[guess_row][guess_col] = "X"
else:
   print("Sorry -- You Lose...")
   board[ship_row][ship_col] = "S"
   print_board(board)
