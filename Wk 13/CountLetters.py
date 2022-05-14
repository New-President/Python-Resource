a=list(input('Enter a sentence:'))

for i in a:
    if i.isalpha():
        continue
    else:
        a.remove(i)
for x in range(len(a)):
    count=0
    for i in