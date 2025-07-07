# text = 'Something'
# print('s' in text)
# print('S' in text)
#
# x = 256
# y = 256
# print(x is y)
#
# x += 1
# y += 1
# print(x is y)
# print(id(x), id(y))
#
# user_name = input('What is your name?')
# print('Hello', user_name)
from itertools import count

# user_input = input('input something')
# print(type(int(user_input)))

#Initialize list

# a = [1,2,3, "test", False, 23.43, "98"]
# print(type(a))

# for i in a:
#     print(type(i))

# print(a[0])
# print(a[-1])
# a.append(9)
# print(a)

my_tuple = (1, 2, 3, None, 5, -5, 'sas',5, False)
# print(my_tuple)
# print(my_tuple.count(5))
# print(my_tuple[4])
my_set = {}
dummy = []

print(my_tuple[-1])

for i in my_tuple:
    dummy.append(i)

print(set(dummy))