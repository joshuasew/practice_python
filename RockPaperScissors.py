# Joshua Sew-Hee
# 6/14/18
# Rock Paper Scissors

print("This is a two-player Rock-Paper-Scissors game.")
print("Remember the rules:")
print("Rock beats scissors\nScissors beats paper\nPaper beats rock")

player1 = input("Player 1 input: ")
player2 = input("Player 2 input: ")
p1 = player1.lower()
p2 = player2.lower()

playAgain = True
while (playAgain == True):
    if ((p1 == 'rock' and p2 == 'scissors') or (p1 == 'scissors' and
    p2 == 'paper') or (p1 == 'paper' and p2 == 'rock')):
        print("Congratulations Player 1! You win.")
    elif ((p2 == 'rock' and p1 == 'scissors') or (p2 == 'scissors' and
    p1 == 'paper') or (p2 == 'paper' and p1 == 'rock')):
        print("Congratulations Player 2! You win.")
    else:
        print("Tie game.")

    q1 = input("Do you want to play again Player 1? (y/n) ")
    q2 = input("Do you want to play again Player 2? (y/n) ")
    if q1 == 'y' and q2 == 'y':
        player1 = input("Player 1 input: ")
        player2 = input("Player 2 input: ")
        p1 = player1.lower()
        p2 = player2.lower()
    else:
        playAgain = False
        print("Thanks for playing.")
