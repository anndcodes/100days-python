import random

print("Infinity Dice 🎲")
print()
sides = int(input("How many sides?: "))
play_again = "yes"


def rollDice(sides):
  print("You rolled ", random.randint(1, sides))
  
while play_again == "yes":
  rollDice(sides)
  play_again = input("Roll again?: ")

