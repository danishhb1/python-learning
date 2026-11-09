from random import shuffle

mylist = ['', 'O', '']


def shuffle_list(mylist):
    shuffle(mylist)
    return mylist


def player_guess():
    guess = ''

    while guess not in ['0', '1', '2']:
        guess = input('Pick a number (0, 1, 2): ')

    return int(guess)


def check_guess(mylist, guess):
    if mylist[guess] == 'O':
        print('Correct guess!')
    else:
        print('Wrong! Better luck next time!')
        print(mylist)


mixedup_list = shuffle_list(mylist)
player_choice = player_guess()
check_guess(mixedup_list, player_choice)
