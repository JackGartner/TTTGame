# Jack Gartner
# Works Cited
# None

##### imports

import gameFunctions
import ioFunctions
import random
##### global constants


##### global variables

debug = False

P1 = 1    # token for player 1
P2 = -1   # token for player 2
BL = 0    # token for empty/blank space

numTurns = 0
val = 0

##### functions

def main():
  # main game logic

  print("hello, game is started...")

  # local constants

  # general constants
  SENTINEL = -1

  # local variables
  numTurns = 0
  val = 0
  # game variables
  gameInPlay = True
  prompt = "Enter a value between 1 and 9 (" + str(SENTINEL) + " to quit): "
  
  a = [
    "0", "0", "0", 
    "0", "0", "0",
    "0", "0", "0"
  ]

  while gameInPlay:
    print("in play \n\n")

    # next player's turn
    numTurns += 1 

    if debug:
      print("debugging....")
      print(a)
      print("turn # " + str(numTurns))
    
    print(a[:3])
    print(a[3:6])
    print(a[6:])
    
    if numTurns % 2 == 0:
      computerMove = random.randint(1, 9)
      a[computerMove - 1] = "o"
    else: # elif numTurns % 2 == 1:
      userInput = ioFunctions.getIntegerInput(prompt)
      # user wants to exit     
      if userInput == SENTINEL:
        break
      elif not (userInput > 0 and userInput < 10):
        print("invalid input " + str(userInput))
      else:
        print("processing human's move")
        a[userInput - 1] = "x"
      
          

      if gameFunctions.isThereAWinInAnyRow(a) == True:
        print(a[:3])
        print(a[3:6])
        print(a[6:])
        print("there is a winner in a row")       
        break
      if gameFunctions.isThereAWinInAnyColumn(a) == True:
        print(a[:3])
        print(a[3:6])
        print(a[6:])
        print("there is a winner in a column")
        break
      if gameFunctions.isThereAWinInAnyDiagonal(a) == True:
        print(a[:3])
        print(a[3:6])
        print(a[6:])
        print("there is a winner in a diagonal")
        break
      if gameFunctions.isThereADraw(a) == True:
        print(a[:3])
        print(a[3:6])
        print(a[6:])
        print("there is a Draw")
        break
      if gameFunctions.isValidGameState(a) == False:
        print("Invalid Game State")
        break
      else:

        print("there is not a winner")


  print("goodbye, game is over")
  print(a)

##### main

if __name__ == "__main__":
  main()
