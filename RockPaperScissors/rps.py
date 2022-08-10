import random

import rpsfun

print('-------------------------------------')
print('WELCOME TO ROCK, PAPER, SCISSORS GAME')
print('-------------------------------------')

player_name = input('Please enter your name: ')
print('-------------------------------------')

print('0: Rock, 1: Paper, 2: Scissors')
print('-------------------------------------')
player_hand = int(input('Pick a hand: '))

if rpsfun.validate_hand(player_hand):
    computer_hand = random.randint(0, 2)

    rpsfun.print_hand(player_hand, player_name)
    rpsfun.print_hand(computer_hand, 'Computer')

    result = rpsfun.judge(player_hand, computer_hand)
    print('Result: ' + str(result))

else:
    print('Pease enter a valid number')
