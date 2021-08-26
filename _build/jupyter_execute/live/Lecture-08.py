#!/usr/bin/env python
# coding: utf-8

# # Modules for data: pandas
# 
# Here we will use the mcd-menu.csv file, which you can download here:
# 
# [mcd-menu.csv](https://raw.githubusercontent.com/UCSD-CSS-001/ucsd-css-001.github.io/main/live/mcd-menu.csv)
# 

# ## Wherefore modules?
# 
# [pypi.org](pypi.org) has 324k packages.  From web servers, to machine learning frameworks, to video games, to bitcoin wallets, to recipe managers, to astronomy databases, etc.
# 
# There are millions of different classes, functions, constants, in these packages.
# 
# 1. we can't load them all in memory
# 
# 2. we can't ask someone writing the next python MIDI music library to check all other previous libraries to make sure no one has used the class names they have in mind.
# 
# Modules create namespaces, and modules manage what is loaded into memory.

# In[1]:


import math


# In[2]:


math.log(4)


# ### What's a module?

# In[3]:


import edsmodule


# In[4]:


dir(edsmodule)


# In[5]:


edsmodule.bigstring


# In[6]:


edsmodule.gigantify(4)


# In[7]:


obj = edsmodule.TestClass(3)


# In[8]:


type(obj)


# In[9]:


import edsmodule as ed


# In[10]:


ed.bigstring


# In[11]:


from edsmodule import bigstring


# In[12]:


bigstring


# In[13]:


from edsmodule import bigstring as bs


# In[14]:


bs


# ## Importing approaches

# In[15]:


import numpy as np
import pandas as pd


# ## Tabular data and DataFrame

# In[16]:


import pandas as pd


# ### Why tabular data

# In[17]:


names = ['alice', 'bob', 'carol', 'david']
heights = [68, 70, 65, 72]
weight = [130, 150, 170, 180]


# In[18]:


bmi = []
for i in range(len(heights)):
    bmi.append(703 * weight[i] / heights[i]**2) #
    


# In[19]:


big_bmi_people = []
for i in range(len(heights)):
    if bmi[i] > 24:
        big_bmi_people.append(names[i])


# In[20]:


big_bmi_people


# In[21]:


people = []
for n,h,w in zip(names, heights, weight):
    people.append({'name':n, 'height':h, 'weight':w})


# In[22]:


for person in people:
    if (703*person['weight']/person['height']**2) > 24:
        print(person)


# In[ ]:





# In[23]:


df = pd.DataFrame({'name':names, 
                   'height':heights, 
                   'weight': weight})


# In[24]:


df


# ## What is a Data Frame?
# 
# ### Foundational data structures
# 
# #### numpy arrays
# 
# differences from lists?  single type.  supports elementwise operations.  handy built in functions.

# In[25]:


import numpy as np

x = [1, 2, 3, 4, 5]
x_array = np.array(x)


# In[26]:


x_array


# In[27]:


# generate a new list: y = x**2
y = []
for item in x:
    y.append(item**2)
y


# In[28]:


y_array = x_array ** 2
y_array


# In[29]:


h = np.array(heights)
w = np.array(weight)


# In[30]:


bmi = 703 * w / h**2
bmi


# In[31]:


pronoun = np.array(['he', 'she', 'ze', 'fe'])


# In[32]:


pronoun == 'he'


# In[33]:


['he', 'she', 'ze', 'fe'] == 'he'


# In[34]:


h.prod()


# #### pandas series
# 
# kinda like an array, kinda like a dictionary.  .values and .index.  We use it mostly like an array.

# In[35]:


print(heights, names)


# In[36]:


h = pd.Series(heights, index = names)


# In[37]:


h


# In[38]:


h ** 2


# In[39]:


h.iloc[3]


# In[40]:


h + 100


# #### pandas dataframe
# 
# kinda like a 2d array / matrix, kinda like a dictionary of column-series, kinda like a dictionary of row-series

# In[41]:


df = pd.DataFrame({'name': names, 'height': heights, 'weight':weight})


# In[42]:


df['name'][2:]


# ## csv and read_csv()

# In[43]:


mcd = pd.read_csv('mcd-menu.csv')


# In[44]:


mcd


# ## DataFrame operations
# 
# ### describe this thing to me

# In[45]:


mcd.shape


# In[46]:


list(mcd.columns)


# ### head and tail

# In[47]:


mcd.tail(3)


# ### selecting columns

# In[48]:


mcd['Calories']


# In[49]:


mcd[['Calories', 'Saturated Fat']]


# ### selecting rows by position

# In[50]:


mcd.iloc[0:2]


# ### selecting cells

# In[51]:


mcd


# In[52]:


