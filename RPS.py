import random
import sys

shape = ["rock", "paper", "scissors"]
print("Welcome to Rock, Paper, Scissors")

def end_game(winner):
    if winner == "none":
        print("Tie! Play again\n")
        rock_paper_scissors()
    else:
        print(winner + " Wins!\n")
        play = input("Would you like to play again? Enter yes or no\n").lower()
        if play == "yes":
            rock_paper_scissors()
        else:
            sys.exit()

def rock_paper_scissors():
    player = input("\nChoose Rock, Paper, or Scissors\n").lower()
    computer = shape[random.randrange(0,2)]

    print("Player: " + player)
    print("Computer: " + computer)
    winner = "none"
    if player == "rock":
        if computer == "paper":
            winner = "Computer"
        elif computer == "scissors":
            winner = "Player"
        end_game(winner)
    elif player == "scissors":
        if computer == "rock":
            winner = "Computer"
        elif computer == "paper":
            winner = "Player"
        end_game(winner)
    elif player == "paper":
        if computer == "scissors":
            winner = "Computer"
        elif computer == "rock":
            winner = "Player"
        end_game(winner)
    else:
        print("Invalid Input. Try Again\n")
        rock_paper_scissors()


rock_paper_scissors()
