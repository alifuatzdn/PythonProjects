import random

def guess_user(x):
    real_num = random.randrange(1, x)
    num = 10
    while num != 0:
        guess = input(f"Enter your guess(1-{x}): ")
        try:
            guess = int(guess)
            if guess > x or guess < 1:
                print(f"Your guess isn't in the interval. Please try again.")
            elif guess == real_num:
                print("You win this game. Congratulations.")
                break
            else:
                num -= 1
                if num == 0:
                    print(f"Wrong guess. You don't have any rights left.")
                else:
                    if guess < real_num:
                        print(f"Wrong guess. Too low, you have {num} rights left.")
                    else:
                        print(f"Wrong guess. Too high, you have {num} rights left.")
        except ValueError:
            print("Invalid guess. Try again.")

def guess_comp(x):
    feedback = 0
    guessed = []
    while feedback != 1:
        guess = random.randrange(1, x+1)
        if guess not in guessed:
            guessed.append(guess)
            if len(guessed) == x:
                print(f"The number must be {guess}. There are no more numbers left in this interval.")
            else:
                while True:
                    print(guess)
                    feedback = input("If the guess is correct enter 1, else 0: ")
                    try:
                        feedback = int(feedback)
                        if feedback != 1 and feedback != 0:
                            print("Invalid choice. Try Again.")
                        else:
                            break
                    except ValueError:
                        print("Invalid choice. Try Again.")
    print("Yes. I've done it.")

guess_comp(10)