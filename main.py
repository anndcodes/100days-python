def loginSystem():
  print("REPLIT LOGIN SYSTEM")
  print(19*"-")
  print()
  username = "david"
  password = "baldies4life"

  while True:
    username_input = input("What is your username: > ")
    password_input = input("What is your password?: > ")
    if username_input == username and password_input == password:
      print("Welcome to Replit!")
      break
    else:
      print("Whoops, I don't recognise that username or password, try again.")
      continue

loginSystem()