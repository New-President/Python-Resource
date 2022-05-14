a=str(input('Enter the vehicle number to be validated:'))
b=ord(a[1].lower())-96#get the coresponding letter value
c=ord(a[2].lower())-96
if b>9:#if second letter is 'H' and above
    d = a.replace(a[1], str(b)).replace(a[2], str(c)).replace(a[0], '').replace(a[-1], '')
    d = list(d)
    d[0:2]=[''.join(d[0:2])]
    e = [int(i) for i in d]  # change from str list to int list
    f = (e[0] * 9 + e[1] * 4 + e[2] * 5 + e[3] * 4 + e[4] * 3 + e[5] * 2) % 19  # formula
elif c>9:#if third letter is 'H' and above
    d = a.replace(a[1], str(b)).replace(a[2], str(c)).replace(a[0], '').replace(a[-1], '')
    d = list(d)
    d[1:3] = [''.join(d[1:3])]
    e = [int(i) for i in d]  # change from str list to int list
    f = (e[0] * 9 + e[1] * 4 + e[2] * 5 + e[3] * 4 + e[4] * 3 + e[5] * 2) % 19  # formula
elif c>9 and b>9:#if second and third letter is 'H' and above
    d = a.replace(a[1], str(b)).replace(a[2], str(c)).replace(a[0], '').replace(a[-1], '')
    d = list(d)
    d[0:2] = [''.join(d[0:2])]
    d[1:3] = [''.join(d[1:3])]
    e = [int(i) for i in d]  # change from str list to int list
    f = (e[0] * 9 + e[1] * 4 + e[2] * 5 + e[3] * 4 + e[4] * 3 + e[5] * 2) % 19  # formula
else:# all letter is below 'H'
    d = a.replace(a[1], str(b)).replace(a[2], str(c)).replace(a[0], '').replace(a[-1], '')
    d = list(d)
    e = [int(i) for i in d]  # change from str list to int list
    f = (e[0] * 9 + e[1] * 4 + e[2] * 5 + e[3] * 4 + e[4] * 3 + e[5] * 2) % 19  # formula
g = 'AZYXUTSRPMLKJHGEDCB'  # ref string
if a[-1] == g[f]:
    print('Validity of vehicle number: Valid')
else:
    print('Validity of vehicle number: Invalid')