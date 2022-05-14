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

print('{:<10}{:<10}{:<10}{:<10}\n'.format('Gen', 'Name', 'Planet', 'Rarity'))
for gen in gen_list:
    for element in gen:
        print('{:<10}{:<10}{:<10}{:<10}'.format(gen_name[gen_list.index(gen)], element[0], element[1], element[2]))
    print()
