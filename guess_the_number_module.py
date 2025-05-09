import random
def greeting_message():
  """Welcome the user "print welcome to guess the number game"""
  print('Welcome to guess the number game.')

attempts = 0
#get the user difficulty choice and validate it
#
#a
#LOOP indefinitely(until the user enters a valid input)
#   print Prompt: 'Choose a difficulty level either "easy" or "hard":'
#   read the difficulty choice
#   convert the difficulty choice to lowercase and strip any whitespaces
#
#   IF the difficulty choice == 'eazy' or 'hard':
#       break out of the loop(a valid input has been entered)
#   Else:
#       print to the user "Invalid input entered"z(this handles when the user enters an empty space)
#   END IF
#END LOOP
#

def get_difficulty():
    while True:
        choice = input('Choose a difficulty, either "easy" or "hard": ').lower().strip()

        if choice == 'easy' or choice == 'hard':
            return choice
        else:
            print('Invalid input entered. type "easy" or "hard".')


EAZY_ATTEMPTS = 10
HARD_ATTEMPTS = 5


#Generate a random integer from 1 and 100 inclusive and store it as SECRET NUMBER
#
def generate_secret_number():
     secret_number = random.randint(1,100)
     return secret_number
#lOOP INDEFINITELY(until the user has guessed the number or have used up their remaining attempts)
#   print User_attempts_remaining
#
#   Loop indefinitely(until the user enters a valid input as a guess)
#       print Prompt: "Make a guess: "
#       read the user_guess
#       convert the user's guess into an integer
#
#       IF user_guess is an integer and in the range of 1 and 100 inclusive:
#           break out of loop(a valid input have been entered)
#       Else:
#           print 'Invalid input chosen' (this handles when the user enters an empty space
#       END IF
#   END LOOP
#
#   #Compare the user's guess to the secret number
#    IF user's guess is same as the secret number:
#       break out of the loop (the user have guessed the number)
#    ELIF user's guess is more than the secret number:
#       print "Too High"
#    Else:
#       print 'Too Low'
#   IF user have guessed != secret number:
#        decrease the user's attempts by 1
#   End IF
#
def get_user_guess():
    while True:
        guess = input('Make a guess: ')
        try:
            int_guess = int(guess)
            if int_guess in range(1, 101):
                return int_guess
            else:
                print('invalid number chosen, you can only enter integers')
        except ValueError:
            print('Invalid input chosen, That is not a number.')



def set_game_by_difficulty(difficulty):
    player_have_guessed_number = False

    while not player_have_guessed_number:
        global  attempts
        if difficulty == 'easy':

            attempts = EAZY_ATTEMPTS
        else:
            attempts = HARD_ATTEMPTS
        print(f'You have {attempts} attempts remaining to guess the number.')

        #this function gets the user's validated integer guess
        user_guess = get_user_guess()
        actual_number = generate_secret_number()
        
        if user_guess == actual_number:
            player_have_guessed_number = True
        elif user_guess > actual_number:
            print('Too high,Try again.')
        elif user_guess > actual_number:
            print('Too low, Try again')



set_game_by_difficulty('hard')
#Tell the user if they won or they lost
#IF user_guess is same as the secret number:
#     print('You won')
#ELse:
#    print('You lose)
#print: 'THe secret number was ' +secret_number
#
#Ask the user if they want to play again
#play_again = ask the user if they want to play again:
# if play_again == 'y':
#     start a new game(loop back to the welcome message)
#Else:
#    print "Goodbye for now come again later"(end program)
#
#
#
#
#
#
#
#EAZY_ATTEMPTS = 10 // this sets the number of attempts for the easy level
#HARD_ATTEMPTS = 5 // this sets the number of attempts for the hard level
