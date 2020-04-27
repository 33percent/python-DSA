a = 10
print(id(a))
b = 20
print(id(b))

b = a
print(id(a) == id(b))