#!/usr/bin/env python
# coding: utf-8

# # P07: Pandas Series and DataFrames

# ## Quick review of modules
# 
# [pypi.org](pypi.org) has 324k packages.  From web servers, to machine learning frameworks, to video games, to bitcoin wallets, to recipe managers, to astronomy databases, etc.
# 
# There are millions of different classes, functions, constants, in these packages.
# 
# 1. we can't load them all in memory
# 
# 2. we can't ask someone writing the next python library to do X to check all other previous libraries to make sure no one has used the class names they have in mind.
# 
# Modules create namespaces, and modules manage what is loaded into memory.

# In[1]:


# import numpy as np, then use np.method to interface with methods
import numpy as np


# In[2]:


np.mean([9,4,5])


# In[3]:


# import certain functions from a module
from statistics import stdev


# In[4]:


stdev([9,4,5])


# ## Import Pandas!
# 
# * DataFrames are an excellent choice if you're dealing with mixed data types
# * Think of them as excel spreadsheets - can have columns of numbers, strings, etc
# * Powerful built in methods for summarizing and analyzing data
# * Powerful built in methods for cleaning data (removing outliers, missing values, and so forth)
# * When importing pandas, always use `pd` unless you have a good reason to do otherwise

# ### Pandas Series
# 
# [Pandas quick start guide for Series](https://pandas.pydata.org/pandas-docs/stable/dsintro.html#series)
# 
# * A **Series** is a 1D array that can hold any type of data (numeric types, non-numeric, Python objects and so forth). Think excel spreadsheet with one column. 
# * Each entry is **labeled** with an index that is used to keep track of what each entry is, and the label can be used to lookup the value corresponding to each index during analysis (remember keys in dictionaries? similar idea)
# * These labels are fixed - they will always index the same value unless you explicitly break that link.
# * The list of labels that forms the index can either be declared upon series creation or, by default, it will range from 0 to len(data)-1.
#     * If you're going to use Pandas to organize your data, specifying usable and informative labels is a good idea because that's one of the main advantages over other data types like lists

# ### Pandas DataFrames
# 
# [Pandas quick start guide for DataFrames](https://pandas.pydata.org/pandas-docs/stable/dsintro.html#dataframe)
# 
# * A DataFrame (DF) is a labeled data struture that can be thought of as a 2D extension of the Series objects (think excel spreadsheet with more than one column)
# * A dataframe can accept many types of input, multiple Series, a dictionary of 1D arrays, another DF, etc.
# * Like a Series, DFs contain data values and their corresponding labels. However, because we're now dealing with a 2D structure, we call the **row labels the index argument** and the **column labels the column argument**. 

# In[5]:


import pandas as pd


# ### Why tabular data?
# * Suppose you want to store and analyze data about multiple attributes/variables like the height and weight of different people
# * We could make three lists: one for the names, one for the heights, and one for the weights
# * Then when we analyze the data, we'd know that `names[0]` corresponds to `heights[0]` and `weights[0]`...but that is pretty clunky and hard to keep track of...

# In[6]:


names = ['john', 'sourabh', 'purva', 'pulkit','panayu']
heights = [68, 70, 67, 72, 64]
weight = [180, 170, 150, 200, 145]


# In[7]:


print(f'Name: {names[0]}, Height: {heights[0]}, Weight {weight[0]}')


# ### A much more effecient approach is to store all of our data in a single dataframe
# * This will allow us to easily access all attributes associated with each person via the index arguments
# * And each attribute will be stored as a single pandas series (column) in the resulting dataframe

# In[8]:


df = pd.DataFrame({'name':names, 
                   'height':heights, 
                   'weight': weight})


# In[9]:


df


# ### A (potentially) more useful way
# * Note that pandas generated a default list of row labels that go from 0:N-1 where N is the number of rows
# * However, we can also specify more useful row names using the `index` keyword upon dataframe creation 

# In[10]:


df = pd.DataFrame({'height':heights, 
                   'weight': weight}, index=names)


# In[11]:


df


# ## Basic indexing: Columns
# * First do it using the column names
# * This works much like you use keys to index into a dictionary
# * Notice that the index arguments (row labels) stay 'attached' to the column that we ask for...

# In[12]:


df['height']


# In[13]:


# weight of just the first two people...
df['weight'][0:2]


# ### Can index using the `.field` syntax

# In[14]:


df.height[0:2]


# In[15]:


# reverse (just like with a list...)
df.weight[::-1]


