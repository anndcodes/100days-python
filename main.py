print(20*"*", "List Generator", 20*"*")
print()
print("Please, enter a starting number, an ending number and a increment number, so I can make a list for you! Useful, innit? 🤗")
print()

starting_number = int(input("Enter a starting number: > "))
ending_number = int(input("Enter an ending number: > "))
increment_number = int(input("And finally an increment number: > "))

for i in range (starting_number, ending_number, increment_number):
  print(i)