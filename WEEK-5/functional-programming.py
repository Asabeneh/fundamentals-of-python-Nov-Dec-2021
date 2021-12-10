# map, filter, reduce
# Let's talk about map [0, 1, 2, 3, 4] => [0, 2, 4, 6, 8]
# Let's talk about map [0, 1, 2, 3, 4] => [0, 1, 4, 9, 16]
# ['Finland', 'Sweden', 'Norway', 'Denmark','Iceland'] => ['FINLAND', 'SWEDEN', 'NORWAY', 'DENMARK', 'ICELAND']

# Let's talk about filter [0, 1, 2, 3, 4] => [0, 2, 4]
# Let's talk about filter [0, 1, 2, 3, 4] => [1, 3]
# Let's talk about reduce [0, 1, 2, 3, 4] => 10
# Let's talk about reduce [1, 2, 3, 4] => 24


''' nums = [0, 1, 2, 3, 4]
new_lst = []
for num in nums:
    new_lst.append(num ** 2)
print(new_lst)
     '''
     
nums = [0, 1, 2, 3, 4]
new_lst = list(map(lambda x : x * 2, nums))
print(new_lst)

''' countries = ['Finland', 'Sweden', 'Norway', 'Denmark','Iceland']
new_lst = []
for c in countries:
    new_lst.append(c.upper())
    
print(new_lst) '''

countries = ['Finland', 'Sweden', 'Norway', 'Denmark','Iceland']
new_lst = list(map(lambda country: [country, country.upper(), country.upper()[:3], len(country)], countries))
print(new_lst)

''' nums = [0, 1, 2, 3, 4]
evens = []
for num in nums:
    if num % 2 == 0:
        evens.append(num)

print(evens)


nums = [0, 1, 2, 3, 4]
odds = []
for num in nums:
    if num % 2 != 0:
        odds.append(num)

print(odds) '''

nums = [0, 1, 2, 3, 4]
evens = list(filter(lambda x: x % 2 == 0, nums))
print(evens)

odds = list(filter(lambda x: x % 2 != 0, nums))
print(odds)

countries = ['Finland', 'Sweden', 'Norway', 'Denmark','Iceland']
countries_with_land = list(filter(lambda country: 'land' in country, countries))
print(countries_with_land)

from functools import reduce

nums = [1, 2, 3, 4]

print(reduce(lambda x, y: x + y, nums))
print(reduce(lambda x, y: x * y, nums))




