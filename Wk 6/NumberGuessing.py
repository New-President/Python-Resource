import random

print('Welcome to Number Guessing Game')
a = 1
b = random.randint(0, 100)
print(b)  # used for checking
c = int(input('Try 1: Enter a number between 1 and 100 (or -1 to end): '))
if c == b:
    print("Bingo, you've got it right!")
    print('Bye-bye!')
    exit()
elif c < b and c != -1:
    print(c, 'is too low.')
elif c > b:
    print(c, 'is too high')
elif c == -1:
    print('Bye-bye!')
    exit()
while a < 5:
    a = a + 1
    d = int(input('Try ' + str(a) + ': Guess again, enter a number between 1 and 100 (or -1 to end):'))
    if d < b and d != -1:
        print(d, 'is too low.')
    elif d > b:
        print(d, 'is too high')
    elif d == b:
        print("Bingo, you've got it right!")
        print('Bye-bye!')
        exit()
    elif d == -1:
        print('Bye-bye!')
        exit()
    else:
        continue
print('Game over. The correct answer is:', b)
print('Bye-bye!')
