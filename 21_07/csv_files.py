import csv

with open("my_csv.csv", "r", newline="", encoding="utf-8-sig'") as my_csv:
    my_reader = csv.DictReader(my_csv)
    data = []
    for row in my_reader:
        data.append(row)

for row in data:
    print(row)