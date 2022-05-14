# Programming I

#########################
#      Mission 9.1        #
#   HDB Resale Prices   #
#########################

# Background
# ==========
# Tom is conducting some research into HDB resale prices as part of his part-time work for a real estate agency.
# Write a program to find out the following:

# a) The 2017 average price for the 4-room flat type (in 2 decimal places)
# b) The number of transactions above the average resale prices in part (a)
# c) The town with the highest resale price for the 5-room flat type in 2017

# Return the result of the three parts in a list of 3 items (e.g., [34535.35,20,'Hougang']

# Important Notes
# ===============
# 1) Comment out ALL input prompts before submitting.
# 2) You MUST use the following variables
#   four_room_average, above_average, town_highest

filename = "C:\\Users\\ziren\\OneDrive - Ngee Ann Polytechnic\\Desktop\\School\\PR1\\Wk 13\\median-resale-prices-for-registered-applications-by-town-and-flat-type.csv"


# START CODING FROM HERE
# ======================

# Create your function here
def ReadCSV(filename):
    file = open(filename, 'r')
    # Part a
    b = 0
    c = 0
    above_average = 0
    e = []
    f = []
    g = []
    for line in file:
        line = line.strip('\n')
        a = line.split(',')
        e.append(a)
    for element in e:
        if '4-room' in element:
            if element[-1] not in ('-', 'na'):
                c += int(element[-1])
                b += 1
    four_room_average = round((c / b), 2)

    # Part b
    for element in e:
        if '4-room' in element:
            if element[-1] not in ('-', 'na'):
                if int(element[-1])>four_room_average:
                    above_average+=1

    # Part c
    for element in e:
        if '5-room' in element:
            if element[-1] not in ('-', 'na'):
                f.append(element[1])
                g.append(element[-1])
    town_highest=f[g.index(max(g))]

    return [four_room_average, above_average, town_highest]


# Do not remove the next line
print(ReadCSV(filename))

# output [459567.74, 33, 'Toa Payoh']
