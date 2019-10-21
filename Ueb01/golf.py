import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv("golf.csv",error_bad_lines=False)

#check datatypes after read in
print(df.dtypes)
#checking for right headings
print(df.columns)

#Generate descriptive statistics that summarize the central tendency, 
#dispersion and shape of a dataset’s distribution, excluding NaN values.
#quoted from pandas dataframe library
print(df.describe())

#Get the mode(s) of each element along the selected axis.
#The mode of a set of values is the value that appears most often. It can be multiple values.
#quoted from pandas dataframe library
print(df.mode())

#prints the first 5 rows of the dataset
print(df.head())


#creates a boxplot for the named columns
#pandas dataframe library
df.boxplot(["Temperature", "Humidity"])
plt.savefig('boxplottemphum.png')

#creates a scatter plot for the named columns
#pandas dataframe library
df.plot.scatter("Temperature", "Humidity")
plt.savefig('corrtemphum.png')

#creates a boxplot for all numeric dataframe columns
#pandas dataframe library
df.plot.box()
plt.savefig('boxplotall.png')

#draws a histogram for all numeric dataframe columns
df.plot.hist()
plt.savefig('histogram.png')

#standardization of the temperature values
df['TemperatureN2']= (df['Temperature']-df['Temperature'].mean())/df['Temperature'].std()

#returns the correlation of both datasets
#we got a positive linear correlation(corrcoef = 1)
print(np.corrcoef(df['Temperature'], df['TemperatureN2']))


df.plot.scatter("Temperature", "TemperatureN2")
plt.savefig('corrtemp.png')

plt.show()