def ok():
    a = str(input("Enter gender [M/F]:"))
    b = int(input('Enter age:'))
    c = str(input('Have you been in a traffic accident before? [Y/N]'))
    d=800
    if a=="M"and b<25:
        d=d*1.8
    elif a=="M" and 25<b<=34:
        d=d*1.5
    elif a=="M" and 35<=b<=44:
        d=d*1.2
    elif a=="M" and 45<=b<=54:
        d=d*1.0
    elif a=="M" and 55<=b<=64:
        d=d*1.4
    elif a=="M" and b>64:
        d=d*1.7
    elif a=="F" and b<25:
        d=d*1.4
    elif a=="F" and 25<b<=34:
        d=d*1.3
    elif a=="F" and 35<=b<=44:
        d=d*1.1
    elif a=="F" and 45<=b<=54:
        d=d*0.9
    elif a=="F" and 55<=b<=64:
        d=d*1.2
    else:
        d=d*1.4
    if c=="Y":
        d=d+300
        print('Your annual premium is:',d)
    else:
        print("Your annual premium is:",d)
while True:
    ok()
