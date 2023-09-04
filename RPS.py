import random


def play():
    user = input("What's your choice: 'r' for rock, 'p' for paper, 's' for scissors?\n")
    computer = random.choice(['r', 'p', 's'])

    if user == computer:
        return "It's a tie."

    elif is_win(user, computer):
        return 'You won!'

    else:
        return 'You lost.'


def is_win(player, opponent):

    win_conditions = {'r':'s', 's':'p', 'p':'r'}
    return opponent == win_conditions[player]


print(play())
