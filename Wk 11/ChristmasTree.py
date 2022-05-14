a = str(input('Enter a character:'))
b = int(input('Enter a number:'))
d=b
e=0
for i in range(b):
    c=''
    c+=' '*(d)
    e=e+1
    d=d-1
    f=(a+' ')*e
    print(c,f,c)
print('Merry Christmas!')
