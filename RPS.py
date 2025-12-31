import random
def main():
    print("-=-Rock Paper Scissors-=-")
    elements = ["Rock", "Paper", "Scissors"]
    computer = random.choice(elements)
    user = User()

    print(computer)    
    if computer == "Paper" and user == "Scissors":
        print("You Win! :)") 
        exit              
    elif computer == "Rock" and user == "Paper":
        print("You Win! :)")
        exit
    elif computer == "Scissors" and user == "Rock":
        print("You Win! :)")
        exit
    elif computer == user:
        print("Draw")
        exit 
    else:
        print("You Lose :(")
        exit 

def User():
    elements = ["Rock", "Paper", "Scissors"]
    while True:
        try:
            user = input("Your choice? ")
            if (user not in elements):
                print("Invalid Input")
                continue
            else:
                return user
        except:
            exit


if __name__ == "__main__":
    main()