# Yong Zi Ren (S10219524J)

import random

try:  # check if save files is in the current directory
    file = open("savedMap.txt", "r")
    file2 = open("savedBuilding.txt", "r")
    file3 = open("savedTurn.txt", "r")
    file4 = open("savedScore.txt", "r")
    file.close()
    file2.close()
    file3.close()
    file4.close()
except:  # create the save files
    file = open("savedMap.txt", "w")
    file2 = open("savedBuilding.txt", "w")
    file3 = open("savedTurn.txt", "w")
    file4 = open("savedScore.txt", "w")
    file.close()
    file2.close()
    file3.close()
    file4.close()



def printmap():
    rownum = 0  # use to identify the row
    print(' ', '  A  ', '  B  ', '  C  ', '  D ', ' ' * 10, '{:<10}{:>1}'.format('Building', 'Remaining'))
    print('', '+-----' * (len(map[0])) + '+', ' '*8, '{:<10}{:>1}'.format('-'*8, '-'*9))
    for row in map:
        rownum += 1
        print(str(rownum), end='')
        for element in row:
            print('| ' + element + ' ', end='')  # print buildings of that row
        if rownum == 1:
            print('|', ' '*8, '{:<10}{:>1}'.format('BCH', building['BCH']))  # print 1st building
            print('', '+-----' * (len(map[0])) + '+', ' '*8, '{:<10}{:>1}'.format('FAC', building['FAC']))  # print 2nd building
        elif rownum == 2:
            print('|', ' '*8, '{:<10}{:>1}'.format('HSE', building['HSE']))  # print 3rd building
            print('', '+-----' * (len(map[0])) + '+', ' '*8, '{:<10}{:>1}'.format('SHP', building['SHP']))  # print 4th building
        elif rownum == 3:
            print('|', ' ' * 8, '{:<10}{:>1}'.format('HWY', building['HWY']))  # print 5th building
            print('', '+-----' * (len(map[0])) + '+')
        else:
            print('|')
            print('', '+-----' * (len(map[0])) + '+')


def printmenu():  # printing main menu
    print('Welcome, mayor of Simp City!')
    print('-' * 28)
    print('1. Start new game\n2. Load saved game\n3. Show high score\n\n0. Exit')


