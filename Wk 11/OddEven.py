Odd_Numbers = []
Even_Numbers = []
while True:
    d=int(input('Please enter a number (0 to end):'))
    if d == 0:
        break
    elif d%2 == 0:
        Even_Numbers.append(d)
    else:
        Odd_Numbers.append(d)
print('Odd Numbers:',str(sorted(Odd_Numbers)))
print('Even Numbers:',str(sorted(Even_Numbers)))
a= (sum(Odd_Numbers)+sum(Even_Numbers))/(len(Odd_Numbers)+len(Even_Numbers))
print('Average:',a)
