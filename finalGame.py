from random import seed
from random import randint

seed(1)
correct_guess = False
secret_number = randint(0,100);
name = input("What mode do you want?\n")

if name.lower() == 'free':
  print("you have chosen free play")
  while not correct_guess:
    guess = int(input("guess the input\n"))
    if guess > secret_number:
      print("your guess is larger than the number")
    elif guess < secret_number:
      print("your guess is smaller than the number")
    else:
      print("you guessed correctly!");
      correct_guess = True



elif name.lower() == 'limited':
  print("you have chosen limited play")
  for x in range(0,9):
    if correct_guess == True:
      break
    guess = int(input("guess the input\n"))
    if guess > secret_number:
      print("your guess is larger than the number")
    elif guess < secret_number:
      print("your guess is smaller than the number")
    else:
      print("you guessed correctly!");
      correct_guess = True
  if correct_guess == False:
    print("you failed!")
