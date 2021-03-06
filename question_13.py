# 13. Write a function to write a comma-separated value (CSV) file. It
# should accept a filename and a list of tuples as parameters. The
# tuples should have a name, address, and age. The file should create
# a header row followed by a row for each tuple. If the following list of
# tuples was passed in:
# [('George', '4312 Abbey Road', 22), ('John', '54 Love Ave',
# 21)] it should write the following in the file:
# name,address,age
# George,4312 Abbey Road,22
# John,54 Love Ave,21

import csv

def write_csv(file_name,list_tuple):
    with open(file_name, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["name","address","age"])
        for x in list_tuple:
            writer.writerow(x)
list_tuple=[('George', '4312 Abbey Road', 22), ('John', '54 Love Ave',21)]

write_csv("sample.csv",list_tuple)
