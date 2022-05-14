def ConvertTemperature(c):
    f = (c * 9 / 5) + 32
    return f


celcius = float(input('Enter temp in degree:'))
fehrenheit = ConvertTemperature(celcius)
print('{:.2f}'.format(fehrenheit))
