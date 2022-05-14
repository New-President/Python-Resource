city_list = [ 'Bangkok', 'Jakarta', 'Seoul', 'Taipei', 'Tokyo' ]
price_list = [ 200.00, 150.00, 400.00, 350.00, 450.00 ]
a=int(input('Enter lowest price ($):'))
b=int(input('Enter highest price ($):'))
c=0
d=0
print('{:<10}{:<10}{:<10}'.format('No', 'City', 'Price'))
while c<5:
    if a<=price_list[c] and b>=price_list[c]:
        d = d + 1
        print('{:<10}{:<10}{:<10}'.format(d, city_list[c], price_list[c]))
        c=c+1
    else:
        c=c+1
if d>0:
    print('Number of cities found:', d)
else:
    print('No city found!')