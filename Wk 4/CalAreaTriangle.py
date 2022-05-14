import math
math
def ok():
    a = float(input('Enter length of side A:'))
    b = float(input('Enter length of side B:'))
    c = float(input('Enter length of side C:'))
    s = (a+b+c)/2
    area = s*(s-a)*(s-b)*(s-c)
    if a+b>c and a+c>b and c+b>a:
        area = math.sqrt(area)
        print('Input lengths can form a triangle of Area',format(area,'.2f'),'square units.')
    else:
        print('Input lengths cannot form a triangle.')
while True:
    ok()