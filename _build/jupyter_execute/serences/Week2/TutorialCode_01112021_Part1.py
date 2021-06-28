#!/usr/bin/env python
# coding: utf-8

# 
# # InClass 01112021 - variable names, lists, slicing, for loops

# ## A few notes about legal variable names
# * A variable cannot start with a number.
# * Variables are case-sensitive (MyVar and myvar and myVar are all different!)
# * A variable has to start with a letter or an underscore
# * A variable can only contain letters, numbers, and underscores
# 

# In[1]:


# these two variables might be pronounced the same, but they are different! 
# python respects capitalization...so the cap "V" in the second makes it a 
# totally different object than the first variable
myvar = 10
myVar = 100
print(myvar)
print(myVar)


# ### can't start with a number

# In[2]:


1var = 10


# ## Lists - a collection that is ordered and changeable and allows duplicate members.

# In[ ]:


# this is a single string object, like we did last week 

a_str = 'john'
print(a_str)


# In[ ]:


# introduction to lists - in this case a list of strings!
names = ['bob', 'vy', 'sunyoung', 'maggie']

# we start indexing with 0!!!
# so this is the first name
print(names[0])

# this is the 3rd name...etc
print(names[2])


# #### If you want to find the last element in a list and you don't know how long the list is, then just start indexing from the end.
# * -1 is the last element
# * -3 is the third to last, etc.

# In[ ]:


print(names[-1])
print(names[-3])


# ## you can also make a list using a bunch of str variables

# In[ ]:


str1 = 'bob'
str2 = 'vy'
str3 = 'sunyoung'
names = [str1, str2, str3]
print(names[1])

# this is handy if you later want to re-use the same variables to make another list
names2 = [str3, str2, str1]


# ## sorting a list
# * sort() is a **method** - or a function that is specifically associated with this object type
# * the sort method modifies the list
# * there is also a "sorted" function that does not modify the list...instead, you assign the output of the sorted function to another variable (another list)

# In[ ]:


names = ['toyota', 'ford', 'honda']

# perm sort a list in alpha order
# this will alter 'names' (can't undo)
names.sort()
print(names)


# ### sort without modifying using the sorted function
# * note that sorted is a general use **function** that can be used across multiple object types, not just for lists

# In[ ]:


names = ['john', 'vy', 'sunyoung', 'maggie']
# sort without modifying
print(sorted(names))
print(names)


# ## Remove (delete) an item from a list

# In[ ]:


# redefine names list
names = ['john', 'vy', 'sunyoung', 'maggie']

print(names)

# remove items from a list
# remove first item...
del names[0]
print(names)


# ## Pop an item from a list and assign to another variable

# In[ ]:


# redefine names list
names = ['john', 'vy', 'sunyoung', 'maggie']

# pop an item - can also pass index to pop() method (e.g. pop(1))
last_name = names.pop()
print(last_name)

print(names)


# ## Quick intro to 'range' function 
# * Create a sequence of numbers
# * non-inclusive of stop value

# In[ ]:


x = range(0,15)
print(x[-1])


# ### Make a list using the range function...

# In[ ]:


# 0-14 (non inclusive of the last number!)
x = list(range(0,15))
print(x)


# ### Start value, stop value, step value
# * make a sequence that increments/decrements at a specified step size

# In[ ]:


skip_num = list(range(0,100,20))
print(skip_num)

skip_num = list(range(30,0,-10))
print(skip_num)

