#coding:utf-8
import csv
my_file = 'data_csv.csv'
with open(my_file) as fp:
    f_csv = csv.reader(fp)
    for row in f_csv:
        print(row)