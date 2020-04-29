my_list = [1,2,3,4]

print(my_list[1])

print(my_list[-1])


my_list[0] = 2
print(my_list)

my_list.append(7)
print(my_list)

my_list.extend([90])

my_list.insert(0,9)
print(my_list)
print(my_list[0:2])

del my_list[0]
del my_list[0:1]
print(my_list)


pow2 = [2 ** x for x in range(10)]
print(pow2)

odd = [x for x in range(20) if x % 2 == 1]
print(odd)