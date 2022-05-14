# Programming I

###########################
#      Mission 9.1          #
#   Distance Based Fare   #   
###########################

# Background
# ==========
# Distance-Based Fares (DBF) is a fare payment scheme currently used across public buses and MRT/LRT trains in Singapore.
# Fares are charged based on the total distance travelled (regardless if it is on a bus or train).
# The distance-based fare calculation is available in the distance-based-fare.csv file provided.
# Based on the route details of bus service 174 (bus_174.csv), write a program to meet the following requirements:

# a) Calculate the distance travelled based on the boarding and alighting bus stop
# b) Calculate the payable fare

# Return the result of the above answers in a list of two items (e.g., [29.0,1.90])

# Important Notes
# ===============
# 1) Comment out ALL input prompts before submitting.
# 2) You MUST use the following variables
#   board, alight, distance, fare

board = input('Enter boarding busstop: ')
alight = input('Enter alighting busstop: ')


# board CODING FROM HERE
# ======================

# Create your function here
def calculate_fare(board, alight):
    file = open("distance-based-fare.csv", 'r')
    fare_list = []
    for line in file:
        line = line.strip('\n')
        a=line.split(',')
        fare_list.append(a)
    fare_list.remove(fare_list[0])
    file = open("bus_174.csv", 'r')
    busstop_list = []
    for line in file:
        line = line.strip('\n')
        a=line.split(',')
        busstop_list.append(a)

    distance = 0
    fare = 0

    for list in busstop_list:
        if str(board) in list:
            distance-=float(list[0])
        elif str(alight) in list:
            distance+=float(list[0])

    for list in fare_list:
        if float(list[0])>=distance:
            fare+=float(list[1])/100
            break

    print(distance, fare)
    return [distance, fare]


# Do not remove the next line
calculate_fare(board, alight)

# input 22009,10499 output [29.0, 1.9]
# input 28169,42059 output [9.2, 1.29]
# input 42089,10041 output [16.9, 1.61]
