#!/usr/bin/env python
# coding: utf-8

# # This is a markdown cell (or text cell). Here we can write notes about the purpose of the code, we can include links to external references. Text cells use the "Markdown language" to format the text. 
# 
# ## next sub-heading with smaller text - use for the next level of notes in your code below
# 
# ### sub-sub-heading
# 
# #### sub-sub-sub-heading, etc.
# 
# * bullet points
# * another bullet point
#   * an indented sub-bullet point 
# 
# **if you want bold text** 
# 
# *italic text*
# 
# [this is a link to a useful guide to the basics of markdown](https://www.markdownguide.org/basic-syntax/)

# ## A string is a collection of characters, surrounded by either single or double quotes
# * notice that because this is a sub-heading in our notebook that is one level down, we use '##' to change the size of the text 

# In[1]:


print("hello python!")


# In[2]:


message = "hello python!"
print(message)


# ### Using ' vs "
# * Note that this is a sub-sub-heading (under the sub-heading of our discussion on strings)*italicized text*, so we use '###'

# In[3]:


message = "hello python! we'll be back next monday"
print(message)


# In[4]:


# vs. 
message = 'hello python! we'll be back next monday'
print(message)


# ## Using methods of an object (in this case a string object)

# In[ ]:


name = "joHn serencEs"
name.title()


# ### why using print here? Because otherwise you just get the output of the last line - if you want to force output, then use the print statement

# In[ ]:


print(name.lower())
print(name.upper())


# ## Some handy methods for data cleaning - make uniform str types...
# * useful for 'cleaning' non-uniform user input or labels in big data sets
# * this is by no means an exhaustive list of methods for the str object type! but if you can use these, then you should be able to figure out how to use many of the other methods

# In[ ]:


name = " john "
print(name)
print(name.rstrip())
print(name.lstrip())
print(name.strip())


# ## Concatenating strings (sticking a bunch of strings together)

# In[ ]:


first_name = "john"
last_name = "serences"
full_name = first_name + " " + last_name + " was here!"
print(full_name.title())


# ## Numerical data types and basic operators [list of operators](https://www.w3schools.com/python/python_operators.asp)
# * integers are whole numbers

# In[ ]:


# int data types (objects)
# integers are WHOLE numbers
x = 2
y = 3

# basic operations
print(x+y)    # add
print(y-x)    # subtract
print(x*y)    # multiply
print(x**y)   # raise to a power


# ## Floating point numbers

# In[ ]:


# this returns a floating point number (decimal)
print(x/y)


# ## How do you figure out what the variable type is? 

# In[ ]:


print(type(x))


# ## Type casting - changing a variable from one type to another

# In[ ]:


# type casting - first int to string
year = 2019
print("this is the year: " + str(year))


# ### Then string to int and then back to str!

# In[2]:


# then string to an int
year = "2021"
print("In 10 years it will be: " + str(int(year) + 10))


# ### You can convert from one type to another with the int(), float(), complex()
# * be careful though as **sometimes there are significant consequences!**
#   * for example, casting a float to an int will cause everything to the right of the decimal place to be truncated

# In[ ]:


# make a floating point number and then type cast as an int to see what happens
x = 2.9
print(int(x)) # does not ROUND!!! truncates

