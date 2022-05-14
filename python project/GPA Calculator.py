
while True:
    creds_grade = 0
    creds = 0
    mod = int(input('How many modules you took:'))
    loop = 0
    while loop < mod:
        loop += 1
        print('\nModule',loop)
        a = float(input('What is the credit unit:'))
        b = float(input('What is your grade score:'))
        c = a*b
        creds += a
        creds_grade += c
    print('Total = {:0.3f}'.format(creds_grade/creds))