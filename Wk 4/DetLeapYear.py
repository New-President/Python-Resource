def ok():
    a = int(input('Please enter the year:'))
    b = a%4
    c = a%400
    d = a%100
    if c == 0:
        print(a,'is a leap year')
    elif d == 0 and c != 0:
        print(a,'is not a leap year')
    elif b == 0:
        print(a,'is a leap year')
    else:
        print(a,'is not a leap year')
while True:
    ok()