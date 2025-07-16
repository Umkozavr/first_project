import os

base_path = os.path.dirname(__file__)
file_path = os.path.join(base_path, "data.txt") #Correct slash, depending on OS
new_file_path = os.path.join(base_path, "data_change.txt")
#
# print(file_path)
#
# #CONTEXT MANAGER
# def read_file():
#     with open(file_path, "r") as data_file: #file is guaranteed to close
#         for line in data_file.readlines():
#             yield line
#
# for data_line in read_file():
#     with open(new_file_path, "a") as new_file:
#         data_line = data_line.replace(".", "").replace(",","")
#         new_file.write(data_line)

project_path = os.path.dirname(base_path)                                  #1 LEVEL UP
#project_path = project_path = os.path.dirname(os.path.dirname(base_path)) #2 LEVELS UP
test_file_path = os.path.join(project_path, "test.txt")


print(project_path)

with open(test_file_path, "r") as test_file:
    print(test_file.read())


