print(15*"*", "Fill in the blank lyrics", 15*"*")
print()
print("Try to figure out the missing word as quickly as you can!")
print()
print()

counter = 1;

while True:
  lyrics = input("Country roads... Take me home to the place I ______. ")
  if lyrics == "belong" or lyrics == "Belong":
    print("Well done! You got it right!")
    break
  else:
    print("Hm try again!")
    counter +=1
print("Thanks for playing")

print("You got the correct lyrics in,", counter, "attempt(s).")