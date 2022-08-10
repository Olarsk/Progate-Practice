def print_hand(hand, name='Guest'):
    hands = ['Rock', 'Paper', 'Scissors']
    print(name + ' picked ' + hands[hand])


def validate_hand(hand):
    if hand < 0 or hand > 2:
        return False
    return True


def judge(player, computer):
    if player == computer:
        return 'Its a draw!'
    elif player == 0 and computer == 1:
        return 'lost'
    elif player == 1 and computer == 2:
        return 'lost'
    elif player == 2 and computer == 0:
        return 'lost'
    else:
        return 'wins!'