def game(turn, scorelist, highscores):
    while turn <= 16:
        name = ['HSE', 'FAC', 'SHP', 'HWY', 'BCH']
        if building['HSE'] == 0:  # removing any building that is 0
            name.remove('HSE')
        elif building['FAC'] == 0:
            name.remove('FAC')
        elif building['SHP'] == 0:
            name.remove('SHP')
        elif building['HWY'] == 0:
            name.remove('HWY')
        elif building['BCH'] == 0:
            name.remove('BCH')
        ran = random.randint(0, len(name) - 1)
        ran2 = random.randint(0, len(name) - 1)
        while ran == ran2:  # change the value of ran2 until it is not the same as ran
            ran2 = random.randint(0, len(name) - 1)
        print('\nTurn {}'.format(turn))
        printmap()
        print('1. Build a {}\n'
              '2. Build a {}\n'
              '3. See current score\n\n'
              '4. Save game\n'
              '0. Exit to main menu'.format(name[ran], name[ran2]))
        while True:  # input validation
            b = input('Your choice?')
            try:
                b = int(b)
            except:
                print('Please use numeric digits.\n')
                continue
            if b > 4:
                print('Please enter a number from 0-4.')
                continue
            break
        if b == 1:
            while True:  # it will loop until user enters the correct building placement/input validation
                c = input('Build where (E.g A1)?')
                d = [char for char in c]
                try:
                    str(d[0])
                    int(d[1])
                except:
                    print('Please enter a letter-number pair. (E.g a1)')
                    continue
                if d[0] not in ('A', 'a', 'B', 'b', 'C', 'c', 'D', 'd'):
                    print('Please choose a column from A to D.')
                    continue
                elif d[1] not in ('1', '2', '3', '4'):
                    print('Please choose a row from 1 to 4.')
                    continue
                elif turn != 1:  # check for illegal placement e.g not next to adjacent building or the location already has building
                    if d[0] in ('A', 'a'):
                        if int(d[1]) == 1:
                            if map[0][1] == '   ' and map[1][0] == '   ':
                                print('You must build next to an existing building.')
                                continue
                            elif map[0][0] != '   ':
                                print('There is already a building here.')
                                continue
                        elif int(d[1]) == 2:
                            if map[0][0] == '   ' and map[2][0] == '   ' and map[1][1] == '   ':
                                print('You must build next to an existing building.')
                                continue
                            elif map[1][0] != '   ':
                                print('There is already a building here.')
                                continue
                        elif int(d[1]) == 3:
                            if map[1][0] == '   ' and map[3][0] == '   ' and map[2][1] == '   ':
                                print('You must build next to an existing building.')
                                continue
                            elif map[2][0] != '   ':
                                print('There is already a building here.')
                                continue
                        elif int(d[1]) == 4:
                            if map[2][0] == '   ' and map[3][1] == '   ':
                                print('You must build next to an existing building.')
                                continue
                            elif map[3][0] != '   ':
                                print('There is already a building here.')
                                continue
                    elif d[0] in ('B', 'b'):
                        if int(d[1]) == 1:
                            if map[0][0] == '   ' and map[1][1] == '   ' and map[0][2] == '   ':
                                print('You must build next to an existing building.')
                                continue
                            elif map[0][1] != '   ':
                                print('There is already a building here.')
                                continue
                        elif int(d[1]) == 2:
                            if map[0][1] == '   ' and map[1][0] == '   ' and map[2][1] == '   ' and map[1][2] == '   ':
                                print('You must build next to an existing building.')
                                continue
                            elif map[1][1] != '   ':
                                print('There is already a building here.')
                                continue
                        elif int(d[1]) == 3:
                            if map[1][1] == '   ' and map[3][1] == '   ' and map[2][0] == '   ' and map[2][2] == '   ':
                                print('You must build next to an existing building.')
                                continue
                            elif map[2][1] != '   ':
                                print('There is already a building here.')
                                continue
                        elif int(d[1]) == 4:
                            if map[2][1] == '   ' and map[3][0] == '   ' and map[3][2] == '   ':
                                print('You must build next to an existing building.')
                                continue
                            elif map[3][1] != '   ':
                                print('There is already a building here.')
                                continue
                    elif d[0] in ('C', 'c'):
                        if int(d[1]) == 1:
                            if map[0][1] == '   ' and map[1][2] == '   ' and map[0][3] == '   ':
                                print('You must build next to an existing building.')
                                continue
                            elif map[0][2] != '   ':
                                print('There is already a building here.')
                                continue
                        elif int(d[1]) == 2:
                            if map[0][2] == '   ' and map[1][1] == '   ' and map[1][3] == '   ' and map[2][2] == '   ':
                                print('You must build next to an existing building.')
                                continue
                            elif map[1][2] != '   ':
                                print('There is already a building here.')
                                continue
                        elif int(d[1]) == 3:
                            if map[1][2] == '   ' and map[3][2] == '   ' and map[2][1] == '   ' and map[2][3] == '   ':
                                print('You must build next to an existing building.')
                                continue
                            elif map[2][2] != '   ':
                                print('There is already a building here.')
                                continue
                        elif int(d[1]) == 4:
                            if map[2][2] == '   ' and map[3][1] == '   ' and map[3][3] == '   ':
                                print('You must build next to an existing building.')
                                continue
                            elif map[3][2] != '   ':
                                print('There is already a building here.')
                                continue
                    elif d[0] in ('D', 'd'):
                        if int(d[1]) == 1:
                            if map[0][2] == '   ' and map[1][3] == '   ':
                                print('You must build next to an existing building.')
                                continue
                            elif map[0][3] != '   ':
                                print('There is already a building here.')
                                continue
                        elif int(d[1]) == 2:
                            if map[0][3] == '   ' and map[1][2] == '   ' and map[1][3] == '   ':
                                print('You must build next to an existing building.')
                                continue
                            elif map[1][3] != '   ':
                                print('There is already a building here.')
                                continue
                        elif int(d[1]) == 3:
                            if map[1][3] == '   ' and map[3][3] == '   ' and map[2][2] == '   ':
                                print('You must build next to an existing building.')
                                continue
                            elif map[2][3] != '   ':
                                print('There is already a building here.')
                                continue
                        elif int(d[1]) == 4:
                            if map[2][3] == '   ' and map[3][2] == '   ':
                                print('You must build next to an existing building.')
                                continue
                            elif map[3][3] != '   ':
                                print('There is already a building here.')
                                continue
                break
            if d[0] in ('a', 'A'):  # changing element of nested list to building
                map[int(d[1]) - 1][0] = name[ran]  # need to minus 1 because index start from 0
                building[name[ran]] -= 1
                turn += 1
            elif d[0] in ('b', 'B'):
                map[int(d[1]) - 1][1] = name[ran]
                building[name[ran]] -= 1
                turn += 1
            elif d[0] in ('c', 'C'):
                map[int(d[1]) - 1][2] = name[ran]
                building[name[ran]] -= 1
                turn += 1
            elif d[0] in ('d', 'D'):
                map[int(d[1]) - 1][3] = name[ran]
                building[name[ran]] -= 1
                turn += 1
        elif b == 2:
            while True:  # it will loop until user enters the correct building placement
                c = input('Build where (E.g A1)?')
                d = [char for char in c]
                try:
                    str(d[0])
                    int(d[1])
                except:
                    print('Please enter a letter-number pair. (E.g a1)')
                    continue
                if d[0] not in ('A', 'a', 'B', 'b', 'C', 'c', 'D', 'd'):
                    print('Please choose a column from A to D.')
                    continue
                elif d[1] not in ('1', '2', '3', '4'):
                    print('Please choose a row from 1 to 4.')
                    continue
                elif turn != 1:  # check for illegal placement e.g not next to adjacent building or the location already has building
                    if d[0] in ('A', 'a'):
                        if int(d[1]) == 1:
                            if map[0][1] == '   ' and map[1][0] == '   ':
                                print('You must build next to an existing building.')
                                continue
                            elif map[0][0] != '   ':
                                print('There is already a building here.')
                                continue
                        elif int(d[1]) == 2:
                            if map[0][0] == '   ' and map[2][0] == '   ' and map[1][1] == '   ':
                                print('You must build next to an existing building.')
                                continue
                            elif map[1][0] != '   ':
                                print('There is already a building here.')
                                continue
                        elif int(d[1]) == 3:
                            if map[1][0] == '   ' and map[3][0] == '   ' and map[2][1] == '   ':
                                print('You must build next to an existing building.')
                                continue
                            elif map[2][0] != '   ':
                                print('There is already a building here.')
                                continue
                        elif int(d[1]) == 4:
                            if map[2][0] == '   ' and map[3][1] == '   ':
                                print('You must build next to an existing building.')
                                continue
                            elif map[3][0] != '   ':
                                print('There is already a building here.')
                                continue
                    elif d[0] in ('B', 'b'):
                        if int(d[1]) == 1:
                            if map[0][0] == '   ' and map[1][1] == '   ' and map[0][2] == '   ':
                                print('You must build next to an existing building.')
                                continue
                            elif map[0][1] != '   ':
                                print('There is already a building here.')
                                continue
                        elif int(d[1]) == 2:
                            if map[0][1] == '   ' and map[2][1] == '   ' and map[1][0] == '   ' and map[1][2] == '   ':
                                print('You must build next to an existing building.')
                                continue
                            elif map[1][1] != '   ':
                                print('There is already a building here.')
                                continue
                        elif int(d[1]) == 3:
                            if map[1][1] == '   ' and map[3][1] == '   ' and map[2][0] == '   ' and map[2][2] == '   ':
                                print('You must build next to an existing building.')
                                continue
                            elif map[2][1] != '   ':
                                print('There is already a building here.')
                                continue
                        elif int(d[1]) == 4:
                            if map[2][1] == '   ' and map[3][0] == '   ' and map[3][2] == '   ':
                                print('You must build next to an existing building.')
                                continue
                            elif map[3][1] != '   ':
                                print('There is already a building here.')
                                continue
                    elif d[0] in ('C', 'c'):
                        if int(d[1]) == 1:
                            if map[0][1] == '   ' and map[1][2] == '   ' and map[0][3] == '   ':
                                print('You must build next to an existing building.')
                                continue
                            elif map[0][2] != '   ':
                                print('There is already a building here.')
                                continue
                        elif int(d[1]) == 2:
                            if map[0][2] == '   ' and map[1][1] == '   ' and map[1][3] == '   ' and map[2][2] == '   ':
                                print('You must build next to an existing building.')
                                continue
                            elif map[1][2] != '   ':
                                print('There is already a building here.')
                                continue
                        elif int(d[1]) == 3:
                            if map[1][2] == '   ' and map[3][2] == '   ' and map[2][1] == '   ' and map[2][3] == '   ':
                                print('You must build next to an existing building.')
                                continue
                            elif map[2][2] != '   ':
                                print('There is already a building here.')
                                continue
                        elif int(d[1]) == 4:
                            if map[2][2] == '   ' and map[3][1] == '   ' and map[3][3] == '   ':
                                print('You must build next to an existing building.')
                                continue
                            elif map[3][2] != '   ':
                                print('There is already a building here.')
                                continue
                    elif d[0] in ('D', 'd'):
                        if int(d[1]) == 1:
                            if map[0][2] == '   ' and map[1][3] == '   ':
                                print('You must build next to an existing building.')
                                continue
                            elif map[0][3] != '   ':
                                print('There is already a building here.')
                                continue
                        elif int(d[1]) == 2:
                            if map[0][3] == '   ' and map[1][2] == '   ' and map[1][3] == '   ':
                                print('You must build next to an existing building.')
                                continue
                            elif map[1][3] != '   ':
                                print('There is already a building here.')
                                continue
                        elif int(d[1]) == 3:
                            if map[1][3] == '   ' and map[3][3] == '   ' and map[2][2] == '   ':
                                print('You must build next to an existing building.')
                                continue
                            elif map[2][3] != '   ':
                                print('There is already a building here.')
                                continue
                        elif int(d[1]) == 4:
                            if map[2][3] == '   ' and map[3][2] == '   ':
                                print('You must build next to an existing building.')
                                continue
                            elif map[3][3] != '   ':
                                print('There is already a building here.')
                                continue
                break
            if d[0] in ('a', 'A'):  # changing element of nested list to building
                map[int(d[1]) - 1][0] = name[ran2]  # need to minus 1 because index start from 0
                building[name[ran2]] -= 1
                turn += 1
            elif d[0] in ('b', 'B'):
                map[int(d[1]) - 1][1] = name[ran2]
                building[name[ran2]] -= 1
                turn += 1
            elif d[0] in ('c', 'C'):
                map[int(d[1]) - 1][2] = name[ran2]
                building[name[ran2]] -= 1
                turn += 1
            elif d[0] in ('d', 'D'):
                map[int(d[1]) - 1][3] = name[ran2]
                building[name[ran2]] -= 1
                turn += 1
        elif b == 3:
            calculator()
            input('Enter any key to continue...')
        elif b == 4:
            file = open( "savedMap.txt", "w")
            file2 = open("savedBuilding.txt", "w")
            file3 = open( "savedTurn.txt", "w")
            for i in map:
                for element in i:
                    file.write('{},'.format(element))
                file.write('\n')
            for i in building:
                file2.write('{},{}\n'.format(i, building[i]))
            file3.write(str(turn))
            file.close()
            file2.close()
            file3.close()
            print('Game Saved!')
            break
        elif b == 0:
            break
    if turn == 17:
        print('\nFinal layout of Simp City:')
        leftnum = 0
        print(' ', '  A  ', '  B  ', '  C  ', '  D  ')
        templist = []
        for row in map:
            leftnum += 1
            for i in building:
                templist.append([i, building[i]])
            print('', '+-----' * (len(map[0])) + '+')
            print(str(leftnum), end='')
            for element in row:
                print('| ' + element + ' ', end='')
            print('|', end='\n')
        print('', '+-----' * (len(map[0])) + '+')
        total = calculator()
        scorelist.append(total)
        scorelist = sorted(scorelist, reverse=True)  # sort scores from highest to lowest
        if scorelist.index(total) + scorelist.count(total)<=10:  # display if payer made it to the leader board
            print('Congratulations! You made the high score board at position {}!'.format(scorelist.index(total)+scorelist.count(total)))
            score_name=str(input('Please enter your name (max 20 chars):'))
            temp = [score_name, total]
            highscores.append(temp)
        else:  # display if user never make it into the leaderboard
            print('You did not made it in the high score board.\nBetter luck next time!')
        highscore()


