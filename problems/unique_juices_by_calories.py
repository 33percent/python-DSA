import string

no_of_friends = 3
juice_list = '3 5 4 6'
"""
first num = no of unique juices
rest = calories of all the uniq juices
a  = 21
b = 1
c = 21
d = 3
e =3
"""
available_juices = 'abcbacbabcc'
"""
assign the juice list to alphabets a through z.
these are the list of available juices.
"""
calorie_intake = 15
"""
actual calorie intake to be mixed.
"""

"""
pseudo code.
1. create a dict of all the juices with their respective names.
2. create a frequency distribution of all the juices.
3. Find the all substrings and see if the individual juice names has the less or equal
    distribution in the dict.
4. If success, exit and send output.
"""
def assign_names_to_juices(juices):
    naming_conventions = string.ascii_letters
    indi_juices = juices.split()
    juice_dict = {}
    for idx,indi in enumerate(range(0,int(indi_juices[0]))):
        juice_dict[naming_conventions[idx]] = int(indi_juices[indi])
    return juice_dict

# def get_element_count_in_array(element, overall_str):
#     count = 0
#     for indi in overall_str:
#         if indi == element:
#             count += 1
#     return count

# def get_juice_distribution(all_juices, juice_dict):
#     freq_dict = {}
#     for item in juice_dict:
#         freq_dict[item] = get_element_count_in_array(item, all_juices)
#     return freq_dict

def sorted_juice_list(juices):
    sorted_list = []
    count = len(juices)
    for i in range(0,count):
        sorted_list.append(juices[i])
    for i in range(0, count):
        for j in range(0, count):
            if sorted_list[i]<sorted_list[j]:
                temp = sorted_list[i]
                sorted_list[i] = sorted_list[j]
                sorted_list[j] = temp
    return sorted_list

def sum_of_first_two_juices(juice_list, juice_dict):
    curr_cal = 0
    for juice in juice_list:
        curr_cal += juice_dict[juice]
    return curr_cal

def calculate_mix_val(curr_string, calorie, juice_dict):
    val = 0
    for curr in curr_string:
        val += juice_dict[curr]
    if val == calorie:
        return curr_string

def mix_cocktail(juice_list,juice_dict, calorie):
    length = len(juice_list)
    for start in range(1,length+1):
        for end in range(length - start + 1):
            temp = end + start - 1
            curr_string = []
            for k in range(end, temp+1):
                curr_string.append(juice_list[k])
            current = calculate_mix_val(curr_string, calorie, juice_dict)
            if current:
                return ''.join(current)

juice_dict = assign_names_to_juices(juice_list)
# juice_dist = get_juice_distribution(available_juices,juice_dict)
sorted_juice_list = sorted_juice_list(available_juices)

sum_of_first_two = sum_of_first_two_juices(sorted_juice_list[:2], juice_dict)
if sum_of_first_two >= calorie_intake:
    print('Sorry you Just have Water')
else:
    curr_cocktail = mix_cocktail(
        juice_list = sorted_juice_list,
        juice_dict = juice_dict,
        calorie = calorie_intake,
    )
    if curr_cocktail:
        print('Moctail combination is {}'.format(curr_cocktail))
    else:
        print('no cocktail for u')