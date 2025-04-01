# analysis.py
# This program analyses the iris data set and outputs
# several plots which can be used for invsetigating
# correlation and unique features
# Author: Daniel Finnerty

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

FILENAME = "iris.data"

with open(FILENAME, "r+") as f:
    # import data from file
    # source: https://www.datacamp.com/tutorial/pandas-read-csv
    data = pd.read_csv(FILENAME, header=None)
    # adding columns to data
    # source: https://www.geeksforgeeks.org/add-column-names-to-dataframe-in-pandas/
    data.columns = [ "sepal length", "sepal width", "petal length", "petal width", "class"] 

NEW_FILENAME = "summary.txt"

with open(NEW_FILENAME, "w") as n:
    # create high level overview
    stats = data.describe()
    n.write(stats.to_string())
    # write data to file as a string
    # source: https://www.geeksforgeeks.org/python-pandas-dataframe-to_string/
    n.write('\n' + '\n' + data.to_string(header=True, index=True))
    
# create histograms of each variable
#data_sepal_l = data[['sepal length','class']]
#print(data_sepal_l)
#sns.histplot(data, x = 'sepal length', hue = 'class')
#plt.show()

data_sepal_l = data[['sepal length']]
plt.hist(data_sepal_l, bins = 9)
plt.show()