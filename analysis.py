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

def hist_plot(variables):
    for variable in variables:
        #(f'data_{variable}') = data[['{variable}','class']]
        #print (f'data_{variable}')
        sns.histplot(data, x = variable, hue = 'class', bins = 20)
        plt.title(f'{variable} histogram plot')
        plt.savefig(f'{variable} hist.png')
        plt.close()

variables = ['sepal length', 'sepal width', 'petal length', 'petal width']
hist_plot(variables)

sns.pairplot(data, hue = 'class', diag_kind = 'hist', diag_kws = {'bins' : 20}) # https://seaborn.pydata.org/generated/seaborn.pairplot.html, https://builtin.com/articles/seaborn-pairplot
plt.show()

# source for bins solution:https://stackoverflow.com/questions/59696426/how-to-change-the-number-of-bins-in-seaborns-pairplot-function