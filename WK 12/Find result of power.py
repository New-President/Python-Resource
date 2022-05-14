def power(x, n):
    a = pow(x, n)
    return a


num1 = float(input('Enter the number for base:'))
num2 = float(input('Enter the number for exponent:'))
result = power(num1, num2)
print(result)
