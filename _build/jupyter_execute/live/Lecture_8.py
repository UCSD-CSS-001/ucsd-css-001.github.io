#!/usr/bin/env python
# coding: utf-8

# # Modules
# 
# `import` `from` `as`
# 
# statistics

# In[1]:


from math import log


# In[2]:


from math import isclose


# In[3]:


from string import punctuation


# In[4]:


import math


# In[5]:


import math as ma


# In[6]:


from random import randint


# # Pandas
# 
# Will use this data: 
# [https://raw.githubusercontent.com/UCSD-CSS-001/ucsd-css-001.github.io/main/live/mcd-menu.csv](https://raw.githubusercontent.com/UCSD-CSS-001/ucsd-css-001.github.io/main/live/mcd-menu.csv)
# 
# - import as pd

# In[7]:


import pandas as pd


# ## Tabular data and DataFrame
# 
# why tabular data?

# In[8]:


names = ['alice', 'bob', 'carol', 'david']
heights = [68, 70, 65, 72]
weight = [130, 150, 170, 180]


# how to make a dataframe from lists

# In[9]:


df = pd.DataFrame({'name':names, 'height':heights, 'weight': weight})


# In[10]:


df


# dataframe.shape

# In[11]:


df.shape


# dataframe.head()  .tail()  .columns

# In[12]:


df.columns


# How to pull out a column.

# In[13]:


h = df['height']


# A dataframe column is a "series".  Looks like a list, but default indexing more like a dictionary.

# In[14]:


h[0]


# index  `.set_index` and `.reset_index`

# In[15]:


df


# How to pull out rows.  (.loc, .iloc)

# In[16]:


df.iloc[0]


# Several ways to get a particular 'cell':
# - get column, then get item in column
# - .loc() index based reference
# - .iloc() integer index based reference

# In[17]:


df['weight'][2]  # pull out the column, and then the row from that column


# In[18]:


df.iloc[2]['weight']  # pull out a row, and then the column from that row.


# ## csv, and read_csv()
# 
# - why csv?

# In[19]:


mcd = pd.read_csv('mcd-menu.csv')


# In[20]:


mcd


# ## logical indexing

# In[21]:


mcd[mcd['Category']=='Salads']


# In[22]:


mcd[(mcd['Category']=='Breakfast') & (mcd['Calories']>1000)]


# In[23]:


mcd[((mcd['Category'] == 'Breakfast') | (mcd['Category'] == 'Smoothies & Shakes')) & (mcd['Calories']>600)]


# In[24]:


mcd[mcd['Category'].isin(['Breakfast', 'Smoothies & Shakes', 'Beverages']) & (mcd['Calories']>600)]


# In[25]:


mcd['Category'].value_counts()


# .isin() method
# 
# pd.isna()
# 
# ## chaining

# In[26]:


max(mcd['Calories'])


# In[27]:


mcd[mcd['Calories'] == 1880]


# In[28]:


mcd.sort_values('Calories').tail(1)


# In[29]:


mcd.sort_values('Calories', ascending=False).head(1)


# ## groupby

# In[30]:


mcd.groupby('Category').head(1)


# ## agg to summarize

# In[31]:


mcd.groupby('Category').aggregate("mean")


# In[32]:


mcd.groupby('Category').aggregate(mean_calories = ('Calories', "mean"))


# In[33]:


mcd.groupby('Category').aggregate(mean_calories = ('Calories', "mean")).sort_values('mean_calories').tail(1)


# In[34]:


mcd['Calories'].mean()


# ## sorting
# 
# .sort_values()
# 
# ## make a new column

# In[35]:


mcd[['Category', 'Item', 'Calories', 'Total Fat', 'Carbohydrates', 'Protein']]


# In[36]:


mcd['Calories from Carbohydrates'] = mcd['Carbohydrates']*4
mcd['Calories from Protein'] = mcd['Protein']*4
mcd['Calories from Fat'] = mcd['Total Fat']*9


# In[37]:


mcd['Predicted Calories'] = mcd['Calories from Carbohydrates'] + mcd['Calories from Protein'] + mcd['Calories from Fat']


# In[38]:


mcd['Error'] = mcd['Calories'] - mcd['Predicted Calories']


# In[39]:


mcd['Error'].mean()


# In[40]:


mcd['New Value'] = 10


# In[41]:


mcd


# # Tasks
# 
# - find the Breakfast with the least calories

# In[42]:


# select just the breakfast
#   logical indexing.

# sort by calories
# take the first one
mcd[ mcd['Category']=='Breakfast' ].sort_values('Calories').head(1)


# In[ ]:





# - calculate 'vul' index, and find highest vul_index food (after filtering out nonsense)
# 
# ratio of vul_index = (protein + fiber) / calories

# In[43]:


mcd['vul'] = (mcd['Protein']+mcd['Dietary Fiber'])/mcd['Calories']


# In[44]:


mcd[['Category', 'Item', 'Calories', 'Protein', 'Dietary Fiber', 'vul']].sort_values('vul', ascending=False)


# In[45]:


mcd[(mcd['vul'] < 1) & (~pd.isna(mcd['vul']))].sort_values('vul', ascending=False).head(1)


# In[46]:


mcd.columns


# - calculate mean, max calories, and n for each category
# 

# In[47]:


(mcd
 .groupby('Category')
 .aggregate(mean_calories = ("Calories", "mean"), 
            max_calories = ("Calories", "max"), 
            n = ("Calories", "count")))


# - pull out max calorie item for each category 

# In[48]:


mcd.sort_values('Calories', ascending = False).groupby('Category').head(1)

