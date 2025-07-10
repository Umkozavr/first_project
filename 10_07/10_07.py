# i = 0
# while i < 5:
#     print("Hi ")
#     i += 1

# while True:
#     my_input = input("Input something: ")
#     if my_input.lower() == "exit":
#         break
#     elif my_input.lower() == "skip":
#         continue
#     elif len(my_input) > 5:
#         print("Your input should be 5 symbols or less!")
#     else:
#         print("Your input is okay!")


#Print all the words with "o", then remove them and print the remaining text
# text = "Sed vitae justo malesuada, commodo libero eu, bibendum mauris"
# text = text.split()
# fin_words = []
#
#
# for i in text:
#     if "o" in i:
#         print(i)
#         continue
#     fin_words.append(i)
#
# print(" ".join(fin_words))

# a = 1
# b = 5
# c = 4
# d = 7
# y = 0
#
# main_number = 47
#
# num_list = [a, b, c, d, y]

# def sum_print(number):
#     if number == 0:
#         print(number)
#     else:
#         print(number + main_number)


# def sum_print(number):
#     if number == 0:
#         return number
#     else:
#         return number + main_number
#
# for i in num_list:
#     print(sum_print(i))

# def print_words(one, two, three, four):
#     print(f"1 — {one}, 2 — {two}, 3 — {three}, 4 — {four}")
#
# print_words("one", "two", "three", "four")

# def power(number, exponent = 2):
#     return number ** exponent
#
#
# print(power(2,4))
# print(power(7))
#
#
# def example(ij, ok, lo = 15, asd = "asd"):
#     print(ij, ok, lo, asd)
#
#
# example(1, 2, asd = "asd")


# def sum_all(*args):
#      for_sum = 0
#      for i in args:
#          for_sum += i
#      print(sum(args))
#
# sum_all(1, 4, 6, 9, 2, 4, 2)

def price_list(**kwargs):
    for title, price in kwargs.items():
        print(f"Product: {title}, price: {price}")

price_list(nokia = 700, samsung = 1500, lenovo = 850, laptop = 5000, iphone = 2000)
