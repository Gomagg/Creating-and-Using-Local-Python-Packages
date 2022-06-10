# Creating-and-Using-Local-Python-Packages
Using Rock-Paper-Scissors game
Rock-Paper-Scissors is a simple two-player game where, at a signal, players make figures with their hands, representing a rock, a piece of paper, or a pair of scissors. The winner is determined according to a set of rules.

 

Rock Paper Scissors:

In rock paper scissors, if the two players choose the same “character” it’s a tie, and the game repeats

Rock beats Scissors

Paper beats Rock

Scissors beats Paper

Here I created a simple version of the (Rock Paper Scissors) game  with Python. One player will be controlled by the computer and the other player controlled by individual playing the game - the user (i.e CPU or Computer vs Player). 

Here I also make use of the inbuilt Python module random and its choice method.

Instructions:

I created a new Python file and called it main.py. Inside it I created the game.

I Created a list called 't' to store all possible options:

"R" for "rock", 

"P" for "paper", 

"S" for "scissors".

While running the program, the user picks an option between ("R", "P" or "S")

If user input is invalid (Program tells the user "not amongst our options"), print an erro and ask for their input again (being a (while) loop)

Using the 'choice' function from the inbuilt Python 'random' module to make a choice for CPU player(computer).

Both player's moves is printed in the format: 'Player (Rock) : CPU (Paper)'

The program checks both player's moves: 

If there is a winner, the program prints "you're the winner", and the program ends. 

If it's a tie (the computer and player pick the same move) and the program (game) restarts again.
