def make_square(n):
    return n ** 2

def print_fullname(firstname, lastname):
    return firstname + ' ' + lastname

def sum_numbers_range(n, m):
    total = 0
    for i in range(n, m + 1):
        total = total + i
    return total

def sum_numbers(*args):
    total = 0
    for i in args:
        total = total + i    
    return total
        