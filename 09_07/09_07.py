# i = input("Input the number: ")
# if i.isnumeric():
#     i = int(i)
#     if i == 1:
#         print("The answer is 1")
#     elif i == 2:
#         print("The answer is 2")
#     else:
#         print("The answer is a lot")
# else:
#     print("Wrong input")

# names = ["Jill", "Matt", "Alex", "Bogdan", "Lisa", "Vicky", "Umka"]
# for i in names:
#     print(i)

# names = ["Joe", "Matt", "Alex", "Jack", "Bogdan", "Lisa", "John",
#          "Vicky", "Umka", "Moe", "Mercy"]
# for name in names:
#     if name.startswith('J'):
#         print("Mr.", end=" ")
#     print(name)


# people = {"Vicky" : 165, "Naum" : 190, "Mary" : 178, "Alex" : 185}
# for person in people:
#     print(f"{person} : {people[person]}")

# people = {"Vicky" : 165, "Naum" : 190, "Mary" : 178, "Alex" : 185}
# for name, height in people.items():
#     print(f"{name} : {height}")


#Print all the words with "o", then remove them and print the remaining text
text = "Sed vitae justo malesuada, commodo libero eu, bibendum mauris"
text = text.split()
fin_words = []


for i in text:
    if "o" in i:
        print(i)
    else:
        fin_words.append(i)

print(" ".join(fin_words))


