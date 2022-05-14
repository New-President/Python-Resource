list1 = [ 'seat', 'afe', 'hay', '+', '-', '.', '+', '*', ',' ]
print('Stay safe.')
a=0
b=0
d=0
while b<9:
    list2 = ['seat', 'afe', 'hay', '+', '-', '.', '+', '*', ',']
    list2.remove(list2[b])
    if list1[b] in list2:
        b=b+1
        d=d+1
    else:
        b=b+1
        a=a+1
unique=a+(d/2)
print('Number of unique items =',unique)