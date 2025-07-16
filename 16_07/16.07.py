#OOP
import json

# def read_file(file_name):
#     file_data = open(file_name, "r")  # Shouldn't do that
#     data = json.load(file_data)
#     file_data.close()
#     return data
#
# data1 = read_file("data1.txt")
# data2 = read_file("data2.txt")
#
# print(data1["Country"])
# print(data1["avg_temp"])
# print(data2["Country"])
# print(data2["avg_temp"])

class CountryData:

    def __init__(self, file_name):
        self.__file_name = file_name
        self.__data = self.__read_file()
        self.__country = self.__data["Country"]
        self.__avg_temp = self.__data["avg_temp"]
        self._comfort = self.__is_comfort()



    @property
    def data(self):
        return self.__data

    @property
    def country(self):
        return self.__country

    @property
    def avg_temp(self):
        return self.__avg_temp

    @property
    def comfort(self):
        return self._comfort

    @comfort.setter
    def comfort(self, value):
        self._comfort = value

    def __read_file(self):
        file_data = open(self.__file_name, "r")
        data = json.load(file_data)
        file_data.close()
        return data

    def __is_comfort(self):
        return self.__avg_temp > 25

    def __str__(self):
        return f"File {self.__file_name} with data {self.__data}"

    def __repr__(self):
        return f"File {self.__file_name} with data {self.__data}"

    def __lt__(self, other):
        return self.avg_temp < other.avg_temp

    def __le__(self, other):
        return self.avg_temp <= other.avg_temp

    def __add__(self, other):
        return [self.data, other.data]

class CountryDataWithMinTemp(CountryData):

    def __init__(self, file_name):
        super().__init__(file_name)
        self.__min_temp = self.data["min_temp"]


    @property
    def min_temp(self):
        return self.__min_temp

data1 = CountryData("data1.txt")
data2 = CountryData("data2.txt")
data3 = CountryDataWithMinTemp("data3.txt")

print(data1 < data2)
print(data1 > data2)
print(data1 <= data2)
print(data1 >= data2)
print(data1 + data2)
