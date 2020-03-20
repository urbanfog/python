print("Please think of a number between 0 and 100! ")
low = 0
high = 100
guess = 0
guessed = False

while guessed == False:
  guess = (low + high) // 2
  print("Is your secret number", str(int(guess))+"?")
  response = input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly. ")
  if response not in "hlcHLC":
    print("Sorry, I did not understand your input.")
  elif response in "hH":
    high = guess
  elif  response in "lL":
    low = guess
  elif response in "cC":
    print("Game over. Your secret number was:", str(int(guess)))
    guessed = True
