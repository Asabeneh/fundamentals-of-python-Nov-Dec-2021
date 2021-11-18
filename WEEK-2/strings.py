# What is string ? 
# A string text data type
# '', ""
# what length of a string 1 or many pages

letters = 'abcdefghijklmnopqrstuvwxyz'
vowels = 'aeiou'
consonants = 'bcdfghjklmnpqrstvwxyz'
print(letters)
print(len(letters))
print(len(vowels))
print(len(consonants))
print(letters.upper())
print(vowels.upper())
print(dir(letters))

challenge = '30 Days Of Python'
print(challenge.upper())
print(challenge.title())
print(challenge.swapcase())
print(challenge.find('0'))
print(challenge.find('y'))
print(challenge.find('f'))

langauge = 'python'
print(langauge.upper())
print(len(langauge))
print(langauge[0:2])
print(langauge[2:])
print(langauge[-2:])
print(langauge[::-1])
print(langauge.lower())
print(langauge.title())
print(langauge.swapcase())
print(langauge.isupper())
print(langauge.islower())
print(langauge.count('o'))

city = 'mississippi'
print(city.count('i'))
print(city.count('s'))
print(city.count('p'))
print(city.find('i'))
print(city.rfind('i'))
print(city)
print(city.strip())
print(list(city))
print('what is th eindex', city.find('I'))

print('i love python'.capitalize())
print('i love python'.title())
country = 'Finland'
print(country.startswith('Fin'))
print(country.startswith('F'))
print(country.endswith('d'))
print(country.endswith('land'))

skills = ['HTML','CSS','JS','Python']
print(', '.join(skills))

print('abac'.isalpha())
print('12abac314'.isalpha())
print('12abac314'.isalnum())
print('123'.isdecimal())
print('123'.isnumeric())
print('123'.isdigit())

# year, first_name, first-name, 2021_current_year
# _if, _range

sentence = 'I love JavaScript. JavaScript is the most important language in this world.'

print(sentence.replace('JavaScript', 'Python'))

first_name = 'Asabeneh'
last_name = 'Yetayeh'
age = 250
country = 'Finland'
city = 'Helsinki'
skills = ['HTML','CSS','JS','Python']
formattedSkills = ', '.join(skills)

full_name = first_name + ' ' + last_name
print(full_name)

# I am Asabeneh Yetayeh. I am 250 years old. I live in Helsinki, Finland. I have HTML, CSS, JS, Python. 

print('I am ' + full_name +'. ' + 'I am ' + str(age) + ' years old. ' + 'I live in ' + city + ', ' + country + '. ' + 'I have ' + ', '.join(skills) + '.' )

print(f'I am {full_name}. I am {age} years old. I live in {city}, {country}. I have {formattedSkills}. ')

print('I am {}. I am {} years old. I live in {}, {}. I have {}. '.format(full_name, age, city, country, formattedSkills))

a = 4
b = 3
print('%d + %d = %d' %(a, b, a + b))
print('%d - %d = %d' %(a, b, a - b))
print('%d * %d = %d' %(a, b, a * b))
print('%d / %d = %.1f' %(a, b, a / b))
print('%d // %d = %d' %(a, b, a // b))
print('{} % {} = {}'.format(a, b, a % b))
print('%d ** %d = %d' %(a, b, a ** b))

print('%s%s' %('water', 'melon'))


print('{} + {} = {}'.format(a, b, a + b))
print('{} - {} = {}'.format(a, b, a - b))
print('{} * {} = {}'.format(a, b, a * b))
print('{} / {} = {:.1f}'.format(a, b, a / b))
print('{} // {} = {}'.format(a, b, a // b))
print('{} % {} = {}'.format(a, b, a % b))
print('{} ** {} = {}'.format(a, b, a ** b))

a = 4
b = 3
div = a / b
print(f'{a} + {b} = {a + b}')
print(f'{a} - {b} = {a - b}')
print(f'{a} * {b} = {a * b}')
print(f'{a} / {b} = {div:0.1f}')
print(f'{a} // {b} = {a // b}')
print(f'{a} % {b} = {a % b}')
print(f'{a} ** {b} = {a ** b}')

sentence = 'I love Python'
print(sentence.split(' love '))
print('I love \n Python very well.')
print('It is hard to write \ in the string')
print('I DONT\'T LIKE THIS ')
print("I DONT'T LIKE THIS ")
print("The old cliche of \"an apple a day keep the doctor away\" might not work")
print('The old cliche of "an apple a day keep the doctor away" might not work')
print('Name','\t', 'Age','\t','Country')
print('John', '\t', '30','\t','Finland')

print('I love to create a tabe \t, why not here \t any where')


city = 'mississippi'
print(set(city))