def cel_to_fahr(Celsius):
    Fahrenheit = (9.0 / 5.0) * (Celsius + 32)
    print('The temperature in Fahrenheit is {:0.1f} degrees\n'.format(Fahrenheit))


def fahr_to_cel(Fahrenheit):
    Celsius = (5.0 / 9.0) * (Fahrenheit - 32)
    print('The temperature in celsius is {:0.1f} degrees\n'.format(Celsius))


while True:
    print('Temperature Conversion')
    print('[1]Fahrenheit to Celsius')
    print('[2]Celsius to Fahrenheit')
    print('[3]Exit')
    a = int(input('Please enter your option : '))
    if a == 3:
        exit()
    elif a == 2:
        b = float(input('Please enter the temperature in Celsius : '))
        cel_to_fahr(b)
    elif a == 1:
        b = float(input('Please enter the temperature in Fahrenheit : '))
        fahr_to_cel(b)
