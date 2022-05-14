def is_even(n):
    if n % 2 == 0:
        return True
    else:
        return False


num_list = [10, -13, 50, 5, 7, 24, 65, -40, 44, 30]
even_string = ''
for i in num_list:
    is_even(i)
    if i == num_list[-1]:
        even_string += str(i)
    elif is_even(i):
        even_string += str(i) + ','
print(even_string, 'are the even numbers')
