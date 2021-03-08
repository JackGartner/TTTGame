def getIntegerInput(prompt):
  while True:
    try:
      userInput = int(input(prompt))       
    except ValueError:
      print("Not an integer! Try again.")
      continue
    else:
      return userInput 
      break 
