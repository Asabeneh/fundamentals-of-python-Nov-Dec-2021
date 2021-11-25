# 

""" time = 'five thirty'

if time == 'five thirty':
    print('Go to the class')
else:
    print('Do some activity') """
    

# if time is 5:30
# please show up to Asabeneh


# if weather is sunny go out freely 
# otherwise go with a raincoat or an umbrella

a = 2.5
if type(a) == 'int':
    if a > 0:
        print(f'{a} is a positive number')
    elif a < 0:
        print(f'{a} is a negative number')
    elif a == 0:
        print(f'{a} is zero')
    else:
        print(f'{a} is not a number')
else:
    print('It floating number')
    
weather = 'rainy'

if weather == 'rainy':
    print('Take a rainycoat with you')
elif weather =='cloudy':
    print('It may rainy')
elif weather == 'sunny':
    print('Go out freely and enjoy the shiny day')
elif weather == 'snowy':
    print('The road might be slipper')
else:
    print('No one knows about the weather')

name = 'Bob'
value = 'Very long name' if len(name) > 7 else 'short name'
print(value)

countries = ['Finland','Sweden','Norway','Denmark','Iceland']
if 'Germany' in countries:
    print(countries.index('Germay'))
    
    
score = 59
if score >= 90:
    print('Your grade is A')
elif score < 90 and score >= 80:
    print('Your score B')
elif score < 80 and score >= 70:
    print('Your score C')
elif score < 70 and score >= 60:
    print('Your score D')
else:
    print('You failed')