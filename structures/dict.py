#create dic
my_dict = {
    'name':'pawan',
    'age':56
}

#update dict
my_dict['age'] = 57
my_dict['last_name'] = 'Kalyan'


#fetch value in dict
print(my_dict['age'])
print(my_dict.get('first_name'))

#removing an element
my_dict.pop('age')
print(my_dict)
my_dict['age'] = 57


print(my_dict.items())
print(my_dict.keys())
print(my_dict.values())

#Python Dictionary Comprehension
squares = { x:x for x in range(6)}
print(squares)

cubes = { x:x*x*x for x in range(11) if x%3 == 0}
print(cubes)

print('marriage' in my_dict)

for i in my_dict:
    print('{} ---> {}'.format(i, my_dict[i]))