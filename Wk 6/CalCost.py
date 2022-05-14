def ok():
    a = int(input('Enter number of pages to print:'))
    if a<=100:#cost for 100 pages and below
        b=a*0.03
    elif a<=300:#cost for pages above 100 and below 300
        b=100*0.03+(a-100)*0.02
    else:#cost for pages above 300
        b = 100 * 0.03 + 200 * 0.02 + (a-300)*0.01
    print('Cost of printing', a, 'pages is ${:0.2f}'.format(b))
count=0
while count < 3:
    count = count + 1
    ok()