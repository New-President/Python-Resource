def ok():
    L=float(input('Loan Amount:'))
    A=float(input('Annual Income:'))
    C=float(input('Current Loans:'))
    S=float(input('Total Savings:'))
    Y=float(input('Years To Pay Back:'))
    Interest_rate=(L+C)/(S+A*Y)
    print('Your interest rate is {:0.2f}'.format(Interest_rate))
counter=0
while counter<3:
    counter = counter + 1
    ok()