print(21*"♡", "Guess the Number Game", 21*"♡")
print()
print("You need to choose a number between 0 and 1.000. Can you guess it?")
print(66*"_")
print()
correct_number = 910
attempts = 0

while True:
  guess_number = int(input("Please, enter a number. > "))
  if guess_number < correct_number and guess_number > 0:
    print("Oops, too low.")
    print()
    attempts += 1
    continue
  elif guess_number > correct_number:
    print("Oops, too high!")
    print()
    attempts += 1
    continue
  elif guess_number == correct_number:
    attempts += 1
    print("YEY!! Correct!! 🥳")
    print()
    print(f"It took you {attempts} guesses to get it correct!")
    print()
    break
    exit()
  elif guess_number < 0:
    print("Oh god... I'm done")
    exit()
  else:
    print("Hmm...")
    
print("Well done! 🤠🫶💖🫶🤠")