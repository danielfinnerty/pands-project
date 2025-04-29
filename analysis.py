# analysis.py
# This program analyses the iris data set and outputs
# several plots which can be used for,
# investigating correlation and unique features.
# Author: Daniel Finnerty


# import required packages
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# Task 3.1

# specify filename of data source
FILENAME = "iris.data"

with open(FILENAME, "r+") as f:
    # import data from file
    data = pd.read_csv(FILENAME, header=None)
    # adding columns to data
    data.columns = [ "sepal length", "sepal width", "petal length", "petal width", "class"] 


# specify new file name
NEW_FILENAME = "summary.txt"

with open(NEW_FILENAME, "w") as n:
    # create high level overview
    stats = data.describe()
    # write data overview to new file, as a string
    n.write(stats.to_string())
    # write measurements data frame to same file as string
    n.write('\n' + '\n' + data.to_string(header=True, index=True))


# Task 3.2

# Function for creating histogram plots
def hist_plot(variables):
    for variable in variables:
        sns.histplot(data, x = variable, hue = 'class', bins = 20)
        plt.title(f'{variable} histogram plot')
        plt.savefig(f'{variable} hist.png')
        plt.close()

# Create list of variables for plotting
variables = ['sepal length', 'sepal width', 'petal length', 'petal width']

# Creat histgram plot for each variable in list
hist_plot(variables)


# Task 3.3

sns.pairplot(data, hue = 'class', diag_kind = 'hist', diag_kws = {'bins' : 20})
plt.savefig('iris pairplot.png')
plt.close()
# source for bins solution:https://stackoverflow.com/questions/59696426/how-to-change-the-number-of-bins-in-seaborns-pairplot-function


# Task  3.4
# source for regression line in pairplot: https://stackoverflow.com/questions/50722972/change-the-regression-line-colour-of-seaborns-pairplot
iris_pair_reg = sns.pairplot(data, hue='class', diag_kind = 'hist', diag_kws = {'bins' : 20}, corner=True)
#plt.show()

# single line: https://stackoverflow.com/questions/76217544/how-to-fit-regression-lines-on-each-non-diagonal-segment-of-a-pairplot-while-re
def regline(x, y, **kwargs):
    sns.regplot(data=kwargs['data'], x=x.name, y=y.name, scatter=False, color=kwargs['color'])

iris_pair_reg.map_offdiag(regline, color='red', data=data)
plt.savefig('pairplot & reg line.png')
plt.close()


# correlation coefficients
# source: https://stackoverflow.com/questions/74538936/how-to-use-pandas-dataframe-corr-with-only-a-specific-number-of-columns
correl_coeff = data.iloc[: , 0:4].corr() 

# colours source: https://matplotlib.org/stable/users/explain/colors/colormaps.html
sns.heatmap(correl_coeff, cmap = 'RdYlGn', annot = True)
plt.title('Correlation Coefficients')
# ticks source: https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.xticks.html
plt.xticks(rotation = 20)
plt.yticks(rotation = 20)
plt.savefig('correlation coeffs.png')


