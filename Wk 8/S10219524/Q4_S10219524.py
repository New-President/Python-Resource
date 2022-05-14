a=input('Enter an 8-bit binary number:')
a=[int(i) for i in a]
b=[2**7,2**6,2**5,2**4,2**3,2**2,2**1,2**0]
c=0
total=0
print('{:<10}{:<10}{:<10}'.format('Index','Digit','Decimal Value'))
while c<8:
    d=a[c]*b[c]
    total=a[c]*b[c]+total
    print('{:<10}{:<10}{:<10}'.format(c, a[c], d))
    c=c+1
print('\nDecimal number:',total)
