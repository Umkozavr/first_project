# from Folder.helper import assist as assist1
# from random import random, randint, randrange
# from Folder.help2 import assist as assist2
# from Folder.help2 import very_useful_function_for_your_easy_life as useful

# def generate_text(text1, text2):
#     return f'Text consist of the words: {text1} and {text2}'
#
# print(generate_text("word", "wall"))


# my_list = [1, 2, 5, 7, 4, 9]
#
# for x in my_list:
#     print(x)


# def gen_progression(limit=100):
#     n = 2
#     num = 1
#     count = 1
#     while count < limit:
#         yield num
#         num += n
#         count += 1

#print(list(gen_progression(10)))
# for number in gen_progression(10):
#     print(number)
# count = 1
# for number in gen_progression(100000000000000000000):
#     if count == 1000000:
#         print(number)
#         break
#     count += 1


# print(randint(0, 1))
# print(randrange(0, 10, 2))

# users = ['user1', 'user2', 'user3']
# print(random.choice(users))
# print(sys.platform)

# assist1()
# assist2()
#
# useful()

# summer = True
#
# if summer:
#     print("The weather is fine")
# else:
#     print("The weather isn't fine")

# numbers = [2, 24, 95, 92, 4, 67, 8]
# print(max(numbers))



# my_list = [1, 2, 3, 4, 5]
#
# def mult_by_2(x):
#     return x * 2
#
# new_list = map(mult_by_2, my_list)
# print(list(new_list))

# my_list = [1, 2, 3, 4, 5]
#
# new_list = map(lambda  x: x*2, my_list)
# print(list(new_list))

# code, number = map(int,input("code and number: ").split())
#
# print(f"code is {code}, number is {number}")

my_list = [10, 23, 6, 9, 15]

# def mult_by_2(x):
#     if x > 10:
#         return x * 2
#     else:
#         return x * 3
#
# new_list = map(lambda x: x * 2 if x > 10 else x * 3, my_list)
# # print(list(new_list))
#
# my_list2 = [1, 2, 3, 4, 5, 6, 7, 8]
#
# def is_even(x):
#     return x % 2 == 0
#
# new_list2 = filter(is_even, my_list2)
#
# print(list(new_list2))
#
# new_list2 = filter(lambda x: x % 2 == 0, my_list2)
#
# print(list(new_list2))

import datetime

# time_now = datetime.datetime.now()
#
# print(time_now.hour)
# print(time_now.weekday())
# print(time_now.isoweekday())
# print(time_now.timestamp())

# simple_date = datetime.datetime(1970, 1, 12)
# print(simple_date)
# print(simple_date.timestamp())

my_time = "2025/07/11 13 hours, 30 mins, 25 secs"

python_date = datetime.datetime.strptime(my_time,"%Y/%m/%d %H hours, %M mins, %S secs")

print(python_date)
print(python_date.isoweekday())
print(python_date.hour)

human_date = python_date.strftime("Year: %y Month: %B Day: %d")

print(human_date)
