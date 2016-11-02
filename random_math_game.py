'''
    GARRETT GUEVARA
    PYTHON PRACTICE
    SIMPLE MATH GUESSING GAME
'''

import random

def game():
    secret_num = random.randint(1, 10)
    lives = 3
    print("Oh no! Someone has planted a bomb between the numbers 1 and 10!")
    print("If you can guess the correct number in 3 tries, \nyou can diffuse the bomb and save the day.")
    
    while lives > 0:
        # print error message if guess is not an int
        try:
            guess = int(input("Here we go...Guess a number between 1 and 10.: "))
        except ValueError:
            print("{} isn't a number! Try again.".format(guess))

        # if input is acceptable          
        else:
            if guess == secret_num:
                print("You got it! The bomb was under number {}! You're a hero!".format(secret_num))
                break
            elif guess > secret_num:
                lives -= 1
                print("That's not it! Your guess was too high.")
                print("You have {} tries left!".format(lives))
            else:
                lives -= 1
                print("That's not it! Your guess was too low.")
                print("You have {} tries left!".format(lives))

    else:
        print("BOOM! The bomb went off, it was under number {}.".format(secret_num))
        reset = True
        while reset:
            # ask play again and sanitize responses
            play_again = (input("\nWould you like to play again? y/n ").lower())
            if play_again == 'y':
                reset = False
                game()
            elif play_again == 'n':
                print("Goodbye!")
                reset = False
            # print error message if guess not 'y' or 'n'
            elif play_again != 'y' or 'n':
                print("Whoops, {} is not an accepted value. Type 'y' for YES or 'n' for NO.".format(play_again))

game()
