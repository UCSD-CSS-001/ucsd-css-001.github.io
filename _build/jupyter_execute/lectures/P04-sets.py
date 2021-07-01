#!/usr/bin/env python
# coding: utf-8

# # P04: dictionaries, sets, and files
# - **Concepts**: ordered vs not, hash
# - **Python dict, set**: hashable, set, dict, .update(), del
# - **Python files**: open, close, with open as fp
# 
# ## Python
# 
# ### Sets
# 
# Sets are *unordered*, *mutable*, *collections*, of *distinct*, *hashable* elements.
# 
# In Python sets are like lists in that they:
#  - are *mutable* (so you can change them),
#  - are *collections* of other objects (so you can iterate over them, get their `len()`, check membership with `in`).
# 
# However, they are unlike lists in that:
# - they are *unordered* so they cannot be indexed or sliced.
# - they may contain only *hashable* items (so they cannot contain things like lists, dictionaries, sets).
# - every item they contain must be *distinct*.
# 
# Sets are created with `set(vals)` where `vals` is typically a list or some other kind of iterable entity.

# In[1]:


x = set(['a', 'b', 3, 4])
print(x)


# Sets can be modified with the methods `.add()` or `.remove()`
# 

# In[2]:


print(x)
x.add('abs')
x.add(10)
print(x)

x.add(3) # no effect
print(x)


# Note: sets are presented in some kind of order, but that order changes when the set is changed.
# 
# Note: adding an existing item has no effect, since sets have only disctinct items.
# 

# In[3]:


print(x)
x.remove(5)
print(x)


# Set membership can be evaluated with `in`

# In[4]:


6 in x


# Sets can be iterated over with a `for loop`

# In[5]:


for item in x:
    print(item)


# Sets are useful because:
# 2. they are efficient for keeping track of unique things.
# 1. they support *set operations* (union, intersection, difference
# 
# #### Set operations

# In[6]:


A = set('panda')
B = set('conga')
print(A)
print(B)


# Set union: items in A or B

# In[7]:


print(A | B)


# Set intersections: items in A and B

# In[8]:


print(A & B)


# Set difference: items in A but not B

# In[9]:


print(A - B)


# Set symmetric difference: items in either set but *not both* sets.  (items in union but not in intersection)

# In[10]:


print(A ^ B)


# 
