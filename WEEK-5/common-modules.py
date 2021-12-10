# import math

import os

''' print(dir(os))
print(os.getcwd())
print()
# print(dir(os.environ))
print(os.environ.items)
# os.mkdir('./WEEK-5/sample-folder')
os.rmdir('./WEEK-5/sample-folder') '''
print(os.listdir())
for d in os.listdir()[1:]:
    for file in os.walk(d):
        print(file)
    
