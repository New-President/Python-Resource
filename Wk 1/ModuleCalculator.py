import time
print('Welcome To The Module Marks Calculator!')
Start = input('Do You Want To Begin The Module Marks Calculator:')
if Start in ('Yes','yes','Y','yeah','Yeah'):
    def Module_Calculator():  # Looping the program
        CT = float(input('Please Enter Common Test Marks:'))  # enter your Common Test marks
        CA = float(input('Please Enter Continuous Assessment Marks:'))  # enter your CA1 marks
        AS = float(input('Please Enter Assignment Marks:'))  # enter your Assessment marked
        Module_Marks = (CT / 60) * 30 + (CA / 75) * 40 + (AS / 80) * 30  # formula to find the total module mark
        print('Your Module Marks is ' + str(Module_Marks))#display your module mark
        if 50 <= Module_Marks < 55: #Everything below is extra to let you know which grade you get
            print('You passed with a D Grade')
            print('Congrats!')
        elif 55 <= Module_Marks < 60:
            print('You passed with a D+ Grade')
            print('Congrats!')
        elif 60 <= Module_Marks < 65:
            print('You passed with a C Grade')
            print('Congrats!')
        elif 65 <= Module_Marks < 70:
            print('You passed with a C+ Grade')
            print('Congrats!')
        elif 70 <= Module_Marks < 75:
            print('You passed with a B Grade')
            print('Impressive!')
        elif 75 <= Module_Marks < 80:
            print('You passed with a B+ Grade')
            print('WOW!')
        elif 80 <= Module_Marks < 101:
            print('You passed with a A Grade')
            print('OMG!')
        elif Module_Marks > 100:
            print('ERROR 404')
            print('Hey! No Cheating!')
        else:
            print('You Failed!')
            print('Better luck next time!')
    while True:
        Module_Calculator()
else:
    print('Thank You And Have A Nice Day!')
    time.sleep(2.5)
    exit()
