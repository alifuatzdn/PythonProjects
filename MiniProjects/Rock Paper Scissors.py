import random

def rps():
    comp_score = 0
    user = 0
    while True:
        choice = input("Enter your choice: ").lower()
        comp = random.randrange(1, 4)
        materials = {1: "rock", 2: "paper", 3: "scissors"}
        if choice == "rock" or choice == "paper" or choice == "scissors":
            if choice == materials[comp]:
                print(f"{choice.capitalize()} = {materials[comp]}, draw. Score: {user}-{comp_score}")
            else:
                if (choice == "rock" and comp == 3) or (choice == "paper" and comp == 1) or (choice == "scissors" and comp == 2):
                    user += 1
                    print(f"{choice.capitalize()} beats {materials[comp]}, you win. Score: {user}-{comp_score}")
                else:
                    comp_score += 1
                    print(f"{materials[comp].capitalize()} beats {choice}, you lose. Score: {user}-{comp_score}")
        else:
            print("Enter a valid choice.")

rps()
