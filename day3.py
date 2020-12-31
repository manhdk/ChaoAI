import csv
import numpy
from numpy import genfromtxt
from pandas import read_csv

csv_path ='samedata/data.csv'

# using the function
with open(csv_path, 'rt', encoding="utf8") as csvfile:
    read_csv = csv.reader(csvfile, delimiter=',')
    for row in read_csv:
        print(row)

# Load csv using NumPy
read_csv = genfromtxt(csv_path, delimiter=',')
print(read_csv)

# Load CSV using Pandas
csv_path ='samedata/data.csv'
names = numpy.array(['preg','plas','pres','skin','test','mass','pedi','age','class'])
data = read_csv(csv_path, names=names)
print(data.shape)

# View first 20 rows
import pandas
names = ['preg', 'plas', 'pres', 'skin', 'test', 'mass', 'pedi', 'age', 'class']
data = pandas.read_csv(csv_path, names=names)
peek = data.head(10)
print(peek)

import pandas
names = ['preg', 'plas', 'pres', 'skin', 'test', 'mass', 'pedi', 'age', 'class']
data = pandas.read_csv(csv_path, names=names)
pandas.set_option('display.width', 100)
pandas.set_option('precision', 3)
description = data.describe()
print(description)
