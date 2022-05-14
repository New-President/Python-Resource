# Yong Zi Ren (S10219524)-P07
count = 0
while count < 3:
    UPC = (input('Enter UPC:'))
    a = [int(i) for i in UPC]
    b = 0
    c = 1
    total1 = 0
    total2 = 0
    while b < len(a) - 1:
        total1 = total1 + a[b]
        b = b + 2
    while c < len(a) - 1:
        total2 = total2 + a[c]
        c = c + 2
    total1 = total1 * 3
    total = (total1 + total2) % 10
    if total != 0:
        total = 10 - total
    if total == a[-1]:
        print('The UPC', UPC, 'is valid.')
    else:
        print('The UPC', UPC, 'is invalid.')
    count = count + 1
