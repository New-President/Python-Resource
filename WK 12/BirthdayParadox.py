import random
a=[]
while True:
    b=random.randint(1,365)
    print('{} was randomly generated.'.format(b))
    if b in a:
        print('Duplicate day! This took {} tries.'.format(len(a)+1))
        exit()
    else:
        a.append(b)