# ## Basic Indexing: Rows
# * Can also index based on row labels
# * This is a bit more complex as there are several methods that make use of either the actual label or the order of entry in the dataframe...
#     * Use df.loc to select a row by its label name
#         * Contrary to usual slicing conventions with lists, both the start and the stop indices are included when using the DF.LOC option...see below for demo. This makes sense because you're indexing by label name, not by a zero-based integer index. 
#     * Use df.iloc to select a row by its integer location (from 0 to length-1 of the axis)
# * You can use booleans to select a set of rows that satisfy some condition (logical indexing)

# In[16]:


# index by row label
df.loc['john':'pulkit']


# In[17]:


# but this won't return anything because pulkit comes after john...
df.loc['pulkit':'john']


# ### `iloc`
# * index by position in dataframe - works just like normal indexing of a list/tuple

# In[18]:


# first three people
df.iloc[0:3]


# In[19]:


# reverse...
df.iloc[::-1]


# ## Loading csv files using `read_csv()`
# 
# * Here we will use the mcd-menu.csv file to create a dataframe, which you can download here:
# 
# * [mcd-menu.csv](https://github.com/UCSD-CSS-001/ucsd-css-001.github.io/tree/main/datasets)
# 
# * Can also find file on slack and on canvas
# 
# * Note that here, I am intentionally using default indices (the numbers 0:N-1) so we don't have to do so much typing...you'll see. 

# In[20]:


mcd = pd.read_csv('mcd-menu.csv')


# In[21]:


mcd


# ## DataFrame operations

# ### Get basic information about the shape of the dataframe and the contents

# In[22]:


# shape - rows by columns, so 260 rows, and 24 columns of data per row
mcd.shape


# In[23]:


# turn the column names into a list...
list(mcd.columns)

# can also do: list(mcd.index) but the index is just default numbers here so not super interesting. 


# ### head and tail
# * see the first few rows of dataframe (`head`) or the last few (`tail`)
# * `head` and `tail` also take optional inputs to specify exactly how many rows you want to view
# * this is super useful to do when you first create a dataframe to make sure that everything looks right...

# In[24]:


# first 3 rows
mcd.head(3)


# In[25]:


# last 5 rows..
mcd.tail(5)


# ### Selecting columns - can do just like with out simpler dataframe example above...
# * use column names...

# In[26]:


mcd['Calories']


# In[27]:


# multiple columns - can be non-contiguous
mcd[['Calories', 'Saturated Fat']]


# ### Selecting rows by position
# * can also select by row label using `.loc` as described above, but since we're using numerial index labels here it makes sense to use `.iloc`

# In[28]:


# first two rows...
mcd.iloc[0:2]


# ### Selecting cells
# * above we selected into specific columns and or rows. 
# * we can also select a subset of rows from a specific column, etc...

# In[29]:


# print out a few rows so we can see the column names...
mcd.head(2)


# In[30]:


# this will give us the first entry in the 'Calories' column
mcd['Calories'].iloc[0:10]


# In[31]:


# shorthand for above...can leave off the explicit .iloc
mcd['Calories'][0]


# ## Getting subset of rows and colums
# * If asking for a non-contiguous set of columns, we can pass in a list defined with `[]`
# * If asking for a contiguous set of columns, we can use `:`
# * Note: need to be super careful using `.loc` (e.g., if you sorted the dataframe, then the following code would return all rows between the one labeled 0 and the one labeled 10...and if they are not in ascending order anymore then that might give you something unexpected!)

# In[32]:


# first 10 rows, Calories and Total Fat columns
# index + name
mcd.loc[0:10, ['Calories','Total Fat']]


# In[33]:


# first 10 rows, all columns between 'Calories' and 'Total Fat'
mcd.loc[0:10, 'Calories':'Total Fat']


# ## Filtering rows via logical indexing
# * logical indexing (boolean indexing) will filter dataframes based on whether certain conditions are met
# * we did some of this with lists, and the concepts are the same, but it can get a little more complex because now we're dealing with larger and multi-dimensional data sets. 
# * start by filtering the dataframe based on the values of entries in a specific row. 

# In[34]:


# return a version of the dataframe with just rows
# where 'Calories' are greater than 1000
mcd[ mcd['Calories'] >= 1000 ]


# In[35]:


# return a version of the dataframe with just rows
# where 'Total Fat' is greater than or equal to 40

# if we want to store the output of this filtering operation
# we need to assign the output (LHS)
fat40 = mcd[ mcd['Total Fat'] >= 40 ]
fat40.head(10)


# ### This also works on non-numerical categories...

# In[36]:


mcd[ mcd['Category'] == 'Breakfast' ]