mcd['Calories'].iloc[0]


# In[53]:


mcd['Calories'][0]


# In[54]:


mcd = mcd.sort_values('Calories')


# In[55]:


mcd['Item'].iloc[0]


# In[56]:


mcd


# ### filtering rows via logical indexing

# In[57]:


mcd[ mcd['Calories'] >= 1000 ]


# In[58]:


mcd[ mcd['Category'] == 'Breakfast' ]


# In[59]:


mcd[ mcd['Category'] == 'Breakfast' ][ mcd['Calories'] > 300][ mcd['Calories'] < 500]


# In[60]:


mcd[ (mcd['Category'] == 'Breakfast') & 
  (mcd['Calories'] > 300) & 
  (mcd['Calories'] < 500) ]


# In[61]:


(mcd['Category'] == 'Breakfast') & (mcd['Calories'] > 300)


# In[62]:


(mcd['Category'] == 'Breakfast') & (mcd['Calories'] > 300)


# In[63]:


mcd [ (mcd['Category'] == 'Breakfast') | (mcd['Calories'] > 300) ]


# - logical indexing.
# - make conjunctions by combining arrays of logical values with &
# - make disjunctions with |
# - and we need to put comparison operations in () before combing

# **.isin()**

# In[64]:


mcd['Category'].isin(['Beverages', 'Breakfast'])


# In[65]:


(mcd['Category'] == 'Beverages') | (mcd['Category'] == 'Breakfast')


# **pd.isna()**

# In[66]:


mcd.iloc[4,3] = np.NaN


# In[67]:


mcd [ mcd['Calories'].isna() ] 


# ### indexes, loc and iloc
# 
# ### make a new column

# In[68]:


mcd['Hello'] = 'hi'


# In[69]:


mcd['PF'] = mcd['Protein'] + mcd['Dietary Fiber']


# In[70]:


mcd


# ### sort_values

# In[71]:


mcd = mcd.sort_values('PF')


# In[72]:


mcd.sort_values('PF', ascending = False)


# In[73]:


# we want the 3 items highest in 'Total Fat'
mcd.sort_values('Total Fat')[-3:]


# In[74]:


mcd.sort_values('Total Fat').tail(3)


# In[75]:


mcd.sort_values('Total Fat').iloc[-3:]


# In[76]:


mcd.sort_values('Total Fat', ascending = False).head(3)


# In[77]:


mcd.sort_values('Total Fat', ascending = False).head(1)


# In[78]:


mcd.sort_values('Total Fat', ascending = False).iloc[0]


# In[79]:


mcd.sort_values('Total Fat', ascending = False)[0]


# ### groupby

# In[80]:


for category in mcd['Category'].unique():
    print(category, 
          'mean calories:', 
          mcd[mcd['Category']  == category]['Calories'].mean())


# In[81]:


mcd.groupby('Category').head(1)


# ### aggregate

# In[82]:


# find the average # of calories per item in category
mcd.groupby('Category').aggregate(m_calories = ('Calories', 'mean'))


# In[83]:



mcd.groupby('Category').aggregate(m_calories = ('Calories', 'mean')).reset_index()


# In[84]:


( mcd
    .groupby('Category')
    .aggregate(m_calories = ('Calories', 'mean'))
    .reset_index() )


# In[85]:


mcd_grp = mcd.groupby('Category')
mcd_agg = mcd_grp.aggregate(m_calories = ('Calories', 'mean'))


# In[86]:


mcd_summary = mcd_agg.reset_index()
mcd_summary


# In[87]:


mcd.aggregate(mean_calories = ('Calories', 'mean'))


# In[88]:


mcd['Calories'].mean()


# ### chaining operations
# 
# ## tasks
# 
# ### Find the breakfast menu item with the fewest calories
# 
# 

# In[89]:


mcd[ mcd['Category'] == 'Breakfast'].sort_values('Calories').head(1)


# In[90]:


mcd[ mcd['Category'] == 'Breakfast'].sort_values('Calories').head(1)


# ### Find the highest vul_index food
# 
# vul_index = 10*(protein grams + fiber grams)/calories

# In[91]:


mcd['vul-index'] = 10*(mcd['Protein'] + mcd['Dietary Fiber'])/mcd['Calories']


# In[92]:


(mcd [ ~ mcd['vul-index'].isna() & ~np.isinf(mcd['vul-index'])]
 .sort_values('vul-index', ascending=False) )


# In[93]:


(mcd[mcd['Calories'] > 0]
.sort_values('vul-index', ascending = False)
.head(1))


# In[ ]:





# ### calculate mean, max calories, and n for each category
# 
# 
# 
# 
# ### pull out max calorie item for each category

# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




