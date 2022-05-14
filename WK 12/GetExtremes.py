num_list = [10, -13, 50, 5, 7, 65, -40, 44, 30]


def get_extremes(list):
    Smallest = min(list)
    Largest = max(list)
    return Smallest, Largest


Smallest, Largest = get_extremes(num_list)
print('Largest =', Largest)
print('Smallest =', Smallest)
