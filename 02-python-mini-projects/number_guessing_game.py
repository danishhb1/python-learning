from random import randint

random_num = randint(1, 100)
guesses = [0]

while True:
    guess = int(input('Please put a number between 1 and 100: '))

    if guess < 1 or guess > 100:
        print('OUT OF BOUNDS!')
        continue

    if guess == random_num:
        print(f'Congratulations! You guessed the number in {len(guesses)} attempts!')
        break

    guesses.append(guess)

    if guesses[-2]:

        if abs(guess - random_num) < abs(guesses[-2] - random_num):
            print('WARMER!')
        elif abs(guess - random_num) > abs(guesses[-2] - random_num):
            print('COLDER!')
        else:
            print('SAME DISTANCE!')

    else:
        if abs(guess - random_num) <= 10:
            print('WARM!')
        else:
            print('COLD!')
