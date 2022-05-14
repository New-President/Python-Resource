def ok():
    over = float(input('Enter monthly sales of sales agent: '))#input monthly sale
    if over >= 10000: #process if more than or equal to 10000
        commission = str(over*0.1) #formula for com amount
        print('The commission rate is : 10%') #show com rate
        print('The commission paid is: $' + commission) #show com amount
    else: #process if less than 10000
        commission = str(over*0.05) #formula for com amount
        print('The commission rate is : 5%') #show com rate
        print('The commission paid is: $' + commission) #show com amount
while True: #loop
    ok()