def savegame():  # load a saved game
    global turn
    file = open("savedMap.txt", "r")
    file2 = open("savedBuilding.txt", "r")
    file3 = open("savedTurn.txt", "r")
    for line in file:
        line = line.strip('\n')
        a = line.split(',')
        a.remove(a[-1])
        map.append(a)
    for line in file2:
        line = line.strip('\n')
        a = line.split(',')
        building[a[0]] = int(a[1])
    for line in file3:
        turn = int(line)
    file.close()
    file2.close()
    file3.close()
    return turn


def calculator():
    hse = []
    fac = []
    fac_num = 0
    bch = []
    shp = []
    hwy = []
    build = [hse, fac, shp, hwy, bch]
    name = ['HSE', 'FAC', 'SHP', 'HWY', 'BCH']
    build_num = 0  # use to identify position of building in build list
    pos_row = 0  # position of list in map
    for row in map:
        hwynum = 0  # use to prove whether the row has been checked for HWY building
        pos = 0  # position of element in list
        for col in row:
            shp_building_list = ['   ']  # the blank space cannot be part of the building, store buildings that is next to SHP
            shp_num = 0
            if col == 'BCH':
                if row.index(col, pos) == 0 or row.index(col, pos) == 3:  # if BCH in A in D
                    bch.append(3)
                else:  # BCH in B and C
                    bch.append(1)
            elif col == 'FAC':
                fac_num += 1
            elif col == 'HSE':
                if 0 < row.index(col, pos) < 3:  # HSE in B or C
                    if row[row.index(col, pos) - 1] == 'FAC' or row[row.index(col, pos) + 1] == 'FAC':  # left or right have FAC
                        hse.append(1)
                    elif 0 < map.index(row, pos_row) < 3:  # HSE in 2 or 3
                        if map[map.index(row, pos_row) - 1][row.index(col, pos)] == 'FAC' or map[map.index(row, pos_row) + 1][row.index(col, pos)] == 'FAC':  # up or down have FAC
                            hse.append(1)
                        elif map[map.index(row, pos_row) - 1][row.index(col, pos)] in ('SHP', 'HSE') and map[map.index(row, pos_row) + 1][row.index(col, pos)] in ('SHP', 'HSE'):  # up and down have HSE or SHP
                            if row[row.index(col, pos) - 1] in ('SHP', 'HSE') and row[row.index(col, pos) + 1] in ('SHP', 'HSE'):  # left and right have HSE or SHP
                                hse.append(4)
                            elif row[row.index(col, pos) - 1] in ('SHP', 'HSE') or row[row.index(col, pos) + 1] in ('SHP', 'HSE'):  # left or right have HSE or SHP
                                if row[row.index(col, pos) - 1] == 'BCH' or row[row.index(col, pos) + 1] == 'BCH':  # left or right have BCH
                                    hse.append(5)
                                else:  # only up, down and left or right have HSE or SHP
                                    hse.append(3)
                            elif row[row.index(col, pos) - 1] == 'BCH' and row[row.index(col, pos) + 1] == 'BCH':  # left and right have BCH
                                hse.append(6)
                            elif row[row.index(col, pos) - 1] == 'BCH' or row[row.index(col, pos) + 1] == 'BCH':  # left or right have BCH
                                if row[row.index(col, pos) - 1] in ('SHP', 'HSE') or row[row.index(col, pos) + 1] in ('SHP', 'HSE'):  # left or right have HSE or SHP
                                    hse.append(5)
                                else:  # only up and down have HSE or SHP and a BCH at either left or right
                                    hse.append(4)
                            else:  # only up and down have HSE or SHP
                                hse.append(2)
                        elif map[map.index(row, pos_row) - 1][row.index(col, pos)] in ('SHP', 'HSE') or map[map.index(row, pos_row) + 1][row.index(col, pos)] in ('SHP', 'HSE'):  # up or down have HSE or SHP
                            if map[map.index(row, pos_row) - 1][row.index(col, pos)] == 'BCH' or map[map.index(row, pos_row) + 1][row.index(col, pos)] == 'BCH':
                                if row[row.index(col, pos) - 1] in ('SHP', 'HSE') and row[row.index(col, pos) + 1] in ('SHP', 'HSE'):  # left and right have HSE or SHP
                                    hse.append(5)
                                elif row[row.index(col, pos) - 1] in ('SHP', 'HSE') or row[row.index(col, pos) + 1] in ('SHP', 'HSE'):  # left or right have HSE or SHP
                                    if row[row.index(col, pos) - 1] == 'BCH' or row[row.index(col, pos) + 1] == 'BCH':  # left or right have BCH
                                        hse.append(6)
                                    else:  # only up or down have 1 HSE or SHP and left or right have HSE or SHP and up or down have 1 BCH
                                        hse.append(4)
                                elif row[row.index(col, pos) - 1] == 'BCH' and row[row.index(col, pos) + 1] == 'BCH':  # left and right have BCH
                                    hse.append(7)
                                elif row[row.index(col, pos) - 1] == 'BCH' or row[row.index(col, pos) + 1] == 'BCH':  # left or right have BCH
                                    if row[row.index(col, pos) - 1] in ('SHP', 'HSE') or row[row.index(col, pos) + 1] in ('SHP', 'HSE'):  # left or right have HSE or SHP
                                        hse.append(6)
                                    else:  # only up or down have 1 HSE or SHP and left or right have 1 BCH and up or down have 1 BCH
                                        hse.append(5)
                                else:  # only up and down have 1 HSE or SHP and up and down have 1 BCH
                                    hse.append(3)
                            else:
                                if row[row.index(col, pos) - 1] in ('SHP', 'HSE') and row[row.index(col, pos) + 1] in ('SHP', 'HSE'):  # left and right have HSE or SHP
                                    hse.append(3)
                                elif row[row.index(col, pos) - 1] in ('SHP', 'HSE') or row[row.index(col, pos) + 1] in ('SHP', 'HSE'):  # left or right have HSE or SHP
                                    if row[row.index(col, pos) - 1] == 'BCH' or row[row.index(col, pos) + 1] == 'BCH':  # left or right have BCH
                                        hse.append(4)
                                    else:  # only up or down have HSE or SHP and left or right have HSE or SHP
                                        hse.append(2)
                                elif row[row.index(col, pos) - 1] == 'BCH' and row[row.index(col, pos) + 1] == 'BCH':  # left and right have BCH
                                    hse.append(5)
                                elif row[row.index(col, pos) - 1] == 'BCH' or row[row.index(col, pos) + 1] == 'BCH':  # left or right have BCH
                                    if row[row.index(col, pos) - 1] in ('SHP', 'HSE') or row[row.index(col, pos) + 1] in ('SHP', 'HSE'):  # left or right have HSE or SHP
                                        hse.append(4)
                                    else:  # only up or down have HSE or SHP and left or right have BCH
                                        hse.append(3)
                                else:  # only 1 HSE or SHP is next it
                                    hse.append(1)
                        elif map[map.index(row, pos_row) - 1][row.index(col, pos)] == 'BCH' and map[map.index(row, pos_row) + 1][row.index(col, pos)] == 'BCH':  # up and down is have BCH
                            if row[row.index(col, pos) - 1] in ('SHP', 'HSE') and row[row.index(col, pos) + 1] in ('SHP', 'HSE'):  # left and right have HSE or SHP
                                hse.append(6)
                            elif row[row.index(col, pos) - 1] in ('SHP', 'HSE') or row[row.index(col, pos) + 1] in ('SHP', 'HSE'):  # left or right have HSE or HSE
                                if row[row.index(col, pos) - 1] == 'BCH' or row[row.index(col, pos) + 1] == 'BCH':  # left or right have BCH
                                    hse.append(7)
                                else:  # only up and down have BCH and left or right have SHP or HSE
                                    hse.append(5)
                            elif row[row.index(col, pos) - 1] == 'BCH' and row[row.index(col, pos) + 1] == 'BCH':  # left and right have BCH
                                hse.append(8)
                            elif row[row.index(col, pos) - 1] == 'BCH' or row[row.index(col, pos) + 1] == 'BCH':  # left or right have BCH
                                if row[row.index(col, pos) - 1] in ('SHP', 'HSE') or row[row.index(col, pos) + 1] in ('SHP', 'HSE'):  # left or right have SHP or HSE
                                    hse.append(7)
                                else:  # only up and down have BCH and left or right have BCH
                                    hse.append(6)
                            else:  # only up and down have BCH
                                hse.append(4)
                        elif map[map.index(row, pos_row) - 1][row.index(col, pos)] == 'BCH' or map[map.index(row, pos_row) + 1][row.index(col, pos)] == 'BCH':  # up or down have BCH
                            if row[row.index(col, pos) - 1] in ('SHP', 'HSE') and row[row.index(col, pos) + 1] in ('SHP', 'HSE'):  # left and right have HSE or SHP
                                hse.append(4)
                            elif row[row.index(col, pos) - 1] in ('SHP', 'HSE') or row[row.index(col, pos) + 1] in ('SHP', 'HSE'):  # left or right have HSE or SHP
                                if row[row.index(col, pos) - 1] == 'BCH' or row[row.index(col, pos) + 1] == 'BCH':  # left or right have BCH
                                    hse.append(5)
                                else:  # only up or down 1 have BCH and left or right have 1 HSE or SHP
                                    hse.append(3)
                            elif row[row.index(col, pos) - 1] == 'BCH' and row[row.index(col, pos) + 1] == 'BCH':  # left and right have BCH
                                hse.append(6)
                            elif row[row.index(col, pos) - 1] == 'BCH' or row[row.index(col, pos) + 1] == 'BCH':  # left or right have BCH
                                if row[row.index(col, pos) - 1] in ('SHP', 'HSE') or row[row.index(col, pos) + 1] in ('SHP', 'HSE'):  # left or right have HSE or SHP
                                    hse.append(5)
                                else:  # only up or down have 1 BCH and left or right have 1 BCH
                                    hse.append(4)
                            else:  # only up or down have 1 BCH
                                hse.append(2)
                        else:
                            if row[row.index(col, pos) - 1] in ('SHP', 'HSE') and row[row.index(col, pos) + 1] in ('SHP', 'HSE'):  # only left and right have HSE or SHP
                                hse.append(2)
                            elif row[row.index(col, pos) - 1] in ('SHP', 'HSE') or row[row.index(col, pos) + 1] in ('SHP', 'HSE'):  # left or right have HSE or SHP
                                if row[row.index(col, pos) - 1] == 'BCH' or row[row.index(col, pos) + 1] == 'BCH':  # left or right have BCH
                                    hse.append(3)
                                else:  # only left or right have 1 HSE or SHP
                                    hse.append(1)
                            elif row[row.index(col, pos) - 1] == 'BCH' and row[row.index(col, pos) + 1] == 'BCH':  # left and right have BCH
                                hse.append(4)
                            elif row[row.index(col, pos) - 1] == 'BCH' or row[row.index(col, pos) + 1] == 'BCH':  # left or right have BCH
                                if row[row.index(col, pos) - 1] in ('SHP', 'HSE') or row[row.index(col, pos) + 1] in ('SHP', 'HSE'):  # left or right have HSE or SHP
                                    hse.append(3)
                                else:  # only left or right have 1 BCH
                                    hse.append(2)
                            else:  # individual HSE with no score increase
                                hse.append(1)
                    elif map.index(row, pos_row) == 0:  # HSE in 1
                        if map[map.index(row, pos_row) + 1][row.index(col, pos)] == 'FAC':  # down have a FAC
                            hse.append(1)
                        elif row[row.index(col, pos) - 1] in ('SHP', 'HSE') and row[row.index(col, pos) + 1] in ('SHP', 'HSE'):  # left and right have HSE or SHP
                            if map[map.index(row, pos_row) + 1][row.index(col, pos)] in ('SHP', 'HSE'):  # down have HSE or SHP
                                hse.append(3)
                            elif map[map.index(row, pos_row) + 1][row.index(col, pos)] == 'BCH':  # down have have BCH
                                hse.append(4)
                            else:  # only left and right have HSE or BCH
                                hse.append(2)
                        elif row[row.index(col, pos) - 1] in ('SHP', 'HSE') or row[row.index(col, pos) + 1] in ('SHP', 'HSE'):  # left or right have HSE or SHP
                            if row[row.index(col, pos) - 1] == 'BCH' or row[row.index(col, pos) + 1] == 'BCH':  # left or right have BCH
                                if map[map.index(row, pos_row) + 1][row.index(col, pos)] in ('SHP', 'HSE'):  # down have HSE or SHP
                                    hse.append(4)
                                elif map[map.index(row, pos_row) + 1][row.index(col, pos)] == 'BCH':  # down have BCH
                                    hse.append(5)
                                else:  # only left or right have 1 BCH and left or right have 1 HSE or SHP
                                    hse.append(3)
                            else:
                                if map[map.index(row, pos_row) + 1][row.index(col, pos)] in ('SHP', 'HSE'):  # down have SHP or HSE
                                    hse.append(2)
                                elif map[map.index(row, pos_row) + 1][row.index(col, pos)] == 'BCH':  # down have BCH
                                    hse.append(3)
                                else:  # only left or right have 1 HSE or SHP
                                    hse.append(1)
                        elif row[row.index(col, pos) - 1] == 'BCH' and row[row.index(col, pos) + 1] == 'BCH':  # left and right have BCH
                            if map[map.index(row, pos_row) + 1][row.index(col, pos)] in ('SHP', 'HSE'):  # down have HSE or SHP
                                hse.append(5)
                            elif map[map.index(row, pos_row) + 1][row.index(col, pos)] == 'BCH':  # down have BCH
                                hse.append(6)
                            else:  # only left and right have BCH
                                hse.append(4)
                        elif row[row.index(col, pos) - 1] == 'BCH' or row[row.index(col, pos) + 1] == 'BCH':   # left or right have BCH
                            if map[map.index(row, pos_row) + 1][row.index(col, pos)] in ('SHP', 'HSE'):  # down have HSE or SHP
                                hse.append(3)
                            elif map[map.index(row, pos_row) + 1][row.index(col, pos)] == 'BCH':  # down have BCH
                                hse.append(4)
                            else:  # only left or right have 1 BCH
                                hse.append(2)
                        else:
                            if row[row.index(col, pos) - 1] in ('SHP', 'HSE') and row[row.index(col, pos) + 1] in ('SHP', 'HSE'):  # left and right have HSE or SHP
                                hse.append(2)
                            elif row[row.index(col, pos) - 1] in ('SHP', 'HSE') or row[row.index(col, pos) + 1] in ('SHP', 'HSE'):  # left or right have HSE or SHP
                                if row[row.index(col, pos) - 1] == 'BCH' or row[row.index(col, pos) + 1] == 'BCH':  # left or right have BCH
                                    hse.append(3)
                                else:  # only left or right have 1 SHP or HSE
                                    hse.append(1)
                            elif row[row.index(col, pos) - 1] == 'BCH' and row[row.index(col, pos) + 1] == 'BCH':  # left and right have BCH
                                hse.append(4)
                            elif row[row.index(col, pos) - 1] == 'BCH' or row[row.index(col, pos) + 1] == 'BCH':  # left or right have BCH
                                if row[row.index(col, pos) - 1] in ('SHP', 'HSE') or row[row.index(col, pos) + 1] in ('SHP', 'HSE'):  # left or right have HSE or SHP
                                    hse.append(3)
                                else:  # only left or right have 1 BCH
                                    hse.append(2)
                            elif map[map.index(row, pos_row) + 1][row.index(col, pos)] == 'BCH':  # only down have BCH
                                hse.append(2)
                            else:   # individual HSE and with 1 SHP or HSE next to it
                                hse.append(1)
                    elif map.index(row, pos_row) == 3:
                        if map[map.index(row, pos_row) - 1][row.index(col, pos)] == 'FAC':  # up have FAC
                            hse.append(1)
                        elif row[row.index(col, pos) - 1] in ('SHP', 'HSE') and row[row.index(col, pos) + 1] in ('SHP', 'HSE'):  # left and right have HSE or SHP
                            if map[map.index(row, pos_row) - 1][row.index(col, pos)] in ('SHP', 'HSE'):  # up have HSE or SHP
                                hse.append(3)
                            elif map[map.index(row, pos_row) - 1][row.index(col, pos)] == 'BCH':  # up have BCH
                                hse.append(4)
                            else:  # only left and right have HSE or SHP
                                hse.append(2)
                        elif row[row.index(col, pos) - 1] in ('SHP', 'HSE') or row[row.index(col, pos) + 1] in ('SHP', 'HSE'):  # left or right have 1 HSE or SHP
                            if row[row.index(col, pos) - 1] == 'BCH' or row[row.index(col, pos) + 1] == 'BCH':   # left or right have 1 BCH
                                if map[map.index(row, pos_row) - 1][row.index(col, pos)] in ('SHP', 'HSE'):  # up have 1 HSE or SHP
                                    hse.append(4)
                                elif map[map.index(row, pos_row) - 1][row.index(col, pos)] == 'BCH':  # up have 1 BCH
                                    hse.append(5)
                                else:  # only left or right have 1 HSE or SHP and 1 BCH
                                    hse.append(3)
                            else:
                                if map[map.index(row, pos_row) - 1][row.index(col, pos)] in ('SHP', 'HSE'):  # up have HSE or SHP
                                    hse.append(2)
                                elif map[map.index(row, pos_row) - 1][row.index(col, pos)] == 'BCH':  # up have BCH
                                    hse.append(3)
                                else:  # only left or right have 1 HSE or BCH
                                    hse.append(1)
                        elif row[row.index(col, pos) - 1] == 'BCH' and row[row.index(col, pos) + 1] == 'BCH':  # left and right have BCH
                            if map[map.index(row, pos_row) - 1][row.index(col, pos)] in ('SHP', 'HSE'):  # up have HSE or SHP
                                hse.append(5)
                            elif map[map.index(row, pos_row) - 1][row.index(col, pos)] == 'BCH':  # up have BCH
                                hse.append(6)
                            else:  # only left and right have BCH
                                hse.append(4)
                        elif row[row.index(col, pos) - 1] == 'BCH' or row[row.index(col, pos) + 1] == 'BCH':  # left or right have 1 BCH
                            if map[map.index(row, pos_row) - 1][row.index(col, pos)] in ('SHP', 'HSE'):
                                hse.append(3)
                            elif map[map.index(row, pos_row) - 1][row.index(col, pos)] == 'BCH':
                                hse.append(4)
                            else:
                                hse.append(2)
                        else:
                            if row[row.index(col, pos) - 1] in ('SHP', 'HSE') and row[row.index(col, pos) + 1] in ('SHP', 'HSE'):
                                hse.append(2)
                            elif row[row.index(col, pos) - 1] in ('SHP', 'HSE') or row[row.index(col, pos) + 1] in ('SHP', 'HSE'):
                                if row[row.index(col, pos) - 1] == 'BCH' or row[row.index(col, pos) + 1] == 'BCH':
                                    hse.append(3)
                                else:
                                    hse.append(1)
                            elif row[row.index(col, pos) - 1] == 'BCH' and row[row.index(col, pos) + 1] == 'BCH':
                                hse.append(4)
                            elif row[row.index(col, pos) - 1] == 'BCH' or row[row.index(col, pos) + 1] == 'BCH':
                                if row[row.index(col, pos) - 1] in ('SHP', 'HSE') or row[row.index(col, pos) + 1] in ('SHP', 'HSE'):
                                    hse.append(3)
                                else:
                                    hse.append(2)
                            elif map[map.index(row, pos_row) - 1][row.index(col, pos)] == 'BCH':
                                hse.append(2)
                            else:
                                hse.append(1)
                elif row.index(col, pos) == 0:  # HSE at A
                    if row[row.index(col, pos) + 1] == 'FAC':  # down have FAC
                        hse.append(1)
                    elif 0 < map.index(row, pos_row) < 3:  # HSE at 2 or 3
                        if map[map.index(row, pos_row) - 1][row.index(col, pos)] == 'FAC' or map[map.index(row, pos_row) + 1][row.index(col, pos)] == 'FAC':  # up or down have FAC
                            hse.append(1)
                        elif map[map.index(row, pos_row) - 1][row.index(col, pos)] in ('SHP', 'HSE') and map[map.index(row, pos_row) + 1][row.index(col, pos)] in ('SHP', 'HSE'):  # up and down have HSE or SHP
                            if row[row.index(col, pos) + 1] in ('SHP', 'HSE'):  # right have HSE or SHP
                                hse.append(3)
                            elif row[row.index(col, pos) + 1] == 'BCH':  # right have BCH
                                hse.append(4)
                            else:  # only up and down have HSE or SHP
                                hse.append(2)
                        elif map[map.index(row, pos_row) - 1][row.index(col, pos)] in ('SHP', 'HSE') or map[map.index(row, pos_row) + 1][row.index(col, pos)] in ('SHP', 'HSE'):  # up or down have HSE or SHP
                            if map[map.index(row, pos_row) - 1][row.index(col, pos)] == 'BCH' or map[map.index(row, pos_row) + 1][row.index(col, pos)] == 'BCH':  # up or down have BCH
                                if row[row.index(col, pos) + 1] in ('SHP', 'HSE'):  # right have SHP or HSE
                                    hse.append(4)
                                elif row[row.index(col, pos) + 1] == 'BCH':  # right have BCH
                                    hse.append(5)
                                else:  # only up or down have 1 HSE or SHP and up or down have 1 BCH
                                    hse.append(3)
                            elif row[row.index(col, pos) + 1] in ('SHP', 'HSE'):  # only up or down have 1 HSE or SHP and right have HSE or SHP
                                hse.append(2)
                            elif row[row.index(col, pos) + 1] == 'BCH':  # only up or down have 1 HSE or SHP and right have BCH
                                hse.append(3)
                            else:  # only up or down have 1 HSE or SHP
                                hse.append(1)
                        elif map[map.index(row, pos_row) - 1][row.index(col, pos)] == 'BCH' and map[map.index(row, pos_row) + 1][row.index(col, pos)] == 'BCH':  # up and down have BCH
                            if row[row.index(col, pos) + 1] in ('SHP', 'HSE'):  # right have HSE or SHP
                                hse.append(5)
                            elif row[row.index(col, pos) + 1] == 'BCH':  # Right have BCH
                                hse.append(6)
                            else:  # only up and down have BCH
                                hse.append(4)
                        elif map[map.index(row, pos_row) - 1][row.index(col, pos)] == 'BCH' or map[map.index(row, pos_row) + 1][row.index(col, pos)] == 'BCH':  # up or down have BCH
                            if row[row.index(col, pos) + 1] in ('SHP', 'HSE'):  # right have HSE or SHP
                                hse.append(3)
                            elif row[row.index(col, pos) + 1] == 'BCH':  # right have BCH
                                hse.append(4)
                            else:  # only up or down have 1 BCH
                                hse.append(2)
                        else:
                            if row[row.index(col, pos) + 1] == 'BCH':  # only right have BCH
                                hse.append(2)
                            else:  # only individual HSE without additional score or 1 HSE or SHP at its right
                                hse.append(1)
                    elif map.index(row, pos_row) == 0:  # HSE at 1
                        if map[map.index(row, pos_row) + 1][row.index(col, pos)] == 'FAC' or row[row.index(col, pos) + 1] == 'FAC':  # right or down have FAC
                            hse.append(1)
                        elif map[map.index(row, pos_row) + 1][row.index(col, pos)] in ('SHP', 'HSE'):  # down have HSE or SHP
                            if row[row.index(col, pos) + 1] in ('SHP', 'HSE'):  # right have HSE or SHP
                                hse.append(2)
                            elif row[row.index(col, pos) + 1] == 'BCH':  # right have BCH
                                hse.append(3)
                            else:  # only down have HSe or SHP
                                hse.append(1)
                        elif map[map.index(row, pos_row) + 1][row.index(col, pos)] == 'BCH':  # down have BCH
                            if row[row.index(col, pos) + 1] in ('SHP', 'HSE'):  # right have HSE or SHP
                                hse.append(3)
                            elif row[row.index(col, pos) + 1] == 'BCH':  # right have BCH
                                hse.append(4)
                            else:  # only down have BCH
                                hse.append(2)
                        else:
                            if row[row.index(col, pos) + 1] == 'BCH':  # only right have BCH
                                hse.append(2)
                            else:  # only individual HSE or HSE or SHP at the right
                                hse.append(1)
                    elif map.index(row, pos_row) == 3:  # HSE at 4
                        if map[map.index(row, pos_row) - 1][row.index(col, pos)] == 'FAC' or row[row.index(col, pos) + 1] == 'FAC':  # left or down have FAC
                            hse.append(1)
                        elif map[map.index(row, pos_row) - 1][row.index(col, pos)] in ('SHP', 'HSE'):  # up have HSE or SHP
                            if row[row.index(col, pos) + 1] in ('SHP', 'HSE'):  # right have SHP or HSE
                                hse.append(2)
                            elif row[row.index(col, pos) + 1] == 'BCH':  # right have have BCH
                                hse.append(3)
                            else:  # only up have HSE or SHP
                                hse.append(1)
                        elif map[map.index(row, pos_row) - 1][row.index(col, pos)] == 'BCH':  # up have BCH
                            if row[row.index(col, pos) + 1] in ('SHP', 'HSE'):  # right have HSE or SHP
                                hse.append(3)
                            elif row[row.index(col, pos) + 1] == 'BCH':  # right have BCH
                                hse.append(4)
                            else:  # only up have BCH
                                hse.append(2)
                        else:  # up don't have any special building
                            if row[row.index(col, pos) + 1] == 'BCH':  # only right have BCH
                                hse.append(2)
                            else:  # only individual HSE or right have HSE or SHP
                                hse.append(1)
                elif row.index(col, pos) == 3:  # HSE in D
                    if row[row.index(col, pos) - 1] == 'FAC':  # left have FAC
                        hse.append(1)
                    elif 0 < map.index(row, pos_row) < 3:  # HSE in 2 or 3
                        if map[map.index(row, pos_row) - 1][row.index(col, pos)] == 'FAC' or map[map.index(row, pos_row) + 1][row.index(col, pos)] == 'FAC':  # up or down have FAC
                            hse.append(1)
                        elif map[map.index(row, pos_row) - 1][row.index(col, pos)] in ('SHP', 'HSE') and map[map.index(row, pos_row) + 1][row.index(col, pos)] in ('SHP', 'HSE'):  # up and down have HSE or SHP
                            if row[row.index(col, pos) - 1] in ('SHP', 'HSE'):  # left have HSE or SHP
                                hse.append(3)
                            elif row[row.index(col, pos) - 1] == 'BCH':  # left have BCH
                                hse.append(4)
                            else:  # only up and down have HSE or SHP
                                hse.append(2)
                        elif map[map.index(row, pos_row) - 1][row.index(col, pos)] == 'BCH' and map[map.index(row, pos_row) + 1][row.index(col, pos)] == 'BCH':  # up and down have BCH
                            if row[row.index(col, pos) - 1] in ('SHP', 'HSE'):  # left have HSE or SHP
                                hse.append(5)
                            elif row[row.index(col, pos) - 1] == 'BCH':  # left have BCH
                                hse.append(6)
                            else:  # only up and down have BCH
                                hse.append(4)
                        elif map[map.index(row, pos_row) - 1][row.index(col, pos)] == 'BCH' or map[map.index(row, pos_row) + 1][row.index(col, pos)] == 'BCH':  # up or down have BCH
                            if map[map.index(row, pos_row) - 1][row.index(col, pos)] in ('SHP', 'HSE') or map[map.index(row, pos_row) + 1][row.index(col, pos)] in ('SHP', 'HSE'):  # up or down have
                                if row[row.index(col, pos) - 1] in ('SHP', 'HSE'):  # left have SHP or HSE
                                    hse.append(4)
                                elif row[row.index(col, pos) - 1] == 'BCH':  # left have BCH
                                    hse.append(5)
                                else:  # up or down have 1 HSE or SHP
                                    hse.append(3)
                            elif row[row.index(col, pos) - 1] in ('SHP', 'HSE'):  # only left have HSE or SHP and up or down have 1 BCH
                                hse.append(3)
                            elif row[row.index(col, pos) - 1] == 'BCH':  # only left have BCH and up or down have 1 BCH
                                hse.append(4)
                            else:  # only up or down have 1 BCH
                                hse.append(2)
                        elif map[map.index(row, pos_row) - 1][row.index(col, pos)] in ('SHP', 'HSE') or map[map.index(row, pos_row) + 1][row.index(col, pos)] in ('SHP', 'HSE'):  # up or down have 1 HSE or SHP
                            if row[row.index(col, pos) - 1] in ('SHP', 'HSE'):  # left have HSE or SHP
                                hse.append(2)
                            elif row[row.index(col, pos) - 1] == 'BCH':  # left have BCH
                                hse.append(3)
                            else:  # only up or down have 1 HSE or SHP
                                hse.append(1)
                        else:  # up or down don't have special building
                            if row[row.index(col, pos) - 1] == 'BCH':  # left have BCH
                                hse.append(2)
                            else:  # individual HSE or left have HSE or SHP
                                hse.append(1)
                    elif map.index(row, pos_row) == 0:  # HSE in 1
                        if map[map.index(row, pos_row) + 1][row.index(col, pos)] == 'FAC' or row[row.index(col, pos) - 1] == 'FAC':  # right or down have FAC
                            hse.append(1)
                        elif map[map.index(row, pos_row) + 1][row.index(col, pos)] in ('SHP', 'HSE'):  # down have SHP or HSE
                            if row[row.index(col, pos) - 1] in ('SHP', 'HSE'):  # left have HSE or SHP
                                hse.append(2)
                            elif row[row.index(col, pos) - 1] == 'BCH':  # left have BCH
                                hse.append(3)
                            else:  # only down have HSE or SHP
                                hse.append(1)
                        elif map[map.index(row, pos_row) + 1][row.index(col, pos)] == 'BCH':  # down have BCH
                            if row[row.index(col, pos) - 1] in ('SHP', 'HSE'):  # left have SHP or HSE
                                hse.append(3)
                            elif row[row.index(col, pos) - 1] == 'BCH':  # left have BCH
                                hse.append(4)
                            else:  # only down have BCH
                                hse.append(2)
                        else:  # down don't have any special building
                            if row[row.index(col, pos) - 1] == 'BCH':  # only left have BCH
                                hse.append(2)
                            else:  # individual HSE or with HSE or SHP at the left
                                hse.append(1)
                    elif map.index(row, pos_row) == 3:  # HSE at 4
                        if map[map.index(row, pos_row) - 1][row.index(col, pos)] == 'FAC' or row[row.index(col, pos) - 1] == 'FAC':  # right or down have FAC
                            hse.append(1)
                        elif map[map.index(row, pos_row) - 1][row.index(col, pos)] in ('SHP', 'HSE'):  # up have HSE or SHP
                            if row[row.index(col, pos) - 1] in ('SHP', 'HSE'):  # left have HSE or SHP
                                hse.append(2)
                            elif row[row.index(col, pos) - 1] == 'BCH':  # left have BCH
                                hse.append(3)
                            else:  # only up have HSE or SHP
                                hse.append(1)
                        elif map[map.index(row, pos_row) - 1][row.index(col, pos)] == 'BCH':  # down have BCH
                            if row[row.index(col, pos) - 1] in ('SHP', 'HSE'):  # left have HSE or SHP
                                hse.append(3)
                            elif row[row.index(col, pos) - 1] == 'BCH':  # left have BCH
                                hse.append(4)
                            else:  # only down have BCH
                                hse.append(2)
                        else:  # down don't have special building
                            if row[row.index(col, pos) - 1] == 'BCH':  # only left have BCH
                                hse.append(2)
                            else:  # individual HSE or HSE or SHP at the left
                                hse.append(1)
            elif col == 'SHP':
                if 0 < row.index(col, pos) < 3:
                    if 0 < map.index(row, pos_row) < 3:
                        for loop in range(4):
                            if map[map.index(row, pos_row) - 1][row.index(col, pos)] not in shp_building_list:
                                shp_building_list.append(map[map.index(row, pos_row) - 1][row.index(col, pos)])
                                shp_num += 1
                            elif map[map.index(row, pos_row) + 1][row.index(col, pos)] not in shp_building_list:
                                shp_building_list.append(map[map.index(row, pos_row) + 1][row.index(col, pos)])
                                shp_num += 1
                            elif row[row.index(col, pos) - 1] not in shp_building_list:
                                shp_building_list.append(row[row.index(col, pos) - 1])
                                shp_num += 1
                            elif row[row.index(col, pos) + 1] not in shp_building_list:
                                shp_building_list.append(row[row.index(col, pos) + 1])
                                shp_num += 1
                    elif map.index(row, pos_row) == 0:
                        for loop in range(3):
                            if map[map.index(row, pos_row) + 1][row.index(col, pos)] not in shp_building_list:
                                shp_building_list.append(map[map.index(row, pos_row) + 1][row.index(col, pos)])
                                shp_num += 1
                            elif row[row.index(col, pos) - 1] not in shp_building_list:
                                shp_building_list.append(row[row.index(col, pos) - 1])
                                shp_num += 1
                            elif row[row.index(col, pos) + 1] not in shp_building_list:
                                shp_building_list.append(row[row.index(col, pos) + 1])
                                shp_num += 1
                    elif map.index(row, pos_row) == 3:
                        for loop in range(3):
                            if map[map.index(row, pos_row) - 1][row.index(col, pos)] not in shp_building_list:
                                shp_building_list.append(map[map.index(row, pos_row) - 1][row.index(col, pos)])
                                shp_num += 1
                            elif row[row.index(col, pos) - 1] not in shp_building_list:
                                shp_building_list.append(row[row.index(col, pos) - 1])
                                shp_num += 1
                            elif row[row.index(col, pos) + 1] not in shp_building_list:
                                shp_building_list.append(row[row.index(col, pos) + 1])
                                shp_num += 1
                elif row.index(col, pos) == 0:
                    if 0 < map.index(row, pos_row) < 3:
                        for loop in range(3):
                            if map[map.index(row, pos_row) - 1][row.index(col, pos)] not in shp_building_list:
                                shp_building_list.append(map[map.index(row, pos_row) - 1][row.index(col, pos)])
                                shp_num += 1
                            elif map[map.index(row, pos_row) + 1][row.index(col, pos)] not in shp_building_list:
                                shp_building_list.append(map[map.index(row, pos_row) + 1][row.index(col, pos)])
                                shp_num += 1
                            elif row[row.index(col, pos) + 1] not in shp_building_list:
                                shp_building_list.append(row[row.index(col, pos) + 1])
                                shp_num += 1
                    elif map.index(row, pos_row) == 0:
                        for loop in range(2):
                            if map[map.index(row, pos_row) + 1][row.index(col, pos)] not in shp_building_list:
                                shp_building_list.append(map[map.index(row, pos_row) + 1][row.index(col, pos)])
                                shp_num += 1
                            elif row[row.index(col, pos) + 1] not in shp_building_list:
                                shp_building_list.append(row[row.index(col, pos) + 1])
                                shp_num += 1
                    elif map.index(row, pos_row) == 3:
                        for loop in range(2):
                            if map[map.index(row, pos_row) - 1][row.index(col, pos)] not in shp_building_list:
                                shp_building_list.append(map[map.index(row, pos_row) - 1][row.index(col, pos)])
                                shp_num += 1
                            elif row[row.index(col, pos) + 1] not in shp_building_list:
                                shp_building_list.append(row[row.index(col, pos) + 1])
                                shp_num += 1
                elif row.index(col, pos) == 3:
                    if 0 < map.index(row, pos_row) < 3:
                        for loop in range(3):
                            if map[map.index(row, pos_row) - 1][row.index(col, pos)] not in shp_building_list:
                                shp_building_list.append(map[map.index(row, pos_row) - 1][row.index(col, pos)])
                                shp_num += 1
                            elif map[map.index(row, pos_row) + 1][row.index(col, pos)] not in shp_building_list:
                                shp_building_list.append(map[map.index(row, pos_row) + 1][row.index(col, pos)])
                                shp_num += 1
                            elif row[row.index(col, pos) - 1] not in shp_building_list:
                                shp_building_list.append(row[row.index(col, pos) - 1])
                                shp_num += 1
                    elif map.index(row, pos_row) == 0:
                        for loop in range(2):
                            if map[map.index(row, pos_row) + 1][row.index(col, pos)] not in shp_building_list:
                                shp_building_list.append(map[map.index(row, pos_row) + 1][row.index(col, pos)])
                                shp_num += 1
                            elif row[row.index(col, pos) - 1] not in shp_building_list:
                                shp_building_list.append(row[row.index(col, pos) - 1])
                                shp_num += 1
                    elif map.index(row, pos_row) == 3:
                        for loop in range(2):
                            if map[map.index(row, pos_row) - 1][row.index(col, pos)] not in shp_building_list:
                                shp_building_list.append(map[map.index(row, pos_row) - 1][row.index(col, pos)])
                                shp_num += 1
                            elif row[row.index(col, pos) - 1] not in shp_building_list:
                                shp_building_list.append(row[row.index(col, pos) - 1])
                                shp_num += 1
                shp.append(shp_num)
            elif 'HWY' in row and hwynum == 0:  # if hwy in row
                if row.index('HWY') == 0:  # if the first HWY is at A
                    if row[row.index('HWY') + 1] == 'HWY' and row[row.index('HWY') + 2] == 'HWY' and row[row.index('HWY') + 3] == 'HWY':  # from A to D
                        for loop in range(4):
                            hwy.append(4)
                    elif row[row.index('HWY') + 1] == 'HWY' and row[row.index('HWY') + 2] == 'HWY':  # from A to C
                        for loop in range(3):
                            hwy.append(3)
                    elif row[row.index('HWY') + 1] == 'HWY':  # from A to B
                        for loop in range(2):
                            hwy.append(2)
                        if row[row.index('HWY') + 3] == 'HWY':  # if there is another HWY at D
                            hwy.append(1)
                    else:
                        if row[row.index('HWY') + 2] == 'HWY' and row[row.index('HWY') + 3] == 'HWY':  # A and from C to D
                            hwy.append(1)
                            for loop in range(2):
                                hwy.append(2)
                        elif row[row.index('HWY') + 2] == 'HWY' or row[row.index('HWY') + 3] == 'HWY':  # A and C or D
                            hwy.append(1)
                            hwy.append(1)
                        else:
                            hwy.append(1)
                elif row.index('HWY') == 1:  # if first HWY is at B
                    if row[row.index('HWY') + 1] == 'HWY' and row[row.index('HWY') + 2] == 'HWY':  # B to D
                        for loop in range(3):
                            hwy.append(3)
                    elif row[row.index('HWY') + 1] == 'HWY':  # B to C
                        for loop in range(2):
                            hwy.append(2)
                    else:
                        if row[row.index('HWY') + 2] == 'HWY':  # B and D
                            hwy.append(1)
                            hwy.append(1)
                        else:
                            hwy.append(1)
                elif row.index('HWY') == 2:  # if first HWY is at C
                    if row[row.index('HWY') + 1] == 'HWY':  # C to D
                        for loop in range(2):
                            hwy.append(2)
                    else:
                        hwy.append(1)
                else:  # if first HWY is at D
                    hwy.append(1)
                hwynum += 1  # set as a checker to mark the entire row has been checked for HWY building
            pos+=1  # increase to start checking from the next element
        pos_row+=1  # increase to start checking from the next row
    if fac_num > 4:  # calculation for more than 4 factory
        for num in range(4):
            fac.append(4)
            fac_num-=1
        for num in range(fac_num):
            fac.append(1)
    else:  # calculation for less than 4 factory
        for num in range(fac_num):
            fac.append(fac_num)
    for num in shp:
        if num == 0:
            shp[shp.index(num)] = 1  # change all score of 0 to 1, 0 means no building is next to SHP in my program
    for buildings in build:  # display the score calculation
        if len(buildings) == 0:
            print('{}: 0'.format(name[build.index(buildings, build_num)]))
        elif len(buildings) == 1:
            print('{}: {}'.format(name[build.index(buildings, build_num)], str(buildings[0])))
        else:
            print('{}: '.format(name[build.index(buildings, build_num)]), end=str(buildings[0]))
            for score in range(len(buildings) - 1):
                print(' + {}'.format(str(buildings[score + 1])), end='')
            print(' = ' + str(sum(buildings)))
        build_num+=1
    total = sum(hwy)+sum(shp)+sum(hse)+sum(bch)+sum(fac)
    print('Total score: {}'.format(total))
    return total


