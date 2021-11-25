# List
# ['Milk', 'Meat', 'Coffe', 'Sugar', 'Honey', 'Mango', 'Tomato', 'Potato']

shoping_list = ['Milk','Meat','Coffee','Honey','Tea','Sugar']
print(shoping_list)
print(len(shoping_list))
names = ['Bill','Steve','Donald','Asabeneh']
# names.remove('Asabeneh')
# names.pop(3)
countries = ['Finland','Sweden','Norway','Denmark','Iceland']

nums = [1, 2, 3, 4, 5]
print(nums[0])
print(nums[1])
print(nums[2])
last_index = len(nums) - 1
print(nums[last_index])
print(nums[-1])
print(nums[-2])
print(nums[-3])
# slicing
print(nums[0:3])
print(nums[2:5])
print(nums[2:])
print(nums[::-1])
print(nums[:3])
print(nums[-3:-1])

# Modifying
""" nums[0] = 10
print(nums)

nums[2] = 33
print(nums) """

# remove item from a list
# pop() remove the last item in a list if an argument is not griven
# pop(index) remove an item of a certain index

""" nums.pop(1)
print(nums)
nums.pop() """

print(nums)
""" nums.insert(1, 22)
print(nums) """

nums.insert(2, 400)
print(nums)

countries = ['Finland','Sweden','Norway','Denmark','Iceland']

print('Russia' in countries)
print('2' in [3, 4, 5, 8, 2])

shoping_list = []
print(len(shoping_list))
shoping_list.append('Milk')
shoping_list.append('Meat')
shoping_list.append('Coffe')
shoping_list.append('Honey')
shoping_list.append('Mango')
shoping_list.append('Yoghurt')
shoping_list.append('Sugar')
print(shoping_list)
shoping_list.remove('Honey')
print(shoping_list)
fruits = ['banana', 'orange', 'mango', 'lemon', 'kiwi', 'lime']
del fruits[3]

print(fruits)
# fruits.clear()
fruits = []
fruits = list()
print(fruits)

postive_nums = [1, 2, 3, 4, 5, 6]
zero = [0]
negative_nums = [-1, -2, -3, -4, -5, -6]
integers = negative_nums[::-1] + zero + postive_nums

print(integers)

a = [1, 2, 3, 4]
b = [5, 6, 7, 8]
c = a  + b
print(c)

fruits = ['banana', 'orange', 'mango', 'lemon']
vegetables = ['Tomato', 'Potato', 'Cabbage', 'Onion', 'Carrot']
fruits_and_vegetables = fruits + vegetables
print(fruits_and_vegetables)

ages = [22, 19, 24, 25, 26, 24, 25, 24]
print(ages.count(24))
print(ages.index(22))
# print(ages[::-1])
# ages.reverse()
# print(ages)
# Mutation 

""" ages.sort(reverse)
print(ages) """
sorted_age = sorted(ages, reverse=True)

