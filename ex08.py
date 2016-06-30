#rps 2-player

# Defines the accepted inputs available to the players
accepted_strings={'rock','paper','scissors'}

# Multiple ways of doing the while loop

# 1st -Player 1 input using "while True"
# while True:
#     player1=input("Player 1: Please type Rock, Paper, or Scissors:")
#     player1_a=player1.lower()
#     player1_b=player1_a.replace(" ","")
#     if player1_b in accepted_strings:
#         break
#     else:
#         continue

# 2nd - Using "while player1_a"
player1=input("Player 1: Please type Rock, Paper, or Scissors:")
player1_=player1.lower().replace(" ","")
while player1_ not in accepted_strings:
    player1=input("Player 1: Please type Rock, Paper, or Scissors:")
    player1_=player1.lower().replace(" ","")

player2=input("Player 2: Please type Rock, Paper, or Scissors:")
player2_=player2.lower().replace(" ","")
while player2_ not in accepted_strings:
    player2=input("Player 2: Please type Rock, Paper, or Scissors:")
    player2_=player2.lower().replace(" ","")


def game(player1_,player2_):

    if player1_==player2_:
        print("This is a tie!")

    elif player1_=="rock":
        if player2_=="scissors":
            print("Player 1 wins with",player1_)
        elif player2_=="paper":
            print("Player 2 wins with",player2_)
        else:
            print("Check this: player1:",player1_,"player2:",player2_)

    elif player1_=="scissors":
        if player2_=="rock":
            print("Player 2 wins with",player2_)
        elif player2_=="paper":
            print("Player 1 wins with",player1_)
        else:
            print("Check this: player1:",player1_,"player2:",player2_)

    elif player1_=="paper":
        if player2_=="rock":
            print("Player 1 wins with",player1_)
        elif player2_=="scissors":
            print("Player 2 wins with",player2_)
        else:
            print("Check this: player1:",player1_,"player2:",player2_)

    else:
        print("Check what has happened here")
        print("Player1:",player1)
        print("Player2:",player2)

    

if __name__=='__main__':
    game(player1_,player2_)
