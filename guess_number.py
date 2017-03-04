import SimpleGUICS2Pygame.simpleguics2pygame as simplegui
import random
import math

num_range = 100



def new_game():
    get_intput()

def range100():
    global num_range
    num_range = random.randrange(0, 100)
    return num_range

def range1000():
    global num_range
    num_range = random.randrange(0, 1000)
    return num_range

def get_input(guess):

    guess = int(guess)
    if guess < num_range:
        print('higher')
    elif guess == num_range:
        print('done')
    else:
        print('lower')
    

f = simplegui.create_frame('guess the number', 200, 200)
f.add_button('range is (0, 100)', range100, 200)
f.add_button('range is (0, 1000)', range1000, 200)
f.add_input('enter a guess:', get_input, 200)

#timer = simplegui.create_timer(1000, tick)  
#timer.start()  

f.start()

new_game()
