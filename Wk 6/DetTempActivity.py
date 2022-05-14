def ok():#Naming the program
    a = float(input('Please enter outdoor temperature:'))#Get temperature
    if a <= -5:#if it's less than -5 display 'Go Bowling'
        print('Go Bowling')
    elif a<=0:#if it's -4to0 display 'Go Skiing'
        print('Go Skiing')
    elif a<=20:#if it's 1to20 display 'Go Jogging'
        print('Go Jogging')
    elif a<=25:#if it's 21to25 display 'Play Tennis; Wear White Clothes'
        print('Play Tennis')
        print('Wear White Clothes')
    elif a<=30:#if it's 26to30 display 'Go Sun-tanning in the park'
        print('Go Sun-tanning in the park')
    else:# everything other temperature display 'Go Swimming'
        print('Go Swimming')
count=0#Extra loop for convenience
while count < 5:
    count = count + 1
    ok()