# ### And we chain together multiple conditions as well...
# * Example: all entries where Category is Breakfast, Calories greater than 300, and Calories less than 500

# In[37]:


mcd[ (mcd['Category'] == 'Breakfast') & 
  (mcd['Calories'] > 300) & 
  (mcd['Calories'] < 500) ]


# ### How does this work? 
# * If we take a look at the filtering conditionals, they will determine all rows where the given condition is met
# * If they are met, you'll get a `True` value returned, and if they are not met, you'll get a `False` value returned...
# * Take a look if we just specify the conditionals...
# * Note that the length of the output matches the length of our dataframe (the number of rows)...i.e., every row has either a `True` or a `False`

# In[38]:


(mcd['Category'] == 'Breakfast') & (mcd['Calories'] > 300)


# In[39]:


# now lets assign this list of booleans to another variable
index = (mcd['Category'] == 'Breakfast') & (mcd['Calories'] > 300)


# In[40]:


# and by substitution, we get...
mcd [ index ]


# ## Review of logical indexing...
# * make conjunctions by combining arrays of logical values with & (and operations)
# * make disjunctions with |  (or operations)
# * and we need to put comparison operations in () before combining

# ## Other handy methods...

# ### Basic math operations...
# * describe is a handy way to get summary stats...
# * mean, std, etc...

# In[41]:


mcd.describe()


# In[42]:


# mean Calories...
mcd.Calories.mean()

# or
# mcd['Calories'].mean()


# In[43]:


# standard deviation
mcd.Calories.std()


# ### Sorting entire dataframe based on values in one column
# * here we can easily find the menu item with the fewest calories
# * sort by the 'Calories' column, then pull out the name of the item
# * default behavior is to not sort in place, so we need to reassign!

# In[44]:


# sort - ascending order by default
mcd.sort_values('Calories')


# In[45]:


# descending order (ascending = False)
mcd.sort_values('Calories', ascending = False)


# ### Chaining together methods
# * Possible to apply multiple methods in one line of code...
# * Careful here...can be super effecient and compact, but you can get carried away and make your code really confusing and hard to understand (even to yourself!)

# In[46]:


# sort and then display the last three rows
mcd.sort_values('Total Fat').tail(3)


# In[47]:


# another way to achieve the same outcome...
mcd.sort_values('Total Fat').iloc[-3:]


# In[48]:


# three highest fat items in descending order
mcd.sort_values('Total Fat', ascending = False).iloc[:3]


# ## Solving simple tasks - examples
# 
# ### Find the breakfast menu item with the fewest calories

# In[49]:


mcd[ mcd['Category'] == 'Breakfast'].sort_values('Calories').head(1)


# ### Find the highest john_index food
# 
# * often times we're asked to filter data based on some parameters (e.g., marketing tells you to define some index and find all items that fall into that category).  
# 
# * define some index: `john_index = 12*(protein grams + fiber grams)/calories`
# * make it a new column in our dataframe...then we can sort by it (or filter by it)
# * All we have to do to make a new column is give it a name and give it some values - just like we can make new `key:value` pairs in a dictionary...

# In[50]:


# this will define a new column on the fly and compute the john-index
mcd['john_index'] = 12 * (mcd['Protein'] + mcd['Dietary Fiber'])/mcd['Calories']


# ### Note the resulting column has some funny stuff in it!

# In[51]:


mcd['john_index'].unique()


# ### Why? 
# * `inf` == infinity...happens when you divide by zero!
#     * for Diet Dr. Pepper, john_index == (1 + 0) / 0
# * `nan` == not-a-number...happens when the thing you try to do isn't a number (like 0/0)
#     * for Coffee and Tea, john_index == (0 + 0) / 0

# In[52]:


mcd.head(2)


# In[53]:


# import numpy for np.isinf() to weed out the inf entries
import numpy as np


# In[54]:


(mcd [ ~ mcd['john_index'].isna() & ~np.isinf(mcd['john_index'])]
 .sort_values('john_index', ascending=False) )


# ### Alternate approach using `.replace()`
# * can also directly replace nan/infs with other values

# In[55]:


mcd['john_index'].replace(np.nan, 0).unique()


# In[56]:


mcd['john_index'].replace(np.inf, 0).unique()


# ### Or you can fill missing values using fillna...
# * For example, can replace all nans with the mean of all other values...

# In[57]:


mcd['john_index'].fillna(mcd['john_index'].mean()).unique()
# remember you need to overwrite mcd or make a new dataframe in order for these changes to 'stick'


# In[58]:


(mcd[mcd['Calories'] > 0]
.sort_values('john_index', ascending = False)
.head(1))

