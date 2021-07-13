#!/usr/bin/env python
# coding: utf-8

# # P04: dictionaries, sets, and files
# - **Concepts**: ordered vs not, hash
# - **Python dict, set**: hashable, set, dict, .update(), del
# - **Python files**: open, close, with open as fp
# 
# ## Concepts
# 
# ### Hashable, immutable
# 
# - [**Immutable**](https://en.wikipedia.org/wiki/Immutable_object) variables/objects cannot be changed after they are created.  For instance, in Python, a string cannot be modified, it can just be replaced with a new string.  In contrast, a list can be modified: you can add new items to it without creating a new list object.
# 
# - **Hashable** variables/objects are immutable, and can support the calculation of a [hash](https://en.wikipedia.org/wiki/Hash_function).  This includes integers, floats, strings, tuples, booleans.
# 
# ### Sets
# 
# ### Dictionary: Hash-table / mapping
# 
# ### Files
# 
# #### Paths
# 
# #### Formats
# 
# ## Python
# 

# 
# ### Dictionaries
# 
# 
# Dictionaries are *unordered*, *mutable*, *collections*, of *key*-*value* pairs.  They are a mapping from *distinct*, *hashable* keys, onto values.
# 
# In Python dictionaries are like lists in that they:
#  - are *mutable* (so you can change them),
#  - are *collections* of other objects (so you can iterate over them, get their `len()`, check membership with `in`).
#  - you can get items with square brackets `[]` (but not with integer index)
# 
# However, they are unlike lists in that:
# - they are *unordered* so they cannot be indexed with integers or sliced.
# - the are *mappings* between *distinct*, *hashable* keys, and values.
# 
# Dictionaries are created with `dict()`, or with `{key:value}` notation.

# In[1]:


courses = dict()
courses['CSS2'] = 'Data/Model Python'
courses['CSS1'] = 'Intro Python'
print(courses)

courses = {'CSS2': 'Data/Model Python', 'CSS1': 'Intro Python'}


# Dictionary elements can be accessed via their keys.

# In[2]:


print(courses['CSS1'])


# Items can be added to dictionaries by assigning to new keys,

# In[3]:


courses['ABB'] = 'Is this a course?'
print(courses)


# Dictionaries can be updated with `.update()`, which will add new keys, and update the values of existing keys.

# In[4]:


new_courses = {'ABB': 'this is not a course', 'CSS100':'Analytic Programming'}
courses.update(new_courses)
print(courses)


# Elements of dictionaries can be deleted with the `del` keyword:

# In[5]:


del courses['ABB']
print(courses)


# You can check if a key exists in a dictionary with `in`:

# In[6]:


print('CSS1' in courses)
print('ABB' in courses)


# 
# 
# #### Keys, Values, Items
# 
# You can get (or iterate over) just the keys with `.keys()`.

# In[7]:


print(courses.keys())
print('')
for k in courses.keys():
    print(k)


# You can get just the values with `.values()`.

# In[8]:


print(courses.values())
print('')
for v in courses.values():
    print(v)


# You can get key-value pairs (as tuples) with `.items()`.

# In[9]:


print(courses.items())
print('')
for pair in courses.items():
    print(pair)


# It is often useful to do assignment unpacking, to unpack the (key,value) tuple into two variables:

# In[10]:


for k,v in courses.items():
    print(f'Course number {k} is titled {v}')


# #### Sorting
# 
# As you saw above, the order of key-value pairs in a dictionary is determined by when they were added.  Often we want to sort the contents either by the keys, or by the values.   In either case, to get a sorted dictionary, we will end up making a new dictionary by inserting key-value pairs in a sorted order.
# 
# **By keys**

# In[11]:


sorted_courses = dict()
for k in sorted(courses.keys()):
    sorted_courses[k] = courses[k]

print(courses)
print(sorted_courses)


# **By values**
# 
# Sorting by values is a bit tricky -- we can sort the values, but we have no reliable way to figure out which keys were associated with the sorted values.  Consequently, we have to sort the key-value items.  But doing so requires that we can tell the `sorted` function to use the second element of the pair to sort.  This is all doable, but involves either writing an anonymous function (not hard, we just havent covered it yet), or importing a library that creates that anonymous function for us.
# 
# We will show you how to do this using the `itemgetter` function from the `operator` library

# In[12]:


from operator import itemgetter # this imports the itemgetter function
print("before sorting, items in order of insertion:  ")
for item in courses.items():
    print(item)

print("default sorting sorts by first element of pair (key):  ")
for item in sorted(courses.items()):
    print(item)

print("sorting by the second element (index=1) of the pair with key=itemgetter(1):  ")
for item in sorted(courses.items(), key=itemgetter(1)):
    print(item)


# Making a new sorted dictionary:

# In[13]:


courses_by_title = dict()

for number,title in sorted(courses.items(), key=itemgetter(1)):
    courses_by_title[number] = title

print(courses_by_title)


# Finally, for a very pithy, advanced syntax, we could do it with dictionary comprehension:

# In[14]:


courses_by_title = {k:v for k,v in sorted(courses.items(), key=itemgetter(1))}
print(courses_by_title)


# 
