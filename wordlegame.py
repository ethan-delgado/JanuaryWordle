# Import random library and store the words of january in a list
import random
wordle_jan2022 = ["rebus", "boost", "truss", "siege", "tiger", "banal", "slump", "crank", "gorge", "query", "drink", "favor", "abbey", "tangy", "panic", "solar", "shire", "proxy", "point", "robot", "prick", "wince", "crimp", "knoll", "sugar", "whack", "mount", "perky", "could", "wrung", "light"]
# INPUT: NONE
def word_choice():
    random_index = random.randint(0, len(wordle_jan2022) - 1)
# PROCESSING: randomly chooses a word from list (wordle_jan2022).
    random_word = wordle_jan2022[random_index].upper()
# OUTPUT: returns selected word.
    return random_word
# INPUT: Asks user for an input
def user_guess(i):
    guess = input("Guess" + str(i) + ":")
# PROCESSING: Checks if the guess is five letters long and is made up of only letters.
    while len(guess) != 5 or guess.isalpha() == False:
        print("Guess must be five letters.")
        guess = input("Guess" + str(i) + ":")
# OUTPUT: returns user guess as all-capital letters.
    guess = guess.upper()
    return guess
def guess_feedback():
# store the answer from the word generating function
    answer = str(word_choice())
    for i in range(1, 7):
        guess = user_guess(i)
        print(guess)
# if the words match the user wins
        if guess == answer:
            print(answer)
            print("\nCongrats, you got it!")
            break
# Restricts the user to only six guesses
        elif i == 6:
            print("\nThe word was:", answer)
# Iterates through both the answer and the guess as a list and compares letters to find relationship
        else:
            output1 = ""
            guess_list = list(guess)
            answer_list = list(answer)
            for i in range(len(guess_list)):
                if guess_list[i] in answer_list:
                    if guess_list[i] == answer_list[i]:
                        output1 += guess_list[i].upper()
                    elif guess_list[i] in answer_list and guess_list[i] != answer_list[i]:  
                        output1 += "#"
                else:
                    output1 += "_"
            print(output1)
# Calls all three functions to initiate the game
def wordle():
    guess_feedback()
print("WORDLE")
print("RULES")
print("An underscore means you guessed the wrong letter.")
print("A # Means you guessed the correct letter but in the wrong spot.")
print("A letter means you guessed the correct letter in the correct spot!")
wordle()
