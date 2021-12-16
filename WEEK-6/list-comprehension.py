# Why learn Python
# Variable, Data types(numbers(int, float, complex)), string, Booleans, List, Tuples, Set, and Dictionary
# Builtin functions(print(), input(), round(), list() ...)
# Operators(arithimetic, comparison, logical)
# Stings methods(.upper(), .lower(), .title())
# List and list methods
# Conditionals(if, if elif)
# Loops(while, for loop)
# Functions
# Lamdba Function
# Higher Order Function
# Functional Programming(map, reduce, Filter)
# Modules
# List Comprehensions

from pprint import pprint

nums = [1, 2, 3, 4, 5] # [1, 4, 6, 8, 10]

''' new_nums = []
for num in nums:
    new_nums.append(num * 2)
print(new_nums) '''

''' new_nums = list(map(lambda x: x * 2, nums))
print(new_nums) '''

new_nums = [num * 2 for num in nums]
print(new_nums)

evens = [num for num in nums if num % 2 == 0]
print(evens)

odds = [num for num in nums if num % 2 != 0]
print(odds)

countries = ['Finland','Sweden','Norway','Denmark','Iceland']

''' for c in countries:
    if 'way' in c:
        print(c) '''

countries_with_land = [c for c in countries if 'land' in c]
print(countries_with_land)

countries_without_land = [c for c in countries if 'land' not in c]
print(countries_without_land)

def sum_all_nums(*args):
    total = 0
    for item in args:
        total = total + item
    return total
    
print(sum_all_nums(10, 20, 30, 100, 20, 20, 100))
pprint([[c, c.upper(), c.upper()[:3], len(c)] for c in countries])

paragraph = """
I am an instructor, developer, content creator and motivator. I am married and I live in Finland. I attended different universities and that gave me an insight for many of the activities I do right now. I teach different technologies specially HTML, CSS, Sass, JS, React, Redux, Node, MongoDB, Python,Data Analysis with Python, and D3.js. In addition, I am a data science and machine learning enthusiast. I enjoy creating different educational materials. So far, I have created 30 Days Of Python, 30Days Of JavaScript, 30 Days Of React, 10 Days of Git and GitHub, 10 Days Of Python, Numpy, Pandas, Matplotlib and 30DaysOfHTML. In the coming years, I will create more programming challenges. After the Corona Pandemic, I will travel around the world, teach programming and meet 30DaysOfJavaScript, 30DaysOfPython and 30DaysOfReact fans.
"""
print(paragraph)
words = paragraph.lower().replace('.', ' ').replace(',', ' ').split()
print(words)
number_words = len(words)
number_unique_words = len(set(words))
lexical_density = (number_unique_words / number_words) * 100
print(lexical_density)
