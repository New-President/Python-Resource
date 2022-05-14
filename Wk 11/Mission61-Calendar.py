# Programming I

#######################
#    Mission 6.2      #
#      Calendar       #
#######################

# Background
# ==========
# Tom wants to print his own calendar. Write a Python program to
# print the month view of a calendar
# Prompt the user for the number of days in the month and which
# day of the week does the first day of the month falls on.


# Important Notes
# ===============
# 1) Comment out ALL input prompts before submitting.
# 2) You MUST use the following variables
#   -   days
#   -   day_of_week

# START CODING FROM HERE
# ======================
# Prompt user to enter number of days and first day of the week
days = int(input('Enter number of days:'))
day_of_week = input('The first day of the week:')


def print_calendar(days, day_of_week):
    a = 1
    b = []
    print('{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}{:>4}'.format('S', 'M', 'T', 'W', 'Th', 'F', 'Sat'))
    while a <= days:
        b.append(a)
        a = a + 1
    b.extend(['', '', '', '', '', ''])
    if day_of_week == 'M':
        b = [''] + b
    elif day_of_week == 'T':
        b = ['', ''] + b
    elif day_of_week == 'W':
        b = ['', '', ''] + b
    elif day_of_week == 'Th':
        b = ['', '', '', ''] + b
    elif day_of_week == 'F':
        b = ['', '', '', '', ''] + b
    elif day_of_week == 'Sat':
        b = ['', '', '', '', '', ''] + b
    list = [b[:7], b[7:14], b[14:21], b[21:28], b[28:]]
    for row in list:
        print('{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}'.format(row[0], row[1], row[2], row[3], row[4], row[5], row[6]))
    if day_of_week == 'Sat':
        print('{:>3}'.format(b[-7]))


# Do not remove the next line
print_calendar(days, day_of_week)
