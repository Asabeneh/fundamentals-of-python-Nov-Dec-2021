# what are logical operators in Python ?
# and, or, not

print(2 > 1)
print(4 > 3)

# and
print(2 > 1 and 4 > 3) # True
print(2 > 1 and 4 < 3) # False
print(2 < 1 and 4 < 3) # False

# or
print(10 > 5) 
print(5 < 8)

print(10 > 5 or 5 < 8) # True
print(10 > 5 or 5 > 8) # True
print(10 < 5 or 5 > 8) # False

# not, negation
print( not True)

print( not 10 < 5 or 5 > 8) # True
print( not 10 < 5 and not 5 > 8) # True

