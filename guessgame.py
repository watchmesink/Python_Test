import random

print('hello lets guess the number from 1 to 10 you have 5 guesses')
secretNumber = random.randint(1,10)
for i in range(1,10):
    print ('guess the number')
    guess = int(input())
    if guess < secretNumber:
        print('too low')
    elif guess > secretNumber:
        print('too high')
    else:
        print('well done, the number is ' + str(guess) + 'you used ' + str(i) + ' guesses')
        break