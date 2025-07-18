my_num = 34

# while True:
#     your_num = int(input("input your number: "))
#
#     if your_num == my_num:
#         break
#     elif your_num > my_num:
#         print("The number's smaller than you think!")
#     else:
#         print("The number's bigger than you think!")

# while (your_num := int(input("input your number: "))) != my_num:
#     if your_num > my_num:
#         print("The number's smaller than you think!")
#     else:
#         print("The number's bigger than you think!")
#
# print("Congrats!")

while True:
    user_input = input("Input something: ")
    match user_input:
        case "hello":
            print("Hi")
        case "bye":
            print("Goodbye")
            break
        case _:
            print("hello, bye?")

