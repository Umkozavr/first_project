# def test():
#     print("test")
#
# test()
# print(test)
# new_test = test
# print(new_test)
# new_test()

# def greet():
#
#     def hello():
#         return "hello"
#
#     return hello()
#
# print(greet())

# def outer():
#
#     def inner():
#         result = 2 + 5
#         return result
#     return inner
#
# print(outer()())
# inner_function = outer()
# print(inner_function())

# def func1(give_me_a_func):
#     print("before")
#     give_me_a_func( )
#     print("after")

# def simple1():
#     print("simple 1")
#
# def simple2():
#     print("simple 2")

# func1(simple1)
# func1(simple2)

# def add_text(func):
#
#     def wrapper():
#         print("before")
#         func()
#         print("after")
#     return wrapper
#
# def simple1():
#     print("simple 1")
#
# @add_text
# def simple2():
#     print("simple 2")

# simple1 = add_text(simple1)
# simple1()
#
# simple2() #add_text(simple2)()

# def add_logs(func):
#
#     def wrapper():
#         print(f"Function {func.__name__} has started")
#         result = func()
#         print(f"Function {func.__name__} has finished")
#         return result
#
#
#     return wrapper
#
#
# @add_logs
# def simple1():
#     print("simple 1")
#
# @add_logs
# def simple2():
#     print("simple 2")
#     print("simple 2")
#
# @add_logs
# def print_nothing():
#     return "nothing"
#
#
# simple1()
# simple2()
#
# print(print_nothing())

# def add_logs(func):
#
#     def wrapper(*args):
#         print(f"Function {func.__name__} has started")
#         result = func(*args)
#         print(f"Function {func.__name__} has finished")
#         return result
#
#
#     return wrapper
#
# @add_logs
# def calc(x):
#     return x * 2
#
# @add_logs
# def simple1():
#     print("simple 1")
#
# @add_logs
# def calc2(x, y):
#     return x * y
#
# print(calc(2))
# print(calc2(3, 4))
# simple1()

#List comprehension

# my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# new_list = map(lambda x: x * 2, my_list)
#
# print(*new_list)

# new_list = [x * 2 for x in my_list]
# print(new_list)

# new_list = [x for x in my_list if x % 2 == 0]
# print(new_list)
#
# new_tuple = tuple(x for x in my_list if x % 2 == 0)
# print(new_tuple)

# new_dict = {}
#
# for x in my_list:
#     new_dict[x] = x * 3
#
# print(new_dict)

# new_dict = {x: x * 3 for x in my_list}

# print(new_dict)

# data = [("one", "two"), ("three", "four")]

# new_dict = {x : y for x, y in data}
# print(new_dict)

# for key, value in data:
#     new_dict[key] = value
#     print(new_dict)

# new_dict = dict(data)
# print(new_dict)

countries = ["USA", "Cuba", "England", "Iceland"]
temps = [23, 33, 35, -1]

new_dict = dict(zip(countries, temps))
print(new_dict)
