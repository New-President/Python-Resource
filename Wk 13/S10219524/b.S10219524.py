# Yong Zi Ren (S10219524) – P07
gen1 = [['Lukia', 'Kalon', 'rare'],
        ['Xernor', 'Unovus', 'normal'],
        ['Articun', 'Kalon', 'normal'],
        ['Zapdus', 'Kalon', 'rare']]

gen2 = [['Arkus', 'Unovus', 'normal'],
        ['Dialgus', 'Galarstar', 'rare'],
        ['Mewt', 'Kalon', 'rare']]

gen3 = [['Palkian', 'Galarstar', 'normal'],
        ['Raikus', 'Unovus', 'rare'],
        ['Kyogros', 'Kalon', 'rare'],
        ['Latius', 'Kalon', 'rare'],
        ['Colalon', 'Galarstar', 'normal']]

gen_list = [gen1, gen2, gen3]
gen_name = ['gen1', 'gen2', 'gen3']
planets = ['Galarstar', 'Unovus', 'Kalon']
total_list = [[0, 0], [0, 0], [0, 0]]

print('Total number of Pokenauts for each planet and rarity:')
for gen in gen_list:
    for element in gen:
        if 'Galarstar' in element:
            if 'normal' in element:
                total_list[0][1] += 1
            else:
                total_list[0][0] += 1
        elif 'Unovus' in element:
            if 'normal' in element:
                total_list[1][1] += 1
            else:
                total_list[1][0] += 1
        elif 'Kalon' in element:
            if 'normal' in element:
                total_list[2][1] += 1
            else:
                total_list[2][0] += 1
for i in range(len(planets)):
    print('{:<9} : rare - {}, normal - {}'.format(planets[i], total_list[i][0], total_list[i][1]))
