secret_num = 1
guess_count = 0
max_guess = 3
while guess_count < max_guess:
    a = int(input('Guess: '))
    guess_count += 1
    if a == secret_num:
        print('You won')
        break
else:
    print('You failed')