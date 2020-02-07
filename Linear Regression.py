#!/usr/bin/env python
# coding: utf-8

# In[1]:





# In[2]:


# write your code here
import numpy as np
import pandas as pd
import matlablib.plot as plt
import pylab as pb
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




# In[ ]:




