map = [['T', ' ', ' ', ' ', 'T'],
       [' ', 'P', ' ', ' ', ' '],
       [' ', ' ', ' ', 'T', ' '],
       [' ', 'T', ' ', ' ', ' ']
       ]
column = '+---' * len(map[0])
for row in map:
    print(column + '+')
    for element in row:
        print('| ' + element + ' ', end='')
    print('|', end='\n')
print(column + '+')

