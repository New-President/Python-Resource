def print_square(side, char):
    for i in range(side):
        for i in range(side):
            print(char,end=' ')
        print()


a=int(input('Enter the side:'))
b=str(input('Enter the character to be shown:'))
print_square(a, b)
