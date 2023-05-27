from getpass import getpass as input

print(35*"-", "EPIC 🪨 📄✂ BATTLE", 35*"-")
print()

result_rock = "Rock beats Scissors 🪨"
result_paper = "Paper beats Rock 📄"
result_scissors = "Scissors beats Paper ✂️"
result_tie = "Aw it's a tie 😓"
result_player1 = "Player One just won the round!"
result_player2 = "Player Two just won the round!"

player1_score = 0
player2_score = 0

while True: 
  print("To start, please select your move (R for 'Rock', P for 'Paper', and S for Scissors.")
  print()
  
  player_one = input("Select your move: R, P or S > ")
  player_two = input("Select your move: R, P or S > ")
  print()
  
  if player_one == "R" and player_two == "S":
    player1_score += 1
    print(result_player1, result_rock)
    print("Player One has", player1_score, "points. And player Two has", player2_score, "points.")
  elif player_one == "P" and player_two == "R":
    player1_score += 1
    print(result_player1, result_paper)
    print("Player One has", player1_score, "points. And player Two has", player2_score, "points.")
  elif player_one == "S" and player_two == "P":
    player1_score += 1
    print(result_player1, result_scissors)
    print("Player One has", player1_score, "points. And player Two has", player2_score, "points.")
  elif player_one == "R" and player_two == "R":
    print(result_tie)
  elif player_one == "P" and player_two == "P":
    print(result_tie)
  elif player_one == "S" and player_two == "S":
    print(result_tie)
  elif player_two == "R" and player_one == "S":
    player2_score += 1
    print(result_player2, result_rock)
    print("Player Two has", player2_score, "points. And player One has", player1_score, "points.")
  elif player_two == "P" and player_one == "R":
    player2_score += 1
    print(result_player2, result_paper)
    print("Player Two has", player2_score, "points. And player One has", player1_score, "points.")
  elif player_two == "S" and player_one == "P":
    player2_score += 1
    print(player_two, result_scissors)
    print("Player Two has", player2_score, "points. And player One has", player1_score, "points.")
  else:
    print("Please, select a correct option, and make sure you use uppercase letter!")

  if player1_score == 3:
    print("The winner is Player One! Congrats 🥳")
    break
    exit()
  elif player2_score == 3:
    print("The winner is Player Two! Congrats 🥳")
    break
    exit()
  elif player1_score != 3 or player2_score != 3:
    continue
  else:
    print("🙂")
print("Congrats to the winner, the game has ended!")