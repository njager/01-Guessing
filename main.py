import sys, random

assert sys.version_info >= (3,7), "This script requires at least Python 3.7"

quit = False

play_game = input("Hi! Want to play a game (Y/Yes or N/No)?") #determine play or no play
play_game = play_game.lower()
while play_game != "yes" or "y":
    if play_game == "yes" or play_game == "y":
        quit = False
        break
    elif play_game == "no" or play_game == "n":
        print("\nSorry to hear that :( Maybe next time!")
        quit = True
        sys.exit()
    else:
        print("I'm sorry, your response doesn't make sense. Yes/Y or No/N?")
        play_game = input()
        play_game = play_game.lower()

print("\nGreat! This is a random number guessing game.")

print("Please choose your desired difficulty")#determine difficulty
difficulty = input("Easy , Medium , Hard:\n")
difficulty = difficulty.lower()
while difficulty != "easy" or "medium" or "hard":
    if difficulty == "easy":
        range = 10
        break
    elif difficulty == "medium":
        range = 100
        break
    elif difficulty == "hard":
        range = 1000
        break
    else:
        print("Sorry, I didn't catch that. Could you please repeat which difficulty you desire?")
        difficulty = input("Easy , Medium , Hard: \n")
        difficulty = difficulty.lower()

print("\nOkay! You chose {}" .format(difficulty))

while not quit:
    random_number = random.randint(1,range) #random number input and guesses begin
    count = 1
    number = -1
    while number != random_number:
        number = input("Please guess a number between 1 and {}: ".format(range))
        if not number.isdigit():
            print("Silly, that's not a number! Try again")
        else:
            number = int(number)
            count = count + 1
            if number > random_number:
                print("Sorry, you didn't get it right")
                print("Too high\n")
            elif number < random_number:
                print("Sorry, you didn't get it right")
                print("Too low\n")
    print("Good job!")
    print("You guessed it in {} tries!".format(count))
    play_again = input("\nWould you like to play again (Y/Yes or N/No)? ")
    play_again = play_again.lower()
    if play_again == "yes" or play_again== "y":
        quit = False
        print("Please choose your desired difficulty")#determine difficulty
        difficulty = input("Easy , Medium , Hard:\n")
        difficulty = difficulty.lower()
        while difficulty != "easy" or "medium" or "hard":
            if difficulty == "easy":
                range = 10
                break
            elif difficulty == "medium":
                range = 100
                break
            elif difficulty == "hard":
                range = 1000
                break
            else:
                print("Sorry, I didn't catch that. Could you please repeat which difficulty you desire?")
                difficulty = input("Easy , Medium , Hard:\n")
                difficulty = difficulty.lower()
    else:
        print("\n\nThanks for playing! See you later!")
        quit = True