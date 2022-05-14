def ok():
    a=int(input('How many children do you have?'))
    b=a*4**2
    print('User with',a,'will have at least:',a,'great grandchildren')
    print('and at most:',b,'great grandchildren')
counter=0
while counter<3:
    counter = counter + 1
    ok()