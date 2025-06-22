import random

top_number = input('pleaser enter top number for guessing range? :- ')

if top_number.isdigit():
    top_number = int(top_number)

    if top_number < 0:
        print('please enter a number larger then 0 next time')
        quit()
else:
    print('please enter a number next time')
    quit()

random_number = random.randint(0,top_number)

guesses = 0

while True:

    guesses += 1

    guess_number = input('pleaser guess a number :- ')

    if guess_number.isdigit():
        guess_number = int(guess_number)
    else:
        print('please enter a number next time')
        continue

    if guess_number == random_number:
        print('you got it!')
        break
    elif guess_number > random_number:
        print('you were above the number')
    else:
        print('you were below the number')

print(f'you take a {guesses} times of guesses for correct guess')

