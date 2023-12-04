import random
import time
#Turning on the game
game_on = 1
#Allow Users to play either coin toss or dice toss guessing game
while game_on == 1:
    #Setting up game parameters
    total_guesses = 0
    total_correct = 0
    game_mode = input("Would you like to play coin toss (CT), dice roll (DR), or quit the game (Q)? ")
    game_mode = game_mode.lower()
    while game_mode not in ["coin toss", "coin", "toss", "ct", "dice roll", "dice", "roll", "dr", "quit", "q", "quit the game"]:
        print("That is not an valid input for selecting a game.")
        game_mode = input("Would you like to play coin toss (CT) or dice roll (DR)? ")
        game_mode = game_mode.lower()
    else:
        if game_mode in ["coin toss", "coin", "toss", "ct"]:
            game_mode = "coin toss"
        elif game_mode in ["dice roll", "dice", "roll", "dr"]:
            game_mode = "dice roll"
        else:
            print("Thank you for playing! Have a great day!")
            game_on = 0
    if game_mode == "coin toss":
        coin_toss = 1
        print("Welcome to the " + game_mode + " guessing game!")
        print()
        while coin_toss == 1:
            #Allowing the user to guess the outcome of the coin flip
            guess = input("Would you like to guess Heads (H) or Tails (T)? ")
            guess = guess.lower()
            while guess not in ["heads", "head", "h", "tails", "tail", "t"]:
                print("That is not an valid input for coin toss guessing.")
                guess = input("Would you like to guess Heads (H) or Tails (T)? ")
                guess = guess.lower()
            else:
                if guess in ["heads", "head", "h"]:
                    guess_display = "Head"
                    guess = 1
                elif guess in ["tails", "tail", "t"]:
                    guess_display = "Tail"
                    guess = 0
            print("Your guess is a " + guess_display)
            total_guesses += 1
            #Produce and display the coin flip
            print("Tossing coin...")
            time.sleep(1)
            toss = random.randint(0,1)
            if toss == 1:
                print("It is a Head!")
                toss_display = "Head"
            else:
                print("It is a Tail!")
                toss_display = "Tail"
            #Evaluate the guess vs. actual toss
            time.sleep(1)
            print("Your guess was a " + guess_display + " and the actual coin toss was a " + toss_display + "!")
            if guess == toss:
                print("Great job! You were correct in your prediction!")
                total_correct += 1
            else:
                print("Unfortunately, that was not the right prediction. Try again!")
            correct_percentage = round(total_correct / total_guesses * 100, 1)
            print("You are correct " + str(total_correct) + " times out of " + str(total_guesses) + " guesses. That is a win percentage of " + str(correct_percentage) + " %!")
            time.sleep(1)
            continue_game = input("Would you like to play again? (Y/N)")
            continue_game = continue_game.lower()
            while continue_game not in ["yes", "y", "ya", "no", "n"]:
                print("That is not an valid input. Please enter Yes (Y) or No (N).")
                continue_game = input("Would you like to play again? (Y/N)")
                continue_game = continue_game.lower()
                time.sleep(1)
            if continue_game in ["no", "n"]:
                print("Thanks for playing the " + game_mode + ". Choose another game?")
                coin_toss = 0
            else:
                print("Alright! Another round!")
    if game_mode == "dice roll":
        dice_roll = 1
        print("Welcome to the " + game_mode + " guessing game!")
        print()
        while dice_roll == 1:
            #Allowing the user to guess the outcome of the dice roll
            guess = input("Please pick a number between 1 and 6. ")
            while int(guess) not in range(1,7):
                print("That is not an valid input for coin toss guessing.")
                guess = input("Please pick a number between 1 and 6. ")
            guess_display = str(guess)
            print("Your guess is a " + guess_display)
            total_guesses += 1
            #Produce and display the dice roll
            print("Rolling dice...")
            time.sleep(1)
            roll = random.randint(1,6)
            roll_display = str(roll)
            #Evaluate the guess vs. actual roll
            time.sleep(1)
            print("Your guess was " + guess_display + " and the actual die roll was a " + roll_display + "!")
            if int(guess) == roll:
                print("Great job! You were correct in your prediction!")
                total_correct += 1
            else:
                print("Unfortunately, that was not the right prediction. Try again!")
            correct_percentage = round(total_correct / total_guesses * 100, 1)
            print("You are correct " + str(total_correct) + " times out of " + str(total_guesses) + " guesses. That is a win percentage of " + str(correct_percentage) + " %!")
            time.sleep(1)
            continue_game = input("Would you like to play again? (Y/N)")
            continue_game = continue_game.lower()
            while continue_game not in ["yes", "y", "ya", "no", "n"]:
                print("That is not an valid input. Please enter Yes (Y) or No (N).")
                continue_game = input("Would you like to play again? (Y/N)")
                continue_game = continue_game.lower()
                time.sleep(1)
            if continue_game in ["no", "n"]:
                print("Thanks for playing the " + game_mode + ". Choose another game?")
                dice_roll = 0
            else:
                print("Alright! Another round!")