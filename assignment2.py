
#Necessary imports
import pandas as pd
import matplotlib.pyplot as plt

# Reading data locally
df = pd.read_csv('/Users/Venkatesh Suvarna/PycharmProjects/DataMining_Assignment2/winequality-red.csv',sep=';')

#plotting boxplot
ax = df.plot(title = 'Box Plot of Various Parameters for Red Wine Dataset', kind = 'box')
ax.set_xlabel('Columns for Wine Quality Data Set')
ax.set_ylabel('Number of instances')
plt.show(ax)