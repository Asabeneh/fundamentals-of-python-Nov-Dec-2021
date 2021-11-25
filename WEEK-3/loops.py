# LOOP: 
# 100 FRIENDS => GREETING
print('Happy New Year!')
print('Happy New Year!')
print('Happy New Year!')
print('Happy New Year!')
print('Happy New Year!')

# We have two kinds of loops:while and for

for i in range(11):
    print(i)
    
   
countries = ['Finland','Sweden','Norway','Denmark','Iceland']

for num in [1, 2, 3, 4, 5]:
    print(num)

for i in range(0, 101, 10):
    print(i)
  
countries_with_land = []  
for c in countries:
    if 'land' in c:
        countries_with_land.append(c)
print(countries_with_land)

countries_without_land = []
for country in countries:
    if 'land' not in country:
        countries_without_land.append(country)
print(countries_without_land)

country_with_way = []
for c in countries:
    if 'way' in c:
        country_with_way.append(c)
print(country_with_way)

nums = [0, 1, 2, 3, 4, 5]

total = 0
for n in nums:
    # total = total + n
    total +=  n
print(total)

evens = []
for n in nums:
    if n % 2 == 0:
        evens.append(n)
print(evens)

for i in range(100):
    if i % 2 != 0:
        print(i)
        
        
nums = [0, 1, 2, 3,-7, 4, 5]
for i in nums:
    if i < 0:
        continue
    print(i)
    
nums = [0, 1, 2, 3,-7, 4, 5]
for i in nums:
    if i < 0:
        break
    print(i)
    

countries = ['Finland','Sweden','Norway','Denmark','Iceland']

for c in countries:
    if 'land' in c:
        continue
    print(c)
    
data = [['Finland', 'FINLAND', 'FIN', 7], ['Sweden', 'SWEDEN', 'SWE', 6], ['Norway', 'NORWAY', 'NOR', 6], ['Denmark', 'DENMARK', 'DEN', 7], ['Iceland', 'ICELAND', 'ICE', 7]] 

nums = []
for lst in data:
    nums.append(lst[3])
print(nums)

for i in range(4, -1, -1):
    print(i)

# 10 to 0

for i in range(10, -1, -1):
    print(i)

  