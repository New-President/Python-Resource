def find_larger(n1, n2):
    numlist = [n1, n2]
    large = max(numlist)
    return large


n1 = int(input('Enter a number:'))
n2 = int(input('Enter a number:'))
larger1 = find_larger(n1, n2)
print('The larger integer is', larger1)

n3 = int(input('Enter a number:'))
n4 = int(input('Enter a number:'))
larger2 = find_larger(n3, n4)
print('The larger integer is', larger2)

largest = find_larger(larger1, larger2)
print('The largest integer is', largest)