a=str(input('Please enter a character:'))
b=['a','e','i','o','u']
c=ord(a[0])-96
if len(a)>1:
    print('Your input must contain exactly one character')
elif a in b:
    print('Your input is a vowel')
    exit()
elif 0<=c<=26:
    print('Your input is a consonant')
else:
    print('Your input is not an alphabet')