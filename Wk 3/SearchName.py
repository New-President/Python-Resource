namList = ["Tom", "Joe", "Mary", "John", "Bob", "Jane"]
a = str(input('Enter name to search:'))
if a in namList:
    print('Name', a, 'is found in position', namList.index(a), 'in the name list.')
else:
    print('Name not found')
input('To exit press enter:')
