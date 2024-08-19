#!/usr/bin/env python
# coding: utf-8

# In[13]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# In[14]:


data=pd.read_csv("E:\DataAnalysis\Electric_Vehicle_Population_data.csv")
data.info()


# In[15]:


print(data.head())


# In[27]:


city_range = data.groupby(['City'], as_index=False)['Electric Range'].sum().head(10)
sns.barplot(data=city_range, x='City',y='Electric Range' , palette="spring")
sns.set(rc={'figure.figsize':(20,5)})
plt.plot()


# In[17]:


sns.histplot(data,x="Model Year", kde="True")
plt.show()


# In[18]:


sns.scatterplot(data=data, x='Legislative District', y='Base MSRP')
plt.show()


# In[19]:


sns.countplot(data=data, x="Electric Vehicle Type")
plt.show()


# In[20]:


sns.countplot(data=data, x="Clean Alternative Fuel Vehicle (CAFV) Eligibility")
sns.set(rc={'figure.figsize':(20,5)})

plt.show()


# In[21]:


sns.countplot(data=data, x="Electric Vehicle Type", hue="Clean Alternative Fuel Vehicle (CAFV) Eligibility")
sns.set(rc={'figure.figsize':(20,5)})

plt.show()


# In[22]:


sns.violinplot(data=data, x="Electric Range")
plt.show()


# In[23]:


sns.boxplot(data=data, x="Legislative District")
plt.show()


# In[24]:


sns.relplot(data=data,x="Legislative District",y="Model Year",hue="Electric Vehicle Type")
plt.show()


# In[ ]:




