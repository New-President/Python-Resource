# Yong Zi Ren (S10219524)-P07
count = 0
while count < 3:  # looping for easier checking
    a = input('Enter 3 integer numbers separated by comma :')  # input the 3 integer as a string
    a = a.split(',')  # splitting the integer with respect to the comma
    b = [int(i) for i in a]  # changing list from string to integer
    c = max(b)  # get the highest number in the list
    if c == b[0] and c == b[1] and c == b[2]:  # check if the 3 numbers are the same
        print('All numbers are equal.')
    else:  # display largest number
        print(c, 'is the largest number.')
    count = count + 1
