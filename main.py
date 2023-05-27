print(10*"*","Loan Calculator", 10*"*")
print()
print("$1000 over 10 years at 5% APR")
print(37*"_")
print()

value = 1000
counter = 0
for i in range(10):
  extra = value * 0.05
  value += extra
  loan = round(value, 2)
  counter += 1
  print("Year", counter, "is", loan)

print()
paid = round((loan - 1000), 2)
print("You paid", paid, "in interest!")

