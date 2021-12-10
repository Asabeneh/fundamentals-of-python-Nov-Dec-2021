# sum_list_of_itmes it takes a list and returns the sum of the items
# sum_of_numbers_range it takes to numbers and sum the numbers between the two numbers
# change_item_upper it takes a list of items and return the list of the upper cases of the item
# square_list_of_items it takes a list and return list with a square items

from pprint import pprint

''' def sum_items(lst):
    total = 0
    for item in lst:
        total = total + item
    return total

print(sum_items([1, 2, 3, 4, 5]))
print(sum_items([100, 200, 300]))
     '''

''' def sum_range_numbers(m, n):
    total = 0
    lst = range(m, n+1)
    for num in lst:
        total = total + num
    return total

print(sum_range_numbers(0, 10))
print(sum_range_numbers(0, 100))
print(sum_range_numbers(50, 60))
print(sum_range_numbers(50, 100)) '''

names = ['Asabeneh','Donlad','Bill','Steve']

''' def change_uppercase(lst):
    new_lst = []
    for item in lst:
        new_lst.append(item.upper())
    return new_lst
        
print(change_uppercase(names))
print(change_uppercase(['Finland','Sweden','Denmark','Norway','Iceland']))
         '''

def change_uppercase(lst):
    return [item.upper() for item in lst]

print(change_uppercase(names))
print(change_uppercase(['Finland','Sweden','Denmark','Norway','Iceland']))


''' nums = [0, 1, 2, 3, 5, 6, 11] # [0, 1, 4, 9]

def square_list_items(lst):
    new_lst= []
    for num in lst:
        new_lst.append(num ** 2)
    return new_lst

print(square_list_items(nums))
print(square_list_items([10, 20, 30])) '''


nums = [0, 1, 2, 3, 5, 6, 11] # [0, 1, 4, 9]

def square_list_items(lst):
    return [num ** 2 for num in lst]

print(square_list_items(nums))
print(square_list_items([10, 20, 30]))

def name_of_fun(a, b):
    return a  + b

    

print(name_of_fun('Water', str(2)))

def calculate_weight(mass, gravity = 9.81):
    return mass * gravity

print(calculate_weight(75))
print(calculate_weight(75, 1.65))

def mix_two_list(lst1, lst2):
    mixed_lst = lst1 + lst2
    new_lst = []
    for item in mixed_lst:
        new_lst.append(item ** 2)
    return new_lst

print(mix_two_list([1, 2], [3, 4]))

print('slslsl', 200, 10, [22, 100, 'string'])

def sum_numbers(*args):
    total = 0
    for item in args:
        total = total + item
        
    return total
    
print(sum_numbers(1, 2, 3, 4, 5, 6, 7, 8, 100, 2000, -3000))

def sample_fun(**kwargs):
    for key in kwargs:
        print(key, kwargs[key])
    
sample_fun(first_name='Asabeneh', last_name='Yetayeh', age = 250, country = 'Finland', skills = ['HTML','CSS','JS','React'])