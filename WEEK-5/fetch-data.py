import requests
from pprint import pprint
url = 'https://api.thecatapi.com/v1/breeds'
response = requests.get(url)
data = response.json()
print(len(data))
pprint(data[:2])

weights = []
for cat in data:
    lowest = cat['weight']['metric'].split(' - ')[0]
    highest = cat['weight']['metric'].split(' - ')[1]
    average = (int(lowest) + int(highest))/2
    weights.append(average)
print(weights)

from functools import reduce

total = reduce(lambda x, y: x + y, weights)

mean = total / len(weights)
print(round(mean, 2))
    