import random


def greeting_message():
    """Welcome the user with a greeting message"""
    print('Welcome to guess the number game.')


def get_difficulty():
    """this asks the user for their difficulty and validates it, eventually returning the
    validated choice
    """
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
    """this generates the secret integer that the user has to guess"""
    secret_number = random.randint(1, 100)
    return secret_number

#
def get_user_guess():
    """this asks the user for their guess and validates its as an integer eventually
    returning the validated guess.
    """
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


# this generates the secret number to be guessed
actual_number = generate_secret_number()


def set_game_by_difficulty(difficulty):
    """this is the main heart of the program as it sets the game by the difficulty
    choice the user entered, shows them their available attempts, performs the whole
    operation of comparing their guess with the secret number, updating their number
    of attempts remaining and eventually return the user's final guess
    """
    attempts = 0
    if difficulty == 'easy':
        attempts = EAZY_ATTEMPTS
    else:
        attempts = HARD_ATTEMPTS

    user_guess = -1

    player_have_guessed_number = False
    while not player_have_guessed_number and attempts > 0:
        print(f'You have {attempts} attempts remaining to guess the number.')

        #this function gets the user's validated integer guess
        user_guess = get_user_guess()

        if user_guess == actual_number:
            player_have_guessed_number = True
            print('Correct!')
        elif user_guess > actual_number:
            print('Too high,Try again.')
        elif user_guess < actual_number:
            print('Too low, Try again')
        if attempts != 0:
            attempts -= 1
    return user_guess


def give_feedback(f_guess):
    """this gives the user feedback of whether they have lost or won and
     the secret number they were trying to guess as output
     """
    if f_guess == actual_number:
        print('You win')
    else:
        print('Sorry, You lose!')
    print(f'The secret number was {actual_number}')


while input('Do you want to play again: "y" or "n": ').lower() == 'y':
    print('\n' * 12)
    greeting_message()
    difficulty_choice = get_difficulty()
    report = set_game_by_difficulty(difficulty_choice)
    give_feedback(report)

print('Goodbye,Thanks for playing!')
