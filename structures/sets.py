my_set = {1,2,3}
print(my_set)
my_set = set([1, 2, 3, 2])
print(my_set)

my_set.update([2, 3, 4])

print(my_set)

A = {1, 2, 3, 4, 5}
B = {4, 5, 6, 7, 8}

print(A | B)
print(A.union(B))
print(A & B)
print(A.intersection(B))
print(A - B)
print(A.difference(B))
print(A ^ B)

As = frozenset([1, 2, 3, 4])