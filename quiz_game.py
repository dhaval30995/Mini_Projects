print('Welcome to My computer quiz!')

playing = input('Do you want to play quiz game? ')

if playing.lower() != 'yes':
    quit()

print("okay! let's play: )")

score = 0

answer = input('what does CPU stand for? ')
if answer.lower() == 'central processing unit': 
    print('correct!')
    score += 1
else:
    print('incorrect!')

answer = input('what does GPU stand for? ')
if answer.lower() == 'graphics processing unit': 
    print('correct!')
    score += 1
else:
    print('incorrect!')
    
answer = input('what does RAM stand for? ')
if answer.lower() == 'random access memory': 
    print('correct!')
    score += 1
else:
    print('incorrect!')

answer = input('what does PSU stand for? ')
if answer.lower() == 'power supply': 
    print('correct!')
    score += 1
else:
    print('incorrect!')

print(f'you got {score} questions correct! ') 
print(f'you got {(score/4) * 100}%.') 