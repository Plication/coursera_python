import random

def number_to_name(number):
    
    if number == 0:
        return 'rock'
    elif number == 1:
        return 'spock'
    elif number == 2:
        return 'paper'
    elif number == 3:
        return 'lizard'
    elif number == 4:
        return 'scissors' 

def name_to_number(guess):
    if guess == 'rock':
        return 0
    elif guess == 'spock':
        return 1
    elif guess == 'paper':
        return 2
    elif guess == 'lizard':
        return 3
    elif guess == 'scissors':
        return 4
    else:
        return 10
    
def rpsls(guess):

    number = random.randrange(0, 4)
    guess_number = name_to_number(guess)
    computer_choice = number_to_name(number)

    print('player choose',guess)
    print('computer choose',computer_choice)

    if guess_number == number:
        print('player and computer tie')
    elif 1 <= guess_number - number <= 2 or -4 <= guess_number - number <= -3:
        print('player win')
    elif -2 <= guess_number - number <= -1 or 3 <= guess_number - number <= 4:
        print('computer win')
    else:
        print('wrong input')

rpsls('rock')
rpsls('spock')
rpsls('paper')
rpsls('lizard')
rpsls('scissors')

while True:
    rpsls(input('your choice:'))
    



        



