import random 

correctNum = random.randint(0, 10)
numGuesses = 1

while True:
    num = input("Enter a number please: ")
    num = int(num)

    if num > correctNum:
      print("Your number is too big.")
    elif num < correctNum:
      print("Your number is  too small.")
    elif num == correctNum:
      print("You have guessed the number in " + str(numGuesses) + " tries. Yay!")
      break

    numGuesses == numGuesses + 1