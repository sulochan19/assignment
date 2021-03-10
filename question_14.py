# 4. Write a function that reads a CSV file. It should return a list of
# dictionaries, using the first row as key names, and each subsequent
# row as values for those keys.
# For the data in the previous example it would return:
# [{'name': 'George', 'address': '4312 Abbey Road', 'age': 22}, {'name':
# 'John', 'address': '54 Love Ave', 'age': 21}]


import csv

def read_csv(file_name):
    with open(file_name, 'r', newline='') as file:
        csvreader = csv.DictReader(file)
        dict_list=[]
        for row in csvreader:
            list=dict(row)
            dict_list.append(list)
        print(dict_list)
read_csv("sample.csv")