import time
print('Welcome to the first ever LGBTQ Test!')
Start = input('Are You Ready To Take The Test:')
if Start in ("yes", "Yes", "Y", "yeah", "yup", "Yup", "Yeah"):
    def No_Homo():
        First = input('What is your gender:')
        Second = input('Which gender do you like:')

        if First in ('Male','male','M','guy','Guy','boy','Boy') and Second in ('Male','male','M','guy','Guy','boy','Boy'):
            print('You are Gay!')
        elif First in ('Female','female','F','Girl','girl') and Second in ('Female','female','F','Girl','girl'):
            print('You are Lesbian!')
        elif Second in ('Both','guy and girl','male and female','both'):
            print('You are Bisexual!')
        else:
            print('You are Straight!')
    while True:
        No_Homo()
else:
    print('Thank You And Have A Nice Day!')
    time.sleep(2.5)
    exit()