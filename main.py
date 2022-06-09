import random

#creating a list of play options
#"R" represents Rock, "P" represents Paper, "S" represents Scissors
t = ["R", "P", "S"]

#assigning a random play to the computer using random choice method
computer = random.choice(t)

#setting player to False
player = False

while player == False:
    #setting player to True
    player = input(
        "To play the game pick an option: \n \'R\' for Rock \n \'P\' for Paper \n \'S\' for Scissors? "
    )
    if player == computer:
        print("The computer and player pick the same move")
    elif player == "R":
        if computer == "P":
            print(
                "Both player's moves in the format: Player (Rock) : Computer (Paper) \n You lose!"
            )
        else:
            print("You're the winner!")
    elif player == "P":
        if computer == "S":
            print(
                "Both player's moves in the format: Player (Paper) : Computer (Scissors) \n You lose!"
            )
        else:
            print("You're the winner!")
    elif player == "S":
        if computer == "R":
            print(
                "Both player's moves in the format: Player (Scissors) : Computer (Rock) \n You lose!"
            )
        else:
            print("You're the winner!")
    else:
        print("not amongst our options")
    #player was set to True, but we want it to be False so the loop continues
    player = False
    # computer = t[randint(0,2)]

#References:
#https://thehelloworldprogram.com/python/python-game-rock-paper-scissors/

#https://www.w3schools.com/python/trypython.asp?filename=demo_ref_random_choice
