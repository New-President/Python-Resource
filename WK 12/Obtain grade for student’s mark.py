mark_list = [['Mary', 90.5], ['Charles', 60.4], ['John', 70.5], ['Javier', 32.0], ['Luke', 46.7]]
print('{:<20}{:<10}{:<10}'.format('Student Name', 'Mark', 'Grade'))


def obtain_grade(b):
    if b < 49.5:
        a = 'F'
    elif b <= 54.5:
        a = 'D'
    elif b <= 59.5:
        a = 'D+'
    elif b <= 64.5:
        a = 'C'
    elif b <= 69.5:
        a = 'C+'
    elif b <= 74.5:
        a = 'B'
    elif b <= 79.5:
        a = 'B+'
    elif b <= 84.5:
        a = 'A'
    else:
        a = 'A+'
    return a

for i in mark_list:
    i.append(obtain_grade(i[1]))

for l in mark_list:
    print('{:<20}{:<10}{:<10}'.format(l[0], l[1], l[2]))
