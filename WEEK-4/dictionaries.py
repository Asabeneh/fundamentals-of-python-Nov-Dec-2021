"""
first_name = 'Asabeneh'
last_name = 'Yetayeh'
age = 250
country = 'Finland'
"""
from pprint import pprint
print({})
print(type({}))

d = dict()
print(d)
print(type(d))

finnish_to_english = {
    'talo':'house',
    'kirja':'book',
    'mies':'man',
    'nainen':'woman',
    'poika':'boy',
    'katso':'to watch'
}

person = {
    'first_name':'Asabeneh',
    'last_name':'Yetayeh',
    'age':250,
    'is_married':True,
    'country':'Finland',
    'kids':('John','Robert','Marta'),
    'skills':['Python','React','Node'],
    'schools':['Wagnegnin', 'Metroplia','Helsinki'],
    'hobbies':['Hikking','Dancing','Football'],
    'address':{
        'city':'Helsinki',
        'street_name':'space street',
        'zipcode':'02270'
    }
    
}

pprint(person)
print(person['age'])
print(person['skills'])
print(len(person['skills']))
person['nationality'] ='Ethiopian'

person['schools'].append('Aalto')

pprint(person)

# print(person['schools'])
print(person.get('schools'))

if 'hobbies' in person:
    print(person['hobbies'])
    
    
print(len(person))

print(finnish_to_english.keys())
print(finnish_to_english.values())
print(finnish_to_english.items())

for item in finnish_to_english.items():
    print(item, item[0], item[1])
    
    for key in person:
        print(key, person[key])
        
        
        
print('katso' in finnish_to_english)

# finnish_to_english.pop('poika')
del finnish_to_english['poika']

pprint(finnish_to_english)

finnish_to_english.clear()
print(finnish_to_english)
person_data_copied = person.copy()