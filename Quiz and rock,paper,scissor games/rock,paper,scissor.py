import random

while True:
    choices=["rock","paper","scissor"]
    computer=random.choice(choices)
    you=None
    while you not in choices:
        you=input("rock, paper or scissor?: ").lower()

    if computer==you:
        print("computer "+computer)
        print("you "+you)
        print("Draw")
    elif you=="rock":
        print("computer "+computer)
        print("you "+you)
        if computer=="paper":
            print("you Lose!")
        else:
            print("you win!")
    elif you=="paper":
        print("computer "+computer)
        print("you "+you)
        if computer=="scissor":
            print("you Lose!")
        else:
            print("you win!")
    elif you=="scissor":
        print("computer "+computer)
        print("you "+you)
        if computer=="rock":
            print("you Lose!")
        else:
            print("you win!")
            
    playagain=input("Do you want to play again(y/n)").lower()
    if playagain=='n':
        break
print("bye!")
        

            


