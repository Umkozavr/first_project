# my_list = [1, 3, 7]
# my_tuple = (2, 0, 8)
# a, b, c = my_tuple
# d, e, f = my_list
#
# print(a, b, c)
# print(d, e, f)
#
# lll = [4, 8, 2, 4, 0, 9, 7, 1, 4, 6]
#
# print(lll[1:5])
# print(lll[:3])
# print(lll[6:])
# print(lll[:])
# print(lll[1::2])
# print(lll[::-2])
#
# my_str = "Just relax and keep going"
# print(len(my_str))
# print(my_str[4:20])
# print(my_str.count("e"))
# print(my_str.find("e"))
# print(my_str.startswith("Just"))
# print(my_str.endswith("ing "))
#
# txt = "ThIs iS a FUnnY waY TO wRITe TeXt"
# print(txt.capitalize())
# print(txt.title())
# print(txt.upper())
# print(txt.lower())
#
# msg = "Hello world!"
# print(msg.replace("world","universe"))
#
# text_w_space = " text "
# print(text_w_space)
# print(text_w_space.strip())
#
# txt_quotes = '"test"'
# print(txt_quotes.strip('"'))

# my_string = "some little text"
# list_from_text = my_string.split()
# print(list_from_text)
#
# p_langs = ["Python", "Ruby", "C#"]
# print(", ".join(p_langs))

a = "one"
b = "two"

# print("First word is", a, ", second word is", b)
#
# my_text = "First word is " + a + ", second word is " + b
# print(my_text)

# my_text = "First word is %s, second word is %s"
# print(my_text % (a, b))

#string format
# my_text = "First word is {}, second word is {}"
# print(my_text.format(a, b))

# my_text = "First word is {1}, second word is {0}"
# print(my_text.format(a, b))
#
#f-string
# some_txt = f"First word is {a}, second word is {b}"
# print(some_txt)

template = "Hello, {0}"
username = input("What is your name?")
print(template.format(username))
