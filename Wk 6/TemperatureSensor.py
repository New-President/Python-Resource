temp_list = [20.5, 22, 21, 29.3, 28.2, 25,26, 28, 26.3,
            25.6, 29.3, 28.4,24.5, 26.3, 25.5, 26.5, 23.3,
             24.3,25.4, 26.5, 23.3, 25.4, 26.3, 25.5]
total = 0
a=0
while a <len(temp_list):
    total = total+temp_list[a]
    a=a+1
average=total/len(temp_list)
print('The average temperature for the day is: {:.2f} degree celsius.'.format(average))