import random

rock = 1
paper = 2
scissors = 3


def playAgain():
    userInput2 = input("Play again? Y/N")
    if userInput2 == ("Y"):
        game()
    elif userInput2 == ("N"):
        return
    else:
        print ("Please try again")
        playAgain()


def game():
    botScore = 0
    playerScore = 0
    computerChoice = random.randint(1, 3)
    userInput = int(input("1 for rock, 2 for paper, 3 for scissors: "))
    if userInput == computerChoice:
        print("Draw")
        print (playerScore,("vs"), botScore)
    elif (userInput == 1 and computerChoice == 3) or (userInput == 2 and computerChoice == 1) or (userInput == 3 and computerChoice == 2):
        print("You win")
        playerScore = playerScore + 1
        print (playerScore,("vs"), botScore)
    else:
        print("You lose")
        botScore = botScore + 1
        print (playerScore,("vs"), botScore)
    playAgain()
    

game()