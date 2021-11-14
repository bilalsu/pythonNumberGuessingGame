import random

def guess(x):
    random_number = random.randint(1,x)
    guess = 0
    while guess != random_number:
        guess = int(input(f'Guess a number between 1 and {x}: '))
        if guess < random_number: print ('Sorry guess again, you guessed too low.')
        elif guess > random_number: print('Sorry guess again, you guessed too high.')
    
    print (f'Yay, congrats. You guessed {random_number} correctly!')

guess(100)

