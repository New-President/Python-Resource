path = "C:\\Users\\ziren\\OneDrive - Ngee Ann Polytechnic\\Desktop\\School\\PR1\\Wk 13\\PRG1_data\\"
datafile = open(path + "colors.csv", "r")
colors_dict = {}
new_colors = {}
b = []
red = []
green = []
blue = []
for line in datafile:
    a = line.split('\n')
    if '' in a:
        a.remove('')
    for i in a:
        a = i.split(',')
    b.append(a)
for element in b:
    colors_dict[element[0]] = element[1]
for value in colors_dict:
    if colors_dict[value] == 'Red':
        red.append(value)
    elif colors_dict[value] == 'Green':
        green.append(value)
    else:
        blue.append(value)
new_colors['Red'] = red
new_colors['Blue'] = blue
new_colors['Green'] = green
print('colors_dict =', colors_dict)
print('new_colors =', new_colors)
