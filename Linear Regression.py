#!/usr/bin/env python
# coding: utf-8

# In[1]:





# In[2]:


# write your code here
import numpy as np
import pandas as pd
import matlablib.plot as plt
import pylab as pb
from sklearn import linear_model

get_ipython().run_line_magic('matplotlib', 'inline')

get_ipython().system('wget -O FuelConsumption.csv https://s3-api.us-geo.objectstorage.softlayer.net/cf-courses-data/CognitiveClass/ML0101ENv3/labs/FuelConsumptionCo2.csv')
    
#reading the data
df = pd.read_csv("FuelConsumption.csv")
df.head()
#summarizing the data
desc = df.describe()

#selecting some features
cdf = df[['ENGINESIZE','CYLINDERS','CO2EMISSIONS','FUELCONSUMPTION_COMB']]
cdf.head(9)

#plotting each of these features

viz= cdf[['ENGINESIZE','CYLINDERS','CO2EMISSIONS','FUELCONSUMPTION_COMB']]
viz.history()
plt.show()

#plot linear regression cylinder vs emission

plt.scatter(cdf.CYLINDERS , cdf.CO2EMISSIONS , color ='red') #plotting the data values as points in red color
plt.xlabel("Cylinders") #giving the x-axis label
plt.ylabel("Emission") #giving the yiaxis label
plt.show()

#Creating train and test dataset
msk = np.random.rand(len(df)) < 0.8
train = cdf[msk]
test = cdf[tmsk]

#training the data distribution
plt.scatter(train.CYLINDERS, train.CO2EMISSIONS,  color='blue')
plt.xlabel("Cylinders")
plt.ylabel("Emission")
plt.show()

#modelling the data
regr = linear_model.LinearRegression()
train_x = np.asanyarray(train[['CYLINDERS']])
train_y = np.asanyarray(train[['CO2EMISSIONS']])
regr.fit (train_x, train_y)
# The coefficients
print ('Coefficients: ', regr.coef_)
print ('Intercept: ',regr.intercept_)

# In[ ]:




