''' import functions

print(dir(functions))
print(make_square(2))
print(functions.print_fullname('John','Doe')) '''


from functions import make_square as square, print_fullname as fullname, sum_numbers as total, sum_numbers_range

print(square(2))
print(fullname('John','Doe'))
print(sum_numbers_range(0, 100))
print(total(1, 2, 3, 4, 5))