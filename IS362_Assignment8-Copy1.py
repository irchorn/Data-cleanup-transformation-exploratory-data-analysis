#!/usr/bin/env python
# coding: utf-8

# # IS211_Assignment8

# In[95]:



import numpy as np


# <b>Load data into a pandas DataFrame</b>

# In[96]:


import pandas as pd
filename = "auto-mpg.data"
column_names = ['mpg', 'cylinders', 'displacement', 'horsepower', 'weight', 'acceleration', 'model_year', 'origin', 'car_name']
df = pd.read_csv(filename, delim_whitespace=True, names=column_names)
df.head(10)


# <b>Replace '?' with 'NaN' and convert column to numeric</b>

# In[75]:


df.sort_values('horsepower', ascending = False)


# In[97]:


df['horsepower'] = df['horsepower'].replace(['?'],'NaN')


# In[98]:


df.sort_values('horsepower')


# In[99]:


print(df.dtypes)


# In[100]:


df['horsepower'] = df['horsepower'].astype(float)


# <b>Convert 'origin' values to ‘USA’, ‘Asia’, and ‘Europe’</b>

# In[101]:


df['origin'] = df['origin'].apply(str)


# In[102]:


df['origin'] = df['origin'].replace(['1','2', '3'],['USA','Asia', 'Europe'])


# In[103]:


df


# <b>Create a bar chart that shows the distribution for cylinders.</b>

# In[104]:


import matplotlib.pyplot as plt
import seaborn as sns
get_ipython().run_line_magic('matplotlib', 'inline')


# In[105]:


from collections import Counter


# In[106]:


sns.distplot(df['cylinders'])


# In[107]:


sns.histplot(df['cylinders'])


# <b>Create a scatterplot that shows the relationship between horsepower and weight.</b>

# In[114]:


var = 'weight'
plot = sns.lmplot(var,'horsepower',df)
plot.set(ylim = (0,150))


# In[113]:


var = 'weight'
plot = sns.lmplot(var,'horsepower',df, hue='origin')
plot.set(ylim = (0,150))


# In[ ]:




