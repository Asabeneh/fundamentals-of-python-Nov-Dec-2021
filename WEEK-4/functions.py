# What is function?
# Function is a set of code that perform a certain task
# It may take an input and it returns an output
# We can reuse functions 
# Function can be builtin function or custom function

print('I love Python', 2021, 'you can put anything as an argument')
print('a', 'b', 'c')

def do_something():
    return 'I am a teaching it is somehting too'

print(do_something())

def make_square(n):
    square = n ** 2
    return square
    
print(make_square(2))
print(make_square(3))
print(make_square(10))
print(make_square(11))
print(make_square(9))

def add_two_nums(a, b):
    return a  + b

print(add_two_nums(1, 9))
print(add_two_nums(-9, 9))
print(add_two_nums(1, 99))

def print_fullname(first_name, last_name):
    full_name = first_name + ' ' + last_name
    return full_name

print(print_fullname('Asabeneh','Yetayeh'))
print(print_fullname('Donald','Trump'))
print(print_fullname('Steve','Jobs'))
print(print_fullname('John','Doe'))

def sum_of_numbers(n):
    total = 0
    for i in range(n+1):
        total = total + i
    return total
print(sum_of_numbers(3)) # 0, 1, 2, 3
print(sum_of_numbers(10)) # 0, 1, 2, 3
print(sum_of_numbers(100))


def calculate_weight(mass = 100, gravity = 9.81):
    return round(mass * gravity, 1)

print(calculate_weight())
print(calculate_weight(75))
print(calculate_weight(75, 1.62))

def check_number(n):
    if n % 2 == 0:
        return 'even'
    return 'odd'

print(check_number(0))
print(check_number(5))
print(check_number(7))
print(check_number(11))
print(check_number(6))



def add_nums(*args):
    total = 0
    for i in args:
        total = total + i
    return total
    
print(add_nums(1, 3, 4, 5, 5, -50, 2300, 50, -2000))