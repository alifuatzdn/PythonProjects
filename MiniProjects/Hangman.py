import random
from words import words

def get_word(words):
    word = random.choice(words)
    while "-" in word or " " in word:
        word = random.choice(words)
    return word.upper()

def print_word(word, list1, list2):
    for i in word:
        if i in list1:
            print(i, end="")
        else:
            print("_", end="")
    if len(list2) != 0:
        print(f" Guessed words: {', '.join(list2)}")
def hangman():
    right = 10
    word = get_word(words)
    right_guessed = []
    wrong_guessed = []
    alph = "qwertyuıopasdfghjklzxcvbnm"
    print("_"*len(word), f"It contain {len(word)} words.")
    while right != 0:
        guess = input("\nEnter a letter or guess: ").upper()
        if right == 0:
            print_word(word, right_guessed, wrong_guessed)
            print(f"You don't have any guess left. The word was {word}.")
        if len(guess) == 1:
            if guess in wrong_guessed or guess in right_guessed:
                print_word(word, right_guessed, wrong_guessed)
                print("You have already enter this letter. Please try again.")
            else:
                if guess in word:
                    right_guessed.append(guess)
                    print_word(word, right_guessed, wrong_guessed)
                else:
                    if guess not in alph.upper():
                        print_word(word, right_guessed, wrong_guessed)
                        print("\nYou entered invalid guess. Please try again")
                    else:
                        right -= 1
                        wrong_guessed.append(guess)
                        print_word(word, right_guessed, wrong_guessed)
                        print(f"Wrong guess. You have {right} rights left.")
        elif len(guess) == len(word):
            if guess == word:
                print(f"{word}\nCongratulation, you win the game.")
            else:
                right -= 1
                print_word(word, right_guessed, wrong_guessed)
                print(f"\nWrong guess. You have {right} rights left.")
        elif len(guess) >= 1:
            print_word(word, right_guessed, wrong_guessed)
            print(f"\nYou should enter {len(word)} letter word. Please try again")
        else:
            print_word(word, right_guessed, wrong_guessed)
            print("\nYou entered invalid guess. Please try again")

hangman()

# 1
# 1
# 1
# 1
# 1
# 1
# 1
