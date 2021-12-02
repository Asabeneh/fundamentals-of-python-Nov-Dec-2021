# empty set
print(set())
print(len(set()))
A = {1, 2, 3, 4, 5, 5, 6, 9}
B = {3, 4, 5, 8, 9}

# A n B = > {3, 4, 5, 8, 9}
# A U B = > {1, 2, 3, 4, 5, 6, 8, 9}
# A \ B => {1, 2, 6}
# B \ A = > {8}
# (A\B) U (B \ A) => {1, 2, 6, 8}

print(A)
print(len(A))
print(B)
print(len(B))

print(7 in A)
print(4 in A)

for item in A:
    print(item)
    
A.add(100)
A.update([7, 11, 15, 25])

print(A)
fruits = {'banana', 'orange', 'mango', 'lemon'}
vegetables = ('tomato', 'potato', 'cabbage','onion', 'carrot')
fruits.update(vegetables)
print(fruits)

print(B)
B.remove(5)
print(B)

fruits = {'banana', 'orange', 'mango', 'lemon'}
print(fruits)
fruits.pop()  # removes the last element from the set
print(fruits)
A.clear()
print(A)
# del A
# print(A)

fruits = ['banana', 'orange', 'mango', 'lemon','orange', 'banana']
print(set(fruits))


A = {1, 2, 3, 4, 5, 5, 6, 9}
B = {3, 4, 5, 8, 9}

# A n B = > {3, 4, 5, 9}
# A U B = > {1, 2, 3, 4, 5, 6, 8, 9}
# A \ B => {1, 2, 6}
# B \ A = > {8}
# (A\B) U (B \ A) => {1, 2, 6, 8}
print(A.union(B))
print(B.union(A))
print(A.intersection(B))
print(B.intersection(A))
print(A.difference(B))
print(B.difference(A))
print(A.symmetric_difference(B))
print(A.isdisjoint(B))

# SET and List allows you to 
# Tuple, Dictionary

# It does not allow duplicate
# No ordering
# We can access item by its index
