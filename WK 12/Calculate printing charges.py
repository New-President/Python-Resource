a = 0
print('{:<10}{:<10}{:<10}'.format('Pages', 'Charges', 'Charge (include GST)'))


def calculateCharge(a):
    if a <= 100:
        b = a * 0.03
    elif a <= 300:
        b = 100 * 0.03 + (a - 100) * 0.02
    else:
        b = 100 * 0.03 + 200 * 0.02 + (a - 300) * 0.01
    return b


def calculateGST(c):
    c = calculateCharge(a) * 1.07
    return c


while a <= 500:
    print('{:<10}{:<10.2f}{:<10.2f}'.format(a, calculateCharge(a), calculateGST(calculateCharge(a))))
    a += 50
