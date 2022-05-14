def ok():
    a = int(input('Enter a integer number:'))
    b = a%5 + a%6
    if b == 0:
        print(a,'is divisible by 5 and 6')
    else:
        print(a,'is not divisible by 5 and 6')
while True:
    ok()