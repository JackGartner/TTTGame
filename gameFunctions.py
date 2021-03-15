
# Global Variables
P1 = "x"   # token for player 1
P2 = "o"   # token for player 2
BL = "0"    # token for BL/blank space


def isThereAWinInAnyRow(a):
  # checking for a wins
  if a[0] == P1 and a[1] == P1 and a[2] == P1:
    return True
  
  # checking for o wins
  if a[0] == P2 and a[1] == P2 and a[2] == P2:
    return True

  # checking for a wins row 2
  if a[3] == P1 and a[4] == P1 and a[5] == P1:
    return True
  # checking for o wins row 2
  if a[3] == P2 and a[4] == P2 and a[5] == P2:
    return True

  # checking for a wins row 3
  if a[6] == P1 and a[7] == P1 and a[8] == P1:
    return True
  # checking for o wins row 3
  if a[6] == P2 and a[7] == P2 and a[8] == P2:
    return True

  # no winner
  return False

def isThereAWinInAnyColumn(a):
  # checking for a wins
  if a[0] == P1 and a[3] == P1 and a[6] == P1:
    return True
  
  # checking for o wins
  if a[0] == P2 and a[3] == P2 and a[6] == P2:
    return True

  # checking for a wins column 2
  if a[1] == P1 and a[4] == P1 and a[7] == P1:
    return True
  # checking for o wins column 2
  if a[1] == P2 and a[4] == P2 and a[7] == P2:
    return True

  # checking for a wins column 3
  if a[2] == P1 and a[5] == P1 and a[8] == P1:
    return True
  # checking for o wins column 3
  if a[2] == P2 and a[5] == P2 and a[8] == P2:
    return True

  # no winner
  return False

def isThereAWinInAnyColumn2(a):
    # checking for x wins
  for i in (0, 3, 6):
    if x[i] == BL:
      return False
    elif x[i] == P1 and x[i - 3] != P1:
      return False

  # checking for o wins
  for i in (0, 3, 6):
    if x[i] == BL:
      return False
    elif x[i] == P2 and x[i - 3] != P2:
      return False

def isThereAWinInAnyDiagonal(a):
  # checking for a wins
  if a[0] == P1 and a[4] == P1 and a[8] == P1:
    return True
  
  if a[0] == P2 and a[4] == P2 and a[8] == P2:
    return True

  # checking for o wins
  if a[2] == P1 and a[4] == P1 and a[6] == P1:
    return True

  if a[2] == P2 and a[4] == P2 and a[6] == P2:
    return True

  # no winner
  return False

def isThereADraw(a):

  # checking for BL spaces
  if a[0] == BL or a[1] == BL or a[2] == BL or a[3] == BL or a[4] == BL or a[5] == BL or a[6] == BL or a[7] == BL or a[8] == BL:
    return False

  # BL spaces
  return True

def isValidGameState(a):
  for i in range (len(a)):
    if (len(a)) == 10:
      return True

def isThereAWinInAnyRow2(a):
  # checking for a wins
  for i in range(3, 6):
    if a[i] == BL:
      return False
    elif a[i] == P1 and a[i + 1] != P1:
      return False

  # checking for o wins
  for i in range(3, 6):
    if a[i] == BL:
      return False
    elif a[i] == P2 and a[i + 1] != P2:
      return False

  # is a winner
  return True





def isGameOver(a):
  product = 1
  for i in range(9):
    product *= a[i]

  if product == 0:
    return False
  
  return True


