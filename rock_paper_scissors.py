import random

self_win = 0
computer_win = 0


while True:

    self_choose = input('please choose from Rock/Paper/Scissors or Q for quit game :- ').lower()

    if self_choose == 'q':
        break
    
    lst = ['rock','paper','scissors']

    if self_choose not in lst:
        print('please select from list')
        continue
    
    random_choice = random.randint(0,2)
    computer_choose = lst[random_choice]

    if self_choose == 'rock' and computer_choose == 'scissors':
        print('you win')
        self_win += 1
    elif self_choose == 'scissors' and computer_choose == 'paper':
        print('you win')
        self_win += 1
    elif self_choose == 'paper' and computer_choose == 'rock':
        print('you win')
        self_win += 1
    elif self_choose == computer_choose:
        print('Tie - both selected same')
    else:
        print('you loose')
        print(f'computer choose {computer_choose}')
        computer_win += 1

print(f'You win total {self_win} times.. \nComputer win total {computer_win} times')

    