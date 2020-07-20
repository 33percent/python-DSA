import keyword

print(keyword.kwlist)

a = 10

print(id(a))


q,w,e = 1,2,3

r,t,_,_ = 1,2,3,6

print(_)

p = i = u = 678
print(p)

h = j = k = 10
j = 20
print(h,j,k)

x = y = z = [1,2,3]
x[1] = 100
print(x,y,z)


tyu = 100
hfgj = tyu
hfgj = 99
print(tyu, hfgj)

print(issubclass(bool, int))
print(isinstance(True, bool)) # True


a = reversed('hello')
print(a)

tuple_ax = (1,2,3)
tuple_bx = (1,2,3)
print(id(tuple_ax) == id(tuple_bx))
print(tuple_ax.__hash__() == tuple_bx.__hash__())

from collections import defaultdict

state_capitals = defaultdict(lambda: 'Boston')

state_capitals['Arkansas'] = 'Little Rock'
state_capitals['California'] = 'Sacramento'
state_capitals['Colorado'] = 'Denver'
state_capitals['Georgia'] = 'Atlanta'

print(state_capitals['delhi'])

# name = input("What is your name? ")
# print(name)
print(dir())
print(dir(__builtins__))

# help(max)

import math
print(math.__doc__)

class Represent(object):
    def __init__(self, x, y):
        self.x, self.y = x, y
    def __repr__(self):
        return "Represent(x={},y=\"{}\")".format(self.x, self.y)
    def __str__(self):
        return "Representing x as {} and y as {}".format(self.x, self.y)

r = Represent(1, "Hopper")

print(r.__repr__)

if __name__ == '__main__':
    print('called as  main file')