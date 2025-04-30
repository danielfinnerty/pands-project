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

# open iris.data file
with open(FILENAME, "r+") as f:
    # import data from file and call it 'data'
    data = pd.read_csv(FILENAME, header=None)
    # specifying column names to 'data' file
    data.columns = [ "sepal length", "sepal width", "petal length", "petal width", "class"] 

# specify new file name
NEW_FILENAME = "summary.txt"

with open(NEW_FILENAME, "w") as n:
    # create high level overview
    stats = data.describe()
    # write overview to new file, as a string
    n.write(stats.to_string())
    # write data frame to same file as string
    n.write('\n' + '\n' + data.to_string(header=True, index=True))



# Task 3.2

# Function for creating histogram plots
def hist_plot(variables):
    for variable in variables:
        # create histogram plot for each variable
        sns.histplot(data, x = variable, hue = 'class', bins = 20)
        # add title of given variable
        plt.title(f'{variable} histogram plot')
        # save .png file of histogram
        plt.savefig(f'{variable} hist.png')
        # close function to allow next variable
        plt.close()

# Create list of variables for plotting
variables = ['sepal length', 'sepal width', 'petal length', 'petal width']

# Creat histgram plot for each variable in list
hist_plot(variables)



# Task 3.3

# create pairplot
sns.pairplot(data, hue = 'class', diag_kind = 'hist', diag_kws = {'bins' : 20})
# save pairplot as .png file
plt.savefig('iris pairplot.png')
plt.close()



# Task  3.4

# create masked pairplot
iris_pair_reg = sns.pairplot(data, hue='class', diag_kind = 'hist', diag_kws = {'bins' : 20}, corner=True)

# create a regression lines for each plot, but hiding the scatter points
def regline(x, y, **kwargs):
    sns.regplot(data=kwargs['data'], x=x.name, y=y.name, scatter=False, color=kwargs['color'])

# merge the regression lines to the pairplot
iris_pair_reg.map_offdiag(regline, color='red', data=data)
# save as .png file
plt.savefig('pairplot & regline.png')
plt.close()


# calculate correlation coefficients
correl_coeff = data.iloc[: , 0:4].corr()

# create heatmap of correlation coefficients
sns.heatmap(correl_coeff, cmap = 'RdYlGn', annot = True)
# add title
plt.title('Correlation Coefficients')
# modify ticks orientation 
plt.xticks(rotation = 20)
plt.yticks(rotation = 20)
# save as .png file
plt.savefig('correlation coeffs.png')


