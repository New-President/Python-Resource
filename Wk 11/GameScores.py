player = ['Hafu', 'Toast', 'Pokimane',
          'Pewdiepie', 'Ninja', 'Markiplier']
results = [[98, 107, 87, 121],
           [88, 111],
           [79, 130, 99],
           [86, 100, 121, 66, 98],
           [108, 79, 92],
           [77, 126, 93, 100, 73, 89],
           ]
a = 0
print('{:<20}{:<10}{:<10}{:<10}'.format('Player', 'P', 'Wins', 'Total'))
for row in results:
    c=0
    for element in row:
        if element >= 100:
            c = c + 1
    b = sum(results[a])
    print('{:<20}{:<10}{:<10}{:<10}'.format(player[a], len(results[a]), c, b))
    a=a+1
