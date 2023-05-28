print("Math Game")
print("Are you good with multiples? Let's find out!")
print()

multiples = int(input("Name your multiples: > "))
points = 0

for i in range(1, 11, 1):
  print(i, "x", multiples, "=")
  question = int(input())
  if question == multiples * i:
    points += 1
    print("Correct, great work 🥳")
  else:
    print("Nope 🙁 the answer was", multiples * i)


print("You scored", points, "out of 10!")











