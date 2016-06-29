#rps 2 player

accepted_strings={'rock','paper','scissors'}
player1_b=""
player2_b=""

while player1_b in accepted_strings:
    player1=input("Player 1: Please type Rock, Paper, or Scissors:")
    player1_a=player1.lower()
    player1_b=player1_a.replace(" ","")

while player2_b in accepted_strings:
    player2=input("Player 2: Please type Rock, Paper, or Scissors:")
    player2_a=player2.lower()
    player2_b=player2_a.replace(" ","")
