import random
while True:
    choices =["rock","paper","scissor"]
    computer = random.choice(choices)
    player = None
    while player not in choices:
        player = input("rock,paper or scissor? : ").lower()
    if player == computer:    
        print("player : ",player)
        print("computer : ",computer)
        print("Tie!")
    elif player == "rock":
        if computer == "paper":
            print("player : ",player)
            print("computer : ",computer)
            print("You lose!")
        if computer == "scissor":
            print("player : ",player)
            print("computer : ",computer)
            print("You win!")
    elif player == "paper":
        if computer == "rock":
            print("player : ",player)
            print("computer : ",computer)
            print("You win!")
        if computer == "scissor":
            print("player : ",player)
            print("computer : ",computer)
            print("You lose!")
    elif player == "scissor":
        if computer == "rock":
            print("player : ",player)
            print("computer : ",computer)
            print("You lose!")
        if computer == "paper":
            print("player : ",player)
            print("computer : ",computer)
            print("You win!")        
    play_again = input("you want to play_again yes/no : ").lower()
    if play_again != "yes":
        break
print("bye")