def highscore():
    print('-' * 9, 'HIGH SCORES', '-' * 9)
    print('{}{:>8}{:>20}'.format('Pos', 'Player', 'Score'))
    print('{}{:>8}{:>20}'.format('-' * 3, '-' * 6, '-' * 5))
    highscores.sort(key=lambda x: x[1], reverse=True)  # sort highscores' nested list according to the 2nd element in descending order
    position = 1
    for row in highscores:
        if position==10:  # deleting 1 space between the position and name as 10 takes up 2 spaces and end the loop
            print('{}.  {:<24}{:>}'.format(position, row[0], row[1]))
            break
        print('{}.   {:<24}{:>}'.format(position, row[0], row[1]))
        position += 1
    print('-'*31, '\n')


while True:  # full game
    printmenu()
    turn = 1
    map = []  # used to store map layout
    building = {}  # to store number of building
    highscores = []  # scores with name
    scorelist = []   # only scores
    file4 = open( "savedScore.txt", "r")
    for line in file4:  # append all the games high scores
        sublist=[]  # temporary list
        line = line.strip('\n')
        a = line.split(',')
        sublist.append(a[0])
        sublist.append(int(a[1]))
        scorelist.append(int(a[1]))
        highscores.append(sublist)
    file4.close()
    a = input('Your choice?')
    try:  # input validation
        a = int(a)
    except:
        print('Please use numeric digits.\n')
        continue
    if a == 1:
        map = [['   ', '   ', '   ', '   '],
               ['   ', '   ', '   ', '   '],
               ['   ', '   ', '   ', '   '],
               ['   ', '   ', '   ', '   ']
               ]  # default map layout
        building = {'BCH': 8, 'HSE': 8, 'SHP': 8, 'HWY': 8, 'FAC': 8}  # default number of building
    elif a == 2:
        turn = savegame()
    elif a==3:
        highscore()
        continue
    elif a == 0:
        exit()
    else:  # if the number entered is more than 3
        print('Invalid Digit\n')
        continue
    game(turn, scorelist, highscores)
    file4 = open( "savedScore.txt", "w")
    for player in highscores:  # save the high score
        file4.write('{},{}\n'.format(player[0], player[1]))
    file4.close()
